---
title: "RAG over-retrieval"
category: trend
tags: [efficienza, rag, retrieval, ricerca]
related_puntate: [20260827, 20260913, 20260925, 20261014]
created: 2026-08-28
updated: 2026-10-14
sources: [raw/puntate/ainews20260827.md, raw/puntate/ainews20260913.md, raw/puntate/ainews20260925.md, raw/pillitteri/pillitteri20260428-differenza-rag-llm-wiki-agentic-search-guida-2026.md, raw/pillitteri/pillitteri20260905-ipazia-avatar-ai-rai-1-codice-carfagna.md, raw/puntate/ainews20261014.md]
---

# RAG over-retrieval

## Introduzione

Trend di ottimizzazione del Retrieval Augmented Generation (RAG): sempre più sistemi scoprono che "cercare troppo" peggiora risultati e costi, e che metodi di indice come IVF possono battere la exact search.

## Evoluzione nel tempo

- Test su centomila documenti mostrano che IVF (inverted file index) bate la exact search di dodici punto due volte più veloce con ottantotto punto tre percento di recall, indicando che il retrieval eccessivo è un problema comune.

## Attori coinvolti

- La comunità del RAG in generale; i metodi di indice sparsi nell'ecosistema open source.

## Timeline delle notizie

- **2026-04-28** — Un confronto tra le tre architetture di memoria esterna per i modelli mette a fianco RAG, il pattern LLM Wiki di Karpathy e l'agentic search: il RAG resta lo standard su corpus grandi e statici ma paga il costo crescente delle query — a 50 milioni di query mensili l'overhead di contesto vale circa 43.750 dollari al mese — mentre l'agentic search costa 0,05-0,30 dollari per query e richiede 100.000-200.000 dollari di sviluppo. Il 75 per cento delle applicazioni enterprise userà architetture ibride entro la fine del 2026. [Fonte: raw/pillitteri/pillitteri20260428-differenza-rag-llm-wiki-agentic-search-guida-2026.md]

- **2026-08-27** — Problema comune nei sistemi RAG: cercano troppo. Test su centomila documenti mostra che IVF batte exact search dodici punto due volte più veloce con ottantotto punto tre percento de recall. [Fonte: raw/puntate/ainews20260827.md]
- **2026-09-05** — Ipazia, l'avatar AI di Codice su Rai 1, è un caso di RAG applicato alla televisione generalista: il modello cerca prima i documenti rilevanti nell'archivio delle dieci edizioni del programma e poi genera la risposta appoggiandosi a quei testi, così le frasi restano ancorate a fonti reali. Ancorare le risposte a un corpus curato riduce le allucinazioni ma non le azzera, e in diretta non c'è modo di correggere dopo: il punto aperto è l'attribuzione delle responsabilità, che resta della redazione. [Fonte: raw/pillitteri/pillitteri20260905-ipazia-avatar-ai-rai-1-codice-carfagna.md]



- **2026-09-13** — [[weknora]] di [[tencent]] (ventiduemila stelle su GitHub) porta il pattern in produzione: le domande semplici ottengono risposte rapide via retrieval, quelle complesse attivano agenti che cercano nella base di conoscenza e sul web. [Fonte: raw/puntate/ainews20260913.md]
- **2026-09-25** — Due release dello stesso giorno spingono nella direzione opposta all'ingrandimento dei contesti: [[stair]] di IBM rinuncia a vector database, embedding e re-ranker e usa l'indice del documento come schema di indirizzamento, allucinando sessantacinque volte meno dei sistemi RAG fine-tuned; [[langextract]] di Google porta l'estrazione dai documenti nell'open source gratuito, dove finora stavano strumenti enterprise da centomila dollari. [Fonte: raw/puntate/ainews20260925.md]
- **2026-10-14** — Timescale rilascia pg_vectorsearch, estensione PostgreSQL per la ricerca vettoriale: a cento milioni di vettori sei millisecondi contro gli otto di HNSW con un quarto della RAM (128 GB invece di 512), indici sette volte più piccoli e build cinquanta volte più rapide, grazie a partizioni per distanza, compressione RaBitQ e scansioni SIMD, sotto licenza PostgreSQL. [Fonte: raw/puntate/ainews20261014.md]




## Collegamenti

- [[modular-graphrag]]
- [[pixelrag]]
- [[retrieval-harness]]
- [[weknora]]
- [[page-index]]
- [[index]]
