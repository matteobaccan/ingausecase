---
title: "AiSOC"
category: strumento
tags: [sicurezza, soc, open-source, agenti, self-hosted]
related_puntate: []
created: 2026-10-31
updated: 2026-10-31
sources: [raw/pillitteri/pillitteri20261031-aisoc-soc-open-source-agenti-ai.md]
---

# AiSOC

## Introduzione

Security Operations Center open source, installabile sui propri server con licenza MIT, che raccoglie i log, li correla in incidenti e li fa analizzare da agenti AI. Nasce il 2 maggio 2026 sull'account GitHub di Beenu Arora, amministratore delegato e cofondatore di Cyble, che secondo il file dei crediti paga lo sviluppo. [Fonte: raw/pillitteri/pillitteri20261031-aisoc-soc-open-source-agenti-ai.md]

## Funzionalità principali

- Esegue 2.530 regole di rilevamento di una libreria da 7.015, più 76 regole a finestra mobile, e ripassa lo storico già raccolto quando arriva nuova threat intelligence.
- Ogni passo dell'agente finisce in un Investigation Ledger con prompt, chiamate agli strumenti, citazioni, verdetto e costo in token, esportabile come bundle firmato da rifare passo per passo.
- Un verdetto che cita un indicatore mai comparso nelle prove viene declassato a revisione umana, i playbook partono spenti e servono tre interruttori d'accordo, con approvazione che non può venire da chi ha fatto la richiesta.

## Installazione e uso

Docker Compose v2 con 8 GB di memoria e 20 GB di disco liberi, poi `make up`; i profili sono Core (16 servizi), Full con event lake e grafo (22 servizi, circa 12 GB) e Demo con dati sintetici. Il modello incluso è un Llama 3.2 da 3 miliardi quantizzato servito da Ollama, sostituibile da console con un provider a pagamento. [Fonte: raw/pillitteri/pillitteri20261031-aisoc-soc-open-source-agenti-ai.md]

## Repository

- github.com/beenuar/AiSOC — al 31 ottobre 2026 conta 5.489 stelle, 561 fork e 19 contributor, con versione 20.4.0.

## Azienda / autore

- Cyble — finanzia le ore di ingegneria e mantiene un prodotto commerciale chiuso costruito sulla stessa piattaforma.

## Timeline delle notizie

- **2026-10-31** — Il progetto documenta il caso della segnalazione numero 220 del 27 maggio 2026, in cui un'iniezione di prompt poteva far chiudere in automatico un allarme: la correzione è arrivata il giorno dopo con la sanificazione dei prompt e il contenuto non fidato racchiuso a parte. Un audit interno del 23 settembre ammette che la guida d'avvio portava a un'installazione senza ingestione, con la console riempita da 15 incidenti inventati scritti nel database. [Fonte: raw/pillitteri/pillitteri20261031-aisoc-soc-open-source-agenti-ai.md]

## Collegamenti

- [[cybersicurezza]]
- [[sicurezza-ai]]
- [[agenti-ai]]
- [[index]]
