---
title: "Bifrost"
category: strumento
tags: [gateway, mcp, open-source, sicurezza]
related_puntate: []
created: 2026-09-25
updated: 2026-09-25
---

# Bifrost

## Introduzione

Gateway AI open source al centro di CVE-2026-90898, la vulnerabilità da punteggio CVSS 9.8 documentata da JFrog il 23 settembre 2026: con l'autenticazione di management disabilitata una richiesta non autenticata poteva registrare un client MCP stdio e avviare un comando sul server.

## Funzionalità principali

- La falla è stata corretta: il caso resta come esempio di superficie di attacco specifica dell'ecosistema MCP, soprattutto quando i componenti di gestione sono esposti senza autenticazione.

## Timeline delle notizie

- **2026-09-23** — JFrog documenta CVE-2026-90898 su Bifrost, esecuzione remota di codice non autenticata via registrazione di un client MCP stdio: punteggio CVSS 9.8, falla corretta.

## Collegamenti

- [[mcp]]
- [[sicurezza-ai]]
- [[index]]
