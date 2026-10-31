---
title: "Wayfinder"
category: strumento
tags: [claude-code, pianificazione, skill, ticket]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
sources: [raw/pillitteri/pillitteri20260821-wayfinder-skill-claude-code-pianificare.md]
---

# Wayfinder

## Introduzione

Skill open source di [[claude-code]] scritta da [[matt-pocock]] che non scrive codice: serve a pianificare un blocco di lavoro più grande di quanto una sola sessione di agente possa contenere, sotto forma di una mappa condivisa di ticket di decisione sull'issue tracker, da risolvere uno alla volta finché la strada verso la destinazione non è chiara. [Fonte: raw/pillitteri/pillitteri20260821-wayfinder-skill-claude-code-pianificare.md]

## Funzionalità principali

- L'unità di lavoro non è una fetta di prodotto da costruire ma una domanda la cui risoluzione è una decisione: quando tutte le decisioni sono prese la mappa è finita, e la skill è costruita attorno a due immagini, la destinazione e la nebbia. [Fonte: raw/pillitteri/pillitteri20260821-wayfinder-skill-claude-code-pianificare.md]
- L'invocazione è bloccata al solo utente tramite il comando `/wayfinder`, perché è un atto deliberato di pianificazione e non qualcosa che l'agente avvia da sé nel mezzo di un altro compito. [Fonte: raw/pillitteri/pillitteri20260821-wayfinder-skill-claude-code-pianificare.md]
- Il problema che attacca è dimensionale: Claude Code lavora in una finestra di circa 200.000 token e un singolo ticket Wayfinder è pensato per stare in una sessione da 100.000 token, mentre un progetto vero — una migrazione di dati o una specifica ampia — non ci sta. [Fonte: raw/pillitteri/pillitteri20260821-wayfinder-skill-claude-code-pianificare.md]

## Timeline delle notizie

- **2026-08-21** — Wayfinder è la skill che ha trainato la diffusione del repository mattpocock/skills, oltre 227.000 stelle da quando è nato il 3 febbraio 2026: mette la pianificazione prima dell'esecuzione e la rende un artefatto condiviso di ticket di decisione sull'issue tracker, con la destinazione che può essere una specifica, una decisione da bloccare o una modifica sul posto. [Fonte: raw/pillitteri/pillitteri20260821-wayfinder-skill-claude-code-pianificare.md]

## Collegamenti

- [[claude-code]]
- [[matt-pocock]]
- [[sviluppo-software-ai]]
- [[index]]
