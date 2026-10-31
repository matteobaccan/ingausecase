---
title: "TacticAI"
category: strumento
tags: [calcio, google-deepmind, graph-neural-network, ricerca, sport]
related_puntate: []
created: 2026-10-06
updated: 2026-10-06
sources: [raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]
---

# TacticAI

## Introduzione

Assistente tattico per il calcio sviluppato da [[google-deepmind]] con il Liverpool FC. La prima versione, descritta su Nature Communications il 19 marzo 2024, lavora sui calci d'angolo; l'11 giugno 2026 il Palmeiras è diventato il primo club a usarlo per leggere il gioco aperto.

## Funzionalità principali

- Previsione del ricevente: indica chi toccherà il pallone, con accuratezza top-3 di 0,782 sulla Premier League 2020-2021. [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]
- Previsione del tiro: stima la probabilità che dal corner nasca una conclusione, con punteggio F1 di 0,71. [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]
- Generazione guidata: propone disposizioni alternative dei giocatori, non solo analizza quelle reali. Su questo compito cinque professionisti del Liverpool, tre data scientist, un video analyst e un assistente allenatore, hanno preferito le proposte dell'AI nel 90% dei casi. [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]
- Modellazione: il campo è trattato come un grafo, con i giocatori come nodi e le relazioni di marcatura come archi, elaborato da una graph neural network. Il geometric deep learning con convoluzioni del gruppo D2 insegna al modello le simmetrie del rettangolo, moltiplicando di fatto per quattro il valore di ogni esempio. [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]
- Addestramento: 7.176 calci d'angolo validi delle stagioni 2020-2021 della Premier League. [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]

## Disponibilità

- Non è un prodotto in vendita: Google DeepMind lo concede in collaborazione diretta a partner selezionati (Liverpool, poi Palmeiras e la federazione brasiliana). [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]
- Il salto al gioco aperto annunciato nel 2026 non è coperto da un articolo scientifico né da metriche pubbliche, a differenza della versione sui corner passata dalla revisione paritaria. [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]

## Azienda / Autore

- [[google-deepmind]]
- [[google]]

## Timeline delle notizie

- **2026-06-15** — L'11 giugno 2026, all'evento Google for Brazil, il Palmeiras è diventato il primo club a usare TacticAI sul gioco aperto, con la promessa di prevedere l'evoluzione dell'azione fino a otto secondi prima a partire da normali dati video televisivi, una lavagna interattiva con trascinamento dei giocatori e la collaborazione della Confederazione calcistica brasiliana in vista dei Mondiali 2026. La prima versione dello strumento, sviluppata da Google DeepMind con il Liverpool FC e descritta su Nature Communications il 19 marzo 2024, si limitava ai calci d'angolo, addestrata su 7.176 situazioni della Premier League 2020-2021. Le capacità annunciate nel 2026 non hanno ancora un articolo scientifico né metriche pubbliche. [Fonte: raw/pillitteri/pillitteri20260615-google-tacticai-deepmind-calcio.md]

## Collegamenti

- [[google-deepmind]]
- [[google]]
- [[index]]
