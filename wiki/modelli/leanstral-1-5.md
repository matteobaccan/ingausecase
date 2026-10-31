---
title: "Leanstral 1.5"
category: modello
tags: [lean, math, mistral, open-weight]
related_puntate: [20260704]
created: 2026-08-12
updated: 2026-09-13
sources: [raw/puntate/ainews20260704.md, raw/pillitteri/pillitteri20260705-leanstral-1-5-mistral-teoremi-lean-4.md]
---

# Leanstral 1.5

## Introduzione

Modello di Mistral da 119 miliardi di parametri (6 attivi) specializzato in dimostrazioni formali in Lean 4: 100% su miniF2F, Apache 2.0.

## Capacità e performance

- Modello da 119 miliardi di parametri, 6 attivi, specializzato in dimostrazioni formali in Lean 4: 100% su miniF2F e 587/672 su PutnamBench. Apache 2.0, API gratuita.

## Azienda di riferimento

- [[mistral]]

## Timeline delle notizie

- **2026-07-04** — Modello da 119 miliardi di parametri, 6 attivi, specializzato in dimostrazioni formali in Lean 4: 100% su miniF2F e 587/672 su PutnamBench. Apache 2.0, API gratuita. [Fonte: raw/puntate/ainews20260704.md]
- **2026-07-05** — Il rilascio del 3 luglio arriva con la curva di test-time scaling che ha fatto discutere: sempre in Pass@8 su PutnamBench, 44 problemi risolti con 50.000 token per tentativo, 244 a 200.000, 493 a un milione, 587 a quattro milioni, con una crescita regolare che non satura prematuramente. Satura miniF2F al 100% anche sul test, segna 87 su FATE-H e 34 su FATE-X e su FLTEval porta il Pass@1 dal 21,9 al 28,9 per cento e il Pass@8 al 43,2 contro il 39,6 di [[claude-opus-4-6]]: un modello con 6 miliardi di parametri attivi che batte un generalista di frontiera su un compito verticale. Il costo è la notizia economica: circa 4 dollari a problema contro i 300 e oltre di Seed-Prover 1.5 nella configurazione high (che risolve sette problemi in meno) e i 54-68 di Aleph Prover, con un'architettura MoE da 119 miliardi su 128 esperti e 4 attivi per token. È addestrato in tre fasi (mid-training, SFT e RL con CISPO) su due ambienti, uno multiturn con il responso del compilatore e uno da agente di codice con accesso al filesystem e a Lean LSP via MCP; i pesi sono su Hugging Face come mistralai/Leanstral-1.5-119B-A6B, in locale serve vLLM 0.24.0 o superiore. Durante i test ha trovato cinque bug mai segnalati su 57 repository open source. [Fonte: raw/pillitteri/pillitteri20260705-leanstral-1-5-mistral-teoremi-lean-4.md]

## Collegamenti

- [[mistral]]
- [[index]]

