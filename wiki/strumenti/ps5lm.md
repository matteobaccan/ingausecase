---
title: "PS5LM Plus"
category: strumento
tags: [open-source, ai-locale, playstation, llama-cpp]
related_puntate: []
created: 2026-10-15
updated: 2026-10-15
sources: [raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]
---

# PS5LM Plus

## Introduzione

Fork del progetto open source PS5LM (licenza GPL-3.0) di Mert Cobanov, che porta llama.cpp sulla PlayStation 5: trasforma il port da payload ad app nativa e le mette a disposizione 11,44 GiB di memoria in un unico blocco, invece dei 6 GiB di un payload. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]

## Funzionalità principali

- Monta llama-server con il backend Vulkan di ggml, appoggiato a un port del driver RADV, e riceve i 12 GiB di memoria diretta e l'accesso alla GPU di cui gode un'app nativa. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]
- Espone sulla porta 8081 le API OpenAI Chat Completions, OpenAI Responses e Anthropic Messages: è quindi utilizzabile da opencode, aider, Codex e Claude Code, che ignorano il nome del modello richiesto e ricevono quello caricato. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]
- Sul televisore mostra una dashboard con velocità di generazione, uso di GPU e CPU, consumi, temperature e ventola; la biblioteca indica in anticipo se un file GGUF entra in memoria e i modelli si possono cercare e scaricare da Hugging Face dalla console, con ripresa del download e controllo SHA-256. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]

## Installazione e uso

- Richiede una PS5 con jailbreak (firmware dalla 7.00 alla 13.60) e i payload kstuff-lite, etaHEN e ShadowMountPlus, con elfldr opzionale per temperature e consumi e ftpsrv per copiare app e modelli; l'ultima versione citata è la v0.8.3 del 13 ottobre. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]

## Performance

- Qwen3.8-27B quantizzato a 2 bit (UD-Q2_K_XL, 9,2 GiB) gira a 20,3 token al secondo con 32k di contesto, la variante IQ2_XXS a 20,7 con 64k, Gemma 4 E4B q4_0 a 61 e Llama 3.2 3B a 124. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]

## Timeline delle notizie

- **2026-10-14** — PS5LM Plus fa girare Qwen 3.8 27B a circa 20 token al secondo sulla GPU di una PlayStation 5 con jailbreak, portando il progetto di Mert Cobanov da payload ad app nativa con 11,44 GiB di memoria: il modello ci sta solo quantizzato a 2 bit, e la pull request con l'app nativa era stata aperta sul repository il 9 ottobre e al 14 risultava ancora in attesa di fusione. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]

## Collegamenti

- [[ai-locale]]
- [[qwen-3-8-27b]]
- [[index]]
