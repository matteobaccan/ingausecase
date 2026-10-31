---
title: "DeepSeek Sparse Attention"
category: strumento
tags: [architettura, deepseek, efficienza, open-weight]
related_puntate: [20260601, 20260602]
created: 2026-08-12
updated: 2026-09-12
sources: [raw/puntate/ainews20260601.md, raw/puntate/ainews20260602.md, raw/pillitteri/pillitteri20260424-deepseek-v4-open-source-cinese-aprile-2026.md]
---

# DeepSeek Sparse Attention

## Introduzione

Architettura di attenzione sparsa di DeepSeek per ridurre i costi di prefill, adottata anche da modelli terzi.

## Funzionalità principali

- La base dell'architettura di DeepSeek V4 è la Hybrid Attention Architecture: la Compressed Sparse Attention (CSA) gestisce il grosso del contesto con una rappresentazione compatta della chiave-valore, mentre la Heavily Compressed Attention (HCA) interviene sui segmenti meno rilevanti. Secondo il paper, V4-Pro richiede il 27% dei FLOPs di inferenza per token rispetto a V3.2 e il 10% della KV cache a parità di contesto. [Fonte: raw/pillitteri/pillitteri20260424-deepseek-v4-open-source-cinese-aprile-2026.md]
- L'architettura DeepSeek Sparse Attention è stata portata nel mondo multimodale dal modello Keye-VL 2.0-30B-A3B, dimezzando il costo di prefill rispetto ai modelli oltre duecento miliardi di parametri.
- La DeepSeek Sparse Attention usata da Keye-VL 2.0 dimezza il costo di prefill rispetto a modelli oltre duecento miliardi di parametri.

## Azienda / Autore

- [[deepseek]]

## Modelli supportati / correlati

- [[keye-vl-2]]

## Timeline delle notizie

- **2026-04-24** — Con DeepSeek V4 arriva la Hybrid Attention Architecture: CSA per il grosso del contesto e HCA per i segmenti meno rilevanti, con il 27% dei FLOPs per token rispetto a V3.2 e il 10% della KV cache. [Fonte: raw/pillitteri/pillitteri20260424-deepseek-v4-open-source-cinese-aprile-2026.md]
- **2026-06-01** — L'architettura DeepSeek Sparse Attention è stata portata nel mondo multimodale dal modello Keye-VL 2.0-30B-A3B, dimezzando il costo di prefill rispetto ai modelli oltre duecento miliardi di parametri. [Fonte: raw/puntate/ainews20260601.md]
- **2026-06-02** — La DeepSeek Sparse Attention usata da Keye-VL 2.0 dimezza il costo di prefill rispetto a modelli oltre duecento miliardi di parametri. [Fonte: raw/puntate/ainews20260602.md]

## Collegamenti

- [[deepseek]]
- [[keye-vl-2]]
- [[index]]

