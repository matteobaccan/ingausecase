"""Caso liyab-confronto: Inga e Liyab sulla stessa macchina, nello stesso job, misurati in
tre modi, per separare quello che dipende dalla CPU del runner da quello che costa il
server HTTP di Inga.

Per ogni modello di "modelli" (case.json; scaricati come fa il runner) e per G giri, con
l'ordine dei tre ruotato a ogni giro:

- Inga API: `inga serve` avviato qui, il prompt del caso liyab-velocita (circa P token,
  chiede di contare fino a 1000) dall'API in streaming, N token; i token del prompt sul
  tempo al primo token, quelli dopo il primo sul tempo dopo il primo; il picco di
  memoria (VmHWM) del server;
- Inga bench: `inga bench -p P -n N -r 1 --json` sotto /usr/bin/time (prompt di token
  casuali, generazione da un contesto vuoto, come llama-bench);
- Liyab: `liyab-cli --json --no-lookup` sotto /usr/bin/time, sullo stesso testo del prompt
  già passato dal ChatML di Qwen3 (le sue statistiche, senza il caricamento).

Ogni motore fa prima una prova non misurata. Voto: la media dei rapporti Inga API su
Liyab (prompt e generazione), su tutti i modelli.
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import inga_api  # noqa: E402
import liyab  # noqa: E402
import runner  # noqa: E402

P, N, G = 512, 128, 3


def inga_api_giro(frasi, r):
    with confronto.IngaDelCaso([]) as m:
        if frasi is None:
            frasi = confronto.frasi_per(m.url, m.extra(), P)
        v = confronto.velocita(m.url, m.extra(), frasi, N, 1)
        info = m.info()
    p = v["prove"][0]
    return frasi, {"pp": p["pp"], "tg": p["tg"], "token_prompt": p["token_prompt"],
                   "picco_mib": round(info["picco_rss_gb"] * 1e9 / 2**20, 1)}


def inga_bench_giro(model):
    so, _, picco = liyab.con_time([os.environ["IUC_INGA"], "bench", model, "-p", str(P), "-n", str(N),
                                   "-r", "1", "--json"])
    rows = json.loads(so[so.index("["):])
    return {"pp": next(x["avg_ts"] for x in rows if x["n_prompt"] == P and x["n_gen"] == 0),
            "tg": next(x["avg_ts"] for x in rows if x["n_gen"] == N and x["n_prompt"] == 0),
            "picco_mib": picco}


def liyab_giro(model, ctx, frasi, r):
    liyab.misura(model, liyab.chatml(confronto._messaggi(10, 99, 1)), 8, ctx, ["--no-lookup"])
    m = liyab.misura(model, liyab.chatml(confronto._messaggi(frasi, r, G)), N, ctx, ["--no-lookup"])
    return {k: m[k] for k in ("pp", "tg", "token_prompt", "picco_mib")}


def media(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def main():
    if not liyab.cartella():
        inga_api.write_result({"stato": "saltato", "motivo": "Liyab non c'è (IUC_LIYAB)"})
        return
    with open(os.path.join(os.environ["IUC_CASE_DIR"], "case.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    ctx = int(os.environ.get("IUC_CTX", "4096"))
    models = runner.load_models()
    out, voci, rapporti = {}, {}, []
    try:
        for key in cfg["modelli"]:
            model = runner.get_model(key, models, os.environ["IUC_CACHE"])
            os.environ["IUC_MODEL_PATH"] = model
            print(f"== {key}", flush=True)
            # prove non misurate: il file nella cache delle pagine, il server una volta
            frasi, _ = inga_api_giro(None, 99)
            inga_bench_giro(model)
            giri = []
            for r in range(G):
                g = {}
                ordine = ["api", "bench", "liyab"][r:] + ["api", "bench", "liyab"][:r]
                for chi in ordine:
                    if chi == "api":
                        _, g["inga_api"] = inga_api_giro(frasi, r)
                    elif chi == "bench":
                        g["inga_bench"] = inga_bench_giro(model)
                    else:
                        g["liyab"] = liyab_giro(model, ctx, frasi, r)
                giri.append(g)
                print(f"  giro {r + 1} ({', '.join(ordine)}): "
                      + "; ".join(f"{k} pp {v['pp']:.1f} tg {v['tg']:.2f} picco {v['picco_mib']}"
                                  for k, v in g.items()), flush=True)
            agg = {k: {m: media([g[k][m] for g in giri]) for m in ("pp", "tg", "picco_mib")}
                   for k in ("inga_api", "inga_bench", "liyab")}
            out[key] = {"giri": giri, "medie": agg, "frasi": frasi}
            a, b, l = agg["inga_api"], agg["inga_bench"], agg["liyab"]
            voci.update({
                f"{key}: prompt, Inga API su Liyab": a["pp"] / l["pp"],
                f"{key}: generazione, Inga API su Liyab": a["tg"] / l["tg"],
                f"{key}: prompt, Inga bench su Liyab": b["pp"] / l["pp"],
                f"{key}: generazione, Inga bench su Liyab": b["tg"] / l["tg"],
                f"{key}: generazione, Inga API su Inga bench": a["tg"] / b["tg"],
                f"{key}: picco di RAM, Inga API (MiB)": a["picco_mib"],
                f"{key}: picco di RAM, Inga bench (MiB)": b["picco_mib"],
                f"{key}: picco di RAM, Liyab (MiB)": l["picco_mib"],
            })
            rapporti += [a["pp"] / l["pp"], a["tg"] / l["tg"]]
    except (RuntimeError, OSError, ValueError, KeyError, StopIteration, runner.Failure,
            subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    for k, v in voci.items():
        print(f"{k}: {round(v, 3) if v is not None else None}")
    inga_api.write_result({"stato": "ok", "voto": sum(rapporti) / len(rapporti), "voci": voci,
                           "dettagli": dict(modelli=out, liyab=liyab.versione(), cpu=os.cpu_count())})


if __name__ == "__main__":
    main()
