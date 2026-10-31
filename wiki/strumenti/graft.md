---
title: "Graft"
category: strumento
tags: [agent, codebase, efficienza, open-source, produttivita]
related_puntate: [20260804, 20260812, 20260908]
created: 2026-08-12
updated: 2026-09-08
---

# Graft

## Introduzione

Strumento che mappa il repository una volta e fa leggere la mappa all'agente: quarantadue percento meno token, quarantasei percento meno tool calls e sessanta percento meno tempo, con tree-sitter puro e tutto locale.

## Funzionalità principali

- Graft costruisce una mappa markdown persistente della tua codebase così gli agenti non devono riscannerizzare tutto a ogni sessione: trentadue percento meno costi e sessanta percento meno latenza.
- Graft risolve lo spreco di token: mappa il repository una volta e l'agente legge la mappa, con quarantadue percento meno token, quarantasei percento meno tool calls e sessanta percento meno tempo; pure tree-sitter, cento percento locale.

## Timeline delle notizie

- **2026-08-04** — Graft costruisce una mappa markdown persistente della tua codebase così gli agenti non devono riscannerizzare tutto a ogni sessione: trentadue percento meno costi e sessanta percento meno latenza.
- **2026-08-12** — Graft risolve lo spreco di token: mappa il repository una volta e l'agente legge la mappa, con quarantadue percento meno token, quarantasei percento meno tool calls e sessanta percento meno tempo; pure tree-sitter, cento percento locale.
- **2026-09-08** — Graft risolve il forgetting della codebase: costruisce la comprensione una volta come file markdown collegati (un nodo per sistema/API/concetto, inglese semplice, no embedding/vector DB), testato su SWE-bench Verified 33/50 vs 27/50 senza Graft con -23% token, -25% tool call, -32% tempo.

## Collegamenti

- [[langgraph]]
- [[index]]

