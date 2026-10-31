---
title: "LLM Wiki"
category: strumento
tags: [conoscenza, locale, mcp, obsidian, wiki]
related_puntate: [20260913]
created: 2026-09-13
updated: 2026-10-11
---

# LLM Wiki

## Introduzione

App desktop locale che trasforma documenti in una wiki strutturata con pagine interconnesse e grafo della conoscenza, dove ogni pagina cita il file sorgente e la wiki si aggiorna man mano che si aggiungono contenuti.

## Funzionalità principali

- Trasformazione di documenti in pagine interconnesse con grafo della conoscenza e citazione del file sorgente su ogni pagina.
- Funziona come vault [[obsidian]] e include un server [[mcp]] per integrare [[claude-code]] e [[codex]].

## Timeline delle notizie

- **2026-04-28** — Il pattern LLM Wiki descrive tre directory — `raw/` con le fonti immutabili, `wiki/` con le pagine markdown generate e un CLAUDE.md che fissa schema e convenzioni — in cui l'agente legge una fonte una volta sola e la compila nella pagina, o nelle pagine, che le competono. Il vantaggio è che il lavoro di sintesi si sposta dall'interrogazione all'ingest: niente embedding, niente similarity search, wiki leggibile da un umano e costo per query tra 0,001 e 0,003 dollari, con il limite dei 50.000-100.000 documenti oltre i quali la manutenzione diventa scomoda.

- **2026-09-13** — L'app desktop locale arriva sulla puntata: documenti che diventano wiki strutturata con grafo della conoscenza, formato vault [[obsidian]] e server [[mcp]] per [[claude-code]] e [[codex]].

## Collegamenti

- [[claude-code]]
- [[codex]]
- [[mcp]]
- [[obsidian]]
- [[index]]
