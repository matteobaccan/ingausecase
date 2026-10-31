---
title: "Cyber Verification Program"
category: strumento
tags: [anthropic, sicurezza, claude, programmi, accesso]
related_puntate: []
created: 2026-10-21
updated: 2026-10-21
---

# Cyber Verification Program

## Introduzione

Programma con cui [[anthropic]] riduce i blocchi anti-cyber di [[claude]] per i professionisti della sicurezza verificati, cioè i filtri in tempo reale che fermano richieste a rischio come l'analisi di un malware o la validazione di un exploit. Dal 6 ottobre 2026 si articola in tre livelli: Defense Access, Red Team Access e Specialized Access.

## Funzionalità principali

- La candidatura si presenta dal Verification Portal con un account Anthropic, una sola per organizzazione, allegando l'attestazione dei controlli di sicurezza; Anthropic punta a rispondere entro sette giorni lavorativi.
- I singoli professionisti possono chiedere solo il Defense Access, mentre Red Team e Specialized sono riservati alle organizzazioni e il livello assegnato è il più alto possibile in base a quanto scritto nella domanda.
- L'approvazione vale solo nei workspace a cui un amministratore assegna il programma; il traffico degli altri workspace non è coperto.

## Requisiti

- Tutti i livelli chiedono un referente di sicurezza nominato, la segnalazione degli incidenti entro 24 ore e delle violazioni sospette entro 72, e accessi sempre personali.
- Dal 15 dicembre 2026 il Defense Access richiede un'autenticazione a più fattori resistente al phishing e non ammette più le API key, da sostituire con credenziali a breve durata.
- Red Team e Specialized limitano gli utenti approvati a 25, impongono account sul dominio del cliente, dispositivi gestiti e controlli sul personale.

## Casi d'uso

- Serve quando i classificatori interrompono un lavoro legittimo come il reverse engineering di un malware o la validazione di un exploit; revisione del codice, threat modeling e patch di problemi noti restano consentiti a tutti.
- Lo sviluppo di ransomware o malware resta bloccato per tutti anche con il programma attivo.

## Azienda/autore

- [[anthropic]]

## Timeline delle notizie

- **2026-10-21** — Pillitteri ricostruisce la procedura di candidatura al Cyber Verification Program: una domanda per organizzazione dal Verification Portal, scelta del livello fra Defense, Red Team e Specialized, attestazione dei controlli di sicurezza e decisione entro sette giorni lavorativi, con assegnazione del programma ai singoli workspace da parte di un amministratore.

## Collegamenti

- [[anthropic]]
- [[claude]]
- [[sicurezza-ai]]
- [[index]]
