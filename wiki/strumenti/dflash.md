---
title: "DFlash"
category: strumento
tags: [decoding, diffusion, inferenza, open-source, speculative, velocita]
related_puntate: [20260612, 20260713]
created: 2026-08-12
updated: 2026-08-12
---

# DFlash

## Introduzione

Modello draft per speculative decoding introdotto con vLLM 0.25, che indovina quindici token per volta validati dal modello principale.

## Funzionalità principali

- DFlash accelera l'inferenza LLM con speculative decoding basato su un diffusion model: otto punto cinque volte più veloce senza perdita di qualità; integrato in vLLM, SGLang e Transformers, con draft model per Qwen, Llama e Kimi.
- DFlash è un drafter per lo speculative decoding introdotto in vLLM 0.25: indovina quindici token per volta e il modello principale verifica tutto in un pass, portando Qwen 3.6 27B oltre centocinquanta token al secondo su due RTX 3090.

## Modelli supportati / correlati

- [[diffusiongemma]]
- [[qwen-3-6]]

## Timeline delle notizie

- **2026-06-12** — DFlash accelera l'inferenza LLM con speculative decoding basato su un diffusion model: otto punto cinque volte più veloce senza perdita di qualità; integrato in vLLM, SGLang e Transformers, con draft model per Qwen, Llama e Kimi.
- **2026-07-13** — DFlash è un drafter per lo speculative decoding introdotto in vLLM 0.25: indovina quindici token per volta e il modello principale verifica tutto in un pass, portando Qwen 3.6 27B oltre centocinquanta token al secondo su due RTX 3090.

## Collegamenti

- [[diffusiongemma]]
- [[qwen-3-6]]
- [[vllm]]
- [[index]]

