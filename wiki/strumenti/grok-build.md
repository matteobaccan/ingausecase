---
title: "Grok Build"
category: strumento
tags: [agent, cli, coding, gaming, harness, open-source, workflow, xai]
related_puntate: [20260508, 20260509, 20260515, 20260717, 20260719, 20260724]
created: 2026-08-12
updated: 2026-09-25
---

# Grok Build

## Introduzione

Tool di sviluppo di xAI basato su Grok, in arrivo su macOS, Windows e Linux, con supporto a planning mode, plugins, skills e MCP, integrazione con Git e browser.

## Funzionalità principali

- xAI sta preparando Grok Build per macOS, Windows e Linux: supporterà planning mode, Plugins, Skills e MCPs, potrà lavorare con l'albero Git, lanciare dev server e lavorare con un browser integrato.
- Grok Build è in arrivo come agente di coding completo, non autocomplete: descrive il progetto e Grok pianifica, codifica e fa debug con fino a otto agenti paralleli, costruendo app, siti e repository interi da plain English; Arena Mode sceglie l'output migliore e la CLI locale mantiene il codice privato.
- xAI ha lanciato Grok Build: CLI agente per coding, app e automazione workflow, in beta precoce riservata ai subscriber SuperGrok Heavy, con il feedback degli utenti che guiderà i miglioramenti.

## Azienda / Autore

- [[xai]]

## Modelli supportati / correlati

- [[grok]]

## Timeline delle notizie

- **2026-05-08** — xAI sta preparando Grok Build per macOS, Windows e Linux: supporterà planning mode, Plugins, Skills e MCPs, potrà lavorare con l'albero Git, lanciare dev server e lavorare con un browser integrato.
- **2026-05-09** — Grok Build è in arrivo come agente di coding completo, non autocomplete: descrive il progetto e Grok pianifica, codifica e fa debug con fino a otto agenti paralleli, costruendo app, siti e repository interi da plain English; Arena Mode sceglie l'output migliore e la CLI locale mantiene il codice privato.
- **2026-05-15** — xAI ha lanciato Grok Build: CLI agente per coding, app e automazione workflow, in beta precoce riservata ai subscriber SuperGrok Heavy, con il feedback degli utenti che guiderà i miglioramenti.
- **2026-07-15** — Un'analisi a livello di rete pubblicata il 12 luglio 2026 dal ricercatore indipendente cereblab documenta che la CLI 0.2.93 ha spedito 5,10 GiB di dati verso un bucket Google Cloud Storage di [[xai]] su un repository di test da 12 GB, mentre al modello ne servivano 192 KB, circa ventisettemilaottocento volte meno, e riguardava file che l'agente non aveva mai aperto: oltre al turno del modello su `POST /v1/responses` esiste un secondo canale, `POST /v1/storage`, che impacchetta il repository tracciato con tutta la sua cronologia e lo carica sul bucket `grok-code-session-traces`. Il 15 luglio xAI ha pubblicato il codice di Grok Build sotto licenza Apache 2.0 e ha azzerato i limiti d'uso, e nel sorgente la funzione di upload risulta disattivata.
- **2026-07-17** — Grok build è open source: Elon Musk ha rilasciato il codice, 2,2 mila stelle, definito il miglior harness open source disponibile.
- **2026-07-19** — Grok Build ha rilasciato cinque skill per asset di gioco con Grok Imagine: cicli di animazione, personaggi coerenti, tileset seamless e icone UI, con frame video-first per movimenti fluidi e output pronti per engine.
- **2026-07-24** — Grok Build ha introdotto Workflows: Grok pianificava il lavoro, eseguiva centinaia di agenti in parallelo per task come triaging di centinaia di issue o review di migliaia di righe di codice, restituendo un report finale.

## Collegamenti

- [[agenti-ai]]
- [[brainless]]
- [[codex]]
- [[grok]]
- [[spec-kit]]
- [[xai]]
- [[index]]

