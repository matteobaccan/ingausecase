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


def scegli(domande=DOMANDE):
    """Le domande fisse del caso (le prime `domande` delle DOMANDE scelte con il seed)."""
    import pyarrow.parquet as pq
    righe = pq.read_table(dati.file("arc-challenge-test")).to_pylist()
    rng = random.Random(SEED)
    scelte = sorted(rng.sample(range(len(righe)), DOMANDE))[:domande]
    return [righe[i] for i in scelte]


def messaggi(el):
    opzioni = "\n".join(f"{l}. {t}" for l, t in zip(el["choices"]["label"], el["choices"]["text"]))
    return [{"role": "user", "content":
             f"{el['question']}\n\n{opzioni}\n\nAnswer with the label of the right option only, "
             "as 'Answer: <label>'."}]


def voto(el, testo):
    # "Answer: X" (l'ultimo, se il modello ragiona prima), poi "answer is X", poi
    # una lettera da sola all'inizio
    e = "[" + re.escape("".join(el["choices"]["label"])) + "]"
    m = (re.findall(r"Answer:\s*\**\(?(" + e + r")\b", testo)
         or re.findall(r"answer is\s*\**\(?(" + e + r")\b", testo, re.I)
         or re.findall(r"^\W*(" + e + r")\b", testo.strip()[:20]))
    dato = m[-1] if m else None
    return float(dato == el["answerKey"]), f"{dato} su {el['answerKey']}"


def main():
    try:
        elementi = scegli()
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    confronto.esegui("arc", elementi, messaggi, voto, max_tokens=256,
                     dettagli={"seed": SEED, "id": [e["id"] for e in elementi]})


if __name__ == "__main__":
    main()
