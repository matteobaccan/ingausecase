---
title: "Claude Duet"
category: strumento
tags: [anthropic, agent, proattivo, claude, opus]
related_puntate: []
created: 2026-10-22
updated: 2026-10-22
---

# Claude Duet

## Introduzione

Claude Duet è l'applicazione di [[anthropic]] in cui [[claude-opus-5-5]] lavora come agente proattivo: manda un riepilogo delle cose che contano, controlla le app collegate durante la giornata e si fa vivo quando serve una decisione. L'azienda l'ha presentata il 21 ottobre 2026 come research preview con lista d'attesa, per gli abbonati Pro e Max degli Stati Uniti.

## Funzionalità principali

- La giornata comincia con un riepilogo delle voci più importanti fra tutte le app collegate; da lì in poi l'agente scrive solo se c'è qualcosa che richiede attenzione, senza che l'utente apra una chat.
- Fra i compiti indicati da Anthropic ci sono riunioni da fissare, previsioni finanziarie o di vendita, dashboard con i dati di più strumenti, prototipi di web app e email di follow-up.
- Si parla con Duet per testo o a voce in un thread continuo, e memoria, skill e app collegate le eredita da Claude; l'app è separata da quella principale e arriva su iOS, Android e claude.ai.
- Gira su una macchina virtuale con un browser proprio nel cloud di Anthropic, quindi non richiede che il dispositivo dell'utente sia acceso, e controlla gli account collegati ogni poche ore per non esaurire i limiti d'uso del piano.
- I connettori sono oltre 6.000 fra plugin e integrazioni del Claude Marketplace, da Gmail e Slack a QuickBooks, Stripe, Gusto, DocuSign e Shopify.

## Cosa chiede prima di agire

- Prima di inviare messaggi, fare pagamenti, firmare documenti o eliminare qualcosa mostra cosa intende fare e aspetta il via libera, con le approvazioni decise dall'auto mode classifier già usato in [[claude-code]] e in Claude in Chrome.
- Negoziare titoli e spostare denaro fra conti restano vietati anche con il permesso; gli acquisti passano da Link di Stripe con una carta virtuale o da Shop Pay.

## Sicurezza

- Le credenziali seguono lo schema di Claude Managed Agents, quindi l'agente non vede direttamente password e token; contro le istruzioni nascoste nei contenuti l'azienda dichiara difese nate dalla ricerca sull'uso del browser, con test avversariali, red team, penetration test esterni e un programma di bug bounty su HackerOne.
- I risultati di quei test non sono pubblicati, quindi la protezione dalle prompt injection vale come impegno dichiarato e non come dato verificato da terzi.

## Disponibilità

- Research preview riservata agli abbonati Pro e Max degli Stati Uniti attraverso una lista d'attesa; Team ed Enterprise non sono ancora inclusi e non sono indicati altri Paesi.

## Azienda / Autore

- [[anthropic]]

## Modelli supportati

- [[claude-opus-5-5]]

## Timeline delle notizie

- **2026-10-22** — Anthropic presenta Claude Duet come agente proattivo basato su Claude Opus 5.5 che lavora in una macchina virtuale nel cloud, controlla le app collegate ogni poche ore e chiede conferma prima di messaggi, pagamenti, firme e cancellazioni; la research preview è riservata agli abbonati Pro e Max statunitensi su lista d'attesa, con oltre 6.000 connettori fra plugin e integrazioni.

## Collegamenti

- [[anthropic]]
- [[claude-opus-5-5]]
- [[claude-code]]
- [[agenti-ai]]
- [[index]]
