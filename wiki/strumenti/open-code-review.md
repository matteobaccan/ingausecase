---
title: "Open Code Review"
category: strumento
tags: [alibaba, code-review, open-source, agente]
related_puntate: [20260914]
created: 2026-09-14
updated: 2026-09-14
sources: [raw/puntate/ainews20260914.md]
---

# Open Code Review

## Introduzione

Sistema di revisione automatica del codice rilasciato da [[alibaba]], che l'azienda dice di aver usato internamente trovando milioni di difetti. [Fonte: raw/puntate/ainews20260914.md]

## Funzionalità principali

- Il loop non è interamente affidato a un LLM: la copertura dei file, il bundling, il matching delle regole e il posizionamento dei commenti sono gestiti da codice deterministico, mentre l'agente si occupa del ragionamento e del contesto del repository. [Fonte: raw/puntate/ainews20260914.md]
- Su un benchmark di 200 pull request attraverso 50 repository open source, Alibaba dichiara precisione e F1 superiori a [[claude-code]] usando lo stesso modello, con circa un nono dei token; il trade-off dichiarato è un recall più basso. [Fonte: raw/puntate/ainews20260914.md]

## Azienda / Autore

- [[alibaba]]

## Timeline delle notizie

- **2026-09-14** — Alibaba rilascia Open Code Review, sistema di revisione automatica del codice usato internamente per trovare milioni di difetti: precisione e F1 superiori a Claude Code su 200 pull request di 50 repository open source, con circa un nono dei token e un recall più basso. [Fonte: raw/puntate/ainews20260914.md]

## Collegamenti

- [[alibaba]]
- [[claude-code]]
- [[sviluppo-software-ai]]
- [[index]]
