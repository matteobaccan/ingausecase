---
title: "TileLang"
category: strumento
tags: [deepseek, huawei, kernel, open-source, cina, gpu]
created: 2026-10-01
updated: 2026-10-01
---

# TileLang

## Introduzione

Linguaggio DSL con sintassi Python per scrivere kernel (GEMM, FlashAttention) mantenendo le prestazioni di CUDA senza il suo linguaggio proprietario. Non nasce in casa DeepSeek: è un progetto dell'organizzazione GitHub tile-ai, sviluppato sotto la guida del professor Zhi Yang della Peking University, con primo rilascio pubblico il 20 gennaio 2025.

## Funzionalità principali

- DeepSeek lo usa già per la maggior parte degli operatori nel training della serie DeepSeek V4; il repository conta 7.872 stelle e 792 fork al 30 settembre 2026.
- Si posiziona anche contro Triton, il DSL per kernel mantenuto da OpenAI, oltre che contro CUDA.

## Azienda / Autore

- Progetto tile-ai (Peking University); adottato da [[deepseek]].

## Timeline delle notizie

- **2026-09-30** — [[deepseek]] rende open source l'intero stack di addestramento adattato ai chip Ascend di [[huawei]], con TileLang e le versioni Ascend di DeepGEMM, DeepEP e FlashMLA; Huawei e DeepSeek presentano anche un supernodo da 128 chip Ascend 950, senza benchmark comparativi contro cluster Nvidia.

## Collegamenti

- [[deepseek]]
- [[huawei]]
- [[nvidia]]
- [[competizione-usa-cina]]
- [[index]]
