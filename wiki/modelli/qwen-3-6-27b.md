---
title: "Qwen3.6-27B"
category: modello
tags: [alibaba, denso, llm, locale, open-weight, qwen]
related_puntate: [20260525, 20260616, 20260704, 20260812, 20260904]
created: 2026-08-12
updated: 2026-09-04
sources: [raw/puntate/ainews20260525.md, raw/puntate/ainews20260616.md, raw/puntate/ainews20260704.md, raw/puntate/ainews20260812.md, raw/puntate/ainews20260904.md]
---

# Qwen3.6-27B

## Introduzione

Modello di Alibaba indicato da Hacker News come ideale per sviluppo locale: 300.000 token/s su MacBook M5 Max e 50 token/s su RTX 5090.

## Capacità e performance

- Qwen 3.6 27B gira su 16 GB di VRAM (RTX 4060 Ti) grazie a Pure Quant: 40 token al secondo con MTP attivi e 64000 token di contesto con KVCache quantizzato.
- Qwen3.6-27B ha ottenuto punteggio perfetto nel nuovo benchmark PromptAuthority-15, che testa chi il modello obbedisce quando sviluppatore, utente e pagina web danno ordini contrastanti: centoventisettemila parametri, zero errori.
- Hacker News lo indica come il modello ideale per sviluppo locale: 300.000 token/s su MacBook M5 Max, 50 token/s su RTX 5090. Descritto come il primo modello locale con intelligenza generale vera.

## Strumenti correlati

- [[promptauthority-15]]
- [[pure-quant]]

## Timeline delle notizie

- **2026-05-25** — Qwen 3.6 27B gira su 16 GB di VRAM (RTX 4060 Ti) grazie a Pure Quant: 40 token al secondo con MTP attivi e 64000 token di contesto con KVCache quantizzato. [Fonte: raw/puntate/ainews20260525.md]
- **2026-06-16** — Qwen3.6-27B ha ottenuto punteggio perfetto nel nuovo benchmark PromptAuthority-15, che testa chi il modello obbedisce quando sviluppatore, utente e pagina web danno ordini contrastanti: centoventisettemila parametri, zero errori. [Fonte: raw/puntate/ainews20260616.md]
- **2026-07-04** — Hacker News lo indica come il modello ideale per sviluppo locale: 300.000 token/s su MacBook M5 Max, 50 token/s su RTX 5090. Descritto come il primo modello locale con intelligenza generale vera. [Fonte: raw/puntate/ainews20260704.md]

- **2026-09-04** — Mirai ha rilasciato speculative decoding per Qwen 3.6 27B nel suo engine uzulu: su chip Apple M5 batte MTPLX di quasi due volte e llama.cpp di oltre tre volte. [Fonte: raw/puntate/ainews20260904.md]
- **2026-08-12** — In un confronto head-to-head Qwen3.6 27B e' stato superato da Muse Glimmer 30B di Meta nella generazione di giochi arcade retrò perfettamente funzionanti. [Fonte: raw/puntate/ainews20260812.md]

## Collegamenti

- [[muse-glimmer]]
- [[promptauthority-15]]
- [[pure-quant]]
- [[uzulu]]
- [[index]]

