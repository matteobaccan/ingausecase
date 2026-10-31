---
title: "pplx-decider-flash 1.2"
category: modello
tags: [decisioni, perplexity, on-device, open-weight, qwen]
related_puntate: []
created: 2026-10-25
updated: 2026-10-25
sources: [raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]
---

# pplx-decider-flash 1.2

## Introduzione

Decision model da 4 miliardi di parametri di [[perplexity]], nome ufficiale pplx-decider-flash-v1.2: non scrive testo ma risponde sul contenuto di un testo o di un'immagine con una probabilità per ciascuna risposta ammessa. È la versione piccola di pplx-decider-v1.2, costruita su [[qwen-3-5|Qwen3.5-4B]] e distillata dai modelli da 27 miliardi della stessa famiglia, circa un settimo delle dimensioni, e arriva sul Mac dell'utente attraverso [[decider-for-mac]]. [Fonte: raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]

## Capacità e performance

- Sul Decision Index 0.3 totalizza 58,88 raggruppando le domande e 60,05 con una domanda per richiesta, contro il 68,09 del modello da 27 miliardi; sulla parte visiva, con immagini fino a 1,6 megapixel, i punteggi sono 72,53 contro 77,43. [Fonte: raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]
- La scheda dichiara un'accuratezza dell'88,8 per cento su 1.497 domande di sviluppo, con errore di calibrazione atteso a 0,021 e punteggio di Brier a 0,163; è Perplexity stessa a tenere il Decision Index su cui il modello primeggia tra i 4B, senza confronti indipendenti con [[jev]], [[clef]] o [[strands-decider-2b]]. [Fonte: raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]
- La licenza dichiarata è Apache 2.0, ma il repository è privato e richiede un token Hugging Face con accesso; il runtime incluso nell'app serve perché llama-server standard non implementa il protocollo del checkpoint, con strati di attenzione non causali e lettura a ogni marcatore speciale. [Fonte: raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]

## Azienda di riferimento

- [[perplexity]]

## Timeline delle notizie

- **2026-10-24** — Esce con Decider for Mac pplx-decider-flash-v1.2: decision model da 4 miliardi di parametri costruito su Qwen3.5-4B, distillato dai 27 miliardi di Perplexity, con 58,88 punti sul Decision Index e una conversione q8_0 da 5,16 GB più 672 MB per il proiettore delle immagini che gira in locale sul Mac. [Fonte: raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]

## Collegamenti

- [[perplexity]]
- [[decider-for-mac]]
- [[pplx-decider-v1-1-27b]]
- [[qwen-3-5]]
- [[decision-model]]
- [[jev]]
- [[index]]
