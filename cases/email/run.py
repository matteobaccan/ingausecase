"""Caso email: smistamento di email e ticket per urgenza e reparto.

Ogni messaggio di messaggi.json va classificato con l'output strutturato (enum) e
confrontato con l'etichetta scritta a mano.
"""

import json
import os
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402

URGENZE = ["alta", "media", "bassa"]
REPARTI = ["amministrazione", "assistenza_tecnica", "commerciale", "logistica", "risorse_umane"]

SCHEMA = {
    "type": "object",
    "properties": {
        "urgenza": {"type": "string", "enum": URGENZE},
        "reparto": {"type": "string", "enum": REPARTI},
    },
    "required": ["urgenza", "reparto"],
}

SISTEMA = (
    "Smisti le email e i ticket che arrivano a un'azienda italiana di distribuzione. "
    "Per ogni messaggio indica l'urgenza e il reparto che deve occuparsene.\n"
    "Urgenza: alta = un'attività è bloccata, c'è un pericolo o un danno in corso, o una "
    "scadenza entro oggi o domani; media = un problema o una richiesta da risolvere nei "
    "prossimi giorni; bassa = informazioni o richieste senza fretta.\n"
    "Reparti: amministrazione (fatture, pagamenti, contabilità, banche, tasse); "
    "assistenza_tecnica (computer, rete, programmi, stampanti, sito, dispositivi); "
    "commerciale (clienti, preventivi, offerte, listini, gare, agenti); logistica "
    "(spedizioni, consegne, corrieri, magazzino, merce); risorse_umane (personale, buste "
    "paga, ferie, assunzioni, permessi, formazione, infortuni)."
)


def main():
    with open(os.path.join(inga_api.case_dir(), "messaggi.json"), encoding="utf-8") as f:
        messaggi = json.load(f)
    conf = {"urgenza": {}, "reparto": {}}
    giusti = {"urgenza": 0, "reparto": 0}
    entrambi = 0
    errori = []
    for m in messaggi:
        msgs = [{"role": "system", "content": SISTEMA},
                {"role": "user", "content": m["testo"]}]
        try:
            dato, _, sec = inga_api.chat(msgs, schema=SCHEMA, max_tokens=64)
        except (ValueError, RuntimeError) as e:
            print(f"{m['id']}: risposta non valida: {e}")
            dato, sec = {}, 0.0
        esito = {}
        for k in ("urgenza", "reparto"):
            atteso, dato_k = m[k], dato.get(k, "-")
            esito[k] = atteso == dato_k
            giusti[k] += esito[k]
            key = f"{atteso} -> {dato_k}"
            conf[k][key] = conf[k].get(key, 0) + 1
        entrambi += all(esito.values())
        if not all(esito.values()):
            errori.append({"id": m["id"], "atteso": {k: m[k] for k in esito}, "dato": dato})
        print(f"{m['id']:2d}: urgenza {dato.get('urgenza')} ({'ok' if esito['urgenza'] else 'attesa ' + m['urgenza']}), "
              f"reparto {dato.get('reparto')} ({'ok' if esito['reparto'] else 'atteso ' + m['reparto']}), {sec:.1f} s")
    n = len(messaggi)
    # confusione: solo le coppie sbagliate, ordinate per frequenza
    confusione = {k: dict(sorted(((p, c) for p, c in v.items() if p.split(" -> ")[0] != p.split(" -> ")[1]),
                                 key=lambda x: -x[1])) for k, v in conf.items()}
    inga_api.write_result({
        "stato": "ok",
        "voto": (giusti["urgenza"] + giusti["reparto"]) / (2 * n),
        "voci": {"urgenza": giusti["urgenza"] / n, "reparto": giusti["reparto"] / n,
                 "entrambi giusti": entrambi / n},
        "dettagli": {"messaggi": n, "confusione": confusione, "errori": errori},
    })


if __name__ == "__main__":
    main()
