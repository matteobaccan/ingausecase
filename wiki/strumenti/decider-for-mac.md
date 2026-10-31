---
title: "Decider for Mac"
category: strumento
tags: [perplexity, decisioni, macos, locale, privacy]
related_puntate: []
created: 2026-10-25
updated: 2026-10-25
---

# Decider for Mac

## Introduzione

App per la barra dei menu di macOS con cui [[perplexity]] fa girare sul computer dell'utente [[pplx-decider-flash|pplx-decider-flash-v1.2]], esponendolo come API locale all'indirizzo http://127.0.0.1:8080/v1/decisions. Le richieste hanno lo stesso formato della Decisions API ospitata, ma restano sulla macchina, senza chiave e senza fatturazione.

## Funzionalità principali

- Il contenuto va nel campo state, testo o immagine, e le domande nel campo questions; il tipo noul restituisce la probabilità di un sì, choice sceglie tra opzioni con un'etichetta e dà la probabilità di ciascuna con un valore di confidenza, score colloca la risposta su una scala decisa da chi scrive il codice, una domanda per richiesta.
- La porta predefinita è la 8080 e si cambia dal menu tra 8000, 8888, 9000, 11435 o un valore a scelta, dove stanno anche l'avvio al login e il percorso dei file del modello; la guida sconsiglia di aprire l'API agli altri computer della rete.
- Gli esempi ufficiali sono quattro script in Python: etichettare una cartella di file privati in un labels.csv, smistare screenshot in cartelle, controllare se sullo schermo compare un errore e un hook di pre-commit che ferma il commit quando una riga somiglia a un segreto.

## Requisiti

- Mac con Apple silicon (M1 o successivo, Intel non supportato), macOS 13 o superiore, 16 GB di memoria e circa 6 GB di spazio libero; al primo avvio l'app scarica un modello da circa 5,8 GB e può chiedere un token Hugging Face con permesso di lettura.
- Rispetto al servizio ospitato cambiano solo l'URL e l'intestazione di autorizzazione: in hosting il modello Flash costa 0,01 dollari per milione di token in ingresso con output gratuito e ha un limite di 10 richieste al secondo per organizzazione.

## Timeline delle notizie

- **2026-10-24** — Il 22 ottobre Perplexity annuncia Decider for Mac, app che porta in locale il decision model da 4 miliardi di parametri senza chiave API e senza costi a consumo; Perplexity non ha ancora chiarito perché il repository del modello sia privato e non pubblica latenza né velocità dell'API locale.

## Collegamenti

- [[perplexity]]
- [[pplx-decider-flash]]
- [[decision-model]]
- [[jev]]
- [[clef]]
- [[strands-decider-2b]]
- [[index]]
