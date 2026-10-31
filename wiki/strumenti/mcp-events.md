---
title: "MCP Events"
category: strumento
tags: [mcp, openai, webhook, chatgpt]
related_puntate: [20260930, 20261001, 20261004]
created: 2026-09-30
updated: 2026-10-04
sources: [raw/tldr/tldr20260930.md, raw/puntate/ainews20261001.md, raw/puntate/ainews20261004.md]
---

# MCP Events

## Introduzione

Funzionalità con cui ChatGPT può sottoscrivere gli aggiornamenti di un server [[mcp]], basata sulla bozza della specifica MCP Events.

## Funzionalità principali

- L'utente sceglie cosa monitorare e cosa deve fare ChatGPT quando arriva un aggiornamento. [Fonte: raw/tldr/tldr20260930.md]
- Supporto alla consegna via webhook e alla verifica dei callback dalla bozza della specifica MCP Events. [Fonte: raw/tldr/tldr20260930.md]
- Non supportati: polling, streaming e le notifiche di controllo `gap` e `terminated` della bozza. [Fonte: raw/tldr/tldr20260930.md]

## Azienda / Autore

- [[openai]]

## Timeline delle notizie

- **2026-09-30** — MCP Events porta ChatGPT a sottoscrivere gli aggiornamenti dei server MCP con consegna webhook e verifica callback dalla bozza della specifica; restano fuori polling, streaming e le notifiche gap e terminated. [Fonte: raw/tldr/tldr20260930.md]
- **2026-10-01** — OpenAI integra MCP Events in ChatGPT: i server MCP possono inviare aggiornamenti real-time a ChatGPT e attivare automazioni per gli utenti su messaggi, commenti e cambi di stato. [Fonte: raw/puntate/ainews20261001.md]
- **2026-10-04** — MCP Events permette agli agenti di attivarsi automaticamente in risposta a trigger esterni: non solo cron o messaggi diretti, ma eventi esterni che diventano input per gli agenti. [Fonte: raw/puntate/ainews20261004.md]







## Collegamenti

- [[mcp]]
- [[openai]]
- [[index]]
