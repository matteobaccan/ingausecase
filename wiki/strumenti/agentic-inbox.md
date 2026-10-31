---
title: "Agentic Inbox"
category: strumento
tags: [agent, cloudflare, email, open-source, self-host]
related_puntate: [20260602, 20260619, 20260705, 20260919]
created: 2026-08-12
updated: 2026-09-19
sources: [raw/puntate/ainews20260602.md, raw/puntate/ainews20260619.md, raw/puntate/ainews20260705.md, raw/puntate/ainews20260919.md]
---

# Agentic Inbox

## Introduzione

Client email self-hosted su Cloudflare Workers con domini custom, storage isolato e assistente AI che genera bozze di risposta da confermare.

## Funzionalità principali

- Agentic Inbox è stato rilasciato open source da Cloudflare: un agente AI legge l'inbox e redige le risposte, gira interamente su Cloudflare Workers con ogni mailbox nel proprio Durable Object, la mail non lascia l'account Cloudflare e si distribuisce con un clic.
- Agentic Inbox di Cloudflare è un client email con agente AI integrato, open source: nessuna API di terze parti, ogni mailbox su Durable Object isolato con SQLite e allegati su R2; l'agente legge la posta, cerca conversazioni e genera bozze senza mai inviare nulla senza conferma esplicita.
- Client email self-hosted su Cloudflare Workers: domini custom, storage isolato per inbox, assistente AI integrato che legge email e genera bozze di risposta (con conferma prima dell'invio). Ricerca storico e conversazioni organizzate.

## Azienda / Autore

- [[cloudflare]]

## Timeline delle notizie

- **2026-06-02** — Agentic Inbox è stato rilasciato open source da Cloudflare: un agente AI legge l'inbox e redige le risposte, gira interamente su Cloudflare Workers con ogni mailbox nel proprio Durable Object, la mail non lascia l'account Cloudflare e si distribuisce con un clic. [Fonte: raw/puntate/ainews20260602.md]
- **2026-06-19** — Agentic Inbox di Cloudflare è un client email con agente AI integrato, open source: nessuna API di terze parti, ogni mailbox su Durable Object isolato con SQLite e allegati su R2; l'agente legge la posta, cerca conversazioni e genera bozze senza mai inviare nulla senza conferma esplicita. La descrizione della puntata del 19 settembre aggiunge che l'agente email è nativo sul Cloudflare Agents SDK con nove tool di gestione della posta, espone endpoint MCP per l'integrazione con Cursor e Claude Code e usa Cloudflare Access JWT per la sicurezza, mentre l'invio resta sempre manuale. [Fonte: raw/puntate/ainews20260619.md] [Fonte: raw/puntate/ainews20260919.md]
- **2026-07-05** — Client email self-hosted su Cloudflare Workers: domini custom, storage isolato per inbox, assistente AI integrato che legge email e genera bozze di risposta (con conferma prima dell'invio). Ricerca storico e conversazioni organizzate. [Fonte: raw/puntate/ainews20260705.md]

## Collegamenti

- [[claude-code]]
- [[cloudflare]]
- [[cursor]]
- [[index]]

