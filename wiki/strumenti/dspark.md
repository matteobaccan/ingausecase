---
title: "DSpark"
category: strumento
tags: [decoding, deepseek, efficienza, inference, locale, open-source]
related_puntate: [20260628, 20260629, 20260703, 20260807]
created: 2026-08-12
updated: 2026-08-12
---

# DSpark

## Introduzione

Strumento che accelera DeepSeek-V4-Flash del doppio in locale, raggiungendo centoventi token al secondo senza perdita di accuratezza.

## Funzionalità principali

- Speculative decoding di DeepSeek che aumenta il throughput dal 51% al 400%, open source insieme al framework di training DeepSpec.
- DeepSeek ha rilasciato modelli di speculative decoding con versioni draft per Gemma 4, Qwen 3, Eagle 3, DFlash e DSpark, che accelerano l'inferenza dei modelli base.
- Supportato da vLLM: propone più token in parallelo e li verifica in un passo; su 8 B300 produce circa 250 token al secondo.

## Azienda / Autore

- [[deepseek]]

## Modelli supportati / correlati

- [[deepseek-v4-flash]]

## Timeline delle notizie

- **2026-06-28** — Speculative decoding di DeepSeek che aumenta il throughput dal 51% al 400%, open source insieme al framework di training DeepSpec.
- **2026-06-29** — DeepSeek ha rilasciato modelli di speculative decoding con versioni draft per Gemma 4, Qwen 3, Eagle 3, DFlash e DSpark, che accelerano l'inferenza dei modelli base.
- **2026-07-03** — Supportato da vLLM: propone più token in parallelo e li verifica in un passo; su 8 B300 produce circa 250 token al secondo.
- **2026-08-07** — DSpark accelera DeepSeek-V4-Flash del doppio in locale: centoventi token al secondo senza perdita di accuratezza.

## Collegamenti

- [[codex]]
- [[deepseek]]
- [[deepseek-v4-flash]]
- [[deepspec]]
- [[llama-factory]]
- [[vllm]]
- [[index]]

