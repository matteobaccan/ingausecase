---
title: "Muse Glimmer"
category: modello
tags: [agent, apache-2.0, giochi, locale, meta, open-weight, webgpu]
related_puntate: [20260811, 20260812]
created: 2026-08-12
updated: 2026-10-04
---

# Muse Glimmer

## Introduzione

Modello da trenta miliardi di parametri di Meta con pesi aperti, Apache due virgola zero, pensato per agenti locali sempre attivi su diciotto GB di RAM. Supportato da Ollama via MLX.

## Capacità e performance

- Meta apre i pesi di Muse Glimmer, modello da trenta miliardi con licenza Apache due virgola zero, pensato per agenti locali sempre attivi: pianifica, chiama tool, gestisce errori e riprova, girando su diciotto GB RAM; Ollama lo supporta via engine MLX su Apple Silicon con ottimizzazioni NVIDIA e AMD in arrivo, e Unsloth lo fa eseguire a due bit con cento chiamate tool su quattordici GB di RAM.
- Muse Glimmer 30B di Meta ha battuto in un head-to-head Gemma 4 31B e Qwen3.6 27B generando giochi arcade retrò perfettamente funzionanti (Space Invaders, Tetris, Arkanoid con multiball) senza freeze o crash; gira nel browser su WebGPU alla stessa velocita' di llama.cpp, circa venticinque token al secondo su M4 Max, e nella virtualizzazione Metal su M1 Ultra segna sette virgola cinquantacinque prompt e otto virgola ottantasette generazione.

## Azienda di riferimento

- [[meta]]

## Strumenti correlati

- [[ollama]]

## Timeline delle notizie

- **2026-08-11** — Meta apre i pesi di Muse Glimmer, modello da trenta miliardi con licenza Apache due virgola zero, pensato per agenti locali sempre attivi: pianifica, chiama tool, gestisce errori e riprova, girando su diciotto GB RAM; Ollama lo supporta via engine MLX su Apple Silicon con ottimizzazioni NVIDIA e AMD in arrivo, e Unsloth lo fa eseguire a due bit con cento chiamate tool su quattordici GB di RAM.
- **2026-08-12** — Muse Glimmer 30B di Meta ha battuto in un head-to-head Gemma 4 31B e Qwen3.6 27B generando giochi arcade retrò perfettamente funzionanti (Space Invaders, Tetris, Arkanoid con multiball) senza freeze o crash; gira nel browser su WebGPU alla stessa velocita' di llama.cpp, circa venticinque token al secondo su M4 Max, e nella virtualizzazione Metal su M1 Ultra segna sette virgola cinquantacinque prompt e otto virgola ottantasette generazione.
- **2026-08-13** — I pesi di Muse Glimmer arrivano su Hugging Face il 10 agosto con licenza Apache 2.0: trenta miliardi di parametri con encoder di percezione multimodale, contesto da 131.072 token e oltre cento lingue, distillato da [[muse-spark-1-2]]; in BF16 pesa 59,6 GB, la quantizzazione a 4 bit scende sotto i 20 GB e gira su una scheda consumer da 24 o 32 GB, con il drafter DFlash che porta la generazione a circa il triplo.



- **2026-08-21** — Alibaba dichiara che [[qwen-3-8-27b]], pubblicato pochi giorni prima con tre miliardi di parametri in meno, supera Muse Glimmer su tutti e otto i benchmark di confronto diretto: i valori vanno letti a piena precisione e non sulle versioni compresse che girano sui computer degli utenti.

## Collegamenti

- [[gemma-4]]
- [[meta]]
- [[ollama]]
- [[qwen-3-6-27b]]
- [[index]]

