---
title: "Gemini CLI"
category: strumento
tags: [agent, coding, google]
related_puntate: [20260623]
created: 2026-08-12
updated: 2026-09-21
---

# Gemini CLI

## Introduzione

CLI di coding di Google, orchestrabile insieme a Claude Code e Codex via rmux.

## Funzionalità principali

- Gemini CLI è orchestrato da Claude Code sullo stesso terminale tramite rmux, la riscrittura Rust di tmux pensata per agenti.

## Timeline delle notizie

- **2026-06-23** — Gemini CLI è orchestrato da Claude Code sullo stesso terminale tramite rmux, la riscrittura Rust di tmux pensata per agenti.

- **2026-09-21** — È tra i quattro agenti vulnerabili a Plugin4Shell, con un percorso diverso dagli altri: il fetch sullo SHA seguito da un checkout di FETCH_HEAD finisce sul ramo sbagliato se il repository ha un ramo predefinito con quel nome. Google ha confermato il 4 agosto 2026 che non correggerà lo strumento, ritirato e sostituito con [[antigravity]] CLI.
- **2026-05-19** — La fine della CLI tradizionale viene annunciata al keynote di [[google-io|Google I/O 2026]] insieme ad Antigravity 2.0: la suite multi-agente standalone con CLI, SDK e voce nativa prende il posto della vecchia interfaccia a riga di comando, con la chiusura prevista entro il 18 giugno 2026.

## Collegamenti

- [[claude-code]]
- [[rmux]]
- [[index]]

