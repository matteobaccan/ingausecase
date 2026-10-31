---
title: "Agent Client Protocol"
category: strumento
tags: [agenti, open-source, protocollo, standard, terminale]
related_puntate: []
created: 2026-10-08
updated: 2026-10-08
---

# Agent Client Protocol

## Introduzione

Standard aperto che definisce come editor di codice e terminali comunicano con
gli agenti AI da riga di comando, pensato per evitare un'integrazione su misura
per ogni agente: la stessa funzione che il Language Server Protocol ha avuto per
i linguaggi di programmazione.

## Capacità e performance

- Usa JSON-RPC 2.0 scambiato su stdin e stdout, il canale che il terminale già
  adopera: richieste, notifiche e risposte separate da un a capo e senza
  interruzioni di riga al loro interno.
- All'inizio del 2026 gli agenti che lo supportano erano oltre venticinque, fra
  cui [[claude-code]], OpenAI Codex e Google Gemini.

## Timeline delle notizie

- **2026-06-02** — [[microsoft]] adotta l'Agent Client Protocol in [[intelligent-terminal]]: il terminale rileva in automatico le CLI compatibili installate sulla macchina e parla con ciascuna attraverso lo stesso protocollo, ricadendo su GitHub Copilot CLI se non ne trova nessuna.

## Collegamenti

- [[intelligent-terminal]]
- [[claude-code]]
- [[mcp]]
- [[index]]
