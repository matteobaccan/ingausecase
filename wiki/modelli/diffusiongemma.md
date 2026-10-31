---
title: "DiffusionGemma"
category: modello
tags: [accuratezza, diffusion, google, moe, open-source, ricerca, velocita]
related_puntate: [20260611, 20260612, 20260613, 20260811, 20260923]
created: 2026-08-12
updated: 2026-09-23
---

# DiffusionGemma

## Introduzione

Progetto di Google sulla text diffusion: report tecnico completo pubblicato con processo e insight aperti alla community.

## Capacità e performance

- DiffusionGemma ha ventisei miliardi MoE basati su Gemma 4 e genera blocchi di testo simultaneamente invece del token singolo: quattro volte più veloce su GPU consumer popolari, diciotto gigabyte di VRAM quantizzato, oltre settecento token al secondo su una singola RTX 5090; Apache 2.0.
- DiffusionGemma-26B genera duecentocinquantasei token contemporaneamente invece che parola per parola: architettura MoE con solo tre punto otto miliardi di parametri attivi, gira su RTX 3090 con diciotto giga di VRAM ed è disponibile su llama.cpp.
- DiffusionGemma genera testo quattro volte più veloce di Gemma 4 standard ma con sei volte più errori: nel test su biografia di Steve Jobs e storia di Tetris ha prodotto trentatré fatti corretti contro ventotto sbagliati, e Google stessa consiglia Gemma 4 standard per la precisione fattuale. Unsloth lo ha ottimizzato a oltre duemila token al secondo (uno punto otto volte più veloce) su diciotto gigabyte di RAM.

## Azienda di riferimento

- [[google]]
- [[unsloth]]

## Timeline delle notizie

- **2026-06-11** — DiffusionGemma ha ventisei miliardi MoE basati su Gemma 4 e genera blocchi di testo simultaneamente invece del token singolo: quattro volte più veloce su GPU consumer popolari, diciotto gigabyte di VRAM quantizzato, oltre settecento token al secondo su una singola RTX 5090; Apache 2.0.
- **2026-06-12** — DiffusionGemma-26B genera duecentocinquantasei token contemporaneamente invece che parola per parola: architettura MoE con solo tre punto otto miliardi di parametri attivi, gira su RTX 3090 con diciotto giga di VRAM ed è disponibile su llama.cpp.
- **2026-06-13** — DiffusionGemma genera testo quattro volte più veloce di Gemma 4 standard ma con sei volte più errori: nel test su biografia di Steve Jobs e storia di Tetris ha prodotto trentatré fatti corretti contro ventotto sbagliati, e Google stessa consiglia Gemma 4 standard per la precisione fattuale. Unsloth lo ha ottimizzato a oltre duemila token al secondo (uno punto otto volte più veloce) su diciotto gigabyte di RAM.
- **2026-08-11** — DiffusionGemma: Google pubblica il report tecnico completo sulla text diffusion, con processo e insight aperti alla community.

- **2026-09-23** — Una variante DiffusionGemma-Jev arriva su Cloud Run di [[google]]: un comando, endpoint compatibile con l'API [[jev]], latenza per singolo step tra trentacinque e sessanta millisecondi, batch da circa cento-centoventitré richieste al secondo, costo di tre dollari l'ora e zero quando inattivo.

## Collegamenti

- [[jev]]
- [[gemini-3-5]]
- [[gemma-4]]
- [[google]]
- [[unsloth]]
- [[index]]

