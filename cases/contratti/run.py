"""Caso contratti: domande con risposta nota su un contratto collettivo, con un distrattore.

Il contratto (il CCNL Commercio e Terziario di Conflavoro) e la Divina Commedia si
scaricano a ogni esecuzione dagli URL di fonti.json (mai nel repository) e si
controllano con il loro sha256 (tools/fonti.py). Tutti e due vanno in una collezione di
documenti di Inga (POST /api/inga/documents: Inga legge i PDF, li divide in chunk e li
indicizza con il modello di embedding e con BM25); ogni domanda nomina la collezione
(inga_documents) e Inga mette nel prompt gli estratti più vicini. La risposta deve
venire dal contratto: deve contenere il dato atteso e citare l'articolo giusto.

Il caso si salta, con il motivo, se un PDF non si scarica; si ferma con un errore se un
PDF scaricato non è quello controllato (sha256 diverso da fonti.json).
"""

import json
import os
import re
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import fonti  # noqa: E402
import inga_api  # noqa: E402

COLLEZIONE = "contratti"
CONTRATTO = "ccnl-commercio-terziario-conflavoro.pdf"
DISTRATTORE = "divina-commedia.pdf"

SISTEMA = (
    "Rispondi alle domande sul contratto collettivo nazionale di lavoro del commercio e "
    "del terziario usando solo gli estratti del contratto. Gli estratti possono venire "
    "anche da altri testi, che non c'entrano con il contratto: ignorali. Rispondi in "
    "italiano con una frase breve che contenga il dato chiesto, e indica in 'sorgente' "
    "il numero dell'articolo del contratto da cui viene la risposta (solo il numero, "
    "per esempio 12)."
)


def compatto(s):
    return re.sub(r"[\s.,'’\-]", "", str(s).casefold())


def numero_articolo(s):
    """'Art. 12 bis' -> '12 bis'; '12' -> '12'; None se non c'è un numero."""
    m = re.search(r"(\d+)(?:\s*(bis|ter|quater))?", str(s or ""), re.I)
    if not m:
        return None
    return m.group(1) + (" " + m.group(2).lower() if m.group(2) else "")


def esito(motivo, stato="saltato"):
    print(f"caso {stato}: {motivo}")
    inga_api.write_result({"stato": stato, "motivo": motivo})
    sys.exit(0)


def main():
    with open(os.path.join(inga_api.case_dir(), "domande.json"), encoding="utf-8") as f:
        domande = [q for q in json.load(f) if q.get("verificata")]
    if not domande:
        esito("nessuna domanda di cases/contratti/domande.json è verificata sul testo")
    caricati = []
    try:
        caricati.append(fonti.in_collezione(inga_api, COLLEZIONE, "ccnl", CONTRATTO))
        caricati.append(fonti.in_collezione(inga_api, COLLEZIONE, "divina-commedia", DISTRATTORE))
    except fonti.Cambiato as e:
        esito(str(e), "errore")
    except OSError as e:
        esito(f"un PDF di fonti.json non si scarica: {e}")
    nome_contratto = caricati[0]["nome"]

    schema = {"type": "object",
              "properties": {"risposta": {"type": "string", "maxLength": 400},
                             "sorgente": {"type": "string", "maxLength": 20}},
              "required": ["risposta", "sorgente"]}
    # "sorgente" e non "articolo": Inga scrive le chiavi in ordine alfabetico, e
    # l'articolo va scritto dopo la risposta, non prima
    ok_r = ok_a = trovate = 0
    quota = []
    righe = []
    for q in domande:
        try:
            dato, raw, sec = inga_api.chat(
                [{"role": "system", "content": SISTEMA}, {"role": "user", "content": q["domanda"]}],
                schema=schema, max_tokens=300, extra={"inga_documents": [{"collection": COLLEZIONE}]})
            info = raw["choices"][0]["message"].get("inga_documents") or {}
        except (ValueError, RuntimeError) as e:
            print(f"{q['id']}: risposta non valida: {e}")
            dato, info, sec = {}, {}, 0.0
        estratti = info.get("excerpts") or []
        dal_contratto = [e for e in estratti if e.get("document") == nome_contratto]
        cit = compatto(q["citazione"])
        trovata = any(cit in compatto(e.get("text", "")) for e in dal_contratto)
        risposta = str(dato.get("risposta", ""))
        r_ok = any(compatto(r) in compatto(risposta) for r in q["risposte"])
        a_ok = numero_articolo(dato.get("sorgente")) == numero_articolo(q["articolo"])
        ok_r += r_ok
        ok_a += a_ok
        trovate += trovata
        if estratti:
            quota.append(1 - len(dal_contratto) / len(estratti))
        print(f"{q['id']:2d}: risposta {'ok' if r_ok else 'NO'}, articolo {dato.get('sorgente')} "
              f"({'ok' if a_ok else 'atteso ' + q['articolo']}), citazione fra gli estratti "
              f"{'sì' if trovata else 'no'}, estratti {len(dal_contratto)} del contratto e "
              f"{len(estratti) - len(dal_contratto)} di altri testi, {sec:.1f} s: {risposta[:120]}")
        righe.append({"id": q["id"], "risposta": risposta, "articolo_dato": dato.get("sorgente"),
                      "articolo_atteso": q["articolo"], "risposta_ok": r_ok, "articolo_ok": a_ok,
                      "citazione_fra_gli_estratti": trovata,
                      "estratti": [{"documento": e.get("document"), "pagina": e.get("page"),
                                    "punteggio": e.get("score"), "da": e.get("retrievers")}
                                   for e in estratti],
                      "modo_documenti": info.get("mode", "nessuno"), "secondi": round(sec, 1)})
    n = len(domande)
    inga_api.write_result({
        "stato": "ok", "voto": (ok_r + ok_a) / (2 * n),
        "voci": {"risposta giusta": ok_r / n, "articolo giusto": ok_a / n,
                 "citazione fra gli estratti": trovate / n,
                 "estratti dal distrattore": sum(quota) / len(quota) if quota else 0.0},
        "dettagli": {"domande": n, "collezione": caricati, "risposte": righe},
    })


if __name__ == "__main__":
    main()
