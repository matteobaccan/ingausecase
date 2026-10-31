---
title: "MCP"
category: strumento
tags: [agent, integrazione, protocollo]
related_puntate: [20260601, 20260729, 20260730, 20260909, 20260910, 20260915, 20260926, 20261004]
created: 2026-08-12
updated: 2026-10-28
sources: [raw/puntate/ainews20260601.md, raw/puntate/ainews20260729.md, raw/puntate/ainews20260730.md, raw/puntate/ainews20260909.md, raw/puntate/ainews20260910.md, raw/puntate/ainews20260915.md, raw/pillitteri/pillitteri20260727-server-mcp-collegare-claude-chatgpt-gemini.md, raw/pillitteri/pillitteri20260806-anaconda-enkrypt-ai-falle-server-mcp.md, raw/puntate/ainews20260926.md, raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md, raw/puntate/ainews20261004.md, raw/controrumore/controrumore20261008-diario-ai-lai-entra-nella-zona-grigia.md, raw/pillitteri/pillitteri20261011-migliori-mcp-claude-code-5-server-installazione.md, raw/pillitteri/pillitteri20261023-mcp-tasks-claude-code-job-lunghi-background.md, raw/pillitteri/pillitteri20261027-webmcp-mcp-differenze-quando-usarli.md, raw/controrumore/controrumore20261028-diario-ai-sicurezza-mercati-e-agenti.md]
---

# MCP

## Introduzione

Model Context Protocol di Anthropic: protocollo standard per connettere strumenti e dati agli agenti AI. Nella versione 2026-07-28 è diventato stateless, più facile da deployare e scalare.

## Funzionalità principali

- Un tutorial ha elencato i cinque pattern architetturali MCP per agenti in produzione: Tool Servers per azioni via API, Resource Servers per contesto strutturato, Prompt Servers per prompt versionati, Gateway Servers per routing centralizzato e Proxy Bridge Servers per collegare sistemi legacy.
- La versione 2026-07-28 del protocollo MCP è live: diventa stateless, più facile da deployare e scalare. Il più grande aggiornamento dal lancio.
- MCP è cambiato: prima sessioni stateful, ora stateless, con ogni richiesta che contiene tutte le informazioni necessarie. Permette distribuzione del traffico e deploy serverless o edge.

## Azienda / Autore

- [[anthropic]]

## Timeline delle notizie

- **2026-06-01** — Un tutorial ha elencato i cinque pattern architetturali MCP per agenti in produzione: Tool Servers per azioni via API, Resource Servers per contesto strutturato, Prompt Servers per prompt versionati, Gateway Servers per routing centralizzato e Proxy Bridge Servers per collegare sistemi legacy. [Fonte: raw/puntate/ainews20260601.md]
- **2026-07-29** — La versione 2026-07-28 del protocollo MCP è live: diventa stateless, più facile da deployare e scalare. Il più grande aggiornamento dal lancio. La guida del 27 luglio, scritta sulla release candidate, aggiunge i punti che la specifica finale ha confermato: Multi Round-Trip Requests, header Mcp-Method e Mcp-Name per gateway e WAF, liste di tool, prompt e risorse cacheabili con `ttlMs` e `cacheScope`, Client ID Metadata Documents al posto della Dynamic Client Registration con validazione RFC 9207, Tasks come estensione `io.modelcontextprotocol/tasks`, il trasporto HTTP+SSE fra le deprecazioni insieme a Roots, Sampling e Logging, schema dei tool passato a JSON Schema 2020-12 ed errore per risorsa mancante spostato da -32002 a -32602. [Fonte: raw/pillitteri/pillitteri20260727-server-mcp-collegare-claude-chatgpt-gemini.md]
- **2026-07-27** — I numeri del protocollo al momento della guida: 9.652 server pubblicati nel registro ufficiale al 24 maggio 2026, oltre 97 milioni di download mensili degli SDK a marzo, 88.936 stelle del repository dei server di riferimento e, lato [[anthropic]], più di 950 connettori nella directory di Claude con le MCP Apps che disegnano interfacce dentro la conversazione e i tunnel per la rete privata ancora in anteprima. La guida ricorda anche il limite pratico che decide l'architettura: ChatGPT non avvia processi locali e accetta solo endpoint HTTPS remoti, quindi un server STDIO privato va esposto solo per davvero e con autenticazione, perché una scansione su 25.000 server MCP ha trovato difetti nel 73% dei casi. [Fonte: raw/pillitteri/pillitteri20260727-server-mcp-collegare-claude-chatgpt-gemini.md]
- **2026-07-30** — MCP è cambiato: prima sessioni stateful, ora stateless, con ogni richiesta che contiene tutte le informazioni necessarie. Permette distribuzione del traffico e deploy serverless o edge. [Fonte: raw/puntate/ainews20260730.md]
- **2026-09-09** — Mobile MCP connette iOS e Android a Claude Code, Codex, Gemini e GitHub Copilot tramite Model Context Protocol, con gestione dispositivi, installazione app, tap, input e log (seimila trecentocinquantatre stelle). [Fonte: raw/puntate/ainews20260909.md]
- **2026-09-09** — DaVinci Resolve supporta ora l'integrazione diretta con Claude o ChatGPT via MCP per editing e color grading automatico. [Fonte: raw/puntate/ainews20260909.md]
- **2026-09-10** — UnityMCP versione quattro punto uno taglia i consumi di contesto e accelera le risposte per l'integrazione con Unity: consumo token dal trentasei al novantadue percento, latenza da centotrenta millisecondi a dieci virgola uno, turno fisso da trentamilanovecentosettantatré a duemilacentocinquantaquattro token. [Fonte: raw/puntate/ainews20260910.md]

- **2026-09-15** — MCP definisce un'estensione per scoprire e caricare le Agent Skills dai server MCP: l'agente scopre le Skill disponibili, ne ottiene i metadati e carica il file `SKILL.md` solo quando serve, invece di riempire in anticipo la finestra di contesto. [Fonte: raw/puntate/ainews20260915.md]

- **2026-08-06** — Due mesi di scansioni di Enkrypt AI su oltre 268.000 tool distribuiti su 25.000 server MCP hanno trovato più di 143.000 vulnerabilità, che toccano il 73 per cento dei server esaminati, con una media dichiarata di oltre cinque difetti per server; il confronto con la rilevazione di ottobre 2025 (1.000 server, 33 per cento con vulnerabilità critiche) non regge perché le due percentuali non applicano lo stesso filtro di gravità. [[anaconda]] ha acquisito Enkrypt AI il 4 agosto 2026, dopo Kilo Code, con l'obiettivo dichiarato di costruire uno stack completo dal governo dei pacchetti alla sicurezza degli agenti. [Fonte: raw/pillitteri/pillitteri20260806-anaconda-enkrypt-ai-falle-server-mcp.md]

- **2026-09-26** — L'utilizzo di MCP è cresciuto del centodiecimila per cento quest'anno. [Fonte: raw/puntate/ainews20260926.md]
- **2026-10-01** — Un server MCP non ufficiale collega [[claude]] a WhatsApp: WhatsApp MCP Server, progetto di Luke Harries con licenza MIT e oltre 6.346 stelle, usa un bridge in Go basato su whatsmeow per autenticarsi via QR code come WhatsApp Web e salva i messaggi in un database SQLite locale, passando al modello solo la porzione di dati chiamata da uno degli strumenti. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]
- **2026-10-04** — Uber pubblica la sua architettura MCP: un gateway centrale tra agenti e servizi interni che traduce le chiamate MCP in HTTP, gRPC o TChannel. Oggi conta oltre ottocento server MCP e più di cinquemila strumenti, e per gestire la scala ha creato Omni MCP, che scopre il server necessario solo al momento dell'esecuzione. [Fonte: raw/puntate/ainews20261004.md]
- **2026-10-08** — Una ricerca descritta da Ars Technica mostra come un prompt malevolo possa propagarsi tra agenti e server Model Context Protocol di organizzazioni diverse: i proof-of-concept hanno coinvolto implementazioni collegate a Google, JPMorgan Chase, Weaviate e Rapid7, sfruttando fiducia implicita, prompt injection indiretta e pivot tra protocolli; diverse falle sono state corrette, ma la ripetizione in ambienti distinti indica un problema architetturale, con ogni nodo chiamato a verificare identità, autorizzazioni, origine dei dati e portata delle azioni. [Fonte: raw/controrumore/controrumore20261008-diario-ai-lai-entra-nella-zona-grigia.md]
- **2026-10-11** — Una guida mette in fila i cinque server MCP più citati per Claude Code — Perplexity, Playwright, Firecrawl, Glif e Chrome DevTools — con il comando di installazione verificato sulla documentazione ufficiale, il costo reale e il rischio di ciascuno. [Fonte: raw/pillitteri/pillitteri20261011-migliori-mcp-claude-code-5-server-installazione.md]
- **2026-10-23** — I MCP Tasks diventano un'estensione ufficiale del protocollo: una chiamata a uno strumento può tornare con un identificativo del lavoro in corso invece del risultato, e il client interroga il server con tasks/get rispettando pollIntervalMs, con gli stati working, input_required, completed, failed e cancelled. La versione di MCP che li porta è uscita il 28 luglio 2026 e il primo client a implementarli è [[claude-code]]. [Fonte: raw/pillitteri/pillitteri20261023-mcp-tasks-claude-code-job-lunghi-background.md]
- **2026-10-26** — Il team Chrome for Developers precisa che [[webmcp]] non sostituisce MCP: il protocollo di Anthropic resta il livello di servizio, persistente e raggiungibile da desktop, mobile e cloud, mentre WebMCP è lo strato contestuale che espone gli strumenti di una pagina all'agente finché la scheda è aperta. La bozza di specifica descrive una pagina WebMCP come un server MCP con gli strumenti scritti lato client, e dichiara che riprenderà da MCP le valutazioni di rischio e le mitigazioni. [Fonte: raw/pillitteri/pillitteri20261027-webmcp-mcp-differenze-quando-usarli.md]
- **2026-10-28** — [[apple]] aggiunge il supporto a MCP in Keynote, Pages e Numbers con l'aggiornamento Creator Studio previsto a novembre, permettendo a strumenti esterni di leggere e modificare contenuti ed eseguire azioni. [Fonte: raw/controrumore/controrumore20261028-diario-ai-sicurezza-mercati-e-agenti.md]






















## Collegamenti

- [[agenti-ai]]
- [[anaconda]]
- [[annota-ai]]
- [[anthropic]]
- [[claude-code]]
- [[davinci-resolve]]
- [[unity-mcp]]
- [[everything-claude-code]]
- [[gemini-cli]]
- [[mobile-mcp]]
- [[mcp-adapter]]
- [[webmcp]]
- [[index]]

