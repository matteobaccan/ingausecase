---
title: "Magic Pointer"
category: strumento
tags: [google-deepmind, gemini, desktop, cursore, interfaccia]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
---

# Magic Pointer

## Introduzione

Puntatore del mouse potenziato da [[gemini]] e sviluppato da [[google-deepmind]] con i product team di Chrome e la divisione hardware dei laptop [[googlebooks|Googlebook]]: invece di indicare un pixel, il cursore capisce cosa si sta guardando, ascolta la voce, ricava il contesto e agisce direttamente sopra la pagina o l'immagine, senza copiare testo in un'altra finestra. Il progetto è stato presentato con un post sul blog DeepMind firmato dai ricercatori Adrien Baranes e Rob Marchant e con due demo interattivi distribuiti su [[ai-studio]]; il CEO di DeepMind Demis Hassabis lo ha rilanciato dal suo profilo definendolo "pretty magical".

## Funzionalità principali

- **Mantenere il flusso**: l'AI funziona in qualunque applicazione senza interruzioni, quindi si può chiedere assistenza su un PDF, un foglio di calcolo o una pagina web senza uscire dal contesto.
- **Mostrare invece di descrivere**: il sistema cattura il contesto visivo e semantico intorno al cursore, quindi sa se si sta puntando una tabella, un volto o un indirizzo, e riduce il testo necessario a descrivere ciò che si vede.
- **Accettare "questo" e "quello"**: il puntatore accetta richieste vocali con pronomi deittici, del tipo "sistema questo" o "sposta quello qui", perché funge da riferimento condiviso con il modello.
- **Trasformare i pixel in entità**: gli elementi statici diventano dati strutturati, quindi la foto di una nota scritta a mano diventa una lista modificabile, il fotogramma di un video che inquadra un ristorante diventa un link prenotabile e una tabella di numeri diventa il grafico chiesto a voce.
- Non è un assistente vocale e non sostituisce le chat di Gemini: è uno strato di suggerimenti contestuali invocato dal puntatore, che lavora offline sul modello Gemini Nano per i task semplici e passa al cloud solo per le richieste pesanti.

## Azienda / Autore

- [[google]]
- [[google-deepmind]]

## Timeline delle notizie

- **2026-05-12** — DeepMind pubblica il post con i quattro principi di design e i due demo su AI Studio, accompagnati da una clip che mostra il puntatore in azione durante la modifica di un'immagine.
- **2026-05-12** — Sul [[googlebooks|Googlebook]] la feature è la punta di diamante del sistema: il cursore analizza l'elemento sotto di sé e propone azioni rilevanti, come creare un evento Calendar precompilato quando passa su una data in una email Gmail, e in modalità multi-selezione chiede a Gemini di comporre due elementi diversi, per esempio mostrare come un divano apparirebbe in un salotto. Google non ha indicato quanta RAM occupi il modello in memoria, ma le indiscrezioni parlano di circa 4 GB allocati staticamente al runtime AI.
- **2026-05-14** — Lo stesso meccanismo arriva su Mac e Windows tramite Stream to Cursor, parte della nuova Gemini Desktop App: legge il contesto di qualunque finestra sotto il cursore e streama il contesto verso gli strumenti di coding.

## Collegamenti

- [[ai-studio]]
- [[gemini]]
- [[google]]
- [[google-deepmind]]
- [[google-io]]
- [[googlebooks]]
- [[index]]
