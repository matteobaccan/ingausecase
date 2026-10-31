---
title: "Qwen3-TTS"
category: modello
tags: [alibaba, locale, tts, voce]
related_puntate: [20260810]
created: 2026-08-12
updated: 2026-08-12
---

# Qwen3-TTS

## Introduzione

Sistema TTS di Alibaba arrivato in llama.cpp: due GGUF da caricare insieme (parlante e tokenizzatore audio), Apache due virgola zero, audio mono ventiquattro kHz.

## Capacità e performance

- Qwen3-TTS e' arrivato in llama punto cpp: due GGUF insieme (parlante e tokenizzatore audio), a Q4_K_M fanno uno punto due GB piu' duecentocinquantacinque MB, Apache due virgola zero, audio mono a ventiquattro kHz; testato con clip di riferimento di nove secondi e quaranta frasi: Q4 su uno virgola sette miliardi gira in tempo reale su CPU desktop normale, il punto sei miliardi va al doppio della velocita', timbro perfetto ma domande piatte, Q8 risolve tutto con novecento MB extra.

## Strumenti correlati

- [[llama-cpp]]

## Timeline delle notizie

- **2026-08-10** — Qwen3-TTS e' arrivato in llama punto cpp: due GGUF insieme (parlante e tokenizzatore audio), a Q4_K_M fanno uno punto due GB piu' duecentocinquantacinque MB, Apache due virgola zero, audio mono a ventiquattro kHz; testato con clip di riferimento di nove secondi e quaranta frasi: Q4 su uno virgola sette miliardi gira in tempo reale su CPU desktop normale, il punto sei miliardi va al doppio della velocita', timbro perfetto ma domande piatte, Q8 risolve tutto con novecento MB extra.

## Collegamenti

- [[llama-cpp]]
- [[index]]

