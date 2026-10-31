---
title: "Decisions API"
category: strumento
tags: [openai, api, agenti, inferenza]
related_puntate: [20261007, 20261008]
created: 2026-10-07
updated: 2026-10-24
sources: [raw/puntate/ainews20261007.md, raw/tldr/tldr20261007.md, raw/puntate/ainews20261008.md, raw/tldr/tldr20261008.md, raw/controrumore/controrumore20261024-diario-ai-sicurezza-regole-e-nuovi.md]
---

# Decisions API

## Introduzione

API di [[openai]] che lascia scegliere all'applicazione il modello, il tool o l'azione giusta in tempo quasi reale. E' pensata per le decisioni di instradamento degli agenti e si appoggia alla Responses API.

## Capacita' e performance

- Prende decisioni fino a dieci volte piu' veloci di [[gpt-6-luna]] attraverso la Responses API, accettando in ingresso testo e immagini. [Fonte: raw/puntate/ainews20261007.md]
- Supporta tre tipi di output — predicati, scelte e punteggi — e costa 0,10 dollari per milione di token in ingresso, senza addebiti per cache in lettura, cache in scrittura o token in uscita. [Fonte: raw/tldr/tldr20261007.md]

## Disponibilita'

- E' in beta pubblica ed e' disponibile per tutti gli sviluppatori. [Fonte: raw/puntate/ainews20261007.md]

## Azienda di riferimento

- [[openai]]

## Timeline delle notizie

- **2026-10-07** — OpenAI apre in beta pubblica la Decisions API, che sceglie modello, tool o azione in tempo quasi reale con decisioni fino a dieci volte piu' rapide di GPT-6 Luna via Responses API; accetta testo e immagini, restituisce predicati, scelte o punteggi e costa 0,10 dollari per milione di token in ingresso. [Fonte: raw/puntate/ainews20261007.md] [Fonte: raw/tldr/tldr20261007.md]
- **2026-10-08** — La Decisions API è basata su un modello multimodale chiamato Jev, costruito su GPT-6 Luna: negli esempi mostrati analizza oggetti come le uova rilevando se sono pulite, sporche o rotte, con una latenza di circa duecentosettanta millisecondi. [Fonte: raw/puntate/ainews20261008.md]
- **2026-10-24** — È disponibile a tutti i clienti dopo la fase di accesso limitato, con la versione pubblica che include modalità vocali e visive: [[openai]] riferisce risposte passate da uno-tre secondi a circa 100-180 millisecondi, e il cliente Speak dichiara una riduzione da 1,4 a 0,13 secondi tra le azioni del tutor linguistico. I dati prestazionali provengono dall'azienda e dai primi clienti, quindi velocità, costo e accuratezza vanno valutati sui singoli flussi di lavoro. [Fonte: raw/controrumore/controrumore20261024-diario-ai-sicurezza-regole-e-nuovi.md]







## Collegamenti

- [[openai]]
- [[gpt-6-luna]]
- [[agenti-ai]]
- [[index]]
