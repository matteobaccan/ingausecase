---
title: "WeatherNext Cyclones"
category: modello
tags: [deepmind, forecasting, meteo, open-weight, uragani]
related_puntate: []
created: 2026-10-12
updated: 2026-10-12
---

# WeatherNext Cyclones

## Introduzione

Famiglia di modelli di machine learning di [[google-deepmind]] addestrati sulla rianalisi atmosferica globale con focus specifico sui cicloni tropicali, non collegata al Gemini che si usa nel browser. La variante descritta nel paper WeatherNext Cyclones, pubblicato su Nature il 6 agosto 2026 con National Hurricane Center, Colorado State University, UK Met Office e University of Waterloo, è quella usata dall'NHC nella stagione 2026; codice e pesi sono usciti lo stesso giorno su GitHub con licenza Apache 2.0, nelle varianti WeatherNext Cyclones, WeatherNext 2 e WeatherNext 2-mini, quest'ultima girante anche in un notebook Google Colab gratuito.

## Capacità e performance

- Le previsioni a tre giorni sul ciclone raggiungono l'accuratezza che i modelli numerici tradizionali ottenevano a due giorni, cioè 24 ore in più di preavviso; DeepMind parla di «circa un decennio di progresso meteorologico in un singolo modello».
- L'ensemble produce fino a mille scenari per run tramite reti generative funzionali, e il cono di previsione si allunga fino a quindici giorni: dove un modello fisico dà poche traiettorie, qui la densità di probabilità si vede nella stessa esecuzione.
- Limite dichiarato dai previsori: il modello produce un numero, non un meccanismo fisico, e su fenomeni fuori dalla distribuzione di addestramento può sbagliare in silenzio; per questo l'NHC combina sempre AI, modelli numerici e giudizio umano.

## Azienda di riferimento

- [[google-deepmind]]

## Timeline delle notizie

- **2026-10-12** — Il National Hurricane Center costruisce sull'avviso di WeatherNext l'uragano Isaias, toccato terra il 9 ottobre vicino a Destin nel Panhandle della Florida come categoria 2 con venti a 100-105 mph: oltre il 60 per cento delle soluzioni dell'ensemble DeepMind indicava quel landfall mentre ECMWF e GFS spingevano la tempesta verso ovest, e la traccia reale coincide con quella del modello. Il direttore Michael Brennan parla di modelli AI «più consistenza», con l'NHC che ha fornito a DeepMind la propria climatologia storica dei cicloni atlantici per il fine-tuning, dopo l'uso già fatto per l'uragano Melissa nel 2025.

## Collegamenti

- [[google-deepmind]]
- [[weathernext-3]]
- [[index]]
