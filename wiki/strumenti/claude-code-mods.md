---
title: "Claude Code Mods"
category: strumento
tags: [anthropic, claude-code, plugin]
created: 2026-10-03
updated: 2026-10-03
---

# Claude Code Mods

## Introduzione

Nuovo tipo di plugin di [[claude-code]] introdotto il 1 ottobre 2026 con la versione 2.1.287: è fatto di funzioni JavaScript o TypeScript che Claude Code chiama a ogni evento interno e che possono osservare l'evento, riscriverlo prima che prosegua o sostituirsi del tutto al comportamento previsto, disegnando anche interfaccia vera come pannelli, barre e bottoni.

## Funzionalità principali

- A differenza di un hook di settings, di una skill o di un server MCP, una mod vive dentro il processo di Claude Code, è diretta e ispezionabile e può aggiungere comandi `/nome` che girano senza passare da un turno del modello.
- La parte di interfaccia funziona solo nel terminale e nella tab "Code" dell'app desktop, mentre gli hook restano attivi anche in VS Code, nella modalità claude -p, nell'Agent SDK e nelle sessioni cloud.
- Gira con gli stessi permessi dell'utente e senza sandbox: può leggere file e chiavi API e approvare da sola azioni che normalmente richiederebbero conferma, per questo Anthropic raccomanda di installare solo mod fidate e di validarle con `claude plugin validate`.

## Azienda / Autore

- [[anthropic]]

## Timeline delle notizie

- **2026-10-01** — Claude Code apre alle mod dalla versione 2.1.287: plugin che girano dentro il processo dell'agente e possono modificarne il comportamento, ridisegnare l'interfaccia o sostituire funzioni esistenti. Il repository ufficiale contiene già quattro mod con codice pubblico (diff, agents-md, sec-default, telemetry), e nelle prime ore ne compaiono diverse della community.

## Collegamenti

- [[anthropic]]
- [[claude-code]]
- [[claude-plugins-official]]
- [[index]]
