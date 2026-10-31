---
title: "Pi Extensible Workflows"
category: strumento
tags: [agenti, orchestrazione, dsl, open-source]
related_puntate: []
created: 2026-10-07
updated: 2026-10-07
sources: [raw/pillitteri/pillitteri20260825-pi-extensible-workflows-guida.md]
---

# Pi Extensible Workflows

## Introduzione

Pacchetto di terze parti per [[pi]], il harness minimale per agenti di coding mantenuto da Earendil. Scritto da Andrea Baccega (vekexasia) e rilasciato a luglio 2026 con licenza MIT, alla versione 5.8.0 conta 193 stelle e aggiunge al core, che non include sub-agent né modalità multi-agente, un modo per orchestrare più agenti in parallelo in maniera deterministica e ripristinabile.

## Capacita' e performance

- Trasforma un compito in uno script JavaScript deterministico che distribuisce il lavoro su più subagent con le primitive `agent()`, `parallel()` e `pipeline()`, registra ogni risultato in un journal e riprende un'esecuzione interrotta senza rieseguire i passi già completati. [Fonte: raw/pillitteri/pillitteri20260825-pi-extensible-workflows-guida.md]
- Lo script gira in un sandbox in cui `Date.now()`, `Math.random()` e `new Date()` senza argomenti sollevano un errore: senza tempo e senza casualità nel codice due esecuzioni seguono lo stesso percorso, e questo rende stabile il resume. Ogni subagent parte da una sessione pulita e restituisce all'orchestratore solo il risultato, non il contesto accumulato. [Fonte: raw/pillitteri/pillitteri20260825-pi-extensible-workflows-guida.md]
- Include lo starter `reviewLoop({ task, maxIterations })`, che alterna i ruoli developer e reviewer finché il revisore approva o si raggiunge il limite di iterazioni, con `shell()` come gate deterministico per far girare test o linter. Richiede Node.js 22.19 o successivo e si installa con `pi install npm:pi-extensible-workflows`. [Fonte: raw/pillitteri/pillitteri20260825-pi-extensible-workflows-guida.md]

## Strumenti correlati

- [[pi]]

## Timeline delle notizie

- **2026-08-25** — Esce la guida a Pi Extensible Workflows, pacchetto MIT di Andrea Baccega che dota Pi di un DSL JavaScript deterministico per orchestrare più agenti: primitive `agent()`, `parallel()`, `pipeline()`, `shell()` e `withWorktree()`, journal per la ripresa senza rieseguire i passi completati e lo starter reviewLoop per il ciclo sviluppatore-revisore. [Fonte: raw/pillitteri/pillitteri20260825-pi-extensible-workflows-guida.md]

## Collegamenti

- [[pi]]
- [[agenti-ai]]
- [[index]]
