---
title: "Intelligent Terminal"
category: strumento
tags: [agenti, microsoft, terminale, windows]
related_puntate: []
created: 2026-10-08
updated: 2026-10-08
sources: [raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]
---

# Intelligent Terminal

## Introduzione

Fork open source e sperimentale di Windows Terminal con un agente AI integrato,
presentato da [[microsoft]] al Build 2026 il 2 giugno e rilasciato lo stesso
giorno nella versione 0.1. È un binario separato, che si installa accanto al
terminale classico senza modificarne il codice, con licenza MIT e in C++;
Microsoft continua a sviluppare Windows Terminal in parallelo.

## Capacità e performance

- L'agent pane è un pannello laterale agganciabile a uno dei quattro lati della
  finestra, si apre con Ctrl+Shift+. e prende il focus con Ctrl+Shift+I: ha
  accesso diretto all'output del terminale, mantiene i thread di conversazione e
  può avviare task in background su nuove schede.
  [Fonte: raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]
- Quando un comando termina con un codice di errore il terminale lo intercetta,
  mostra un indicatore nella barra di stato e apre il pannello con il contesto
  già caricato; nelle impostazioni si sceglie fra il solo rilevamento e il
  suggerimento automatico della soluzione.
  [Fonte: raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]
- L'agente si invoca dalla Command Palette con `?` e una richiesta in linguaggio
  naturale, mentre Ctrl+Shift+/ apre la gestione delle sessioni con gli agenti
  attivi, i task lunghi e le conversazioni passate.
  [Fonte: raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]
- Si appoggia ad [[agent-client-protocol]]: l'applicazione avvia la CLI
  dell'agente come sottoprocesso locale e scambia messaggi JSON-RPC 2.0 su stdin
  e stdout, rilevando le CLI già installate fra cui [[claude-code]], OpenAI Codex
  e Google Gemini, con fallback su GitHub Copilot CLI installato via WinGet.
  [Fonte: raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]
- Il terminale non chiama API cloud e non conserva la cronologia: passa il
  contesto della shell alla CLI locale, ed è l'agente scelto a comunicare con il
  proprio fornitore. [Fonte: raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]

## Disponibilità

- Gratuito e open source, richiede Windows 11 e una CLI agente; si installa dal
  Microsoft Store, con `winget install Microsoft.IntelligentTerminal` o dal
  sorgente su GitHub. È dichiarato come esperimento, non come prodotto maturo.
  [Fonte: raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]

## Azienda di riferimento

- [[microsoft]]

## Timeline delle notizie

- **2026-06-02** — [[microsoft]] presenta al Build 2026 Intelligent Terminal, fork open source di Windows Terminal con un agente integrato nell'agent pane: rilevamento automatico degli errori con correzione suggerita, task in background, sessioni ripristinabili e comunicazione con le CLI degli agenti via [[agent-client-protocol]]; al lancio il repository conta circa 744 stelle. [Fonte: raw/pillitteri/pillitteri20260608-intelligent-terminal-microsoft-windows-terminal-ai.md]

## Collegamenti

- [[microsoft]]
- [[agent-client-protocol]]
- [[claude-code]]
- [[github-copilot]]
- [[warp-terminal]]
- [[index]]
