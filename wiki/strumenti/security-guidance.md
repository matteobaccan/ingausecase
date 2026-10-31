---
title: "Security Guidance"
category: strumento
tags: [anthropic, claude-code, plugin, sicurezza]
created: 2026-10-03
updated: 2026-10-03
---

# Security Guidance

## Introduzione

Plugin gratuito pubblicato da [[anthropic]] il 26 maggio 2026 sul marketplace ufficiale di [[claude-code]]: intercetta in tempo reale le scritture di codice e blocca circa 25 pattern vulnerabili prima che arrivino al commit, con il matching interamente locale e nessuna chiamata all'API esterna.

## Funzionalità principali

- Si aggancia come pre-tool hook agli strumenti write, edit e multi-edit, esegue regex su circa 25 pattern noti e blocca la scrittura se trova qualcosa di sospetto, suggerendo subito la versione sicura.
- Copre otto famiglie: command injection nei workflow GitHub Actions, child_process.exec, eval e new Function, XSS via innerHTML e dangerouslySetInnerHTML, pickle deserialization, os.system, hardcoded secret e input validation.
- È un filtro regex e non un SAST a flusso di dati: cattura il low-hanging fruit e va affiancato a Snyk, GitHub Advanced Security o Semgrep.

## Azienda / Autore

- [[anthropic]]

## Timeline delle notizie

- **2026-05-26** — Anthropic pubblica Security Guidance, plugin gratuito del marketplace ufficiale che si aggancia come pre-tool hook e blocca circa 25 pattern vulnerabili in otto famiglie con matching locale; nelle prime ventiquattro ore supera i 157.000 download.

## Collegamenti

- [[anthropic]]
- [[claude-code]]
- [[claude-plugins-official]]
- [[sicurezza-ai]]
- [[index]]
