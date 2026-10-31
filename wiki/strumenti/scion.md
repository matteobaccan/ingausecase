---
title: "Scion"
category: strumento
tags: [anthropic, git, open-source, source-control, sviluppo]
related_puntate: [20261014]
created: 2026-10-14
updated: 2026-10-14
---

# Scion

## Introduzione

Sistema di source control costruito da [[anthropic]] in cinque mesi per sostituire internamente Git: troppo lento per l'era degli agenti che scrivono codice.

## Funzionalità principali

- Scarica solo ciò che serve, calcola tutto sul server e registra solo le modifiche incrementali, invece di decine di gigabyte da scaricare a ogni operazione.
- Sviluppato da sette ingegneri con l'aiuto di [[claude]]: ad Anthropic il server al collasso con duemilacinquecento merge al giorno a maggio e oltre trentamila a settembre.

## Azienda / Autore

- [[anthropic]]

## Timeline delle notizie

- **2026-10-14** — Anthropic racconta di aver abbandonato Git per Scion, sistema di source control costruito in cinque mesi da sette ingegneri e Claude: i merge passati da duemilacinquecento al giorno a maggio a oltre trentamila a settembre avevano reso insostenibili clone da decine di gigabyte e server al collasso; Scion scarica solo ciò che serve, calcola sul server e registra le modifiche in modo incrementale. Anthropic precisa che Scion non è pensato come sostituto di git per l'uso generale: il sistema nasce per un monorepo unico usato da client in rete (agenti, CI, ambienti di sviluppo), dove il collo di bottiglia si è spostato su infrastruttura dimensionata per la scala umana; il post porta anche due esempi di quando gli ingegneri hanno detto di no a Claude, fra cui una revisione avversariale troppo difensiva che aveva spinto il modello ad aggiungere validazioni inutili. Attenzione all'omonimia: esiste anche uno Scion di Google, un banco di prova per orchestrare più agenti.

## Collegamenti

- [[anthropic]]
- [[claude]]
- [[sviluppo-software-ai]]
- [[index]]
