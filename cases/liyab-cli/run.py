"""Caso liyab-cli: Inga e Liyab senza server HTTP, ognuno con il suo comando di misura,
sullo stesso file del modello e sulla stessa macchina.

- Inga: `inga bench -p 512 -n 128 -r 3 --json` (un solo caricamento, una prova non
  misurata, poi pp512 e tg128 come llama-bench: il prompt è di token casuali, la
  generazione parte da un contesto vuoto);
- Liyab: `liyab-cli --json` sul prompt del caso liyab-velocita (circa 512 token, passato
  dal ChatML di Qwen3, che chiede di contare fino a 1000), 128 token, R volte dopo una
  prova non misurata, una volta con le sue impostazioni (le bozze dal testo decise da
  lui) e una con `--no-lookup` (senza bozze, come Inga);
- la memoria: il picco di memoria residente di ogni processo da `/usr/bin/time -v`, lo
  stesso modo per tutti e due (tutti e due mappano il GGUF: le pagine del file lette
  contano). Il runner non avvia `inga serve` ("avvia_inga": false): nient'altro di Inga
  in memoria.

Voto: la media dei rapporti di velocità Inga su Liyab senza bozze (1 = come Liyab).
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

P, N, R = 512, 128, 3
FRASI = 33  # circa 512 token con il tokenizer di Qwen3 (quante ne misura liyab-velocita)


def con_time(cmd, timeout=3600):
    """cmd sotto /usr/bin/time -v: stdout, stderr e il picco di memoria residente in MiB."""
    full = ["/usr/bin/time", "-v", *cmd]
    print("$ " + " ".join(cmd[:4]) + " ...", flush=True)
    p = subprocess.run(full, capture_output=True, text=True, timeout=timeout)
    m = re.search(r"Maximum resident set size \(kbytes\):\s*(\d+)", p.stderr)
    if p.returncode != 0:
        raise RuntimeError(f"{os.path.basename(cmd[0])} è uscito con {p.returncode}: {p.stderr[-1200:]}")
    return p.stdout, p.stderr, (round(int(m.group(1)) / 1024, 1) if m else None)


def liyab_prove(model, ctx, extra):
    prove = []
    for r in range(R + 1):
        testo = liyab.chatml(confronto._messaggi(FRASI, r, R))
        cmd = [os.path.join(liyab.cartella(), "liyab-cli"), "-m", model, "-p", testo, "-n", str(N),
               "--temp", "0", "--ctx", str(ctx), "--threads", str(os.cpu_count() or 4), "--json", *extra]
        so, _, picco = con_time(cmd)
        t = next(json.loads(x) for x in so.splitlines() if x.startswith("{") and '"turn"' in x)
        if r == 0:
            continue  # la prova non misurata: porta il file nella cache delle pagine
        pt, ct = t["prompt_tokens"], t["generated_tokens"]
        prove.append({"token_prompt": pt, "token_generati": ct, "picco_mib": picco,
                      "bozze": [t.get("draft_tokens_proposed"), t.get("draft_tokens_accepted")],
                      "pp": pt / (t["ttft_ms"] / 1000), "tg": (ct - 1) / (t["decode_ms"] / 1000)})
        print(f"    {extra or 'predefinito'} prova {r}: {pt} token, {prove[-1]['pp']:.1f} tok/s; "
              f"{ct} generati, {prove[-1]['tg']:.2f} tok/s; bozze {prove[-1]['bozze']}; picco {picco} MiB",
              flush=True)
    return {"pp": sum(p["pp"] for p in prove) / R, "tg": sum(p["tg"] for p in prove) / R,
            "picco_mib": max(p["picco_mib"] or 0 for p in prove) or None, "prove": prove}


def main():
    if not liyab.cartella():
        inga_api.write_result({"stato": "saltato", "motivo": "Liyab non c'è (IUC_LIYAB)"})
        return
    model, exe = os.environ["IUC_MODEL_PATH"], os.environ["IUC_INGA"]
    ctx = int(os.environ.get("IUC_CTX", "4096"))
    out = {}
    try:
        so, _, picco = con_time([exe, "bench", model, "-p", str(P), "-n", str(N), "-r", str(R), "--json"])
        rows = json.loads(so[so.index("["):])
        out["inga"] = {"pp": next(r["avg_ts"] for r in rows if r["n_prompt"] == P and r["n_gen"] == 0),
                       "tg": next(r["avg_ts"] for r in rows if r["n_gen"] == N and r["n_prompt"] == 0),
                       "picco_mib": picco, "righe": rows}
        print(f"    Inga: pp{P} {out['inga']['pp']:.1f}, tg{N} {out['inga']['tg']:.2f} tok/s, picco {picco} MiB",
              flush=True)
        out["liyab"] = liyab_prove(model, ctx, [])
        out["liyab_senza_bozze"] = liyab_prove(model, ctx, ["--no-lookup"])
    except (RuntimeError, StopIteration, ValueError, KeyError, subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    i, l, n = out["inga"], out["liyab"], out["liyab_senza_bozze"]
    pp, tg = i["pp"] / n["pp"], i["tg"] / n["tg"]
    voci = {f"lettura del prompt (~{P} token), Inga su Liyab": pp,
            f"generazione ({N} token), Inga su Liyab senza bozze": tg,
            f"generazione ({N} token), Inga su Liyab con le sue bozze": i["tg"] / l["tg"],
            "generazione, Inga (tok/s)": i["tg"], "generazione, Liyab senza bozze (tok/s)": n["tg"],
            "generazione, Liyab con le sue bozze (tok/s)": l["tg"],
            "picco di memoria residente, Inga (MiB)": i["picco_mib"],
            "picco di memoria residente, Liyab (MiB)": n["picco_mib"]}
    if i["picco_mib"] and n["picco_mib"]:
        voci["picco di memoria, Inga su Liyab"] = i["picco_mib"] / n["picco_mib"]
    print(f"prompt {pp:.2f}x, generazione {tg:.2f}x (con le bozze di Liyab {i['tg'] / l['tg']:.2f}x), "
          f"memoria Inga {i['picco_mib']} MiB, Liyab {n['picco_mib']} MiB")
    inga_api.write_result({"stato": "ok", "voto": (pp + tg) / 2, "voci": voci,
                           "dettagli": dict(out, liyab_commit=liyab.versione(), cpu=os.cpu_count())})


if __name__ == "__main__":
    main()
