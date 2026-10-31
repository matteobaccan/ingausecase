---
title: "Laya"
category: modello
tags: [decisioni, latenza, locale, open-source]
related_puntate: [20260921, 20260922, 20260929]
created: 2026-09-21
updated: 2026-09-29
sources: [raw/puntate/ainews20260921.md, raw/puntate/ainews20260922.md, raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md, raw/puntate/ainews20260929.md]
---

# Laya

## Introduzione

Modello decisionale locale presentato il 21 settembre 2026 come alternativa più veloce a [[jev]]: lavora offline, occupa circa un gigabyte di memoria ed è distribuito in open source su GitHub. [Fonte: raw/puntate/ainews20260921.md]

## Capacità e performance

- Dichiara 86,5 decisioni al secondo contro le 3,2 di Jev, con un tempo di risposta mediano di 9 millisecondi contro 313. [Fonte: raw/puntate/ainews20260921.md]
- Il confronto è fra modelli che non generano testo ma scelgono un'opzione fra quelle fornite, il caso d'uso su cui è nato Jev. [Fonte: raw/puntate/ainews20260921.md]
- Non genera testo e non produce token uno alla volta: prende in ingresso uno stato e una domanda tipizzata e restituisce probabilità calibrate in un unico passaggio in avanti, su tre tipi di domanda — choice (una probabilità per ciascuna opzione data), score (un valore su una scala ordinata) e noul (la probabilità che un'affermazione sia vera o falsa). [Fonte: raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md]
- L'architettura è un encoder bidirezionale che ricorda ModernBERT, con schema di attenzione globale e locale e meccanismo RoPE per la codifica posizionale, e tokenizzazione affidata al tokenizer Rust di Hugging Face: non un modello generativo in stile GPT. [Fonte: raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md]
- Il repository convaiinnovations/laya porta più checkpoint pubblici: uno in inglese da 421 milioni di parametri su backbone ModernBERT-large con contesto di 512 token, uno multilingue da 322 milioni su mmBERT-base che copre oltre cento lingue con contesto fino a 1.024 token estendibile a 8.000, e una variante specializzata in decisioni tipizzate, quella usata nel port MLX. Rispondono in circa 33 millisecondi. [Fonte: raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md]

## Timeline delle notizie

- **2026-09-21** — Laya, modello decisionale locale che batte Jev in velocità: 86,5 decisioni al secondo contro 3,2, circa un gigabyte di memoria, funzionamento offline e tempo di risposta mediano di 9 millisecondi contro 313. Open source, disponibile su GitHub. [Fonte: raw/puntate/ainews20260921.md]
- **2026-09-22** — Laya modello System One a pesi aperti batte Jev cloud-based a Tetris con decisioni 11 volte più veloci, gira su MacBook Air 16 GB. [Fonte: raw/puntate/ainews20260922.md]
- **2026-09-18** — Il modello è pubblicato da Nandakishor M con licenza Apache-2.0 su Hugging Face, tre giorni dopo il lancio di Jev, con la motivazione dichiarata di dimostrare che si può addestrare un modello piccolo e vicino allo stato dell'arte senza il supporto di un'azienda. [Fonte: raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md]
- **2026-09-19** — Esce [[laya-mlx]], il port su MLX per i Mac con chip Apple Silicon: risposte in 7-14 millisecondi, sotto il gigabyte di memoria, nessun byte inviato fuori dal dispositivo e benchmark su M3 Max con 13,42 e 7,39 millisecondi di latenza mediana. Laya riempie in tre giorni il vuoto lasciato da [[jev]], che resta un servizio hostato, chiuso e non disponibile in Europa. [Fonte: raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md]
- **2026-09-22** — Quattro giorni dopo il lancio il repository originale supera le 15.400 stelle con più di 1.270 fork, una crescita spinta non da un annuncio aziendale ma dalla reazione della community a un modello hostato e chiuso; attorno al progetto nascono una variante Core ML per il Neural Engine dei Mac, un porting per Node.js via ONNX Runtime e un tool di confronto diretto laya-vs-jev. [Fonte: raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md]
- **2026-09-29** — Laya Decision gira in locale dentro [[unsloth-desktop]] con quattro gigabyte di RAM, su CPU, Mac, Windows, Linux e GPU, servito tramite un'API compatibile [[jev]]. [Fonte: raw/puntate/ainews20260929.md]

## Collegamenti

- [[ai-locale]]
- [[jev]]
- [[laya-mlx]]
- [[typesafe-ai]]
- [[index]]
