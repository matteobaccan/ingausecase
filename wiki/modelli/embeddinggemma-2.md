---
title: "EmbeddingGemma 2"
category: modello
tags: [embedding, google, multimodale, open-weight, on-device]
related_puntate: [20261007, 20261012]
created: 2026-10-07
updated: 2026-10-12
sources: [raw/puntate/ainews20261007.md, raw/tldr/tldr20261007.md, raw/pillitteri/pillitteri20261006-embeddinggemma-2-google-embedding-multimodale-open.md, raw/pillitteri/pillitteri20261009-google-foresight-mac-trascrizione-riunioni-offline.md, raw/puntate/ainews20261012.md]
---

# EmbeddingGemma 2

## Introduzione

Modello di embedding multimodale open source di [[google]], il primo a unificare testo, codice, immagini, video e audio in un unico spazio vettoriale. Con 740 milioni di parametri e circa 540 MB di RAM per l'esecuzione locale, e' pensato per ricerca e recupero (RAG) offline senza inviare dati al cloud.

## Capacita' e performance

- Con 740 milioni di parametri mappa testo, codice, immagini, audio e video in uno spazio di embedding condiviso e, secondo quanto riportato, batterebbe modelli specializzati dal doppio delle dimensioni. [Fonte: raw/puntate/ainews20261007.md]
- E' distribuito con licenza Apache 2.0 ed e' costruito per l'inferenza on-device: abilita ricerca e recupero multimodale senza mandare i dati al cloud, ed e' indicato per RAG offline abbinato a Gemma 4. [Fonte: raw/tldr/tldr20261007.md]
- E' costruito a moduli sull'architettura di Gemma 4: un blocco base da 270 milioni di parametri per testo e codice, un encoder visivo da 170 milioni per immagini e frame video e un encoder audio da 300 milioni, caricabili dallo stesso checkpoint secondo il bisogno. [Fonte: raw/pillitteri/pillitteri20261006-embeddinggemma-2-google-embedding-multimodale-open.md]
- Quantizzata, la versione completa occupa circa 567 MB di RAM attiva su un Pixel 11 Pro e la sola parte testuale scende a 191 MB; tutte le modalita' condividono un contesto da 8.192 token e producono vettori da 768 dimensioni, accorciabili a 512, 256 o 128 con la Matryoshka Representation Learning. [Fonte: raw/pillitteri/pillitteri20261006-embeddinggemma-2-google-embedding-multimodale-open.md]
- Nell'MTEB Code sale da 68,76 a 78,68 punti (circa +14%), mantiene 61,36 nell'MTEB multilingual e parte da 50,67 sul recupero video e 49,39 sui compiti audio MAEB; la conversione di un'immagine in vettore richiede 37,3 millisecondi sulla GPU di un MacBook M5 Pro. [Fonte: raw/pillitteri/pillitteri20261006-embeddinggemma-2-google-embedding-multimodale-open.md]

## Azienda di riferimento

- [[google]]

## Timeline delle notizie

- **2026-10-07** — Google presenta EmbeddingGemma 2, modello di embedding multimodale open source da 740 milioni di parametri che unifica testo, codice, immagini, video e audio in un unico spazio vettoriale; gira localmente su circa 540 MB di RAM, e' distribuito con licenza Apache 2.0 e batterebbe modelli specializzati dal doppio delle dimensioni. [Fonte: raw/puntate/ainews20261007.md] [Fonte: raw/tldr/tldr20261007.md]
- **2026-10-09** — Google AI Edge Foresight, l'app sperimentale per Mac che trascrive le riunioni offline, è la vetrina di EmbeddingGemma 2: il modello di embedding serve a ritrovare i passaggi giusti dentro appunti e documenti indicizzati. [Fonte: raw/pillitteri/pillitteri20261009-google-foresight-mac-trascrizione-riunioni-offline.md]
- **2026-10-12** — EmbeddingGemma 2 (DUE) è descritto come modello di embedding multimodale da 865 megabyte per ricerca semantica locale su video, audio, codice e PDF: un'app Mac open source che lo usa per cercare nei file locali risulterebbe più precisa di Spotlight. [Fonte: raw/puntate/ainews20261012.md]







## Collegamenti

- [[google]]
- [[open-source]]
- [[index]]
