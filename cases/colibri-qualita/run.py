"""Caso colibri-qualita: le stesse domande a Inga e a Colibri, sullo stesso file del modello.

ARC domande di ARC-Challenge e GSM domande di GSM8K (le prime delle domande fisse dei
casi arc e gsm8k, dati.json), fatte e valutate come in quei casi, a Inga e a `coli
serve` con lo stesso GGUF, greedy. Voto: la parte di risposte giuste di Inga; le voci
dicono anche quella di Colibri, per test e in tutto, e quante risposte hanno lo stesso
testo. Un modello di un'architettura che Colibri non ha si dà come saltato.
"""

import os
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import dati  # noqa: E402
import inga_api  # noqa: E402

ARC, GSM = 20, 20


def main():
    arc, gsm = confronto.caso("arc"), confronto.caso("gsm8k")
    casi = {"ARC": (arc, 256), "GSM8K": (gsm, 512)}
    try:
        elementi = ([{"test": "ARC", "el": e} for e in arc.scegli(ARC)]
                    + [{"test": "GSM8K", "el": e} for e in gsm.scegli(GSM)])
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return

    def messaggi(x):
        return casi[x["test"]][0].messaggi(x["el"])

    def voto(x, testo):
        return casi[x["test"]][0].voto(x["el"], testo)

    r = confronto.esegui("colibri-qualita", elementi, messaggi, voto,
                         max_tokens=lambda x: casi[x["test"]][1], motori=("colibri",), scrivi=False,
                         dettagli={"arc": [x["el"]["id"] for x in elementi if x["test"] == "ARC"],
                                   "gsm8k": [x["el"]["indice"] for x in elementi if x["test"] == "GSM8K"]})
    if r.get("stato") == "ok":
        righe = r["dettagli"]["risposte"]
        for test in casi:
            mie = [riga for riga, x in zip(righe, elementi) if x["test"] == test]
            if mie:
                for m, nome in (("inga", "Inga"), ("colibri", "Colibri")):
                    r["voci"][f"{test}, {nome}"] = sum(riga[m]["voto"] for riga in mie) / len(mie)
    inga_api.write_result(r)


if __name__ == "__main__":
    main()
