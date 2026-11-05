"""Caso q6k: il secondo kernel Q6_K di generazione di Inga (debug.q6k_kernel=v2, spento di
default) contro il primo, sulla stessa macchina.

`inga bench -p 0 -n 128 -r 5 -t T --ab debug.q6k_kernel=v2` con 2 e 4 thread: le due
varianti nello stesso processo, a ripetizioni alternate, e il rapporto v2 / v1 della
tabella di --ab. Serve una build di Inga che abbia la chiave (ramo exp/0.45-q6k o più
recente): con una che non la conosce il caso dice errore. Il JSON tiene `lscpu`.
Voto: il rapporto con 4 thread.
"""

import os
import re
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402

N, R, THREADS = 128, 5, (2, 4)
NUM = re.compile(r"[-+]?\d+(?:\.\d+)?")


def esegui(cmd, timeout=1800):
    print("$ " + " ".join(cmd), flush=True)
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    print(p.stdout, flush=True)
    if p.returncode != 0:
        raise RuntimeError(f"{os.path.basename(cmd[0])} è uscito con {p.returncode}: "
                           f"{(p.stderr or p.stdout)[-1500:]}")
    return p.stdout


def ab(exe, model, t):
    """La riga tg128 della tabella di --ab: (t/s v1, t/s v2, rapporto, testo della riga)."""
    out = esegui([exe, "bench", model, "-p", "0", "-n", str(N), "-r", str(R), "-t", str(t),
                  "--ab", "debug.q6k_kernel=v2"])
    for riga in out.splitlines():
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if len(celle) >= 7 and celle[3] == f"tg{N}":
            v1, v2, r = (float(NUM.search(c).group()) for c in celle[4:7])
            return v1, v2, r, riga.strip()
    raise RuntimeError(f"nessuna riga tg{N} nella tabella di --ab")


def main():
    model, exe = os.environ["IUC_MODEL_PATH"], os.environ["IUC_INGA"]
    out = {"lscpu": subprocess.run(["lscpu"], capture_output=True, text=True).stdout,
           "cpu_logiche": os.cpu_count()}
    print(out["lscpu"], flush=True)
    voci = {}
    try:
        for t in THREADS:
            v1, v2, r, riga = ab(exe, model, t)
            out[f"v1_tg_t{t}"], out[f"v2_tg_t{t}"], out[f"riga_t{t}"] = v1, v2, riga
            voci[f"generazione con {t} thread, kernel Q6_K v2 su v1"] = r
    except (RuntimeError, ValueError, AttributeError, subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    for k, v in voci.items():
        print(f"{k}: {v:.3f}", flush=True)
    inga_api.write_result({
        "stato": "ok",
        "voto": voci["generazione con 4 thread, kernel Q6_K v2 su v1"],
        "voci": voci,
        "dettagli": out,
    })


if __name__ == "__main__":
    main()
