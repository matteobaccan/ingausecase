---
title: "Trivy"
category: strumento
tags: [open-source, scanner, sicurezza]
related_puntate: [20260521]
created: 2026-08-12
updated: 2026-09-21
sources: [raw/puntate/ainews20260521.md, raw/pillitteri/pillitteri20260816-litellm-supply-chain-attacco-2026.md]
---

# Trivy

## Introduzione

Scanner di sicurezza open source per container e codebase, avvelenato da TeamPCP a marzo 2026.

## Funzionalità principali

- Trivy è stato avvelenato da TeamPCP a marzo, nell'ambito di un'operazione di supply chain attack che ha colpito poi Checkmarx (aprile) e TanStack (maggio).

## Azienda / Autore

- [[teampcp]]

## Timeline delle notizie

- **2026-05-21** — Trivy è stato avvelenato da TeamPCP a marzo, nell'ambito di un'operazione di supply chain attack che ha colpito poi Checkmarx (aprile) e TanStack (maggio). La ricostruzione dell'attacco a [[litellm]] mostra il ruolo dello scanner nella catena: il progetto lo installava senza bloccarne la versione, quindi il codice malevolo è entrato nella build in automatico senza che gli aggressori toccassero LiteLLM direttamente, e la conseguenza è stato un archivio da 153 gigabyte con 433.909 file da 2.488 organizzazioni, ancora in parte validi cinque mesi dopo. [Fonte: raw/puntate/ainews20260521.md] [Fonte: raw/pillitteri/pillitteri20260816-litellm-supply-chain-attacco-2026.md]

## Collegamenti

- [[teampcp]]
- [[index]]

