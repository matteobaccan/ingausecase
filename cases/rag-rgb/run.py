"""Caso rag-rgb: risposte da documenti rumorosi e rifiuto quando la risposta non c'è.

Dati: RGB (Chen et al., "Benchmarking Large Language Models in Retrieval-Augmented
Generation", AAAI 2024), file en_refine.json, scaricato a ogni esecuzione (dati.json;
licenza CC BY-NC-SA 4.0, uso non commerciale). Ogni domanda di RGB ha passaggi di
notizie che contengono la risposta (positive) e passaggi sullo stesso tema che non la
contengono (negative).

Due collezioni di documenti di Inga, con un sottoinsieme fisso (seed):
- rumore: per RUMORE domande, POSITIVI passaggi positivi e NEGATIVI negativi ciascuna;
  la risposta deve contenere il dato atteso (come in RGB: per ogni parte della risposta,
  una delle sue varianti);
- rifiuto: per RIFIUTO altre domande, solo NEGATIVI_RIFIUTO passaggi negativi; la
  risposta giusta è dire che negli estratti non c'è (found: false), senza darla lo stesso.
Ogni domanda nomina la sua collezione (inga_documents): Inga cerca gli estratti e li
mette nel prompt, come nella chat.
"""

import json
import os
import random
import re
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import dati  # noqa: E402
import inga_api  # noqa: E402

RUMORE, RIFIUTO = 20, 20
POSITIVI, NEGATIVI, NEGATIVI_RIFIUTO = 3, 3, 5
SEED = 5

SISTEMA = (
    "Answer the question using only the excerpts given, which come from news articles. "
    "Answer in English with one short sentence that contains the fact asked for. If the "
    "excerpts do not contain the answer, set found to false and say so in answer; do not "
    "answer from your own knowledge."
)
SCHEMA = {
    "type": "object",
    "properties": {"answer": {"type": "string", "maxLength": 300}, "found": {"type": "boolean"}},
    "required": ["answer", "found"],
}


def norm(s):
    return re.sub(r"[\s.,'’\-]", "", str(s).casefold())


def giusta(risposta, attese):
    """Come RGB: ogni parte della risposta attesa (una lista di varianti) c'è."""
    r = norm(risposta)
    gruppi = [a if isinstance(a, list) else [a] for a in attese]
    return all(any(norm(v) in r for v in g) for g in gruppi)


def chiedi(q, collezione):
    msgs = [{"role": "system", "content": SISTEMA}, {"role": "user", "content": q["query"]}]
    try:
        dato, raw, sec = inga_api.chat(msgs, schema=SCHEMA, max_tokens=200,
                                       extra={"inga_documents": [{"collection": collezione}]})
        info = raw["choices"][0]["message"].get("inga_documents") or {}
    except (ValueError, RuntimeError) as e:
        print(f"{q['id']}: risposta non valida: {e}")
        return {}, {}, 0.0
    return dato, info, sec


def main():
    try:
        with open(dati.file("rgb-en"), encoding="utf-8") as f:
            righe = [json.loads(line) for line in f if line.strip()]
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    except OSError as e:
        inga_api.write_result({"stato": "saltato", "motivo": f"i dati di RGB non si scaricano: {e}"})
        return
    adatte = [r for r in righe if len(r["positive"]) >= POSITIVI and len(r["negative"]) >= NEGATIVI_RIFIUTO]
    random.Random(SEED).shuffle(adatte)
    rumore = sorted(adatte[:RUMORE], key=lambda r: r["id"])
    rifiuto = sorted(adatte[RUMORE:RUMORE + RIFIUTO], key=lambda r: r["id"])
    for q in rumore:
        for j, t in enumerate(q["positive"][:POSITIVI] + q["negative"][:NEGATIVI]):
            inga_api.add_document("rgb-rumore", f"q{q['id']}-{j}.txt", text=t)
    for q in rifiuto:
        for j, t in enumerate(q["negative"][:NEGATIVI_RIFIUTO]):
            inga_api.add_document("rgb-rifiuto", f"q{q['id']}-{j}.txt", text=t)
    print(f"{len(rumore)} domande con rumore, {len(rifiuto)} senza la risposta nei documenti")

    out = []
    ok_rumore = trovati_rumore = positivo_fra_estratti = 0
    for q in rumore:
        dato, info, sec = chiedi(q, "rgb-rumore")
        estratti = [e.get("document", "") for e in info.get("excerpts") or []]
        pos = any(e.startswith(f"q{q['id']}-") and int(e.split("-")[1].split(".")[0]) < POSITIVI
                  for e in estratti)
        ok = giusta(dato.get("answer", ""), q["answer"])
        ok_rumore += ok
        trovati_rumore += bool(dato.get("found"))
        positivo_fra_estratti += pos
        print(f"rumore {q['id']:3d}: {'ok' if ok else 'NO'}, passaggio giusto fra gli estratti "
              f"{'sì' if pos else 'no'}, {sec:.1f} s: {str(dato.get('answer', ''))[:120]}")
        out.append({"id": q["id"], "tipo": "rumore", "domanda": q["query"], "attesa": q["answer"],
                    "risposta": dato.get("answer"), "found": dato.get("found"), "ok": ok,
                    "positivo_fra_estratti": pos, "estratti": estratti, "secondi": round(sec, 1)})
    ok_rifiuto = 0
    for q in rifiuto:
        dato, info, sec = chiedi(q, "rgb-rifiuto")
        # come RGB: un rifiuto che poi dà la risposta (dal modello, non dagli estratti)
        # non è un rifiuto
        ok = dato.get("found") is False and not giusta(dato.get("answer", ""), q["answer"])
        ok_rifiuto += ok
        print(f"rifiuto {q['id']:3d}: {'ok' if ok else 'NO'}, {sec:.1f} s: {str(dato.get('answer', ''))[:120]}")
        out.append({"id": q["id"], "tipo": "rifiuto", "domanda": q["query"], "attesa": q["answer"],
                    "risposta": dato.get("answer"), "found": dato.get("found"), "ok": ok,
                    "secondi": round(sec, 1)})
    a, b = ok_rumore / len(rumore), ok_rifiuto / len(rifiuto)
    inga_api.write_result({
        "stato": "ok",
        "voto": (a + b) / 2,
        "voci": {"risposta giusta con rumore": a, "rifiuto senza la risposta": b,
                 "passaggio giusto fra gli estratti": positivo_fra_estratti / len(rumore),
                 "risposte date con rumore": trovati_rumore / len(rumore)},
        "dettagli": {"seed": SEED, "risposte": out},
    })


if __name__ == "__main__":
    main()
