---
title: "Looped transformers"
category: trend
tags: [architettura, ricerca, inferenza, costi]
related_puntate: []
created: 2026-10-07
updated: 2026-10-07
---

# Looped transformers

## Introduzione

Architettura in cui lo stesso blocco di strati viene applicato piu' volte di fila ai dati di ogni token, invece di attraversare una pila di strati tutti diversi una volta sola: la rete guadagna profondita' di calcolo senza aggiungere parametri, perché i pesi dei passaggi successivi sono quelli del primo. Un transformer classico da 80 strati ha 80 gruppi di pesi distinti, uno «looped» può averne 40 e farli girare due volte, con la stessa profondita' di calcolo e meta' della memoria per i pesi.

## Fatti

- Il filone di ricerca non e' nuovo: il paper Hyperloop Transformers (Zeitoun, Torroba-Hennigen e Kim, aprile 2026) sostiene prestazioni comparabili a un transformer normale con circa il 50% di parametri in meno, mentre DeepLoop (luglio 2026) lavora sulla stabilita' dell'addestramento quando gli stessi pesi vengono attraversati piu' volte.
- Il numero di passaggi e' di fatto una manopola di servizio: a parita' di pesi, un laboratorio può addestrare una volta sola e vendere profili diversi cambiando quante volte il modello gira su se' stesso. I passaggi riusano i pesi ma non la cache delle chiavi e dei valori, perché gli stati intermedi sono diversi a ogni giro.

## Timeline delle notizie

- **2026-10-07** — Una pagina pubblica di Microsoft nota da uno screenshot descrive GPT-6.1 Sol come basato sugli stessi pesi di GPT-6 Sol ma con due passaggi di inferenza invece di tre: e' la prima traccia ufficiale dei looped transformers che The Information aveva attribuito a GPT-6 Astra, ma Microsoft non usa mai quel termine e OpenAI non ha commentato.

## Collegamenti

- [[gpt-6-1-sol]]
- [[gpt-6-astra]]
- [[microsoft]]
- [[index]]
