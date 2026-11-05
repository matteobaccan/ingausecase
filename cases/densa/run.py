"""Caso densa: la generazione di un modello denso (Qwen3-4B Q4_K_M) sulla CPU di Inga, su un
runner con SMT (4 vCPU, 2 core), dove da 2 a 4 thread Inga guadagna poco (caso q6k).

- Scala: `inga bench -p 0 -n 128 -r 3 -t T --json` con 1, 2, 3 e 4 thread.
- Divisione del lavoro, con 2 e 4 thread, `inga bench -p 0 -n 128 -r 5 -t T --ab CHIAVE=VALORE`
  (le due varianti nello stesso processo, a ripetizioni alternate; gli stessi bit):
  `debug.cpu_task_kb` (i KiB di pesi di un compito, 64 di default) a 16 e 256,
  `debug.cpu_tasks_per_thread=1` (una sola fetta di righe per thread, come llama.cpp),
  `debug.cpu_spin_us=0` (i thread fermi dormono subito invece di girare 5 ms).
- Pagine grandi: `debug.weights_thp` (i pesi riordinati in memoria anonima con
  MADV_HUGEPAGE) si legge al caricamento, quindi niente --ab:
  esecuzioni alternate senza e con `--set debug.weights_thp=true` (ABAB, `-r 3`), con 2 e
  4 thread; durante quelle con la chiave il caso legge `AnonHugePages` del processo da
  /proc (se il kernel ha dato davvero pagine da 2 MiB).
- Profilo: `inga bench -p 0 -n 64 -r 1 -t T --profile` con 2 e 4 thread (il tempo per
  tipo di operazione per token).
Serve una build di Inga con le chiavi (ramo exp/0.45 o più recente). Il JSON tiene `lscpu`
e lo stato delle pagine grandi trasparenti del kernel.
Voto: il rapporto migliore fra le varianti con 4 thread (sopra 1: più veloce del default).
"""

import json
import os
import re
import subprocess
import sys
import threading
import time

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402

N, R_AB, R = 128, 5, 3
THREADS = (2, 4)
VARIANTI = ["debug.cpu_task_kb=16", "debug.cpu_task_kb=256", "debug.cpu_tasks_per_thread=1",
            "debug.cpu_spin_us=0"]
NUM = re.compile(r"[-+]?\d+(?:\.\d+)?")


def esegui(cmd, timeout=1800, picco=None):
    """Esegue `cmd`; con `picco` (una lista) vi aggiunge il massimo di AnonHugePages (kB)
    del processo, letto ogni secondo."""
    print("$ " + " ".join(cmd), flush=True)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    massimo = [0]
    if picco is not None:
        def guarda():
            while p.poll() is None:
                try:
                    with open(f"/proc/{p.pid}/smaps_rollup") as f:
                        for riga in f:
                            if riga.startswith("AnonHugePages:"):
                                massimo[0] = max(massimo[0], int(riga.split()[1]))
                except OSError:
                    pass
                time.sleep(1)
        threading.Thread(target=guarda, daemon=True).start()
    so, se = p.communicate(timeout=timeout)
    print(so, flush=True)
    if picco is not None:
        picco.append(massimo[0])
    if p.returncode != 0:
        raise RuntimeError(f"{os.path.basename(cmd[0])} è uscito con {p.returncode}: {(se or so)[-1500:]}")
    return so


def tg(exe, model, t, extra=(), picco=None):
    js = esegui([exe, *extra, "bench", model, "-p", "0", "-n", str(N), "-r", str(R), "-t", str(t), "--json"],
                picco=picco)
    rows = json.loads(js[js.index("["):])
    return next(r["avg_ts"] for r in rows if r["n_gen"] == N and r["n_prompt"] == 0)


def ab(exe, model, t, variante):
    """La riga tg128 della tabella di --ab: (t/s default, t/s variante, rapporto, riga)."""
    out = esegui([exe, "bench", model, "-p", "0", "-n", str(N), "-r", str(R_AB), "-t", str(t),
                  "--ab", variante])
    for riga in out.splitlines():
        celle = [c.strip() for c in riga.strip().strip("|").split("|")]
        if len(celle) >= 7 and celle[3] == f"tg{N}":
            a, b, r = (float(NUM.search(c).group()) for c in celle[4:7])
            return a, b, r, riga.strip()
    raise RuntimeError(f"nessuna riga tg{N} nella tabella di --ab {variante}")


def leggi(path):
    try:
        with open(path) as f:
            return f.read().strip()
    except OSError as e:
        return f"(non letto: {e})"


def main():
    model, exe = os.environ["IUC_MODEL_PATH"], os.environ["IUC_INGA"]
    out = {"lscpu": subprocess.run(["lscpu"], capture_output=True, text=True).stdout,
           "cpu_logiche": os.cpu_count(),
           "thp_enabled": leggi("/sys/kernel/mm/transparent_hugepage/enabled"),
           "thp_defrag": leggi("/sys/kernel/mm/transparent_hugepage/defrag"),
           "kernel": os.uname().release}
    print(out["lscpu"], out["thp_enabled"], out["thp_defrag"], flush=True)
    voci = {}
    errori = []
    # La scala da 1 a 4 thread.
    for t in (1, 2, 3, 4):
        try:
            out[f"tg_t{t}"] = tg(exe, model, t)
        except (RuntimeError, StopIteration, ValueError, subprocess.TimeoutExpired) as e:
            errori.append(f"scala t{t}: {type(e).__name__}: {e}")
    if "tg_t2" in out and "tg_t4" in out:
        voci["da 2 a 4 thread (default)"] = out["tg_t4"] / out["tg_t2"]
    # Le varianti della divisione del lavoro.
    for t in THREADS:
        for v in VARIANTI:
            try:
                a, b, r, riga = ab(exe, model, t, v)
                out[f"ab_{v}_t{t}"] = {"default": a, "variante": b, "rapporto": r, "riga": riga}
                voci[f"{v} con {t} thread, sul default"] = r
            except (RuntimeError, ValueError, AttributeError, subprocess.TimeoutExpired) as e:
                errori.append(f"{v} t{t}: {type(e).__name__}: {e}")
    # Le pagine grandi, esecuzioni alternate.
    for t in THREADS:
        base, thp, picchi = [], [], []
        try:
            for _ in range(2):
                base.append(tg(exe, model, t))
                thp.append(tg(exe, model, t, ("--set", "debug.weights_thp=true"), picco=picchi))
        except (RuntimeError, StopIteration, ValueError, subprocess.TimeoutExpired) as e:
            errori.append(f"weights_thp t{t}: {type(e).__name__}: {e}")
        out[f"thp_t{t}"] = {"senza": base, "con": thp, "anon_huge_kb": picchi}
        if base and thp:
            voci[f"debug.weights_thp con {t} thread, sul default"] = (sum(thp) / len(thp)) / (sum(base) / len(base))
    # Il profilo per operazione.
    for t in THREADS:
        try:
            out[f"profilo_t{t}"] = esegui([exe, "bench", model, "-p", "0", "-n", "64", "-r", "1", "-t", str(t),
                                           "--profile"])
        except (RuntimeError, subprocess.TimeoutExpired) as e:
            errori.append(f"profilo t{t}: {type(e).__name__}: {e}")
    out["errori"] = errori
    for k, v in voci.items():
        print(f"{k}: {v:.3f}", flush=True)
    con4 = [v for k, v in voci.items() if k.endswith("con 4 thread, sul default")]
    if not con4:
        inga_api.write_result({"stato": "errore", "motivo": "; ".join(errori) or "nessuna misura",
                               "dettagli": out})
        return
    inga_api.write_result({"stato": "ok", "voto": max(con4), "voci": voci, "dettagli": out})


if __name__ == "__main__":
    main()
