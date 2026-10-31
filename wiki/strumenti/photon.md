---
title: "Photon"
category: strumento
tags: [ricerca, rust, latenza, agenti, perplexity]
related_puntate: []
created: 2026-09-25
updated: 2026-09-25
sources: [raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md]
---

# Photon

## Introduzione

Motore di recupero e ordinamento scritto in Rust che alimenta la modalità Fast Search di [[perplexity]], presentato il 24 settembre 2026: sostituisce quello che l'azienda descrive come un motore di ricerca open source modificato in casa e, secondo Perplexity, è stato costruito da un piccolo gruppo di ingegneri con l'aiuto di centinaia di agenti IA. [Fonte: raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md]

## Funzionalità principali

- Usa indici che conoscono il formato dei documenti, record di ordinamento compatti e operazioni su disco asincrone in blocchi, con la costruzione dell'indice tenuta separata dal percorso che serve le query. [Fonte: raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md]
- I numeri dichiarati dall'azienda: il tempo di risposta al 99° percentile scende da circa 800 a circa 65 millisecondi, le macchine necessarie per servire lo stesso carico sono il 20 per cento in meno, ogni documento contiene circa 2,5 volte più dati e il costo per compito sugli agenti è inferiore del 68 per cento su sei benchmark agentici con qualità definita "paragonabile". Sono dichiarazioni misurate dall'azienda sul proprio preset predefinito, non misure indipendenti. [Fonte: raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md]
- Il compromesso che il post tecnico ammette: la rilevanza misurata con l'indice DCG scende di 0,24 punti, da 2,45 a 2,21, e la disponibilità della risposta, cioè la quota di casi in cui i risultati contengono davvero quello che serve, cala di circa 3 punti percentuali, dal 59,6 al 56,7 per cento. [Fonte: raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md]

## Timeline delle notizie

- **2026-09-25** — Photon debutta come motore della modalità Fast Search della Search API di Perplexity: 95 per cento dei risultati entro 230 millisecondi e latenza mediana di 160, al prezzo di un dollaro ogni mille richieste contro i cinque della ricerca standard, con un compromesso dichiarato di 0,24 punti di rilevanza e circa tre punti di disponibilità della risposta in meno. [Fonte: raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md]

## Collegamenti

- [[agenti-ai]]
- [[perplexity]]
- [[index]]
