---
title: "pxpipe"
category: strumento
tags: [claude-code, open-source, proxy, risparmio-token, visione]
related_puntate: []
created: 2026-10-11
updated: 2026-10-11
sources: [raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]
---

# pxpipe

## Introduzione

Proxy locale di Steven Chong che trasforma il contesto testuale più ingombrante in pagine PNG, sfruttando il fatto che il costo in token di un'immagine dipende dai pixel e non da quanto testo contiene. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]

## Funzionalità principali

- Intercetta le richieste di [[claude-code]] e converte prompt di sistema, documentazione dei tool, cronologia vecchia e blocchi di `tool_result` in immagini prima di inviarli al modello. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]
- Il taglio dichiarato è del 59-70 per cento sulle richieste: un caso documentato porta 48.000 caratteri di prompt di sistema da circa 25.000 token testuali a circa 2.700 token immagine su una sola pagina. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]
- Limite dichiarato dagli autori: la visione del modello non è OCR, quindi hash, ID, segreti, percorsi e numeri esatti possono non essere recuperati byte per byte e vanno tenuti come testo. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]

## Installazione e uso

- Si avvia con `npx pxpipe-proxy` e si punta Claude Code al proxy con `ANTHROPIC_BASE_URL=http://127.0.0.1:47821`. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]

## Repository

- pxpipe di Steven Chong, 5.505 stelle e licenza MIT; la fonte non riporta l'indirizzo del repository.

## Timeline delle notizie

- **2026-07-11** — pxpipe porta 5.505 stelle e rappresenta lo strato più radicale del risparmio token: invece di comprimere il testo lo rende immagine, con un rapporto vicino a 9 a 1 sui blocchi densi e una demo su Fable 5 scesa da 42,21 a 6,06 dollari, al prezzo di una precisione non garantita su stringhe che devono tornare identiche. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]

## Collegamenti

- [[claude-code]]
- [[caveman]]
- [[headroom]]
- [[rtk]]
- [[index]]
