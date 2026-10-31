---
title: "ChatGPT Ads"
category: strumento
tags: [ads, gdpr, openai, pixel, privacy, tracciamento]
related_puntate: []
created: 2026-09-21
updated: 2026-10-16
sources: [raw/pillitteri/pillitteri20260821-chatgpt-ads-europa-31-paesi.md, raw/pillitteri/pillitteri20260921-openai-cookie-obi-chatgpt-tracciamento-siti.md, raw/controrumore/controrumore20261006-diario-ai-lai-entra-nella-sfera-privata.md, raw/pillitteri/pillitteri20261006-chatgpt-annunci-visivi-generazione-immagini.md, raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md]
---

# ChatGPT Ads

## Introduzione

Piattaforma pubblicitaria di [[openai]]: il pilota è partito negli Stati Uniti il 9 febbraio 2026, limitato agli utenti adulti loggati dei piani Free e Go, da marzo si è esteso a Canada, Australia e Nuova Zelanda e il 18 agosto 2026 l'azienda ha annunciato l'espansione a 31 mercati europei — i 27 Stati membri dell'Unione Europea più Norvegia, Islanda, Liechtenstein e Svizzera — attiva dal 24 agosto. È la più grande espansione geografica della piattaforma, che passa da 9 a circa 40 mercati in un colpo solo. [Fonte: raw/pillitteri/pillitteri20260821-chatgpt-ads-europa-31-paesi.md]

## Funzionalità principali

- La pubblicità riguarda solo i piani Free e Go e resta separata dalle risposte del modello; in Europa gli annunci partono senza personalizzazione, con una Privacy Policy dedicata aggiornata il 14 agosto 2026, perché l'area europea è il mercato pubblicitario più regolamentato del pianeta e OpenAI ha dovuto adattare i propri sistemi di consenso prima di entrare. [Fonte: raw/pillitteri/pillitteri20260821-chatgpt-ads-europa-31-paesi.md]
- La misurazione lato inserzionista passa dal pixel di OpenAI: la pagina carica lo script bzrcdn.openai.com/sdk/oaiq.min.js e manda gli eventi a bzr.openai.com/v1/sdk/events, e il browser allega da solo il cookie di identificazione. [Fonte: raw/pillitteri/pillitteri20260921-openai-cookie-obi-chatgpt-tracciamento-siti.md]

## Il cookie __obi

- Il cookie si chiama __obi, vive sul dominio openai.com e collega il browser di chi usa ChatGPT ai siti degli inserzionisti che hanno installato il pixel di OpenAI; lo ha documentato il 20 settembre 2026 l'analisi indipendente di Buchodi, secondo cui funziona anche per chi non ha effettuato l'accesso e viene classificato dall'azienda tra i cookie di analisi. OpenAI, interpellata il 14 settembre, non ha risposto nel merito. [Fonte: raw/pillitteri/pillitteri20260921-openai-cookie-obi-chatgpt-tracciamento-siti.md]
- Il flusso è in tre passaggi: il client genera 16 byte casuali e li manda all'endpoint /backend-api/bazaar/obi/sync-token, che risponde con un token JWT firmato RS256 con l'identificativo dell'account, un codice di 22 caratteri chiamato obi e una scadenza di 60 secondi; il gettone viene spedito a bzr.openai.com/v1/obi/sync e il server imposta il cookie __obi su .openai.com con attributi SameSite=None; Secure, flag HttpOnly e Max-Age di 31.536.000 secondi, cioè un anno esatto. [Fonte: raw/pillitteri/pillitteri20260921-openai-cookie-obi-chatgpt-tracciamento-siti.md]
- L'SDK prende l'identità dell'utente da quattro canali etichettati in, fm, ht e js; email, telefono e nome vengono trasformati con SHA-256 prima dell'invio mentre paese, regione, città e codice postale partono in chiaro, e gli indirizzi delle pagine sono ridotti a dominio e percorso senza query string. Nel campione osservato pesano più i dati raschiati in automatico (685 eventi) di quelli consegnati volontariamente (255), il campo più raccolto è il CAP con 100 eventi su 28 siti e il riconoscimento automatico dei dati risulta attivo su 638 pixel su 881. [Fonte: raw/pillitteri/pillitteri20260921-openai-cookie-obi-chatgpt-tracciamento-siti.md]

## Azienda / Autore

- [[openai]]

## Timeline delle notizie

- **2026-08-21** — ChatGPT mostra annunci pubblicitari in 31 mercati europei, Italia compresa, dal 24 agosto 2026: annuncio del 18 agosto, sei mesi dopo il pilota statunitense, solo per i piani Free e Go, senza personalizzazione in Europa e con Privacy Policy aggiornata il 14 agosto. [Fonte: raw/pillitteri/pillitteri20260821-chatgpt-ads-europa-31-paesi.md]
- **2026-09-21** — Un'analisi indipendente ricostruisce il cookie __obi sul dominio openai.com: collega il browser di chi usa ChatGPT ai siti degli inserzionisti con il pixel di OpenAI, funziona anche senza accesso, dura un anno (SameSite=None; Secure, HttpOnly) e viene classificato dall'azienda tra i cookie di analisi. [Fonte: raw/pillitteri/pillitteri20260921-openai-cookie-obi-chatgpt-tracciamento-siti.md]
- **2026-10-06** — OpenAI annuncia un nuovo formato visuale per gli annunci in ChatGPT, da testare negli Stati Uniti durante la generazione di immagini, con inserzioni etichettate e separate dal contenuto del modello e strumenti ampliati di attribuzione, misurazione incrementale e brand measurement. [Fonte: raw/controrumore/controrumore20261006-diario-ai-lai-entra-nella-sfera-privata.md] La ricostruzione di Pillitteri aggiunge che il test parte a fine ottobre solo negli Stati Uniti con un primo gruppo di inserzionisti, che riguarda gli utenti dei piani gratuito e Go mentre Plus, Pro, Business, Enterprise ed Edu restano esclusi, e che il business pubblicitario di ChatGPT aveva toccato 1 miliardo di dollari di ricavi annualizzati in circa 200 giorni dall'annuncio, con l'espansione di Ads Manager oltre i 60 mercati. I partner di misurazione citati includono Hightouch, LiveRamp, AppsFlyer, Adjust e Northbeam, con DoubleVerify e Integral Ad Science per la brand safety e le «Negative Phrases» per bloccare il contesto sgradito. [Fonte: raw/pillitteri/pillitteri20261006-chatgpt-annunci-visivi-generazione-immagini.md]
- **2026-10-16** — 404 Media ha sperimentato il targeting pubblicitario di ChatGPT con due campagne di prova: segnali contestuali delle richieste e segmenti di pubblico da email, numeri telefonici o identificatori già posseduti dagli inserzionisti. La redazione solleva dubbi di trasparenza ma non dimostra letture esterne delle conversazioni. [Fonte: raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md]







## Collegamenti

- [[chatgpt]]
- [[openai]]
- [[regolamentazione]]
- [[index]]
