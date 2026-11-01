"""Caso gsm8k: problemi di aritmetica a parole (GSM8K, test), Inga contro llama.cpp.

DOMANDE problemi fissi (seed) del test di GSM8K (dati.json, licenza MIT), a Inga e a
llama-server con lo stesso file del modello, greedy. Il modello ragiona e chiude con
"Answer: <numero>"; giusto se il numero è quello di GSM8K (dopo "####").
"""

import os
import random
import re
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import dati  # noqa: E402
import inga_api  # noqa: E402

DOMANDE = 30
SEED = 8
ISTRUZIONE = ("Solve the problem step by step, briefly. Then write the final answer on the "
              "last line as 'Answer: <number>' (only the number, no units).")


def numero(s):
    s = s.replace(",", "").replace("$", "")
    m = re.findall(r"-?\d+(?:\.\d+)?", s)
    return float(m[-1]) if m else None


def scegli(domande=DOMANDE):
    """I problemi fissi del caso (i primi `domande` dei DOMANDE scelti con il seed),
    ognuno con il suo indice nel test."""
    import pyarrow.parquet as pq
    righe = pq.read_table(dati.file("gsm8k-test")).to_pylist()
    rng = random.Random(SEED)
    scelte = sorted(rng.sample(range(len(righe)), DOMANDE))[:domande]
    return [dict(righe[i], indice=i) for i in scelte]


def messaggi(el):
    return [{"role": "user", "content": f"{el['question']}\n\n{ISTRUZIONE}"}]


def voto(el, testo):
    atteso = numero(el["answer"].split("####")[-1])
    m = re.findall(r"Answer:\s*([^\n]+)", testo)
    dato = numero(m[-1]) if m else numero(testo)
    ok = dato is not None and atteso is not None and abs(dato - atteso) < 1e-6
    return float(ok), f"{dato} su {atteso}"


def main():
    try:
        elementi = scegli()
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    confronto.esegui("gsm8k", elementi, messaggi, voto, max_tokens=512,
                     dettagli={"seed": SEED, "indici": [e["indice"] for e in elementi]})


if __name__ == "__main__":
    main()
