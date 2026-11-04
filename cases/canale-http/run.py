"""Caso canale-http: quanto costa il canale HTTP di Inga, sulla stessa macchina e nello
stesso job, misurando lo stesso modello in cinque modi (G giri, ordine ruotato a ogni
giro, una prova non misurata per ogni modo):

- bench: `inga bench -p P -n N -r 1 --json` (prompt casuale, generazione da un contesto
  vuoto, come llama-bench): la velocità del motore da solo;
- bench_d: lo stesso con `-d P` (P token già nella cache prima di ogni prova, non
  misurati: la generazione dopo un prompt lungo quanto quello dei casi);
- bench_t: `bench` con `-t` pari ai processori meno uno (il default è un thread per core
  fisico, cioè 2 su un runner a 4 vCPU con SMT);
- run_corto: `inga run -p` con un prompt corto (una frase): la sessione completa senza
  la cache lunga;
- run: `inga run <modello> -p TESTO -n N`, lo stesso prompt del caso liyab-velocita
  (circa P token, chiede di contare fino a 1000): il motore con la sessione completa
  (template, prompt vero) ma senza server, la riga delle statistiche su stderr;
- api: `inga serve` avviato qui, la stessa richiesta dall'API senza streaming: la
  velocità vista dal client (token della risposta sul tempo oltre il primo token del
  server) e quella del motore (inga_timings.predicted_per_second);
- stream: la stessa richiesta in streaming (come liyab-velocita): la velocità vista dal
  client (token dopo il primo sul tempo dopo il primo) e quella del motore;
- stream_meno: in streaming, con `--threads-decode` pari ai processori meno uno (il
  thread che scrive sulla rete non contende un core ai thread di generazione).

Se la velocità del motore in streaming (inga_timings) è vicina a quella del client, il
rallentamento sta dentro il processo (contesa dei core, lavoro per token del server);
se il motore va come bench e il client no, sta nel canale (relay, JSON, scrittura).
Voto: la media, sui modelli, della generazione in streaming vista dal client sulla
generazione di bench (1 = il canale non costa niente).
"""

import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import inga_api  # noqa: E402
import liyab  # noqa: E402
import runner  # noqa: E402

P, N, G = 512, 128, 3
MODI = ["bench", "bench_d", "bench_t", "run", "run_corto", "api", "stream", "stream_meno"]
RIGA = re.compile(r"prompt: (\d+) tokens \((\d+) cached\), ([\d.]+) tok/s \| first token: ([^|]+)\| "
                  r"answer: (\d+) tokens, ([\d.]+) tok/s")


def bench_giro(model, extra=()):
    so, _, picco = liyab.con_time([os.environ["IUC_INGA"], "bench", model, "-p", str(P), "-n", str(N),
                                   "-r", "1", "--json", *extra])
    rows = json.loads(so[so.index("["):])
    return {"pp": next(x["avg_ts"] for x in rows if x["n_prompt"] == P and x["n_gen"] == 0),
            "tg": next(x["avg_ts"] for x in rows if x["n_gen"] == N and x["n_prompt"] == 0),
            "picco_mib": picco}


def profilo(model, d):
    """`inga bench --profile` at depth d: the time per operation kind per generated
    token (the tg row's profile), so the share of the attention at depth P shows."""
    so, _, _ = liyab.con_time([os.environ["IUC_INGA"], "bench", model, "-p", "0", "-n", str(N), "-d", str(d),
                               "-r", "1", "--profile", "--json"])
    rows = json.loads(so[so.index("["):])
    row = next(x for x in rows if x["n_gen"] == N)
    return {"tg": row["avg_ts"], "profile": row.get("profile")}


def ab_split(model, d):
    """`inga bench --ab debug.attn_split=true` at depth d: the CPU's decode attention
    split over chunks of 256 positions on the threads (split-KV, 0.44.0, off by default)
    against one task per KV head, in the same process, runs in ABBA order (the sums differ
    in their order only: `--ab` compares the next token's distributions); None for a build
    without the key (it fails)."""
    try:
        so, _, _ = liyab.con_time([os.environ["IUC_INGA"], "bench", model, "-p", "0", "-n", str(N),
                                   "-d", str(d), "-r", "4", "--ab", "debug.attn_split=true", "--json"])
    except RuntimeError:
        return None
    rows = [x for x in json.loads(so[so.index("["):]) if x.get("n_gen") == N]
    by = {x.get("ab_variant"): x for x in rows}
    a = by.get("default")
    b = next((x for k, x in by.items() if k != "default"), None)
    if not a or not b:
        return None
    return {"spento": a["avg_ts"], "split": b["avg_ts"], "split_su_spento": b["avg_ts"] / a["avg_ts"]}


def ab_f16(model, d):
    """`inga bench --ab debug.attn_f16=false` at depth d: the CPU's attention reading
    the f16 cache straight from its bits (0.44.0) against reading it position by
    position into a copy (before), in the same process, runs in ABBA order; None for a
    build without the key (it fails)."""
    try:
        so, _, _ = liyab.con_time([os.environ["IUC_INGA"], "bench", model, "-p", "0", "-n", str(N),
                                   "-d", str(d), "-r", "4", "--ab", "debug.attn_f16=false", "--json"])
    except RuntimeError:
        return None
    rows = [x for x in json.loads(so[so.index("["):]) if x.get("n_gen") == N]
    by = {x.get("ab_variant"): x for x in rows}
    a = by.get("default")
    b = next((x for k, x in by.items() if k != "default"), None)
    if not a or not b:
        return None
    return {"f16": a["avg_ts"], "copia": b["avg_ts"], "f16_su_copia": a["avg_ts"] / b["avg_ts"]}


def run_giro(model, ctx, frasi, r):
    home = os.path.join(inga_api.work_dir(), "inga-home-run")
    os.makedirs(home, exist_ok=True)
    testo = confronto._messaggi(frasi, r, G)[0]["content"]
    return run_testo(model, ctx, testo)


def run_testo(model, ctx, testo):
    home = os.path.join(inga_api.work_dir(), "inga-home-run")
    cmd = [os.environ["IUC_INGA"], "--home", home, "run", model, "-p", testo, "-n", str(N),
           "--ctx", str(ctx), "--seed", str(inga_api.SEED), "--temp", "0", "--offline"]
    _, se, picco = liyab.con_time(cmd)
    m = RIGA.search(se)
    if not m:
        raise RuntimeError(f"inga run senza la riga delle statistiche: {se[-800:]!r}")
    return {"pp": float(m.group(3)), "tg": float(m.group(6)), "token_prompt": int(m.group(1)),
            "token_generati": int(m.group(5)), "picco_mib": picco}


def _server(timings):
    t = timings or {}
    return {"tg_motore": t.get("predicted_per_second"), "pp_motore": t.get("prompt_per_second"),
            "ttft_ms_motore": t.get("ttft_ms")}


def api_giro(frasi, r, argomenti):
    with confronto.IngaDelCaso(argomenti) as m:
        inga_api.chat(confronto._messaggi(10, 99, 1), max_tokens=8, url=m.url, extra=m.extra())
        _, data, secondi = inga_api.chat(confronto._messaggi(frasi, r, G), max_tokens=N, url=m.url,
                                         extra=m.extra(), timeout=3600)
        info = m.info()
    u, t = data.get("usage") or {}, data.get("inga_timings") or {}
    pt, ct = u.get("prompt_tokens"), u.get("completion_tokens")
    if not pt or not ct or not t.get("ttft_ms"):
        raise RuntimeError(f"risposta senza usage o inga_timings: {u} {t}")
    ttft = t["ttft_ms"] / 1000
    out = {"pp": pt / ttft, "tg": (ct - 1) / (secondi - ttft), "token_prompt": pt,
           "token_generati": ct, "secondi": round(secondi, 3),
           "picco_mib": round(info["picco_rss_gb"] * 1e9 / 2**20, 1)}
    out.update(_server(t))
    return out


def stream_giro(frasi, r, argomenti):
    with confronto.IngaDelCaso(argomenti) as m:
        inga_api.stream(confronto._messaggi(10, 99, 1), max_tokens=8, url=m.url, extra=m.extra())
        x = inga_api.stream(confronto._messaggi(frasi, r, G), max_tokens=N, url=m.url, extra=m.extra(),
                            timeout=3600)
        info = m.info()
    u = x["usage"] or {}
    pt, ct = u.get("prompt_tokens"), u.get("completion_tokens")
    if not pt or not ct or x["ttft"] is None or ct < 2:
        raise RuntimeError(f"risposta senza usage o senza token: {u} {x['testo'][:200]!r}")
    out = {"pp": pt / x["ttft"], "tg": (ct - 1) / (x["secondi"] - x["ttft"]), "token_prompt": pt,
           "token_generati": ct, "ttft": round(x["ttft"], 3), "secondi": round(x["secondi"], 3),
           "pezzi": x["pezzi"], "picco_mib": round(info["picco_rss_gb"] * 1e9 / 2**20, 1)}
    out.update(_server(x["timings"]))
    return out


def media(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def main():
    with open(os.path.join(os.environ["IUC_CASE_DIR"], "case.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    ctx = int(os.environ.get("IUC_CTX", "4096"))
    cpu = os.cpu_count() or 2
    meno = ["--threads-decode", str(max(1, cpu - 1))]
    t_meno = ["-t", str(max(1, cpu - 1))]
    models = runner.load_models()
    out, voci, rapporti = {}, {}, []
    try:
        for key in cfg["modelli"]:
            model = runner.get_model(key, models, os.environ["IUC_CACHE"])
            os.environ["IUC_MODEL_PATH"] = model
            print(f"== {key}", flush=True)
            # il numero di frasi per circa P token, dal server; poi la prova non misurata
            # di bench e di run (api e stream la fanno a ogni avvio del server)
            with confronto.IngaDelCaso([]) as m:
                frasi = confronto.frasi_per(m.url, m.extra(), P)
            bench_giro(model)
            run_giro(model, ctx, frasi, 99)

            def misura(chi, r):
                if chi == "bench":
                    return bench_giro(model)
                if chi == "bench_d":
                    return bench_giro(model, ["-d", str(P)])
                if chi == "bench_t":
                    return bench_giro(model, t_meno)
                if chi == "run":
                    return run_giro(model, ctx, frasi, r)
                if chi == "run_corto":
                    return run_testo(model, ctx, confronto._messaggi(1, r, G)[0]["content"])
                if chi == "api":
                    return api_giro(frasi, r, [])
                if chi == "stream":
                    return stream_giro(frasi, r, [])
                return stream_giro(frasi, r, meno)

            giri = []
            for r in range(G):
                ordine = MODI[r:] + MODI[:r]
                g = {chi: misura(chi, r) for chi in ordine}
                giri.append(g)
                print(f"  giro {r + 1} ({', '.join(ordine)}): "
                      + "; ".join(f"{k} pp {v['pp']:.1f} tg {v['tg']:.2f}"
                                  + (f" (motore {v['tg_motore']:.2f})" if v.get("tg_motore") else "")
                                  for k, v in g.items()), flush=True)
            agg = {k: {m: media([g[k].get(m) for g in giri])
                       for m in ("pp", "tg", "tg_motore", "pp_motore", "picco_mib")} for k in MODI}
            profili = {str(d): profilo(model, d) for d in (0, P)}
            ab = {str(d): ab_f16(model, d) for d in (P, 4 * P)}
            for d, x in ab.items():
                if x:
                    print(f"  attenzione f16 a d={d}: {x['f16']:.2f} tok/s contro {x['copia']:.2f} "
                          f"letta per posizione ({x['f16_su_copia']:.3f}x)", flush=True)
                    voci[f"{key}: generazione a d={d}, attenzione f16 su quella per posizione"] = x["f16_su_copia"]
            # Split-KV at 2048 tokens on both models, 4096 on the small one only (the
            # prompt of 4096 tokens on Qwen3-4B would take most of an hour on this runner).
            split = {str(d): ab_split(model, d) for d in ((4 * P, 8 * P) if "0.6b" in key else (4 * P,))}
            for d, x in split.items():
                if x:
                    print(f"  split-KV a d={d}: {x['split']:.2f} tok/s contro {x['spento']:.2f} "
                          f"spento ({x['split_su_spento']:.3f}x)", flush=True)
                    voci[f"{key}: generazione a d={d}, split-KV su spento"] = x["split_su_spento"]
            for d, pr in profili.items():
                ops = sorted((pr.get("profile") or {}).get("ops") or [], key=lambda o: -o["ns_per_token"])
                print(f"  profilo d={d}: {pr['tg']:.2f} tok/s, "
                      + ", ".join(f"{o['op']} {o['ns_per_token'] / 1e6:.2f} ms" for o in ops[:6]), flush=True)
            out[key] = {"giri": giri, "medie": agg, "frasi": frasi, "threads_decode_meno": meno[1],
                        "profili": profili, "ab_attn_f16": ab,
                        "ab_attn_split": split}
            b = agg["bench"]["tg"]
            for chi in MODI:
                voci[f"{key}: generazione {chi}, tok/s"] = agg[chi]["tg"]
                if chi != "bench":
                    voci[f"{key}: generazione {chi} su bench"] = agg[chi]["tg"] / b
                if agg[chi]["tg_motore"]:
                    voci[f"{key}: generazione {chi}, il motore, tok/s"] = agg[chi]["tg_motore"]
                    voci[f"{key}: generazione {chi}, il motore su bench"] = agg[chi]["tg_motore"] / b
                voci[f"{key}: prompt {chi}, tok/s"] = agg[chi]["pp"]
            rapporti.append(agg["stream"]["tg"] / b)
    except (RuntimeError, OSError, ValueError, KeyError, StopIteration, runner.Failure,
            subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    for k, v in voci.items():
        print(f"{k}: {round(v, 3) if v is not None else None}")
    inga_api.write_result({"stato": "ok", "voto": min(1.0, sum(rapporti) / len(rapporti)), "voci": voci,
                           "dettagli": dict(modelli=out, cpu=cpu)})


if __name__ == "__main__":
    main()
