---
title: "Spyware mercenario e catene di exploit"
category: trend
tags: [spyware, iphone, sicurezza, citizen-lab, exploit]
related_puntate: []
created: 2026-09-21
updated: 2026-10-31
---

# Spyware mercenario e catene di exploit

## Introduzione

Lo spyware mercenario è un software di sorveglianza venduto a governi e agenzie e usato contro bersagli mirati, che costa milioni di dollari a bersaglio e colpisce giornalisti, attivisti, avvocati, politici e diplomatici. [[apple]] invia notifiche di minaccia dal 2021 e finora ha avvisato utenti in oltre 150 paesi, su tre canali contemporaneamente, notifica push, email e messaggio visibile facendo login su account.apple.com: la ridondanza è voluta e serve a difendersi dalle imitazioni.

## Attori coinvolti

- Citizen Lab, il laboratorio dell'Università di Toronto che indaga sugli abusi degli spyware di Stato, e Access Now, la ong che offre assistenza ai bersagli.
- Google Threat Intelligence Group, iVerify e Lookout, che hanno documentato la catena DarkSword.
- SlowMist, società specializzata in attacchi alle criptovalute.

## Notizie rilevanti

- **Ricevere la notifica non vuol dire che il telefono è stato bucato**: significa che i sistemi di Apple hanno individuato attività coerente con un attacco individualmente mirato con un livello di confidenza alto, e solo un'analisi forense può stabilire se l'attacco sia andato a segno. Le notifiche riguardano spesso tentativi avvenuti alcuni mesi prima dell'avviso, quindi non è detto che l'attacco sia in corso.
- La reazione istintiva di cancellare tutto e ripristinare il telefono è l'errore peggiore, perché distrugge le tracce prima dell'analisi forense.
- Il nome DarkSword è stato attribuito dai siti di notizie a due cose diverse, la catena di exploit documentata a marzo e l'avviso di settembre, che nell'originale non cita DarkSword.

## Timeline delle notizie

- **2026-08-14** — Il 13 agosto 2026 Apple invia una nuova ondata di notifiche di minaccia a utenti in 110 paesi, avvertendoli di essere finiti nel mirino di uno spyware mercenario; a dare per primo la notizia è John Scott-Railton, ricercatore senior del Citizen Lab, con un thread che spiega passo per passo cosa deve fare chi riceve l'avviso. La notifica non riguarda la stragrande maggioranza degli utenti, ma se arriva va presa sul serio e gestita con metodo, senza cancellare il dispositivo.
- **2026-09-21** — DarkSword è una catena di exploit per iPhone quasi tutta in JavaScript che parte da una pagina web, sfrutta sei vulnerabilità di cui tre zero-day al momento degli attacchi iniziati nel novembre 2025 e arriva al controllo completo del dispositivo su iOS dalla 18.4 alla 18.7: un iframe carica il loader, il codice esce dalla sandbox di Safari passando per il processo grafico, risale in mediaplaybackd e sfrutta due falle del kernel XNU, poi un payload ruba messaggi, dati di Telegram e WhatsApp, cronologia di Safari, keychain, posizione e portafogli di criptovalute e cancella i report dei crash per non lasciare tracce. Google Threat Intelligence Group, iVerify e Lookout l'hanno descritta il 18 marzo 2026 e Apple l'ha corretta.
- **2026-09-19** — Il CISO di SlowMist pubblica su X un avviso in cinque punti su una catena che parte da una pagina aperta con Safari e si chiude con l'estrazione di chiavi private e frasi mnemoniche dai wallet, con correzione di memoria in WebKit e JavaScriptCore, aggiramento dei Pointer Authentication Codes, uscita dalla sandbox WebContent e risalita a root nel kernel per portare via il Keychain: le versioni indicate vanno da iOS 13 a iOS 26.5, ma né Apple né Google né iVerify hanno confermato la parte alta dell'intervallo, e nell'avviso originale il nome DarkSword non compare.
- **2026-10-15** — Il Citizen Lab documenta AdFection, uno spyware consegnato attraverso annunci pubblicitari senza che la vittima clicchi nulla: il banner carica un codice che interroga un server NOAS, che restituisce JavaScript ed exploit solo ai dispositivi bersaglio e una risposta vuota a tutti gli altri, così l'annuncio sembra innocuo anche a chi lo controlla. Il report collega Discover-Tech, azienda israeliana con la piattaforma Controlium, a Candiru (oggi Saito Tech) — il caso ricostruito è Al Jazeera, con almeno 45 dispositivi presi di mira fra 2024 e 2025 — e cita Bindecy e Intelos fra i venditori collegati; Google ha chiuso a Discover-Tech l'accesso alle proprie piattaforme di scambio pubblicitario e attivato protezioni Safe Browsing.
- **2026-10-31** — Venerdì 30 ottobre 2026 [[apple]] ha avvisato singolarmente utenti iPhone in 99 Paesi di essere presi di mira da uno spyware mercenario, seconda ondata di Threat Notification in undici settimane dopo i 110 Paesi del 13 agosto e con un programma che ha ormai raggiunto oltre 150 Paesi; l'azienda non attribuisce gli attacchi a nessun attore né regione e non pubblica quante persone ricevano l'avviso. Tra i destinatari il giornalista libanese Radwan Mortada, già avvisato nel 2021, mentre il Citizen Lab si aspetta un'ondata con parecchi casi confermati e Access Now aveva segnalato dopo agosto richieste di assistenza fra il 30 e il 40 per cento sopra il solito.







## Collegamenti

- [[apple]]
- [[cybersicurezza]]
- [[sicurezza-ai]]
- [[telegram]]
- [[index]]
