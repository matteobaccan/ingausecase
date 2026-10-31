---
title: "Android MCP"
category: trend
tags: [agent, android, mcp, os]
related_puntate: [20260514]
created: 2026-08-12
updated: 2026-09-21
---

# Android MCP

## Introduzione

MCP nativo nel sistema operativo Android per azioni cross-app tramite annotazione @AppFunction, con agenti che concatenano funzioni tra app diverse.

## Timeline delle notizie

- **2026-05-14** — Android ora ha MCP nativo nell'OS per azioni cross-app: le app espongono funzioni come tool per Gemini e altri agenti con l'annotazione '@AppFunction', funziona come MCP ma in locale sul device, senza server né round-trip di rete; disponibile su Android 16+, Early Access Program già aperto.
- **2026-05-19** — A Google I/O il concetto diventa il cuore tecnico di [[gemini-intelligence]]: il sistema può eseguire azioni multi-step direttamente sul dispositivo senza chiedere conferma a ogni passaggio, con l'inferenza on-device come default per le azioni sensibili e il cloud usato solo previo consenso esplicito.
- **2026-06-18** — Con il rilascio stabile di [[android-17]] il protocollo prende il nome di AppFunctions: è una nuova API di piattaforma che si appoggia ad Android MCP e permette a ogni applicazione di dichiarare le proprie capacità come strumenti richiamabili da Gemini, esposti con una sola annotazione nel codice, così invece di un assistente che indovina cosa fare le app gli mettono a disposizione azioni precise e tipizzate.

## Collegamenti

- [[android-17]]
- [[gemini-intelligence]]
- [[index]]

