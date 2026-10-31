---
title: "World Labs Atlas"
category: modello
tags: [3d, gaussian-splatting, robotica, world-model]
created: 2026-09-23
updated: 2026-09-23
sources: [raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]
---

# World Labs Atlas

## Introduzione

World model presentato da [[world-labs]] il 1 settembre 2026: non è un'app da scaricare, ma un modello che impara com'è fatto lo spazio e lo restituisce navigabile da qualsiasi angolazione. La differenza con un generatore di video è la geometria: un generatore di video produce fotogrammi che sembrano veri ma non sa dove sono gli oggetti nello spazio, mentre Atlas tiene traccia della struttura tridimensionale e permette di girare intorno alla scena. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]

## Capacità

- Generazione con controllo della telecamera: da un'immagine di riferimento produce foto e video con posizione e angolo di ripresa decisi da chi comanda, fino a un minuto di video a risoluzione 1440p. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]
- Ricostruzione spaziale: ricostruisce una scena reale partendo da una sola foto o da oltre cento, e spesso bastano due o tre immagini, restituendo sia nuovi fotogrammi sia il 3D vero e proprio sotto forma di nuvola di punti o di gaussian splat. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]
- Simulazione spazio-tempo: fa evolvere la scena nel tempo, non solo nello spazio; la generazione di immagini da testo eredita la coerenza spaziale del resto. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]
- È descritto come un omni model addestrato da zero per lavorare insieme su testo, immagini, video e 3D nello stesso spazio di ragionamento, con un trasformatore a diffusione autoregressivo sotto il cofano. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]

## Performance

- Sulla ricostruzione 3D da poche viste dichiara un errore medio di 25,3 contro i 28,7 del miglior modello specializzato rivale e i 36,4 di un altro concorrente, dove più basso è meglio. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]
- Sui video con telecamera controllata i valutatori umani lo hanno preferito ai modelli rivali nel 75 per cento dei casi contro MiniMax H, nell'81 contro Gemini Omni Flash, nell'86 contro Happy Horse 1.1 e nel 94 contro Seedance 2.5. World Labs ammette che nessun singolo benchmark cattura davvero cosa sappia fare Atlas, i confronti sono scelti dall'azienda e alcuni avversari sono modelli video puri, non world model. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]

## Disponibilità

- Non c'è un'app, un'API pubblica, un prezzo né una data di uscita: World Labs lo apre solo a partner selezionati dietro un modulo di richiesta, anche dall'Italia, quindi per un uso quotidiano serve aspettare. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]

## Azienda di riferimento

- [[world-labs]]

## Timeline delle notizie

- **2026-09-01** — [[world-labs]] presenta Atlas, world model 3D che unisce generazione con controllo della telecamera, ricostruzione spaziale da poche foto, simulazione spazio-temporale e generazione di immagini, con uscita in nuvola di punti o gaussian splat già compatibile con motori grafici e software di effetti visivi. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]

## Collegamenti

- [[world-labs]]
- [[world-models]]
- [[video-ai]]
- [[index]]
