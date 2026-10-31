---
title: "Bonsai 27B"
category: modello
tags: [locale, open-weight, quantizzazione]
related_puntate: [20260715, 20260720, 20260918, 20260919]
created: 2026-08-12
updated: 2026-09-19
sources: [raw/puntate/ainews20260715.md, raw/puntate/ainews20260720.md, raw/puntate/ainews20260918.md, raw/puntate/ainews20260919.md]
---

# Bonsai 27B

## Introduzione

Modello da ventisette miliardi con quantizzazione a un bit: da cinquantaquattro a 3,8 gigabyte, gira in browser con kernel WebGPU custom.

## Capacità e performance

- Bonsai 27B con quantizzazione a un bit riduce da cinquantaquattro a 3,8 gigabyte (novanta per cento di riduzione) mantenendo il novanta per cento dell'intelligenza: con kernel WebGPU custom scritti da Fable 5 e GPT-5.6 Sol gira in browser, versioni ternary e one-bit disponibili, licenza Apache 2.0.
- Bonsai ha compresso Qwen 3.6 27B a 3,9 giga con un bit per peso: venti token al secondo su GTX 1660 Super e tool calling perfetto su loop multi-step, il modello che non doveva funzionare funziona.

## Timeline delle notizie

- **2026-07-15** — Bonsai 27B con quantizzazione a un bit riduce da cinquantaquattro a 3,8 gigabyte (novanta per cento di riduzione) mantenendo il novanta per cento dell'intelligenza: con kernel WebGPU custom scritti da Fable 5 e GPT-5.6 Sol gira in browser, versioni ternary e one-bit disponibili, licenza Apache 2.0. [Fonte: raw/puntate/ainews20260715.md]
- **2026-07-20** — Bonsai ha compresso Qwen 3.6 27B a 3,9 giga con un bit per peso: venti token al secondo su GTX 1660 Super e tool calling perfetto su loop multi-step, il modello che non doveva funzionare funziona. [Fonte: raw/puntate/ainews20260720.md]
- **2026-09-18** — Ternary Bonsai 2 27B è la nuova versione ternary della famiglia, basata su Qwen 3.8 27B: nove volte più piccola della controparte full-precision, mantiene il 98,2% delle performance aggregate con un footprint di 5,9 gigabyte e guadagni dichiarati in coding agente, ragionamento multimodale e tool use a lungo orizzonte, disponibile sotto Apache 2.0. [Fonte: raw/puntate/ainews20260918.md]
- **2026-09-19** — Il team [[orca-router]] pubblica Ternary Bonsai 2 27B Uncensored senza toccare un solo peso: l'abliteration è stata spostata nel runtime, con centoventinove siti di intervento residuale regolabili al momento dell'inferenza, e il modello funziona localmente su Apple Silicon. [Fonte: raw/puntate/ainews20260919.md]

## Collegamenti

- [[prismml]]

- [[fable-5]]
- [[gemma-4]]
- [[gpt-5-6-sol]]
- [[orca-router]]
- [[qwen-3-6]]
- [[index]]

