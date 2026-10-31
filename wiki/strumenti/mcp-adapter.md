---
title: "MCP Adapter"
category: strumento
tags: [wordpress, mcp, agenti, plugin, open-source]
related_puntate: []
created: 2026-10-06
updated: 2026-10-06
---

# MCP Adapter

## Introduzione

Plugin ufficiale di [[wordpress]] che fa da ponte tra la Abilities API — l'elenco standard delle azioni che un sito WordPress sa compiere, nel core dalla versione 6.9 — e il [[mcp]], lo standard aperto con cui client come Claude Desktop o Cursor scoprono e usano strumenti esterni. La versione 0.7.0, uscita il 2 ottobre 2026, è la prima pubblicata nella directory dei plugin di wordpress.org, dopo oltre un anno passato soltanto su GitHub e Composer.

## Funzionalità principali

- Traduce ogni ability — nome in forma di namespace, schema tipizzato per input e output, funzione di permessi e funzione di esecuzione — in uno strumento, una risorsa o un prompt del protocollo MCP, rendendola raggiungibile dai client.
- Il server predefinito espone tre strumenti generali: mcp-adapter-discover-abilities elenca le abilities, mcp-adapter-get-ability-info ne legge la scheda e mcp-adapter-execute-ability le esegue, sull'indirizzo /wp-json/mcp/mcp-adapter-default-server.
- Due canali di trasporto, HTTP con endpoint registrati da WordPress e STDIO (che richiede WP-CLI), più un'interfaccia per scriverne di propri; chi si collega via HTTP si autentica come utente WordPress, quindi conta quello che quell'utente può fare.
- La 0.7.0 porta il supporto alla revisione 2026-07-28 del protocollo, con la scoperta del server senza sessione, metadati per ogni richiesta e i tre header HTTP Mcp-Method, Mcp-Name e Mcp-Param-*; i client fermi alla revisione 2025-11-25 restano coperti e i tool richiamabili direttamente possono chiedere un dato mancante all'utente restituendo McpInputRequired.

## Installazione e uso

- Requisiti: WordPress 6.9 o successivo (la pagina del plugin indica test fino alla 7.1.2) e PHP 7.4 o successivo, WP-CLI per il trasporto STDIO e Node.js per il proxy remoto sul trasporto HTTP.
- Installazione dalla directory dei plugin oppure come pacchetto Composer (wordpress/mcp-adapter su Packagist).
- Da solo il plugin non cambia nulla per un sito: le abilities sono private per impostazione predefinita e per esporle a MCP vanno marcate come pubbliche nei metadati (meta.mcp.public a true).
- Il rischio si sposta sul codice di chi registra le abilities: il lavoro lo fa il permission_callback di ciascuna ability, e l'annuncio ufficiale elenca quattro indicazioni — niente __return_true sulle operazioni distruttive, utenti dedicati con capability ridotte per l'accesso MCP in produzione, abilities di sola lettura sugli endpoint HTTP pubblici, monitoraggio e log dell'uso.

## Repository

- Il codice sta nel repository dell'organizzazione WordPress su GitHub (github.com/WordPress/mcp-adapter), con licenza GPL-2.0: al 6 ottobre 1.794 stelle, 203 fork e 69 fra issue e pull request aperte.
- La pagina del plugin nella directory segna oltre 40.000 installazioni attive, un dato da leggere con prudenza perché il plugin è in directory da pochi giorni.

## Azienda / autore

- Autore dichiarato nella directory: WordPress.org (profilo wordpressdotorg), dentro l'iniziativa AI Building Blocks for WordPress del team AI del progetto.
- Presentato da Pascal Birchler il 17 luglio 2025 sul blog del team AI di WordPress e raccontato da Jonathan Bossenger il 4 febbraio 2026 su developer.wordpress.org; la 0.7.0 è stata rilasciata da Ovidiu Galatan, il contributor più attivo del repository.
- Il progetto parallelo wordpress-mcp di Automattic è stato archiviato con 944 stelle e il suo README rimanda a mcp-adapter come plugin e pacchetto Composer canonico.

## Limiti e avvertenze

- La numerazione resta sotto la 1.0 e la 0.7.0 rompe di nuovo la compatibilità: sparivano le classi DTO generate, i tre validatori (tool, risorse, prompt) e il filtro mcp_adapter_validation_enabled, i transport personalizzati devono delegare a HttpRequestHandler o a McpWireOrchestrator e l'uso come libreria Composer incorporata nel proprio plugin risulta deprecato.
- Stare nella directory non rende ufficiale un plugin: tra i cinque plugin MCP presenti il 6 ottobre c'erano WPVibe di SeedProd con oltre 50.000 installazioni attive e Royal MCP con oltre 10.000, ma solo MCP Adapter ha come autore WordPress.org.

## Timeline delle notizie

- **2026-10-06** — MCP Adapter 0.7.0 è la prima versione del plugin ufficiale di WordPress per il Model Context Protocol pubblicata nella directory dei plugin, dopo oltre un anno di presenza solo su GitHub e Composer: collega la Abilities API del core 6.9 ai client MCP, con tre strumenti generali, trasporti HTTP e STDIO e il supporto alle revisioni 2025-11-25 e 2026-07-28. Il rilascio rompe la compatibilità con il codice scritto sopra le versioni precedenti, mentre le abilities restano private per impostazione predefinita e la sicurezza dipende dal permission_callback di ciascuna.

## Collegamenti

- [[mcp]]
- [[wordpress]]
- [[agenti-ai]]
- [[claude-code]]
- [[index]]
