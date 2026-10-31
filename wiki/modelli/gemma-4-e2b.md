---
title: "Gemma 4 E2B"
category: modello
tags: [fine-tuning, google, llm, on-device, open-weight]
related_puntate: [20260617, 20260710, 20261014]
created: 2026-08-12
updated: 2026-10-14
sources: [raw/puntate/ainews20260617.md, raw/puntate/ainews20260710.md, raw/pillitteri/pillitteri20260703-gemma-4-255-token-browser-webgpu-fable-5.md, raw/puntate/ainews20261014.md]
---

# Gemma 4 E2B

## Introduzione

Variante della famiglia Gemma 4 ottimizzata per il fine-tuning su singola GPU, dimostrata sulla traduzione dal coreano classico.

## Capacità e performance

- Gemma 4 E2B gira su Intel AI PC con supporto LiteRT NPU via OpenVINO: uno punto tre volte più veloce in prefill rispetto a GPU, due punto otto volte meglio in performance per watt, task in background senza throttling termico o consumo pesante di batteria.
- Gemma 4 E2B permette il fine-tuning su singola GPU: nella dimostrazione traduce coreano classico in testo moderno con accuratezza passata dal quattro all'ottanta per cento.

## Azienda di riferimento

- [[google]]
- [[intel]]

## Strumenti correlati

- [[openvino]]

## Timeline delle notizie

- **2026-06-17** — Gemma 4 E2B gira su Intel AI PC con supporto LiteRT NPU via OpenVINO: uno punto tre volte più veloce in prefill rispetto a GPU, due punto otto volte meglio in performance per watt, task in background senza throttling termico o consumo pesante di batteria. [Fonte: raw/puntate/ainews20260617.md]
- **2026-07-03** — Gemma 4 E2B, la variante "effective 2B" pensata per l'on-device, è quella che gira nel browser tramite transformers.js con device WebGPU e quantizzazione q4f16: l'architettura mix-and-match attiva solo una parte dei parametri per token, ed è per questo che un modello di quella taglia tiene il passo su una GPU di consumo o integrata. Una implementazione di riferimento della stessa variante è stata misurata intorno ai 125 token al secondo su una RTX 5090 con Chrome stabile. [Fonte: raw/pillitteri/pillitteri20260703-gemma-4-255-token-browser-webgpu-fable-5.md]



- **2026-07-10** — Gemma 4 E2B permette il fine-tuning su singola GPU: nella dimostrazione traduce coreano classico in testo moderno con accuratezza passata dal quattro all'ottanta per cento. [Fonte: raw/puntate/ainews20260710.md]
- **2026-10-14** — Le ottimizzazioni arrivate con Gemini 4 Argon spingono Gemma 4 E2B oltre i centomila token al secondo su singola A100 con vLLM: 124.000 in prefill e 110.000 end-to-end, 2,9 volte più veloce senza perdita di qualità, con sessantaquattro simulazioni Python live in parallelo. [Fonte: raw/puntate/ainews20261014.md]




## Collegamenti

- [[google]]
- [[intel]]
- [[modus]]
- [[openvino]]
- [[index]]

