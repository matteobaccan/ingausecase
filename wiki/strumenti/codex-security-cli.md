---
title: "Codex Security CLI"
category: strumento
tags: [cli, openai, sicurezza]
related_puntate: [20260730, 20260906, 20260930]
created: 2026-08-12
updated: 2026-10-25
sources: [raw/puntate/ainews20260730.md, raw/puntate/ainews20260906.md, raw/puntate/ainews20260930.md, raw/pillitteri/pillitteri20261022-nodejs-vulnerabilita-brotli-cve-2026-111497.md, raw/pillitteri/pillitteri20261023-node2shell-rce-nodejs-24-22-0.md, raw/pillitteri/pillitteri20261024-migliori-strumenti-ai-audit-sicurezza-codice-confronto.md]
---

# Codex Security CLI

## Introduzione

CLI di OpenAI per la sicurezza del codice: trova vulnerabilità nei repository e genera report. In rilascio preliminare e open source.

## Funzionalità principali

- Codex Security CLI era un lancio segreto già trapelato: trovava vulnerabilità nei repository e generava report. In rilascio preliminare e open source.

## Azienda / Autore

- [[openai]]

## Timeline delle notizie

- **2026-07-30** — Codex Security CLI era un lancio segreto già trapelato: trovava vulnerabilità nei repository e generava report. In rilascio preliminare e open source. [Fonte: raw/puntate/ainews20260730.md]

- **2026-09-06** — OpenAI ha rilasciato codex-security su GitHub: trova vulnerabilità nel codice, le verifica e propone correzioni, include scansione Docker in blocco, tutto open source. [Fonte: raw/puntate/ainews20260906.md]
- **2026-09-30** — Codex Security Cloud estende la linea: scansiona repository GitHub interi, rivede i commit nuovi, indaga sui problemi trovati e prepara i fix anche a computer spento, con i modelli cyber-capable forniti tramite Daybreak Blue e il plugin in Codex desktop e web. [Fonte: raw/puntate/ainews20260930.md]
- **2026-10-22** — OpenAI Codex Security figura nei crediti dell'advisory di Node.js per CVE-2026-111497, la scrittura fuori dai limiti nel decoder Brotli corretta con le versioni 26.12.1, 24.22.1 e 22.23.4; la correzione porta la firma di Matteo Collina e Antoine du Hamel. [Fonte: raw/pillitteri/pillitteri20261022-nodejs-vulnerabilita-brotli-cve-2026-111497.md]
- **2026-10-23** — La falla Brotli trovata da Codex Security e corretta il 21 ottobre diventa una RCE dimostrata: Imperva ha eseguito codice arbitrario su Node.js 24.22.0 con Node2Shell, inviando dati compressi costruiti apposta all'immagine Docker ufficiale per Linux arm64. [Fonte: raw/pillitteri/pillitteri20261023-node2shell-rce-nodejs-24-22-0.md]
- **2026-10-24** — La CLI, Apache-2.0 con 11.191 stelle, si installa con npm install --global @openai/codex-security e si usa con cs scan, con opzioni per le cartelle scelte, il diff rispetto a un branch e una modalità profonda a più lavoratori in parallelo; i risultati si esportano in SARIF, JSON o CSV e si importano gli alert di GitHub code scanning. Il servizio cloud è in anteprima di ricerca per gli utenti Enterprise, Business, Edu e Pro con fatturazione a token, non modifica mai il codice da solo e non usa fuzzing né firme, ma ragionamento del modello e uso di strumenti. [Fonte: raw/pillitteri/pillitteri20261024-migliori-strumenti-ai-audit-sicurezza-codice-confronto.md]













## Collegamenti

- [[codex]]
- [[openai]]
- [[sicurezza-ai]]
- [[index]]

