---
title: "PixelRAG"
category: strumento
tags: [open-source, rag, retrieval, ricerca, screenshot, vision]
related_puntate: [20260621, 20260622, 20260623, 20260707, 20260719, 20260726, 20260731]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260621.md, raw/puntate/ainews20260622.md, raw/puntate/ainews20260623.md, raw/puntate/ainews20260707.md, raw/puntate/ainews20260719.md, raw/puntate/ainews20260726.md, raw/puntate/ainews20260731.md]
---

# PixelRAG

## Introduzione

Sistema di retrieval che salta il parsing HTML: fa screenshot della pagina e legge direttamente dai pixel, superando il baseline text RAG su Wikipedia. Include un plugin per Claude Code.

## Funzionalità principali

- PixelRAG è un sistema di retrieval che ignora il parsing HTML e lavora direttamente su screenshot: indicizza trenta milioni di immagini di Wikipedia e batte il miglior baseline testuale del diciotto percento; plugin per Claude Code incluso, nessun server MCP richiesto.
- PixelRAG salta completamente il parsing HTML: screenshot della pagina e un modello vision legge la risposta direttamente dai pixel; cento percento open source, con plugin Claude Code che dà occhi a Claude.
- PixelRAG salta il parsing HTML: screenshot della pagina e visione AI legge i pixel, con integrazione Claude Code tramite plugin MCP e nessuna dipendenza dalla struttura DOM.

## Timeline delle notizie

- **2026-06-21** — PixelRAG è un sistema di retrieval che ignora il parsing HTML e lavora direttamente su screenshot: indicizza trenta milioni di immagini di Wikipedia e batte il miglior baseline testuale del diciotto percento; plugin per Claude Code incluso, nessun server MCP richiesto. [Fonte: raw/puntate/ainews20260621.md]
- **2026-06-22** — PixelRAG salta completamente il parsing HTML: screenshot della pagina e un modello vision legge la risposta direttamente dai pixel; cento percento open source, con plugin Claude Code che dà occhi a Claude. [Fonte: raw/puntate/ainews20260622.md]
- **2026-06-23** — PixelRAG salta il parsing HTML: screenshot della pagina e visione AI legge i pixel, con integrazione Claude Code tramite plugin MCP e nessuna dipendenza dalla struttura DOM. [Fonte: raw/puntate/ainews20260623.md]
- **2026-07-07** — Non legge HTML ma la pagina come la vedi tu: cattura screenshot e recupera risposte direttamente dai pixel, supera il baseline testuale del 18,1%. Include plugin Claude Code. [Fonte: raw/puntate/ainews20260707.md]
- **2026-07-19** — PixelRAG indicizza screenshot invece di HTML, costruendo il RAG su quello che l'utente vede davvero: trenta milioni di screenshot Wikipedia, +18,1 per cento di accuratezza rispetto al miglior RAG testuale, con plugin Claude Code per la navigazione visiva. [Fonte: raw/puntate/ainews20260719.md]
- **2026-07-26** — Sistema di retrieval che saltava completamente il parsing HTML: screenshot della pagina, recupero dell'immagine e lettura diretta dai pixel. Batteva il baseline text RAG del 18,1 percento su Wikipedia, con plugin per Claude Code. [Fonte: raw/puntate/ainews20260726.md]
- **2026-07-31** — A 8.000 stelle su GitHub: non converte HTML in testo, fa screenshot della pagina, vettorizza le immagini e cerca con FAISS. Wikipedia precaricata con otto milioni di articoli. [Fonte: raw/puntate/ainews20260731.md]

## Collegamenti

- [[claude-code]]
- [[lang-extract]]
- [[open-source]]
- [[videorag]]
- [[index]]

