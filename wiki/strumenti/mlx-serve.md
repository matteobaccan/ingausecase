---
title: "MLX-Serve"
category: strumento
tags: [apple-silicon, inferenza, locale, mlx]
related_puntate: [20261002]
created: 2026-10-03
updated: 2026-10-03
sources: [raw/puntate/ainews20261002.md]
---

# MLX-Serve

## Introduzione

Motore di inferenza per Apple silicon giunto alla versione 26.10.1, con aumenti di velocità su tutta la linea e nuove funzionalità per modelli GGUF e pack eseguibili.

## Funzionalità principali

- Qwen 3.8 27B con drafter guadagna il 66% su M5 Ultra, il 28% su M4 Max e il 37% su M1 Pro; Qwen Flash Next segna +11% in decode su M4 Max e +51% in prefill su M5 Ultra, mentre Gemma 4, Qwen, LFM 2.5, Spark e Bonsai 2 risultano tutti più veloci. [Fonte: raw/puntate/ainews20261002.md]
- I modelli GGUF girano su un engine MLX proprietario scritto in Zig e Metal, i pack in formato Sushi-format Flash Next sono eseguibili direttamente e Qwen-Image 2.1 modifica immagini da istruzioni. [Fonte: raw/puntate/ainews20261002.md]

## Timeline delle notizie

- **2026-10-02** — Esce MLX-Serve 26.10.1, con aumenti di velocità su tutta la linea (Qwen 3.8 27B con drafter +66% su M5 Ultra) e nuove funzionalità: modelli GGUF su engine MLX proprietario in Zig e Metal, pack Sushi-format Flash Next eseguibili direttamente e drafting attivo di default. [Fonte: raw/puntate/ainews20261002.md]
- **2026-10-02** — Esce MLX-Serve 26.10.1 con aumenti di velocità su tutta la linea: Qwen 3.8 27B con drafter guadagna il 66% su M5 Ultra, il 28% su M4 Max e il 37% su M1 Pro, mentre Qwen Flash Next segna +11% in decode su M4 Max e +51% in prefill su M5 Ultra; i modelli GGUF girano su un engine MLX proprietario in Zig e Metal e Qwen-Image 2.1 modifica immagini da istruzioni. [Fonte: raw/puntate/ainews20261002.md]




## Collegamenti

- [[qwen-3-8-27b]]
- [[ai-locale]]
- [[index]]
