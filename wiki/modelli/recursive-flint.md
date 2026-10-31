---
title: "Recursive Flint"
category: modello
tags: [llm, mixture-of-experts, coding, locale, agenti]
related_puntate: []
created: 2026-10-22
updated: 2026-10-23
---

# Recursive Flint

## Introduzione

Flint è un modello mixture-of-experts di Recursive pensato per il coding agentico su hardware locale: 40 miliardi di parametri in totale, dei quali 2,5 attivati per token.

## Capacità e performance

- Genera più di 125 token al secondo su un MacBook Pro con M4 Pro e più di 150 su un RTX Spark da 64 GB con contesti brevi.
- Può essere usato come modello di coding quotidiano per completare attività in locale senza inviare dati a un server remoto.

## Sviluppo

- È stato costruito da zero da un team ristretto di persone e agenti in meno di quattro mesi.

## Azienda di riferimento

- Recursive, che pubblica l'annuncio sul proprio sito.

## Timeline delle notizie

- **2026-10-22** — Recursive presenta Flint, mixture-of-experts da 40 miliardi di parametri con 2,5 miliardi attivi per token, tarato per il coding su hardware locale e capace di oltre 150 token al secondo su un RTX Spark da 64 GB. La scheda completa aggiunge i numeri: 39,8 miliardi di parametri totali, 256 esperti per strato con 6 scelti per token più uno sempre attivo, contesto dichiarato a 262.144 token (512.000 nel post di Recursive, con il consiglio di restare sotto 256.000) e compressione NVFP4 a 4 bit che resta entro 0,7 punti dall'originale sui benchmark. I punteggi dichiarati sono 74,2% su SWE-bench Verified, 54,9% su Terminal-Bench 2.1 e 89,7% su SWE-bench Pro v2, con licenza Apache 2.0 e pesi su Hugging Face; Recursive ammette che Flint l'hanno costruito persone con l'aiuto di Eureka Machine, non l'IA da sola.

## Collegamenti

- [[ai-locale]]
- [[nvidia]]
- [[index]]
