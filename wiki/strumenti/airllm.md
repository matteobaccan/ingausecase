---
title: "AirLLM"
category: strumento
tags: [efficienza, gpu, inference, inferenza, open-source, ottimizzazione]
related_puntate: [20260602, 20260717, 20260802, 20260805, 20261011]
created: 2026-08-12
updated: 2026-10-11
---

# AirLLM

## Introduzione

Strumento che fa girare modelli giganti su GPU low-end caricando una layer alla volta, senza quantizzazione, distillazione o pruning. Fino a modelli da due virgola otto trilioni.

## Funzionalità principali

- AirLLM usa layer-wise inference: carica, calcola e scarica un layer alla volta invece dell'intero modello, permettendo di eseguire LLM da settanta B su una GPU da quattro GB.
- airllm di Gavin Li esegue modelli da quattrocentocinque miliardi di parametri su GPU da otto GB, una layer GPU alla volta con streaming del resto: settanta miliardi in quattro GB e DeepSeek 671B in dodici, ventiduemila stelle, Apache 2.0.
- AirLLM carica una sola layer alla volta in GPU: Kimi K3 girava sotto 4 GB di VRAM senza quantizzazione. 24.000 stelle.

## Azienda / Autore

- [[nvidia]]
- [[unsloth]]

## Modelli supportati / correlati

- [[chandra-ocr-2]]
- [[kimi-k3]]

## Timeline delle notizie

- **2026-06-02** — AirLLM usa layer-wise inference: carica, calcola e scarica un layer alla volta invece dell'intero modello, permettendo di eseguire LLM da settanta B su una GPU da quattro GB.
- **2026-07-17** — airllm di Gavin Li esegue modelli da quattrocentocinque miliardi di parametri su GPU da otto GB, una layer GPU alla volta con streaming del resto: settanta miliardi in quattro GB e DeepSeek 671B in dodici, ventiduemila stelle, Apache 2.0.
- **2026-08-02** — AirLLM carica una sola layer alla volta in GPU: Kimi K3 girava sotto 4 GB di VRAM senza quantizzazione. 24.000 stelle.
- **2026-08-05** — AirLLM fa girare modelli giganti su GPU low-end: quattro giga per Llama3 70B, otto giga per 405B e modelli fino a due virgola otto T, senza quantizzazione, distillazione o pruning, caricando una layer alla volta; per le MoE carica solo l'esperto attivo.
- **2026-10-11** — AirLLM esegue modelli enormi su GPU deboli tramite inferenza layer-by-layer: centosettanta miliardi di parametri su quattro gigabyte e Llama 3.1 da quattrocentocinquanta miliardi su otto, con supporto a Llama, Qwen e Mistral su Linux, Windows e Mac; la velocità sembra però limitata.




## Collegamenti

- [[chandra-ocr-2]]
- [[kimi-k3]]
- [[nvidia]]
- [[open-source]]
- [[unsloth]]
- [[index]]

