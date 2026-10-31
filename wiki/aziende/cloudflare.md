---
title: "Cloudflare"
category: azienda
tags: [cloudflare, cloud, edge, infra, infrastruttura, open-source, scraping, usa]
related_puntate: [20260602, 20260604, 20260619, 20260624, 20260702, 20260806, 20260807, 20260917, 20261002, 20261003, 20261004, 20261005, 20261020, 20261021]
created: 2026-08-12
updated: 2026-10-29
---

# Cloudflare

## Introduzione

Azienda di infrastruttura web e edge AI, con servizi come Workers AI e Monetization Gateway per monetizzare API e pagine.

## Modelli

- [[grok]]

## Strumenti

- [[agentic-inbox]]
- [[kitesurf]]
- [[monetization-gateway]]
- [[sandstorm]]

## Timeline delle notizie

- **2026-05-19** — Cloudflare racconta di aver lanciato Claude Mythos Preview contro oltre cinquanta dei propri repository di produzione: il modello ha concatenato bug di bassa gravità in attacchi funzionanti contro runtime, edge data path e protocol stack, arrivando al dirottamento completo del flusso di controllo in dieci casi documentati, una valutazione operativa di quanto un modello generalista possa affiancare un red team specializzato.

- **2026-06-02** — Cloudflare ha rilasciato open source Agentic Inbox, un client email agentico che gira interamente su Workers e Durable Objects senza che la posta lasci il proprio account.
- **2026-06-04** — Cloudflare ha stretto una partnership con xAI per portare Grok su AI Gateway: modelli LLM, audio, immagine e video disponibili via Gateway, fatturati direttamente da Cloudflare, senza autenticazione aggiuntiva né chiavi API extra.
- **2026-06-19** — Cloudflare ha rilasciato Agentic Inbox, client email completo con agente AI integrato, completamente open source: niente API di terze parti, ogni mailbox gira su Durable Object isolato con database SQLite e allegati su R2; l'agente legge la posta, cerca conversazioni e genera bozze, ma non invia mai nulla senza conferma esplicita.
- **2026-06-24** — Cloudflare ha aperto un'API per scraping completo di siti web: restituisce HTML, Markdown o JSON, renderizza JavaScript, con supporto IA per estrazione intelligente di dati e livello gratuito disponibile.
- **2026-07-02** — Lista d'attesa aperta per Monetization Gateway: permette di addebitare per qualsiasi pagina web, dataset, API o tool MCP dietro Cloudflare, con pagamenti in stablecoin tramite il protocollo aperto X402.
- **2026-08-06** — Cloudflare OS rimasterizza Sandstorm: piattaforma vibe coding personale con sandbox ultra sicura, ogni gadget isolato e modifica AI del software senza rischi.
- **2026-08-07** — Cloudflare ha presentato Kitesurf, browser per agenti costruito interamente su Workers: scritto in Rust, usa da tre a sette volte meno CPU e memoria rispetto a Chromium, si avvia per richiesta ed e' gratuito in beta.

- **2026-09-16** — Cloudflare rende operativo il blocco predefinito dei crawler AI sui nuovi domini, distinguendo bot training/agent/search all'edge. L'annuncio è del 1-2 luglio 2026, con lo slogan "Content Independence Day, un anno dopo", e introduce una tassonomia in tre categorie (Search, Training, Agent): sulle pagine con pubblicità i crawler Training e Agent vengono bloccati per impostazione predefinita, mentre quelli di ricerca restano consentiti, e i crawler mixed-use che non separano gli scopi (circa il 36% del traffico dei crawler) vengono bloccati anch'essi dal 15 settembre 2026. Il nuovo default vale per i nuovi clienti, i nuovi siti dei clienti esistenti e i piani gratuiti, non per i siti già attivi, e il Pay Per Crawl evolve in Pay Per Use, che compensa l'editore quando il contenuto genera valore reale, con Ceramic.ai e You.com come primi partner e un Monetization Gateway in arrivo.
- **2026-09-17** — Rilascia come open source una skill che trasforma qualsiasi agente in un auditor di sicurezza, articolata in sei fasi — ricognizione, ricerca delle vulnerabilità, validazione, verifica, output strutturato e report — e costruita sullo stesso codice che l'azienda usa internamente.
- **2026-07-19** — Dalle 17:03 UTC del 17 luglio il WAF include due regole con azione predefinita Block contro [[wordpress|wp2shell]] e la SQL injection che completa la catena, distribuite sia nel Managed Ruleset sia nel Free Ruleset: i piani gratuiti risultano protetti in automatico, mentre su Pro, Business ed Enterprise le Managed Rules vanno verificate a mano, e la copertura vale solo per il traffico che passa davvero dalla rete di Cloudflare. L'azienda invita a monitorare i Security Events per le richieste che corrispondono alle due regole.
- **2026-09-20** — La vicenda [[brevo]] mostra il lato opposto dei Worker: con una chiave API a vita lunga con permessi pieni sull'account, trovata nel codice sorgente del cliente, si creano Worker, route e record DNS senza allarmi, e il Worker riscrive sul bordo le risposte del fornitore rimuovendo header di sicurezza come il Content-Security-Policy, mentre i server di origine restano intatti.
- **2026-09-30** — Cloudflare usa modelli frontier per generare e provare attacchi contro il proprio Web Application Firewall, individuando 49 risultati abbastanza significativi da richiedere ulteriori analisi: quasi tutti riguardano command injection o server-side request forgery, classi in cui variazioni dell'input possono aggirare regole troppo specifiche.



- **2026-10-02** — Cloudflare rilascia due decision model addestrati internamente, Clef e Clef-flash, un'idea che si sta diffondendo rapidamente.
- **2026-10-02** — Cloudflare rilascia il 1° ottobre 2026 due modelli decisionali open source, [[clef]] e Clef-flash, ospitati su Workers AI e scaricabili gratis da Hugging Face con licenza Apache 2.0, con latenze dichiarate più basse e punteggi migliori rispetto a [[jev]]. Clef eredita un esperimento precedente in cui Cloudflare aveva adattato DiffusionGemma per esporre i logprob in modo deterministico, basandosi su un lavoro indipendente di Matt Mastracci su vLLM, ma cambia backbone passando a Qwen.



- **2026-10-03** — Cloudflare Clef batte Jev in due settimane: Qwen congelato fa un solo prefill, un piccolo schema head valuta tutte le opzioni in parallelo e non viene generato testo, per quattro volte la velocità di Jev e doppia precisione su alcuni benchmark, con codice aperto.
- **2026-10-04** — Cloudflare presenta Decision 2.0: modelli per classificazione e routing da zero virgola sei a ventisette miliardi di parametri, disponibili su Ollama come Clef e Clef Flash.
- **2026-10-05** — Porta in beta la Web Search API: collega le risposte AI a dati web in tempo reale con zero retention, passando tutto attraverso AI Gateway.
- **2026-10-18** — Dal 15 settembre 2026 i nuovi domini protetti da Cloudflare bloccano di default Training e Agent sulle pagine con annunci, mentre Search passa: il vecchio interruttore unico «Block AI bots» è diviso in tre controlli, ma per gli agenti esiste solo il blocco e non un'istruzione di esclusione come per i crawler. Attribuire a questo cambio i blocchi degli agenti come Muse resta un sospetto, perché il default vale per i nuovi domini.
- **2026-10-20** — Cloudflare presenta [[clairic]], modello di estrazione dati della nuova classe "System One": estrae, calcola, stima e prevede valori da input non strutturati senza generare token e accompagna le uscite con punteggi di confidenza.
- **2026-10-21** — Fra i quattro strumenti per cercare bug nel codice usciti ora, la Security Audit Skill di Cloudflare ricontrolla ogni finding con un agente fresco invece di fidarsi della prima scansione.
- **2026-10-24** — La skill security-audit pubblicata a giugno sotto licenza MIT trasforma un coding agent in auditor di sicurezza e al 24 ottobre conta 43.428 stelle, 2.712 fork e 85 fra issue e pull request aperte; dal file di circa 450 righe usato su un singolo repository è nato l'harness interno Vulnerability Discovery Harness, che su 128 repository ha prodotto 20.799 candidati grezzi e 7.245 risultati lavorabili dopo deduplica, con il tasso di rigetto in validazione sceso dal 40 all'11 per cento. L'harness completo non è pubblico e quei numeri sono misurati sui repository dell'azienda, non sulla skill.
- **2026-10-29** — Ha segnalato un problema di isolamento nel modello GLM-5.3 su Workers AI: tra il 27 agosto e il 9 settembre 155 risposte hanno contenuto dati di richieste precedenti di altri clienti, tutte associate a prompt molto lunghi e senza prove di sfruttamento intenzionale. Il difetto combinava la gestione della cache KV e la modalità di esecuzione di SGLang; il modello è stato disattivato e poi ripristinato con correzioni, ma i dati non sono stati verificati indipendentemente.




























## Collegamenti

- [[agentic-inbox]]
- [[grok]]
- [[kitesurf]]
- [[monetization-gateway]]
- [[sandstorm]]
- [[xai]]
- [[cloudflare-computer]]
- [[index]]

