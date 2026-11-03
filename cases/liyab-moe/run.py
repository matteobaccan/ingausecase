"""Caso liyab-moe: una mixture of experts più grande della RAM che le si dà, con Inga e con
Liyab, che leggono tutti e due dal disco gli esperti che non tengono in memoria.

Lo stesso GGUF (Qwen3-30B-A3B Q4_K_M), lo stesso budget di RAM: Inga con `--mem-limit`
(argomenti_serve di case.json), Liyab con `--memory-budget` (gli stessi GB, in MiB). Un
motore alla volta, la cache delle pagine svuotata prima di ognuno (se sudo lo permette),
come nel caso colibri-moe.

- velocità: il prompt di liyab-velocita (circa P token, N generati, R prove dopo una non
  misurata): Inga dall'API in streaming, Liyab dalle statistiche di `liyab-cli --json`
  (senza bozze);
- risposte: ARC domande di ARC-Challenge e GSM problemi di GSM8K (dei casi arc e gsm8k),
  greedy; a Liyab lo stesso dialogo passato dal ChatML di Qwen3;
- memoria: il picco residente del server di Inga (VmHWM) e di ogni processo di
  liyab-cli (/usr/bin/time).

Voto: la media dei rapporti di velocità Inga su Liyab.
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import dati  # noqa: E402
import inga_api  # noqa: E402
import liyab  # noqa: E402

P, N, R = 512, 128, 3
ARC, GSM = 6, 4


def ram_gb():
    args = json.loads(os.environ.get("IUC_ARGOMENTI_SERVE") or "[]")
    return float(args[args.index("--mem-limit") + 1].rstrip("GgBb"))


def main():
    if not liyab.cartella():
        inga_api.write_result({"stato": "saltato", "motivo": "Liyab non c'è (IUC_LIYAB)"})
        return
    model, ctx = os.environ["IUC_MODEL_PATH"], int(os.environ.get("IUC_CTX", "4096"))
    arc, gsm = confronto.caso("arc"), confronto.caso("gsm8k")
    casi = {"ARC": (arc, 256), "GSM8K": (gsm, 512)}
    try:
        elementi = ([{"test": "ARC", "el": e} for e in arc.scegli(ARC)]
                    + [{"test": "GSM8K", "el": e} for e in gsm.scegli(GSM)])
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    ram = ram_gb()
    budget = ["--memory-budget", str(int(ram * 1024))]
    out = {"ram_gb": ram}

    def voto(x, testo):
        v = casi[x["test"]][0].voto(x["el"], testo)
        return v[0] if isinstance(v, tuple) else v

    try:
        # Inga
        out["inga_cache_svuotata"] = confronto.svuota_cache()
        with confronto.IngaDelCaso() as m:
            frasi = confronto.frasi_per(m.url, m.extra(), P)
            out["inga"] = confronto.velocita(m.url, m.extra(), frasi, N, R)
            risposte_i = []
            for x in elementi:
                try:
                    t, _, _ = inga_api.chat(casi[x["test"]][0].messaggi(x["el"]),
                                            max_tokens=casi[x["test"]][1], url=m.url, extra=m.extra())
                except (RuntimeError, OSError, ValueError) as e:
                    t = f"[errore: {e}]"
                risposte_i.append(t)
                print(f"  Inga {x['test']}: {voto(x, t)}", flush=True)
            out["inga"]["picco_mib"] = round(m.info()["picco_rss_gb"] * 1e9 / 2**20, 1)
        # Liyab
        out["liyab_cache_svuotata"] = confronto.svuota_cache()
        liyab.misura(model, liyab.chatml(confronto._messaggi(10, 99, 1)), 8, ctx, ["--no-lookup", *budget])
        prove = [liyab.misura(model, liyab.chatml(confronto._messaggi(frasi, r, R)), N, ctx,
                              ["--no-lookup", *budget]) for r in range(R)]
        out["liyab"] = {"pp": sum(p["pp"] for p in prove) / R, "tg": sum(p["tg"] for p in prove) / R,
                        "prove": [{k: p[k] for k in ("pp", "tg", "token_prompt", "picco_mib")} for p in prove]}
        risposte_l, picchi = [], [p["picco_mib"] for p in prove]
        for x in elementi:
            try:
                g = liyab.misura(model, liyab.chatml(casi[x["test"]][0].messaggi(x["el"])),
                                 casi[x["test"]][1], ctx, ["--no-lookup", *budget], timeout=7200)
                t = g["risposta"]
                picchi.append(g["picco_mib"])
            except (RuntimeError, OSError, ValueError, StopIteration, subprocess.TimeoutExpired) as e:
                t = f"[errore: {e}]"
            risposte_l.append(t)
            print(f"  Liyab {x['test']}: {voto(x, t)}", flush=True)
        out["liyab"]["picco_mib"] = max(p for p in picchi if p) if any(picchi) else None
    except (RuntimeError, OSError, ValueError, KeyError, StopIteration, subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    gi = sum(voto(x, t) for x, t in zip(elementi, risposte_i)) / len(elementi)
    gl = sum(voto(x, t) for x, t in zip(elementi, risposte_l)) / len(elementi)
    pp, tg = out["inga"]["pp"] / out["liyab"]["pp"], out["inga"]["tg"] / out["liyab"]["tg"]
    voci = {f"lettura del prompt (~{P} token), Inga su Liyab": pp,
            f"generazione ({N} token), Inga su Liyab": tg,
            "lettura del prompt, Inga (tok/s)": out["inga"]["pp"], "lettura del prompt, Liyab (tok/s)": out["liyab"]["pp"],
            "generazione, Inga (tok/s)": out["inga"]["tg"], "generazione, Liyab (tok/s)": out["liyab"]["tg"],
            "picco di RAM, Inga (MiB)": out["inga"]["picco_mib"], "picco di RAM, Liyab (MiB)": out["liyab"]["picco_mib"],
            "risposte giuste, Inga": gi, "risposte giuste, Liyab": gl,
            "risposte con lo stesso testo": sum(a.strip() == b.strip() for a, b in zip(risposte_i, risposte_l)) / len(elementi)}
    print(f"budget {ram} GB; prompt {pp:.2f}x, generazione {tg:.2f}x; giuste Inga {gi:.2f}, Liyab {gl:.2f}; "
          f"picco Inga {out['inga']['picco_mib']} MiB, Liyab {out['liyab']['picco_mib']} MiB")
    out.update(risposte_inga=risposte_i, risposte_liyab=risposte_l, frasi=frasi, liyab=liyab.versione())
    inga_api.write_result({"stato": "ok", "voto": (pp + tg) / 2, "voci": voci, "dettagli": out})


if __name__ == "__main__":
    main()
