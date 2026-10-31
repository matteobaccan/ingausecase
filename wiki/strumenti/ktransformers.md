---
title: "ktransformers"
category: strumento
tags: [gpu, inferenza, open-source]
related_puntate: [20260718, 20260901]
created: 2026-08-12
updated: 2026-09-13
sources: [raw/puntate/ainews20260718.md, raw/puntate/ainews20260901.md, raw/pillitteri/pillitteri20260913-streaming-disco-modelli-moe-portatile.md]
---

# ktransformers

## Introduzione

Progetto open source della Tsinghua University per eseguire modelli enormi su GPU consumer con contesti lunghi.

## Funzionalità principali

- ktransformers della Tsinghua University esegue DeepSeek-V3 con centotrentanovemila token di contesto su una singola GPU da ventiquattro gigabyte: fino a ventotto volte più veloce rispetto alle configurazioni standard, oltre diciassettemila stelle su GitHub.

## Azienda / Autore

- [[tsinghua]]

## Timeline delle notizie

- **2026-07-18** — ktransformers della Tsinghua University esegue DeepSeek-V3 con centotrentanovemila token di contesto su una singola GPU da ventiquattro gigabyte: fino a ventotto volte più veloce rispetto alle configurazioni standard, oltre diciassettemila stelle su GitHub. [Fonte: raw/puntate/ainews20260718.md]
- **2026-09-01** — KTransformers, framework cinese open source. Esegue DeepSeek R-uno 671 miliardi su una singola RTX 4090: fino a ventotto volte più veloce. Fine-tuning di DeepSeek V-tre su quattro GPU consumer. Supporto immediato per Kimi K-due, GLM 5 e MiniMax. [Fonte: raw/puntate/ainews20260901.md]
- **2026-09-13** — Nel confronto tra i tre motori a streaming da disco è la strada della velocità: framework Python del laboratorio MADSys di Tsinghua con Approaching.AI, nato da un paper a SOSP 2025, tiene gli esperti routed nella RAM di sistema mentre la parte densa e gli esperti più caldi stanno sulla GPU — inferenza ibrida CPU-GPU, il disco non c'entra. Con una o due schede consumer e una CPU dual-socket macina 1.200-1.800 token al secondo in prefill e 21-28 token al secondo in generazione su DeepSeek-R1, numeri vicini al cloud; serve però davvero una GPU e parecchia RAM di sistema. Nella classifica GitHub è terzo con 19.505 stelle, dietro [[ds4]] (22.318) e [[colibri]] (28.756). [Fonte: raw/pillitteri/pillitteri20260913-streaming-disco-modelli-moe-portatile.md]

## Collegamenti

- [[tsinghua]]
- [[colibri]]
- [[ds4]]
- [[index]]

