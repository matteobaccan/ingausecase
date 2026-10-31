---
title: "Brevo"
category: azienda
tags: [email-marketing, supply-chain, cloudflare, worker, crm]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
---

# Brevo

## Introduzione

Piattaforma di email marketing e CRM già nota come Sendinblue, usata da siti e newsletter per inviare campagne e gestire contatti. Il 14 settembre 2026 ha servito codice malevolo dai propri domini per circa cinque ore e mezza, dopo che un attaccante ha usato una chiave API di [[cloudflare]] trovata nel codice sorgente per far passare il traffico attraverso un Worker sotto il suo controllo; l'azienda lo ha confermato in un post-mortem pubblicato il 17 settembre.

## Funzionalità principali

- Widget e script incorporabili dai siti clienti, tra cui sdk-loader.js, brevo-conversations.js e i form di sibforms.com: sono questi gli elementi che l'attacco ha usato come veicolo di distribuzione.

## Timeline delle notizie

- **2026-09-20** — La società di sicurezza Sansec stima in più di centomila i siti che incorporavano gli script coinvolti, una cifra che arriva da una ricerca su PublicWWW e che quindi conta i siti che montano quei widget, non quelli di cui sia stata dimostrata la compromissione. Per chi gestisce un sito la parte scomoda arriva dopo: il codice malevolo usciva da domini di Brevo con certificato valido, quindi nessun controllo di integrità lo ha intercettato, e il Worker rimuoveva anche header di sicurezza come il Content-Security-Policy.
- **2026-09-20** — La causa tecnica è nel post-mortem: una chiave API Cloudflare a vita lunga, con permessi pieni sull'account, era conservata dentro il codice sorgente dell'applicazione e con quella si potevano creare Worker, route e record DNS senza che scattasse un allarme. Chi controlla un Worker riscrive quello che il visitatore riceve senza toccare un solo file sul server di origine, ed è esattamente quello che è accaduto: chi avesse scaricato il file direttamente dai server di Brevo lo avrebbe trovato pulito, chi lo riceveva passando dalla rete Cloudflare no.
- **2026-09-20** — Le due ricostruzioni della finestra oraria non coincidono al minuto: Brevo colloca la creazione dell'hostname di appoggio alle 14:23 UTC del 14 settembre, il primo test del Worker alle 14:28, l'attivazione della route su brevo.com alle 14:42 e l'impatto pieno alle 15:01, con l'aggiornamento del Worker alle 16:07 per colpire anche i file JavaScript dei clienti e le pagine su sibforms.com; Sansec, misurando dall'esterno, indica come ultima copia pulita di sdk-loader.js quella delle 16:04:23 e colloca la consegna del malware tra le 16:05:18 e le 20:12:53. Il Worker malevolo viene rimosso alle 20:30 e una verifica indipendente conferma pagine pulite alle 20:42, mentre un certificato TLS per cdn.sendibt1.com risulta creato il 25 agosto, quasi tre settimane prima, e dal 15 settembre gli host malevoli hanno smesso di risolvere.
- **2026-09-20** — La vicenda rientra nella stessa famiglia dell'attacco alla catena di fornitura npm di [[tanstack]], con script malevoli serviti dai domini di un fornitore invece che pubblicati su un registro di pacchetti.

## Collegamenti

- [[attacco-supply-chain-npm]]
- [[cloudflare]]
- [[cybersicurezza]]
- [[tanstack]]
- [[wordpress]]
- [[index]]
