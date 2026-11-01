"""Caso ifeval: richieste con istruzioni verificabili (IFEval), Inga contro llama.cpp.

DOMANDE richieste fisse (seed) di IFEval (dati.json, licenza Apache 2.0), fra quelle
con solo istruzioni controllabili da verifiche.py, a Inga e a llama-server con lo
stesso file del modello, greedy. Il voto di una risposta è la quota delle sue
istruzioni rispettate (IFEval "instruction-level, strict"); la voce "richieste con
tutte le istruzioni" è quella "prompt-level".
"""

import json
import os
import random
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import confronto  # noqa: E402
import dati  # noqa: E402
import inga_api  # noqa: E402
from verifiche import VERIFICHE  # noqa: E402

DOMANDE = 30
SEED = 10


def main():
    try:
        with open(dati.file("ifeval"), encoding="utf-8") as f:
            righe = [json.loads(line) for line in f if line.strip()]
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    adatte = [r for r in righe if all(i in VERIFICHE for i in r["instruction_id_list"])]
    rng = random.Random(SEED)
    elementi = sorted(rng.sample(adatte, DOMANDE), key=lambda r: r["key"])

    def messaggi(el):
        return [{"role": "user", "content": el["prompt"]}]

    def voto(el, testo):
        esiti = []
        for iid, kw in zip(el["instruction_id_list"], el["kwargs"]):
            kw = {k: v for k, v in (kw or {}).items() if v is not None}
            try:
                esiti.append(bool(VERIFICHE[iid](testo, kw)))
            except (KeyError, TypeError, ValueError):
                esiti.append(False)
        mancate = [i.split(":")[1] for i, e in zip(el["instruction_id_list"], esiti) if not e]
        return sum(esiti) / len(esiti), "tutte" if not mancate else "no " + ",".join(mancate)

    confronto.esegui("ifeval", elementi, messaggi, voto, max_tokens=700,
                     dettagli={"seed": SEED, "chiavi": [e["key"] for e in elementi],
                               "richieste_adatte": len(adatte)})
    # la quota delle richieste con tutte le istruzioni rispettate (prompt-level)
    path = os.environ["IUC_RESULT"]
    with open(path, encoding="utf-8") as f:
        res = json.load(f)
    if res.get("stato") == "ok":
        rr = res["dettagli"]["risposte"]
        for m in ("inga", "llama.cpp"):
            nome = "Inga" if m == "inga" else "llama.cpp"
            res["voci"][f"richieste con tutte le istruzioni, {nome}"] = \
                sum(r[m]["voto"] == 1.0 for r in rr) / len(rr)
        inga_api.write_result(res)


if __name__ == "__main__":
    main()
