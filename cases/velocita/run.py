"""Caso velocita: Inga contro llama.cpp sullo stesso file del modello, sulla stessa macchina.

- velocità: `inga bench -p 512 -n 128 -r 3 --json` e `llama-bench -p 512 -n 128 -r 3
  -o json`, con tutti i thread della macchina; la lettura del prompt (pp512) e la
  generazione (tg128) di Inga divise per quelle di llama.cpp;
- perplexity: `inga perplexity` e `llama-perplexity` sul test di wikitext-2 (il file che
  usa llama.cpp, dati.json), CHUNKS pezzi di 512 token; il rapporto deve stare vicino a 1
  (la rotazione notturna di Inga chiede l'1 %).
Il server di Inga avviato dal runner resta fermo intanto (non riceve richieste).
Voto: la media dei due rapporti di velocità (1 = come llama.cpp).
"""

import json
import os
import re
import subprocess
import sys
import zipfile

sys.path.insert(0, os.environ["IUC_TOOLS"])
import dati  # noqa: E402
import inga_api  # noqa: E402
import llama  # noqa: E402

CHUNKS = 40
P, N, R = 512, 128, 3


def esegui(cmd, timeout=3600):
    print("$ " + " ".join(cmd), flush=True)
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"{os.path.basename(cmd[0])} è uscito con {p.returncode}: "
                           f"{(p.stderr or p.stdout)[-1500:]}")
    return p.stdout, p.stderr


def main():
    if not llama.cartella():
        inga_api.write_result({"stato": "saltato", "motivo": "llama.cpp non c'è (IUC_LLAMA)"})
        return
    model, exe, t = os.environ["IUC_MODEL_PATH"], os.environ["IUC_INGA"], llama.threads()
    try:
        z = zipfile.ZipFile(dati.file("wikitext-2"))
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    testo = os.path.join(inga_api.work_dir(), "wiki.test.raw")
    with open(testo, "wb") as f:
        f.write(z.read("wikitext-2-raw/wiki.test.raw"))

    out = {}
    try:
        # velocità
        js, _ = esegui([exe, "bench", model, "-p", str(P), "-n", str(N), "-r", str(R), "--json"])
        rows = json.loads(js[js.index("["):])
        out["inga_pp"] = next(r["avg_ts"] for r in rows if r["n_prompt"] == P and r["n_gen"] == 0)
        out["inga_tg"] = next(r["avg_ts"] for r in rows if r["n_gen"] == N and r["n_prompt"] == 0)
        js, _ = esegui([llama.programma("llama-bench"), "-m", model, "-p", str(P), "-n", str(N),
                        "-r", str(R), "-t", t, "-o", "json"])
        rows = json.loads(js[js.index("["):])
        out["llama_pp"] = next(r["avg_ts"] for r in rows if r["n_prompt"] == P and r["n_gen"] == 0)
        out["llama_tg"] = next(r["avg_ts"] for r in rows if r["n_gen"] == N and r["n_prompt"] == 0)
        # perplexity
        so, se = esegui([exe, "perplexity", model, "-f", testo, "--ctx", "512", "--chunks", str(CHUNKS)])
        m = re.search(r"perplexity:\s*([\d.]+)\s*±\s*([\d.]+)", so + se)
        out["inga_ppl"], out["inga_ppl_err"] = float(m.group(1)), float(m.group(2))
        so, se = esegui([llama.programma("llama-perplexity"), "-m", model, "-f", testo, "-c", "512",
                         "--chunks", str(CHUNKS), "-t", t, "-b", "512"])
        m = re.search(r"Final estimate: PPL = ([\d.]+) \+/- ([\d.]+)", so + se)
        out["llama_ppl"], out["llama_ppl_err"] = float(m.group(1)), float(m.group(2))
    except (RuntimeError, StopIteration, ValueError, AttributeError, subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    pp, tg = out["inga_pp"] / out["llama_pp"], out["inga_tg"] / out["llama_tg"]
    ppl = out["inga_ppl"] / out["llama_ppl"]
    print(f"pp{P}: Inga {out['inga_pp']:.1f}, llama.cpp {out['llama_pp']:.1f} tok/s ({pp:.2f}x); "
          f"tg{N}: Inga {out['inga_tg']:.2f}, llama.cpp {out['llama_tg']:.2f} tok/s ({tg:.2f}x); "
          f"perplexity Inga {out['inga_ppl']:.4f}, llama.cpp {out['llama_ppl']:.4f} ({ppl:.4f})")
    inga_api.write_result({
        "stato": "ok",
        "voto": (pp + tg) / 2,
        "voci": {f"lettura del prompt (pp{P}), Inga su llama.cpp": pp,
                 f"generazione (tg{N}), Inga su llama.cpp": tg,
                 "perplexity, Inga su llama.cpp": ppl},
        "dettagli": dict(out, threads=int(t), chunks=CHUNKS, llama_cpp=llama.versione()),
    })


if __name__ == "__main__":
    main()
