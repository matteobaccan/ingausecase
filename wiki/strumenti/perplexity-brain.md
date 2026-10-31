---
title: "Perplexity Brain"
category: strumento
tags: [perplexity, agent, memoria, context-graph]
related_puntate: []
created: 2026-09-15
updated: 2026-09-15
---

# Perplexity Brain

## Introduzione

Sistema di memoria persistente presentato da [[perplexity]] il 18 giugno 2026 per il suo agente [[perplexity-computer]]. Non conserva le preferenze o il tono dell'utente come fanno le memorie di ChatGPT e Claude: registra come l'agente ha svolto il lavoro, cosa ha funzionato, cosa è fallito e quali correzioni ha ricevuto.

## Funzionalità principali

- Si appoggia a un context graph, una rete navigabile che preserva le relazioni fra progetti, decisioni, file e fonti invece di essere una lista piatta di note, implementata come wiki gestita da un modello linguistico e caricata automaticamente nella sandbox dell'agente.
- Ogni voce di memoria mantiene un collegamento alla propria origine — sessione, file o connettore — e si ispeziona e cancella dalla sezione Customize, voce Memory.
- Il carattere auto-migliorante sta in una funzione di sintesi che a intervalli regolari, per esempio durante la notte, riverifica il grafo, applica le correzioni accumulate, scarta i vicoli ciechi e ricostruisce la wiki pronta per il giorno dopo.
- I numeri dichiarati dall'azienda sono venticinque percento di correttezza in più su compiti che richiedono contesto passato, sedici percento di recall in più e tredici percento di costo per task in meno, perché un agente che parte informato ha bisogno di meno passaggi e meno token.

## Azienda / Autore

- [[perplexity]]

## Timeline delle notizie

- **2026-06-18** — Perplexity presenta Brain in research preview per gli abbonati Max ed Enterprise Max: memoria automatica e inferita del lavoro dell'agente, con context graph rivisto di notte e tracciabilità della fonte per ogni voce. I benchmark sono di prima parte e riferiti a una research preview.

## Collegamenti

- [[perplexity-computer]]
- [[perplexity]]
- [[index]]
