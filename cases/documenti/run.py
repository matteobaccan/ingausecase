"""Caso documenti: domande sulla wiki di AINews, con la risposta e la pagina citata.

Per ogni domanda Inga riceve tre pagine della wiki come documenti (inga_documents):
la pagina con la risposta e due pagine della stessa cartella scelte con un seed fisso
fra quelle che non contengono la risposta, in ordine mescolato. Le pagine stanno
intere nel contesto: niente recupero per embedding (vedi README.md).
"""

import json
import os
import random
import re
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402

WIKI = os.path.join(os.path.dirname(os.path.dirname(inga_api.case_dir())), "wiki")
SEED_PAGINE = 11
DIMENSIONE_PAGINE = (1200, 6000)  # byte: pagine né vuote né troppo lunghe

SISTEMA = (
    "Rispondi alle domande usando solo i documenti dati, che sono pagine di una wiki di "
    "notizie sull'intelligenza artificiale. Rispondi in italiano con una frase breve che "
    "contenga il dato chiesto, e indica in 'pagina' il nome del documento da cui viene "
    "la risposta."
)


def compatto(s):
    return re.sub(r"[\s.,'’\-]", "", str(s).casefold())


def leggi(pagina):
    with open(os.path.join(WIKI, pagina + ".md"), encoding="utf-8") as f:
        return f.read()


def distrattori(q, rng):
    cartella = q["pagina"].split("/")[0]
    candidati = []
    for nome in sorted(os.listdir(os.path.join(WIKI, cartella))):
        pagina = f"{cartella}/{nome[:-3]}"
        if not nome.endswith(".md") or pagina == q["pagina"]:
            continue
        size = os.path.getsize(os.path.join(WIKI, pagina + ".md"))
        if not DIMENSIONE_PAGINE[0] <= size <= DIMENSIONE_PAGINE[1]:
            continue
        candidati.append(pagina)
    rng.shuffle(candidati)
    scelti = []
    for pagina in candidati:
        t = compatto(leggi(pagina))
        if not any(compatto(r) in t for r in q["risposte"]):
            scelti.append(pagina)
        if len(scelti) == 2:
            return scelti
    raise RuntimeError(f"domanda {q['id']}: distrattori non trovati")


def main():
    with open(os.path.join(inga_api.case_dir(), "domande.json"), encoding="utf-8") as f:
        domande = json.load(f)
    risposte_ok = pagine_ok = 0
    modi = {}
    righe = []
    for q in domande:
        rng = random.Random(SEED_PAGINE * 1000 + q["id"])
        pagine = [q["pagina"]] + distrattori(q, rng)
        rng.shuffle(pagine)
        schema = {
            "type": "object",
            "properties": {
                "risposta": {"type": "string", "maxLength": 400},
                "pagina": {"type": "string", "enum": pagine},
            },
            "required": ["risposta", "pagina"],
        }
        docs = [{"name": p, "text": leggi(p)} for p in pagine]
        msgs = [{"role": "system", "content": SISTEMA},
                {"role": "user", "content": q["domanda"]}]
        try:
            dato, raw, sec = inga_api.chat(msgs, schema=schema, max_tokens=300,
                                           extra={"inga_documents": docs})
            info = raw["choices"][0]["message"].get("inga_documents") or {}
        except (ValueError, RuntimeError) as e:
            print(f"{q['id']}: risposta non valida: {e}")
            dato, info, sec = {}, {}, 0.0
        modo = info.get("mode", "nessuno")
        modi[modo] = modi.get(modo, 0) + 1
        risposta = str(dato.get("risposta", ""))
        r_ok = any(compatto(r) in compatto(risposta) for r in q["risposte"])
        p_ok = dato.get("pagina") == q["pagina"]
        risposte_ok += r_ok
        pagine_ok += p_ok
        print(f"{q['id']:2d}: risposta {'ok' if r_ok else 'NO'}, pagina {'ok' if p_ok else 'NO'} "
              f"({dato.get('pagina')}), {modo}, {sec:.1f} s: {risposta[:120]}")
        righe.append({"id": q["id"], "risposta": risposta, "pagina_data": dato.get("pagina"),
                      "pagina_attesa": q["pagina"], "pagine_date": pagine,
                      "risposta_ok": r_ok, "pagina_ok": p_ok, "modo_documenti": modo,
                      "secondi": round(sec, 1)})
    n = len(domande)
    inga_api.write_result({
        "stato": "ok",
        "voto": (risposte_ok + pagine_ok) / (2 * n),
        "voci": {"risposta giusta": risposte_ok / n, "pagina giusta": pagine_ok / n},
        "dettagli": {"domande": n, "modo_documenti": modi, "risposte": righe},
    })


if __name__ == "__main__":
    main()
