---
title: "rtk"
category: strumento
tags: [claude-code, costi, proxy, rust]
related_puntate: [20260510, 20260906]
created: 2026-08-12
updated: 2026-10-11
sources: [raw/puntate/ainews20260510.md, raw/puntate/ainews20260906.md, raw/pillitteri/pillitteri20260421-claude-code-token-10-repo-github-risparmio.md, raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]
---

# rtk

## Introduzione

Proxy Rust a binario unico che taglia il 60-90% dei token su Claude Code.

## Funzionalità principali

- rtk taglia il 60-90% dei token su Claude Code: è un proxy Rust con binario unico, tra i sei repo GitHub che eliminano abbonamenti per quasi 3.000 dollari al mese.

## Timeline delle notizie

- **2026-04-21** — rtk, «Rust Token Killer» con 31.234 stelle al 21 aprile 2026, è un binario Rust senza dipendenze che si mette davanti ai comandi shell e filtra l'output prima che arrivi a Claude: nei benchmark pubblicati `cargo test` passa da 155 righe a 3 e `npm install` da 4.000 righe a 15. [Fonte: raw/pillitteri/pillitteri20260421-claude-code-token-10-repo-github-risparmio.md]

- **2026-07-11** — rtk arriva a 70.205 stelle ed è descritto come il secondo strumento del gruppo: un binario Apache 2.0 installabile via Homebrew o Cargo che intercetta i comandi Bash tramite un hook di riscrittura e applica rimozione del rumore, raggruppamento, troncamento e deduplicazione, con un esempio che porta una sessione da circa 118.000 a 23.900 token. Il limite strutturale è che l'hook copre solo il tool Bash e lascia intatti Read, Grep e Glob. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]

- **2026-05-10** — rtk taglia il 60-90% dei token su Claude Code: è un proxy Rust con binario unico, tra i sei repo GitHub che eliminano abbonamenti per quasi 3.000 dollari al mese. [Fonte: raw/puntate/ainews20260510.md]

- **2026-09-06** — Intercetta i comandi di terminale e comprime l'output prima che arrivi al modello, con il settanta percento di risparmio token; funziona automaticamente con Claude Code, Cursor, Copilot e Codex. [Fonte: raw/puntate/ainews20260906.md]

## Collegamenti

- [[claude-code]]
- [[index]]

