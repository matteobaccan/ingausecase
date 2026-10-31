---
title: "DeepSeek Harness"
category: strumento
tags: [agent, beta, coding, deepseek]
related_puntate: [20260803, 20260915, 20261001, 20261002, 20261011]
created: 2026-08-12
updated: 2026-10-11
---

# DeepSeek Harness

## Introduzione

Agente di coding di DeepSeek, pubblicato su GitHub il 13 agosto 2026 in versione v0.1 Developer Preview con licenza MIT e comando da terminale `dsh`: è l'agent harness, cioè il runtime che trasforma un modello in un agente capace di leggere file, eseguire comandi e portare avanti compiti in più passi. Competitor diretto e dichiarato di Claude Code e Codex.

## Funzionalità principali

- DeepSeek ha aperto il reclutamento beta per DeepSeek Harness, nuovo agente di coding con focus su software engineering autonomo, pianificazione, uso di tool ed esecuzione codice, memoria persistente e consapevolezza del repository; competitor diretto di Claude Code e Codex.
- È costruito sopra Cordis, un meta-framework in cui modelli, strumenti, skill, sessioni, sandbox, filesystem, cicli di esecuzione e perfino l'interfaccia web sono plugin sostituibili: il motto del repository è "Everything is a Plugin" e ogni plugin contribuisce servizi, eventi tipizzati ed effetti reversibili a un contesto condiviso, senza un core privilegiato da modificare.
- Si avvia con `npx @deepseek-ai/dsh web`, apre una Web UI su localhost:3080 e legge i modelli dalla variabile `DEEPSEEK_API_KEY` (con endpoint personalizzabile via `DEEPSEEK_BASE_URL`); la configurazione passa da file `cordis.yml` a strati sovrapposti, così una modifica è una patch e non un fork.

## Azienda / Autore

- [[deepseek]]

## Timeline delle notizie

- **2026-08-03** — DeepSeek ha aperto il reclutamento beta per DeepSeek Harness, nuovo agente di coding con focus su software engineering autonomo, pianificazione, uso di tool ed esecuzione codice, memoria persistente e consapevolezza del repository; competitor diretto di Claude Code e Codex.
- **2026-08-13** — DeepSeek pubblica `deepseek-harness` su GitHub con licenza MIT e in poche ore il repository supera le 27.000 stelle: versione v0.1 in Developer Preview, codice in TypeScript, posizionamento frontale come alternativa cinese e gratuita a [[claude-code]]. Il progetto nasce per far girare i modelli V4-Pro e V4-Flash come agenti autonomi e attacca su tre fronti: prezzo (runtime gratis, modelli a una frazione dei costi occidentali), licenza aperta contro l'approccio proprietario di Anthropic e quello chiuso di Codex, e modularità radicale, con i plugin pubblicabili sotto il topic GitHub `dsh-plugin`. Il README avverte in maiuscolo che ci saranno modifiche che rompono la compatibilità e che il formato delle sessioni non è stabile, quindi va usato per sperimentare e non in produzione. Il progetto è guidato da Cui Tianyi, entrato in DeepSeek a marzo 2026 dopo un percorso in Jane Street, con una squadra dedicata formata a maggio 2026.

- **2026-08-17** — DeepSeek Harness segna il record di velocità di crescita su GitHub: oltre 20.000 stelle in poco più di un'ora dal rilascio del 13 agosto, circa 50.000 in dodici ore e 141.532 stelle con 14.350 fork al 17 agosto, contro i 5,7 giorni di DeepSeek R1 e i circa 1,2 di Grok-1; un test indipendente misura però un consumo di token dieci volte superiore a un concorrente minimalista, e su cinque strumenti di terze parti nessuno ha funzionato al primo colpo.

- **2026-09-01** — Raggiunge 200mila stelle, comparato a Claude Code e Codex.
- **2026-09-15** — DeepSeek Harness supera le centosessantamila stelle in pochi giorni: il framework per costruire agenti di programmazione è modulare su tutto (modello, strumenti, sandbox, interfaccia e lo stesso loop dell'agente), i componenti si cambiano dal file di configurazione senza toccare il codice base ed è compatibile con DeepSeek, Claude, GPT e Gemini; una singola riga di comando avvia l'interfaccia web locale.
- **2026-09-18** — Supera le duecentomila stelle su GitHub inglobando [[claude-code]] e [[codex]]: la lettura della fonte è che la comunità non usi i modelli cinesi solo per risparmiare, ma ci costruisca sopra l'infrastruttura, e che per il miglior costo per bug risolto si parta da qui.
- **2026-10-01** — DeepSeek Harness per desktop diventa disponibile su macOS e Windows: sembra essere l'evoluzione dell'interfaccia desktop per i modelli DeepSeek.
- **2026-10-02** — DeepSeek Harness è disponibile su Windows e macOS come alternativa open source alle app di Claude e ChatGPT per lavorare sul computer: tutto è un plugin, completamente configurabile, e usa qualsiasi modello IA, locale o via API.
- **2026-10-11** — Sul modello di DeepSeek Harness nasce DeepSeek Bot, plugin open source non ufficiale che crea bot persistenti con la propria API key e collega qualsiasi modello o agente locale, ereditando l'architettura "tutto è plugin" di DSH.










## Collegamenti

- [[adr]]
- [[claude-code]]
- [[codex]]
- [[deepseek]]
- [[deepseek-v4-flash]]
- [[deepseek-v4-pro]]
- [[opencode-go]]
- [[sviluppo-software-ai]]
- [[index]]

