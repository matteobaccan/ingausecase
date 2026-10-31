---
title: "SemIf"
category: strumento
tags: [jev, mit, open-source, rt-3090, webgpu]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
---

# SemIf

## Introduzione

Clone open source di [[jev]] pubblicato il 16 settembre 2026 con il nome OpenJev e poi rinominato: riproduce il contratto d'uso del modello di [[typesafe-ai]] — uno stato in ingresso, domande e opzioni definite a runtime, una probabilità per ogni opzione — con modelli aperti, senza l'architettura né i dati di addestramento dell'originale. Il README dichiara che si tratta di un progetto indipendente e non affiliato.

## Funzionalità principali

- La tecnica è un solo passaggio in avanti nella rete con lettura dei logit delle sole opzioni consentite, senza generare token: su una RTX 3090 risponde a 21 criteri sì/no sullo stesso stato in 1,023 secondi con un Qwen3.5-4B congelato, contro i 5,332 secondi della generazione dello stesso array JSON, 5,21 volte di più, con una concordanza di 18 criteri su 21.
- Gira anche nel browser via WebGPU con il Qwen3.5-4B quantizzato da 3,01 GB o con [[minicpm5-2b]] da 1,56 GB, e ha un backend MLX per Apple Silicon; il riuso dello stato fra più domande porta lo scoring a 20,03 decisioni al secondo contro 2,33.
- Sui 102 esempi pubblicati da TypeSafe il Qwen3.5-4B di SemIf raggiunge una concordanza di 0,845 contro lo 0,883 dichiarato per Jev, 3,8 punti sotto; i numeri vengono dal README, non da verifiche indipendenti.

## Repository

- 2.685 stelle su GitHub e 165 fork al 21 settembre 2026, licenza MIT.

## Timeline delle notizie

- **2026-09-21** — SemIf, nato il 16 settembre come OpenJev, è il più seguito dei cloni open source di Jev: 2.685 stelle e 165 fork, licenza MIT, base Qwen3.5-4B con MiniCPM5-2B per il browser e demo WebGPU senza lista d'attesa; su RTX 3090 risponde a 21 criteri in 1,023 secondi contro 5,332 della generazione JSON.

## Collegamenti

- [[jev]]
- [[kev]]
- [[minicpm5-2b]]
- [[typesafe-ai]]
- [[index]]
