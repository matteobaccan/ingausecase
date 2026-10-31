---
title: "Claude Managed Agents"
category: strumento
tags: [agent, anthropic, api, budget, enterprise, produzione]
related_puntate: [20260701, 20260723, 20260808, 20261009, 20261010, 20261012]
created: 2026-08-12
updated: 2026-10-15
---

# Claude Managed Agents

## Introduzione

Sistema di Anthropic per gestire agenti Claude aziendali con livelli di effort configurabili, webhook, memory store e stream di eventi per sub-agent.

## Funzionalità principali

- Aggiornato con streaming degli eventi di sessione, override per-sessione, nuovi tipi di webhook, paginazione inversa e scoping delle credenziali.
- Anthropic ha aggiornato Claude Managed Agents con livelli di effort configurabili per agente, sessioni con eventi precaricati, fino a cinquecento skill per sessione, webhook per ambienti, memory store e stream di eventi per sub-agent.
- Claude Managed Agents ha ricevuto quattro aggiornamenti in una settimana: budget per sessione, pausa automatica al limite e ripresa modificabile, per spesa prevedibile e controllo completo.

## Azienda / Autore

- [[anthropic]]

## Timeline delle notizie

- **2026-04-11** — Claude Managed Agents entra in public beta il 9 aprile 2026: suite di API componibili per agenti cloud-hosted con infrastruttura gestita, sandbox isolati per sessione, tool nativi come code execution e web browsing e streaming via Server-Sent Events. I prezzi prevedono 0,08 dollari per ora di sessione attiva, 10 dollari ogni 1.000 ricerche web e token Sonnet 4.6 a 3/15 dollari per milione input/output; il credential vault cifra i secret e supporta OAuth nativo per ClickUp, Slack e Notion, e i primi ad adottarlo sono Notion, Asana e Sentry.

- **2026-07-01** — Aggiornato con streaming degli eventi di sessione, override per-sessione, nuovi tipi di webhook, paginazione inversa e scoping delle credenziali.
- **2026-07-23** — Anthropic ha aggiornato Claude Managed Agents con livelli di effort configurabili per agente, sessioni con eventi precaricati, fino a cinquecento skill per sessione, webhook per ambienti, memory store e stream di eventi per sub-agent.
- **2026-08-08** — Claude Managed Agents ha ricevuto quattro aggiornamenti in una settimana: budget per sessione, pausa automatica al limite e ripresa modificabile, per spesa prevedibile e controllo completo.
- **2026-10-09** — Una guida di [[anthropic]] mostra come costruire automazioni con Claude Managed Agents: agenti che leggono Slack o GitHub su schedule, con credenziali e memoria, e pubblicano aggiornamenti, configurati via Claude Code e con crediti API inclusi nei piani Max e Team.
- **2026-10-10** — Managed Agents Dynamic Workflows passano in beta pubblica: un agente lead scrive un piano di lavoro in più fasi, ogni fase può coinvolgere molti agenti e alla fine i risultati vengono ricomposti, per carichi ambiziosi. Una dimostrazione del 12 ottobre ha assegnato i ticker azionari ad agenti separati e ne ha rivisto i risultati prima del report finale: secondo i presentatori il metodo trova più dettagli ma costa molto più di un singolo agente, e il limite di spesa della sessione è impostato dallo sviluppatore mentre il modello in esecuzione non lo conosce.
- **2026-10-12** — Anthropic pubblica la documentazione ufficiale dei workflow dinamici in Managed Agents: con settanta bug piantati in un codebase da 116.000 righe un singolo agente ne trova tra 14 e 27, un workflow dinamico 66 a ogni esecuzione, e un'esecuzione può distribuire fino a mille agenti.
- **2026-10-15** — La tracciatura OpenTelemetry arriva anche su Claude Managed Agents, insieme alla Messages API e agli SDK di Claude. Con la beta pubblica del 14 ottobre le sessioni possono finire passo per passo in Datadog, Grafana, Langfuse o negli altri strumenti di osservabilità indicati da Anthropic, e il tracciamento lato API è l'unico che vede i turni degli agenti e gli strumenti eseguiti lato server. Le destinazioni di un'organizzazione con vincoli HIPAA, FERPA o K-12 esportano solo i metadati, e Managed Agents non è idoneo alla zero data retention.













## Collegamenti

- [[agenti-ai]]
- [[anthropic]]
- [[claude-code]]
- [[claude-science]]
- [[index]]

