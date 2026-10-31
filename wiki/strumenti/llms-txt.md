---
title: "llms.txt"
category: strumento
tags: [seo, agent, open-source, documentazione]
created: 2026-10-01
updated: 2026-10-01
---

# llms.txt

## Introduzione

File di testo in formato Markdown, collocato nella radice di un sito, che riassume in modo compatto struttura e contenuti principali per i modelli linguistici e gli agenti AI. La proposta è di Jeremy Howard, cofondatore di Answer.AI, lanciata nel settembre 2024.

## Funzionalità principali

- Offre ai modelli una mappa curata del sito, così non devono ricostruirla scansionando decine di URL.
- Il repository della specifica conta 2.417 stelle a fine maggio 2026.

## Adozione e limiti

- Circa il 10% dei siti ha creato un llms.txt, ma i bot AI lo richiedono nello 0,1% dei casi: su 62.100 visite di bot AI in 90 giorni solo 84 hanno toccato il file.
- I crawler di ricerca (Googlebot, GPTBot) non lo usano per il ranking; alcuni agenti applicativi (Claude Desktop, Cursor, Continue, Cline) lo leggono nei flussi di retrieval.
- La guida Search di Google del 15 maggio 2026 lo elenca tra le cose che non servono per la ricerca generativa, mentre Chrome lo verifica con un audit sperimentale in Lighthouse (categoria Agentic Browsing).

## Timeline delle notizie

- **2026-05-30** — Google dice da una parte che llms.txt non serve per la ricerca generativa e dall'altra lo controlla con un audit di Chrome: su 62.100 richieste di bot AI in 90 giorni solo 84 hanno toccato il file, lo 0,1%, mentre il file è letto davvero da alcuni agenti applicativi.

## Collegamenti

- [[ai-overviews]]
- [[mcp]]
- [[open-source]]
- [[index]]
