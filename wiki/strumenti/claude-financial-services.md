---
title: "Claude for Financial Services"
category: strumento
tags: [anthropic, finanza, agent, enterprise]
related_puntate: []
created: 2026-09-12
updated: 2026-09-12
sources: [raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
---

# Claude for Financial Services

## Introduzione

Pacchetto di dieci template di agenti AI per il settore finanziario presentato da [[anthropic]] a New York il 5 maggio 2026, con l'obiettivo di automatizzare il lavoro ripetitivo di banche, fondi e asset manager: lettura dei risultati trimestrali, aggiornamento dei modelli di valutazione, note di ricerca, riconciliazione contabile e preparazione di pitchbook M&A. Nella terminologia di Anthropic un agente è la composizione di tre elementi: skill (file Markdown con istruzioni operative e conoscenza di dominio), connector verso fonti dati esterne via [[mcp]] e subagent Claude richiamati per compiti specifici. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]

## Funzionalità principali

- Earnings Reviewer: legge trascrizioni delle earnings call e filing, estrae le revisioni di guidance, aggiorna il modello a tre prospetti e produce una nota di ricerca pronta per la revisione del senior. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Market Researcher: genera la "morning note" su un paniere di ticker collegandosi a feed di notizie e dati fondamentali. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Model Builder: costruisce modelli DCF, LBO, a tre prospetti e comparables in Excel con celle collegate dinamicamente, a partire dai filing della società. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Gli altri sette template sono Pitch Agent, Meeting Prep Agent, Valuation Reviewer, GL Reconciler, Month-End Closer, Statement Auditor e KYC Screener. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Tutti i template producono bozze destinate alla revisione umana: non eseguono transazioni, non approvano onboarding e non scrivono direttamente nei libri contabili. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]

## Installazione e uso

- Tre forme di deployment: plugin nel workspace collaborativo [[claude-cowork]], plugin in [[claude-code]] dal marketplace ufficiale (comandi come /dcf, /comps, /earnings, /lbo) e agente headless su [[managed-agents-api]], con endpoint API /v1/agents, job notturni e webhook sui nuovi filing. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Il repository pubblico anthropics/financial-services contiene i cookbook YAML e lo script scripts/deploy-managed-agent.sh; le skill funzionano anche con prompt in italiano. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Integrazione Microsoft 365: add-in per Excel, PowerPoint e Word in disponibilità generale e per Outlook in beta, con un singolo agente che condivide il contesto tra le applicazioni. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]

## Partner dati

- Undici fornitori integrati via MCP: Moody (rating e rischio per oltre 600 milioni di società, come app nativa dentro Claude), FactSet, Morningstar, S&P Global con i tear sheet di Capital IQ, LSEG, PitchBook, Daloopa, MT Newswires, Aiera per le trascrizioni delle earnings call, Chronograph ed Egnyte. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]

## Casi d'uso

- JP Morgan: il CEO Jamie Dimon ha costruito dal vivo una dashboard su asset swap e bid-ask spread del Tesoro americano in venti minuti. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Bridgewater ha usato Claude per le prime versioni del suo Investment Analyst Assistant; AIG dichiara tempi di revisione interna compressi di cinque volte e accuratezza salita dal 75% al 90% nei task di sottoscrizione; Walleye Capital afferma che il 100% dei collaboratori usa Claude Code. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]

## Performance

- Sul benchmark Finance Agent di Vals AI Claude Opus 4.7 raggiunge il 64,37%, il punteggio più alto del settore; sull'esperienza di FundamentalLabs alla Financial Modeling World Cup il modello ha superato cinque dei sette livelli con l'83% di accuratezza nei task complessi. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]
- Il limite dichiarato è il restante 36% di risposte con errori più o meno gravi: ogni output va trattato come la bozza di un junior, non come un risultato finale. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]

## Azienda di riferimento

- [[anthropic]]

## Timeline delle notizie

- **2026-05-09** — Anthropic presenta dieci agenti finanziari pronti all'uso, l'integrazione con Microsoft 365, gli accordi con Moody, FactSet, Morningstar e S&P Global e la partnership con JP Morgan; la crescita annualizzata della società nel trimestre precedente è stata di circa ottanta volte secondo Fortune. [Fonte: raw/pillitteri/pillitteri20260509-claude-finanza-agenti-financial-services-2026.md]

## Collegamenti

- [[anthropic]]
- [[claude]]
- [[claude-cowork]]
- [[claude-code]]
- [[managed-agents-api]]
- [[chatgpt-financial-services]]
- [[mcp]]
- [[index]]
