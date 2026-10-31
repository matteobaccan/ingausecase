---
title: "Code2LoRA"
category: strumento
tags: [efficienza, fine-tuning, lora, repository]
related_puntate: [20260613]
created: 2026-08-12
updated: 2026-08-12
---

# Code2LoRA

## Introduzione

Distilla il contesto del repository in un adattatore LoRA: zero token extra durante l'inferenza.

## Funzionalità principali

- Code2LoRA distilla il contesto del repository in un adattatore LoRA invece di riempire il prompt a ogni query: una singola passata sullo snapshot, un adattatore e zero token extra; per codebase in evoluzione usa una GRU a singolo layer che traccia i commit, aggiornando lo stato nascosto in meno di dieci millisecondi per ogni git diff.

## Timeline delle notizie

- **2026-06-13** — Code2LoRA distilla il contesto del repository in un adattatore LoRA invece di riempire il prompt a ogni query: una singola passata sullo snapshot, un adattatore e zero token extra; per codebase in evoluzione usa una GRU a singolo layer che traccia i commit, aggiornando lo stato nascosto in meno di dieci millisecondi per ogni git diff.

## Collegamenti

- [[trellis]]
- [[index]]

