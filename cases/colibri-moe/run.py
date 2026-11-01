"""Caso colibri-moe: una mixture of experts più grande della RAM che le si dà, con Inga e
con Colibri, che leggono tutti e due dal disco gli esperti che non tengono in memoria.

Lo stesso GGUF (Qwen3-30B-A3B Q4_K_M, models.json), lo stesso budget di RAM: Inga con
`--mem-limit` (argomenti_serve di case.json), Colibri con `--ram` (RAM_GB, lo stesso
numero di GB). Un motore alla volta, perché il modello non sta due volte nei 16 GB del
runner: il runner non avvia Inga ("avvia_inga": false), lo avvia confronto.IngaDelCaso;
prima di ogni motore la cache delle pagine del sistema si svuota (se sudo lo permette),
così nessuno legge il file dalla RAM lasciata dall'altro.

Per ogni motore, appena pronto: la velocità come nel caso colibri-velocita (prompt di
circa P token, N token generati, R ripetizioni, dall'API in streaming), poi le risposte
a ARC domande di ARC-Challenge e GSM problemi di GSM8K (quelli dei casi arc e gsm8k),
valutate come in quei casi; il picco di memoria residente del processo (VmHWM, con i
figli) a fine prova. Voto: la media dei rapporti di velocità Inga su Colibri.
"""

import os
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import dati  # noqa: E402
import inga_api  # noqa: E402

P, N, R = 512, 128, 3
ARC, GSM = 6, 4


def ram_gb():
    """Il budget di --mem-limit di case.json (es. 8G), in GB per Colibri."""
    args = confronto.json.loads(os.environ.get("IUC_ARGOMENTI_SERVE") or "[]")
    v = args[args.index("--mem-limit") + 1]
    return int(float(v.rstrip("GgBb")))


def main():
    arc, gsm = confronto.caso("arc"), confronto.caso("gsm8k")
    casi = {"ARC": (arc, 256), "GSM8K": (gsm, 512)}
    try:
        elementi = ([{"test": "ARC", "el": e} for e in arc.scegli(ARC)]
                    + [{"test": "GSM8K", "el": e} for e in gsm.scegli(GSM)])
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    ram = ram_gb()
    stato = {}

    def misura(motore, url, extra):
        svuotata = confronto.svuota_cache()
        if "frasi" not in stato:
            stato["frasi"] = confronto.frasi_per(url, extra, P)
        v = confronto.velocita(url, extra, stato["frasi"], N, R)
        v["cache_svuotata"] = svuotata
        return v

    r = confronto.esegui("colibri-moe", elementi, lambda x: casi[x["test"]][0].messaggi(x["el"]),
                         lambda x, t: casi[x["test"]][0].voto(x["el"], t),
                         max_tokens=lambda x: casi[x["test"]][1], motori=("colibri",),
                         in_sequenza=True, inga=confronto.IngaDelCaso(), ram=ram, misura=misura,
                         scrivi=False, dettagli={"ram_gb": ram})
    if r.get("stato") != "ok":
        inga_api.write_result(r)
        return
    m = r["dettagli"].get("misure") or {}
    if "inga" not in m or "colibri" not in m:
        r.update(stato="errore", motivo="la velocità non è stata misurata su tutti e due i motori")
        inga_api.write_result(r)
        return
    pp = m["inga"]["pp"] / m["colibri"]["pp"]
    tg = m["inga"]["tg"] / m["colibri"]["tg"]
    giuste = {k: r["voci"][k] for k in ("Inga", "Colibri", "risposte con lo stesso testo")}
    r["voci"] = {f"lettura del prompt (~{P} token), Inga su Colibri": pp,
                 f"generazione ({N} token), Inga su Colibri": tg,
                 "risposte giuste, Inga": giuste["Inga"],
                 "risposte giuste, Colibri": giuste["Colibri"],
                 "risposte con lo stesso testo": giuste["risposte con lo stesso testo"]}
    r["voto"] = (pp + tg) / 2
    r["dettagli"]["frasi"] = stato.get("frasi")
    print(f"budget {ram} GB; prompt: Inga {m['inga']['pp']:.1f}, Colibri {m['colibri']['pp']:.1f} tok/s; "
          f"generazione: Inga {m['inga']['tg']:.2f}, Colibri {m['colibri']['tg']:.2f} tok/s; "
          f"giuste Inga {giuste['Inga']:.2f}, Colibri {giuste['Colibri']:.2f}")
    inga_api.write_result(r)


if __name__ == "__main__":
    main()
