"""Caso thread: quanto della differenza di velocità in generazione fra Inga, llama.cpp e
Liyab viene dal numero di thread.

velocita e liyab-velocita lanciano Inga senza -t: in generazione Inga usa un thread per
core fisico (2 su un runner a 4 vCPU con SMT), llama.cpp e Liyab ne ricevono 4. Qui tutti e
tre generano 128 token con 2 e con 4 thread, 3 ripetizioni, sulla stessa macchina:
- Inga: `inga bench -p 0 -n 128 -r 3 -t T --json`;
- llama.cpp: `llama-bench -p 0 -n 128 -r 3 -t T -o json`;
- Liyab: `liyab-cli --threads T --json`, un prompt breve e 128 token, la media di 3 prove
  (i token dopo il primo sul tempo di decodifica, come liyab-velocita).
Il JSON tiene anche `lscpu`. Voto: Inga su llama.cpp con 4 thread ciascuno.
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402
import liyab  # noqa: E402
import llama  # noqa: E402

N, R, THREADS = 128, 3, (2, 4)


def esegui(cmd, timeout=1800):
    print("$ " + " ".join(cmd), flush=True)
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"{os.path.basename(cmd[0])} è uscito con {p.returncode}: "
                           f"{(p.stderr or p.stdout)[-1500:]}")
    return p.stdout


def tg_bench(cmd):
    js = esegui(cmd)
    rows = json.loads(js[js.index("["):])
    return next(r["avg_ts"] for r in rows if r["n_gen"] == N and r["n_prompt"] == 0)


def tg_liyab(model, ctx, t):
    testo = liyab.chatml([{"role": "user", "content": "Racconta la storia di Roma antica, in breve."}])
    liyab.genera(model, testo, 8, ctx)  # carica e scalda
    prove = []
    for _ in range(R):
        cmd = [os.path.join(liyab.cartella(), "liyab-cli"), "-m", model, "-p", testo, "-n", str(N),
               "--temp", "0", "--ctx", str(ctx), "--threads", str(t), "--json"]
        so = esegui(cmd)
        turno = next(json.loads(x) for x in so.splitlines() if x.startswith("{") and '"turn"' in x)
        ct, ms = turno["generated_tokens"], turno["decode_ms"]
        if ct < 2 or not ms:
            raise RuntimeError(f"liyab-cli senza token o senza tempi: {turno}")
        prove.append((ct - 1) / (ms / 1000))
    return sum(prove) / len(prove), prove


def main():
    model, exe = os.environ["IUC_MODEL_PATH"], os.environ["IUC_INGA"]
    ctx = int(os.environ.get("IUC_CTX", "2048"))
    out = {"lscpu": subprocess.run(["lscpu"], capture_output=True, text=True).stdout,
           "cpu_logiche": os.cpu_count()}
    print(out["lscpu"], flush=True)
    try:
        for t in THREADS:
            out[f"inga_tg_t{t}"] = tg_bench([exe, "bench", model, "-p", "0", "-n", str(N), "-r", str(R),
                                             "-t", str(t), "--json"])
            if llama.cartella():
                out[f"llama_tg_t{t}"] = tg_bench([llama.programma("llama-bench"), "-m", model, "-p", "0",
                                                  "-n", str(N), "-r", str(R), "-t", str(t), "-o", "json"])
            if liyab.cartella():
                out[f"liyab_tg_t{t}"], out[f"liyab_prove_t{t}"] = tg_liyab(model, ctx, t)
        # Inga come la lanciano velocita e liyab-velocita: senza -t.
        out["inga_tg_default"] = tg_bench([exe, "bench", model, "-p", "0", "-n", str(N), "-r", str(R), "--json"])
    except (RuntimeError, StopIteration, ValueError, subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    voci = {}
    for t in THREADS:
        if f"llama_tg_t{t}" in out:
            voci[f"generazione con {t} thread, Inga su llama.cpp"] = out[f"inga_tg_t{t}"] / out[f"llama_tg_t{t}"]
        if f"liyab_tg_t{t}" in out:
            voci[f"generazione con {t} thread, Inga su Liyab"] = out[f"inga_tg_t{t}"] / out[f"liyab_tg_t{t}"]
    voci["Inga con 4 thread su Inga con 2"] = out["inga_tg_t4"] / out["inga_tg_t2"]
    if "llama_tg_t4" in out:
        voci["llama.cpp con 4 thread su llama.cpp con 2"] = out["llama_tg_t4"] / out["llama_tg_t2"]
        voci["Inga senza -t su llama.cpp con 4 thread"] = out["inga_tg_default"] / out["llama_tg_t4"]
    for k, v in voci.items():
        print(f"{k}: {v:.3f}", flush=True)
    inga_api.write_result({
        "stato": "ok",
        "voto": voci.get("generazione con 4 thread, Inga su llama.cpp", voci["Inga con 4 thread su Inga con 2"]),
        "voci": voci,
        "dettagli": dict(out, llama_cpp=llama.versione() if llama.cartella() else None),
    })


if __name__ == "__main__":
    main()
