---
title: "Bonsai 2 27B"
category: modello
tags: [ternario, compressione, open-weight, reasoning]
related_puntate: [20260925, 20260928]
created: 2026-09-22
updated: 2026-09-28
sources: [raw/tldr/tldr20260918.md, raw/puntate/ainews20260925.md, raw/puntate/ainews20260928.md]
---

# Bonsai 2 27B

## Introduzione

Modello ternario con pesi -1,0,+1 e scaling FP16, 1,76 bit per peso e 5,9GB footprint, contesto 262k token multimodale. [Fonte: raw/tldr/tldr20260918.md]

## Timeline delle notizie

- **2026-09-18** — PrismML rilascia Bonsai 2 27B con pesi ternari e 9x compressione. [Fonte: raw/tldr/tldr20260918.md]
- **2026-09-25** — La variante Uncensored di Bonsai-2 27B pesa sei e sette gigabyte e ha riconoscimento delle immagini e del giapponese particolarmente forti, con la stessa quantizzazione a tre valori; per usarla in ComfyUI serve un llama.cpp dedicato e la soluzione pratica è avviare Bonsai a parte e chiamarlo da ComfyUI come se fosse Ollama, con la memoria video che scende da diecimiladuecentonovanta MiB a duemilacentoquarantanove MiB. [Fonte: raw/puntate/ainews20260925.md]

- **2026-09-28** — Ternary Bonsai 2.27B di [[prismml]] gira sei volte più veloce su Mac, il 503,2 per cento rispetto alla baseline: record ottenuto in meno di tre giorni dall'apertura della challenge su Yukon Research, con il contributo di agenti costruiti su Claude, GPT, Grok, DeepSeek e Gemini. [Fonte: raw/puntate/ainews20260928.md]

## Collegamenti

- compressione modelli
- [[index]]
