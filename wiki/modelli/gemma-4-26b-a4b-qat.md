---
title: "Gemma 4 26b-a4b-it-qat"
category: modello
tags: [google, llm, moe, quantizzazione]
related_puntate: [20260618, 20260622]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260618.md, raw/puntate/ainews20260622.md]
---

# Gemma 4 26b-a4b-it-qat

## Introduzione

Modello sparse MoE di Google con quattro miliardi di parametri attivi, eseguibile su laptop gaming con 8 GB VRAM.

## Capacità e performance

- Gemma 4 26B A4B QAT raggiunge venticinque token al secondo e oltre trecentoventi in prefill su otto GB VRAM più sedici GB RAM grazie a TurboQuant.
- Gemma 4 26b-a4b-it-qat è un modello sparse MoE con solo quattro miliardi di parametri attivi: gira su RTX quattromilasessanta laptop GPU con otto GB VRAM a oltre venti tok/s decode, senza cloud, API o hack di offload; QAT (quantization aware training) di Google più supporto MTP (multi token prediction) nelle ultime build llama.cpp, funziona su qualsiasi GPU consumer da sei-otto GB.

## Strumenti correlati

- [[llama-cpp]]
- [[llama-cpp-turboquant]]
- [[turboquant]]

## Timeline delle notizie

- **2026-06-18** — Gemma 4 26B A4B QAT raggiunge venticinque token al secondo e oltre trecentoventi in prefill su otto GB VRAM più sedici GB RAM grazie a TurboQuant. [Fonte: raw/puntate/ainews20260618.md]
- **2026-06-22** — Gemma 4 26b-a4b-it-qat è un modello sparse MoE con solo quattro miliardi di parametri attivi: gira su RTX quattromilasessanta laptop GPU con otto GB VRAM a oltre venti tok/s decode, senza cloud, API o hack di offload; QAT (quantization aware training) di Google più supporto MTP (multi token prediction) nelle ultime build llama.cpp, funziona su qualsiasi GPU consumer da sei-otto GB. [Fonte: raw/puntate/ainews20260622.md]

## Collegamenti

- [[llama-cpp]]
- [[llama-cpp-turboquant]]
- [[turboquant]]
- [[index]]

