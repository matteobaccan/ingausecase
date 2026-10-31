---
title: "Violoop"
category: strumento
tags: [hardware, agent, ai-locale, automazione, kickstarter]
created: 2026-10-18
updated: 2026-10-18
---

# Violoop

## Introduzione

Piccolo box con intelligenza artificiale che si collega al computer, legge lo schermo e muove mouse e tastiera al posto dell'utente, venduto dalla startup BVIO Technology (Hong Kong, team a Shenzhen) in prevendita su Kickstarter a 399 dollari, con prezzo previsto in negozio a 699 e campagna che si chiude il 30 ottobre 2026. Si presenta al computer come una normale tastiera USB, quindi non servono driver, e legge lo schermo sul dispositivo stesso.

## Funzionalità principali

- Tre modalità: Instant, che suggerisce il passo successivo e basta premere Tab; attività lunghe su più app in sequenza; Away Mode, che continua a schermo bloccato e manda una notifica al telefono quando ha finito o serve l'utente.
- Per ogni azione sceglie il canale più affidabile: script e API al 99% in circa 10 millisecondi, scorciatoie da tastiera al 95% in 20, elementi di accessibilità al 90% in 50 e clic sull'interfaccia grafica al 70% in 200.
- L'autorizzazione passa da un chip separato (un microcontrollore STM32H563) e da un pulsante fisico cablato a quel chip e non al software AI; in Away Mode l'ok si dà dall'app sul telefono.

## Hardware

Processore RK3576 a otto core con acceleratore AI da 26 TOPS, 13 GB di memoria, 128 GB di archiviazione, Wi-Fi a doppia banda, Bluetooth 5.2 e schermo AMOLED touch; 450 grammi, 90×92×80 millimetri e alimentatore proprio a 12 volt.

## Modelli supportati

Il modello locale è [[qwen|Qwen]] 8B quantizzato a 4 bit e gira interamente sul box; per i compiti più pesanti l'utente collega la propria chiave API di [[claude]] (Anthropic), [[openai]] o [[google]], e paga il provider direttamente, mentre il servizio opzionale Violoop AI plan di BVIO ha un prezzo non pubblicato.

## Timeline delle notizie

- **2026-10-18** — Violoop è in prevendita su Kickstarter a 399 dollari: a dodici giorni dalla chiusura la campagna segna 2.318.432 euro raccolti su un obiettivo di 8.893 con 4.783 sostenitori, ma le consegne oscillano tra ottobre e novembre e per l'Italia non c'è una data, perché dipende dalla certificazione CE. Il 70% di riuscita sui clic grafici, il confronto col Mac mini M4 e l'addestramento su oltre 200 app sono dati dichiarati da BVIO e non verificati da terzi.

## Collegamenti

- [[qwen]]
- [[claude]]
- [[openai]]
- [[google]]
- [[agenti-ai]]
- [[ai-locale]]
- [[index]]
