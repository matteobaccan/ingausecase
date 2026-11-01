"""Caso arc: domande di scienze a scelta multipla (ARC-Challenge, test), Inga contro
llama.cpp.

DOMANDE domande fisse (seed) del test di ARC-Challenge (dati.json, licenza CC BY-SA
4.0), a Inga e a llama-server con lo stesso file del modello, greedy. La risposta è
"Answer: <lettera>"; giusta se è la lettera di ARC.
"""

import os
import random
import re
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import dati  # noqa: E402
import inga_api  # noqa: E402

DOMANDE = 60
SEED = 9


def main():
    import pyarrow.parquet as pq
    try:
        righe = pq.read_table(dati.file("arc-challenge-test")).to_pylist()
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    rng = random.Random(SEED)
    scelte = sorted(rng.sample(range(len(righe)), DOMANDE))
    elementi = [righe[i] for i in scelte]

    def messaggi(el):
        opzioni = "\n".join(f"{l}. {t}" for l, t in zip(el["choices"]["label"], el["choices"]["text"]))
        return [{"role": "user", "content":
                 f"{el['question']}\n\n{opzioni}\n\nAnswer with the label of the right option only, "
                 "as 'Answer: <label>'."}]

    def voto(el, testo):
        etichette = "".join(el["choices"]["label"])
        m = re.search(r"Answer:\s*\**\(?([" + re.escape(etichette) + r"])\b", testo)
        if not m:
            m = re.search(r"\b([" + re.escape(etichette) + r"])\b", testo.strip()[:20])
        dato = m.group(1) if m else None
        return float(dato == el["answerKey"]), f"{dato} su {el['answerKey']}"

    confronto.esegui("arc", elementi, messaggi, voto, max_tokens=16,
                     dettagli={"seed": SEED, "id": [e["id"] for e in elementi]})


if __name__ == "__main__":
    main()
