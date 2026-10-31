---
title: "PII-Tracer"
category: modello
tags: [perplexity, classificatore, open-source, privacy, pii]
related_puntate: []
created: 2026-09-15
updated: 2026-09-15
---

# PII-Tracer

## Introduzione

Classificatore di dati personali sviluppato dal Secure Intelligence Institute di [[perplexity]] e rilasciato open source su Hugging Face il 1 settembre 2026: è il componente che decide quando il lavoro di [[perplexity-computer]] deve passare dal cloud al modello locale, e sta dietro il Privacy Gate di Hybrid Compute.

## Capacità

- È un encoder bidirezionale da 0,6 miliardi di parametri costruito sopra la spina dorsale di Qwen3: legge il testo con attenzione bidirezionale su una finestra di 4.096 token e usa una testa di etichettatura lineare che assegna 37 etichette, coprendo nove tipi di dato personale più i marcatori di posizione.
- L'addestramento è durato tre epoche su circa 714.000 esempi, con decodifica vincolata (Viterbi) che all'inferenza tiene insieme le etichette in modo coerente.

## Performance

- Nei numeri dichiarati da Perplexity batte GPT-5.6 Sol sul compito di trovare ogni menzione di un dato sensibile: F1 a livello di carattere 0,629, coerenza su identificatori ripetuti 79,4 percento contro 57,0, coerenza tra turni diversi 77,6 contro 55,1 e 0,691 sui casi difficili con sei-dieci menzioni contro 0,464.
- Su una conversazione corta, sotto i mille caratteri, il richiamo arriva a 0,975 ma scivola a 0,687 quando la chat supera i diecimila caratteri; facendo scorrere finestre di analisi sovrapposte a metà il richiamo risale a 0,965.

## Disponibilità

- Open source: il codice e i pesi del classificatore sono pubblicati su Hugging Face.

## Azienda di riferimento

- [[perplexity]]

## Timeline delle notizie

- **2026-09-01** — Perplexity apre il codice di PII-Tracer, l'encoder da 0,6 miliardi di parametri che fa da cancello ai dati personali in Hybrid Compute su Mac.

## Collegamenti

- [[perplexity]]
- [[open-source]]
- [[index]]
