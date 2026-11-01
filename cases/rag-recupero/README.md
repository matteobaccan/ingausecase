# rag-recupero

Misura **solo il recupero** delle collezioni di documenti di Inga, senza il modello di
chat, su un test pubblico: [SciFact](https://huggingface.co/datasets/mteb/scifact) del
benchmark BEIR (affermazioni scientifiche e abstract giudicati pertinenti; licenza
CC BY-SA 4.0).

- **Dati:** scaricati a ogni esecuzione da [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json)
  (revisione fissata, sha256 controllato), mai nel repository.
- **Sottoinsieme fisso** (seed 7): 60 domande di test, i loro abstract pertinenti e altri
  abstract a caso fino a 1000, in una collezione di Inga.
- **Ricerca:** per ogni domanda, `GET /api/inga/documents/search` (la stessa ricerca della
  chat con `inga_documents`: embedding, BM25, fusione e, se c'è, il reranker). Gli
  estratti diventano documenti nell'ordine in cui compaiono.
- **Voto:** nDCG@10 medio. Voci: nDCG@10, recall@10, recall@5, MRR@10.

I numeri **non** sono confrontabili con quelli pubblicati su SciFact intero (5183
abstract, collezione più difficile): servono a confrontare le versioni di Inga e i
modelli di embedding fra loro. Le versioni di Inga senza la ricerca diretta
(`/api/inga/documents/search`) danno il caso come saltato.
