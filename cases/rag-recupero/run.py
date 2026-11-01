"""Caso rag-recupero: la ricerca nelle collezioni di documenti, misurata su SciFact (BEIR).

Solo il recupero, senza il modello di chat: per ogni affermazione scientifica di
SciFact, gli abstract che Inga trova (GET /api/inga/documents/search, la stessa ricerca
che la chat fa con inga_documents: embedding, BM25 e fusione) confrontati con quelli
giudicati pertinenti da SciFact.

Dati (dati.json, scaricati a ogni esecuzione, CC BY-SA 4.0): le domande di test, i
giudizi e il corpus. Un sottoinsieme fisso (seed): DOMANDE domande, i loro abstract
pertinenti e altri abstract a caso fino a CORPUS. I numeri non sono confrontabili con
quelli pubblicati su SciFact intero (5183 abstract): servono a confrontare le versioni
di Inga fra loro.
"""

import json
import math
import os
import random
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import dati  # noqa: E402
import inga_api  # noqa: E402

COLLEZIONE = "scifact"
DOMANDE = 60
CORPUS = 1000
SEED = 7
K = 10


def jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    # una versione di Inga senza la ricerca diretta: il caso è saltato
    try:
        inga_api.search_documents(COLLEZIONE, "prova", k=1)
    except inga_api.NonDisponibile as e:
        inga_api.write_result({"stato": "saltato", "motivo": str(e)})
        return
    except RuntimeError:
        pass  # la collezione non c'è ancora: la ricerca diretta esiste
    try:
        corpus = {d["_id"]: d for d in jsonl(dati.file("scifact-corpus"))}
        queries = {q["_id"]: q["text"] for q in jsonl(dati.file("scifact-domande"))}
        giudizi = {}
        with open(dati.file("scifact-giudizi"), encoding="utf-8") as f:
            next(f)
            for line in f:
                qid, did, score = line.split()
                if int(score) > 0:
                    giudizi.setdefault(qid, set()).add(did)
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    except OSError as e:
        inga_api.write_result({"stato": "saltato", "motivo": f"i dati di SciFact non si scaricano: {e}"})
        return

    rng = random.Random(SEED)
    scelte = sorted(q for q in giudizi if q in queries)
    rng.shuffle(scelte)
    scelte = sorted(scelte[:DOMANDE], key=int)
    pertinenti = sorted({d for q in scelte for d in giudizi[q]})
    altri = sorted(set(corpus) - set(pertinenti))
    rng.shuffle(altri)
    documenti = sorted(pertinenti + altri[:CORPUS - len(pertinenti)])
    for i, did in enumerate(documenti):
        d = corpus[did]
        inga_api.add_document(COLLEZIONE, f"{did}.txt", text=f"{d.get('title', '')}\n\n{d['text']}")
        if (i + 1) % 200 == 0:
            print(f"{i + 1}/{len(documenti)} abstract nella collezione", flush=True)

    ndcg = rec = rec5 = mrr = 0.0
    righe = []
    for qid in scelte:
        attesi = giudizi[qid]
        passaggi = inga_api.search_documents(COLLEZIONE, queries[qid], k=3 * K)
        trovati = []
        for p in passaggi:
            did = str(p.get("document", "")).removesuffix(".txt")
            if did not in trovati:
                trovati.append(did)
        top = trovati[:K]
        dcg = sum(1 / math.log2(i + 2) for i, d in enumerate(top) if d in attesi)
        idcg = sum(1 / math.log2(i + 2) for i in range(min(len(attesi), K)))
        n = dcg / idcg
        r = len(attesi & set(top)) / len(attesi)
        r5 = len(attesi & set(top[:5])) / len(attesi)
        rr = next((1 / (i + 1) for i, d in enumerate(top) if d in attesi), 0.0)
        ndcg += n
        rec += r
        rec5 += r5
        mrr += rr
        print(f"{qid:>5}: nDCG@10 {n:.2f}, recall@10 {r:.2f}, primo pertinente "
              f"{'-' if not rr else round(1 / rr)}: {queries[qid][:90]}")
        righe.append({"id": qid, "domanda": queries[qid], "attesi": sorted(attesi), "trovati": top,
                      "ndcg10": round(n, 3), "recall10": round(r, 3)})
    n = len(scelte)
    inga_api.write_result({
        "stato": "ok",
        "voto": ndcg / n,
        "voci": {"nDCG@10": ndcg / n, "recall@10": rec / n, "recall@5": rec5 / n, "MRR@10": mrr / n},
        "dettagli": {"domande": n, "abstract": len(documenti), "seed": SEED,
                     "modello_embedding": os.environ.get("INGA_EMBEDDING_MODEL"), "risposte": righe},
    })


if __name__ == "__main__":
    main()
