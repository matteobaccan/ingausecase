"""Caso documenti: domande sulla wiki di AINews, con la risposta e la pagina citata.

Le 15 pagine con le risposte, 45 altre pagine della wiki (scelte con un seed fisso fra
quelle che non contengono nessuna delle risposte attese) e la Divina Commedia
(scaricata da fonti.json e controllata con il suo sha256) vanno in una collezione di
documenti di Inga (POST /api/inga/documents, indicizzata con il modello di embedding e
con BM25). Ogni domanda nomina la collezione (inga_documents): Inga cerca gli estratti
più vicini e li mette nel prompt; la risposta deve contenere il dato atteso e citare la
pagina giusta.
"""

import json
import os
import random
import re
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import fonti  # noqa: E402
import inga_api  # noqa: E402

WIKI = os.path.join(os.path.dirname(os.path.dirname(inga_api.case_dir())), "wiki")
COLLEZIONE = "wiki"
DISTRATTORE = "divina-commedia.pdf"
ALTRE_PAGINE = 45
SEED_PAGINE = 11
DIMENSIONE_PAGINE = (1200, 6000)  # byte: pagine né vuote né troppo lunghe

SISTEMA = (
    "Rispondi alle domande usando solo gli estratti dati, che vengono da pagine di una "
    "wiki di notizie sull'intelligenza artificiale e da altri testi. Rispondi in "
    "italiano con una frase breve che contenga il dato chiesto, e indica in 'sorgente' il "
    "numero [n] dell'estratto da cui viene la risposta."
)


def compatto(s):
    return re.sub(r"[\s.,'’\-]", "", str(s).casefold())


def leggi(pagina):
    with open(os.path.join(WIKI, pagina + ".md"), encoding="utf-8") as f:
        return f.read()


def altre_pagine(domande):
    """ALTRE_PAGINE pagine della wiki, fisse (seed), che non contengono nessuna risposta."""
    giuste = {q["pagina"] for q in domande}
    risposte = [compatto(r) for q in domande for r in q["risposte"]]
    candidati = []
    for cartella in sorted(os.listdir(WIKI)):
        if not os.path.isdir(os.path.join(WIKI, cartella)):
            continue
        for nome in sorted(os.listdir(os.path.join(WIKI, cartella))):
            pagina = f"{cartella}/{nome[:-3]}"
            if not nome.endswith(".md") or pagina in giuste:
                continue
            size = os.path.getsize(os.path.join(WIKI, pagina + ".md"))
            if DIMENSIONE_PAGINE[0] <= size <= DIMENSIONE_PAGINE[1]:
                candidati.append(pagina)
    random.Random(SEED_PAGINE).shuffle(candidati)
    scelte = []
    for pagina in candidati:
        t = compatto(leggi(pagina))
        if not any(r in t for r in risposte):
            scelte.append(pagina)
        if len(scelte) == ALTRE_PAGINE:
            return sorted(scelte)
    raise RuntimeError("non ci sono abbastanza pagine senza le risposte")


def main():
    with open(os.path.join(inga_api.case_dir(), "domande.json"), encoding="utf-8") as f:
        domande = json.load(f)
    pagine = sorted({q["pagina"] for q in domande}) + altre_pagine(domande)
    for p in pagine:
        inga_api.add_document(COLLEZIONE, p + ".md", text=leggi(p))
    print(f"{len(pagine)} pagine della wiki nella collezione {COLLEZIONE}")
    try:
        commedia = fonti.in_collezione(inga_api, COLLEZIONE, "divina-commedia", DISTRATTORE)
    except fonti.Cambiato as e:
        print(f"caso in errore: {e}")
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    except OSError as e:
        motivo = f"la Divina Commedia non si scarica: {e}"
        print(f"caso saltato: {motivo}")
        inga_api.write_result({"stato": "saltato", "motivo": motivo})
        return
    schema = {
        "type": "object",
        "properties": {
            "risposta": {"type": "string", "maxLength": 400},
            "sorgente": {"type": "integer", "minimum": 1, "maximum": 99},
        },
        "required": ["risposta", "sorgente"],
    }
    # la pagina citata è quella dell'estratto [n] indicato in "sorgente", come Inga
    # numera gli estratti nel prompt; "sorgente" viene dopo "risposta" in ordine
    # alfabetico, l'ordine in cui Inga scrive le chiavi
    risposte_ok = pagine_ok = trovate = 0
    quota = []
    modi = {}
    righe = []
    for q in domande:
        msgs = [{"role": "system", "content": SISTEMA},
                {"role": "user", "content": q["domanda"]}]
        try:
            dato, raw, sec = inga_api.chat(msgs, schema=schema, max_tokens=300,
                                           extra={"inga_documents": [{"collection": COLLEZIONE}]})
            info = raw["choices"][0]["message"].get("inga_documents") or {}
        except (ValueError, RuntimeError) as e:
            print(f"{q['id']}: risposta non valida: {e}")
            dato, info, sec = {}, {}, 0.0
        modo = info.get("mode", "nessuno")
        modi[modo] = modi.get(modo, 0) + 1
        estratti = info.get("excerpts") or []
        documenti = [e.get("document") for e in estratti]
        trovata = q["pagina"] + ".md" in documenti
        if estratti:
            quota.append(documenti.count(commedia["nome"]) / len(estratti))
        risposta = str(dato.get("risposta", ""))
        r_ok = any(compatto(r) in compatto(risposta) for r in q["risposte"])
        per_numero = {e.get("n"): e.get("document") for e in estratti}
        citata = per_numero.get(dato.get("sorgente"))
        p_ok = citata == q["pagina"] + ".md"
        risposte_ok += r_ok
        pagine_ok += p_ok
        trovate += trovata
        print(f"{q['id']:2d}: risposta {'ok' if r_ok else 'NO'}, pagina {'ok' if p_ok else 'NO'} "
              f"([{dato.get('sorgente')}] {citata}), pagina giusta fra gli estratti {'sì' if trovata else 'no'}, "
              f"{len(estratti)} estratti, {sec:.1f} s: {risposta[:120]}")
        righe.append({"id": q["id"], "risposta": risposta, "estratto_citato": dato.get("sorgente"),
                      "pagina_data": citata,
                      "pagina_attesa": q["pagina"], "risposta_ok": r_ok, "pagina_ok": p_ok,
                      "pagina_fra_gli_estratti": trovata, "estratti": documenti,
                      "modo_documenti": modo, "secondi": round(sec, 1)})
    n = len(domande)
    inga_api.write_result({
        "stato": "ok",
        "voto": (risposte_ok + pagine_ok) / (2 * n),
        "voci": {"risposta giusta": risposte_ok / n, "pagina giusta": pagine_ok / n,
                 "pagina giusta fra gli estratti": trovate / n,
                 "estratti dal distrattore": sum(quota) / len(quota) if quota else 0.0},
        "dettagli": {"domande": n, "pagine_della_wiki": pagine, "divina_commedia": commedia,
                     "modo_documenti": modi, "risposte": righe},
    })


if __name__ == "__main__":
    main()
