---
title: "Strands Decider 2B"
category: strumento
tags: [aws, classificazione, decisioni, open-source]
related_puntate: [20261002]
created: 2026-10-03
updated: 2026-10-03
sources: [raw/tldr/tldr20261002.md, raw/pillitteri/pillitteri20261002-aws-strands-decider-2b-jev.md]
---

# Strands Decider 2B

## Introduzione

Modello open source di Amazon per classificazione, routing e scoring veloci: è l'ingresso di Amazon nella corsa ai decision model, accanto a [[clef]] e [[kev]].

## Capacità e performance

- È pensato per task veloci di classificazione, routing e scoring. [Fonte: raw/tldr/tldr20261002.md]

## Azienda di riferimento

- [[amazon]]

## Timeline delle notizie

- **2026-10-01** — AWS pubblica Strands Decider 2B, modello open source da 2 miliardi di parametri che non scrive testo ma sceglie tra opzioni predefinite: parte da Qwen3.5-2B, sostituisce la previsione della parola successiva con un pointer head da poco più di un milione di parametri e un adattatore LoRA di rango 16, con latenza mediana di 106 millisecondi su RTX 3090 e 72% su JevBench con Brier 0,35. È scaricabile gratis da Hugging Face sotto Apache 2.0 con codice, script di addestramento e dati. [Fonte: raw/pillitteri/pillitteri20261002-aws-strands-decider-2b-jev.md]

- **2026-10-02** — Amazon entra nella corsa ai decision model con Strands Decider 2B, modello open source per classificazione, routing e scoring veloci. [Fonte: raw/tldr/tldr20261002.md]

## Collegamenti

- [[amazon]]
- [[strands]]
- [[clef]]
- [[index]]