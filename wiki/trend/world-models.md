---
title: "World Models"
category: trend
tags: [robotica, simulazione, world-model]
related_puntate: [20260722, 20260725, 20260729, 20260730, 20260910, 20260917, 20260919, 20260921, 20261006]
created: 2026-08-12
updated: 2026-10-28
sources: [raw/puntate/ainews20260722.md, raw/puntate/ainews20260725.md, raw/puntate/ainews20260729.md, raw/puntate/ainews20260730.md, raw/puntate/ainews20260910.md, raw/puntate/ainews20260917.md, raw/puntate/ainews20260919.md, raw/puntate/ainews20260921.md, raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md, raw/pillitteri/pillitteri20260923-tripo-ai-p2-finanziamento-quad.md, raw/tldr/tldr20261001.md, raw/puntate/ainews20261006.md, raw/pillitteri/pillitteri20261012-runway-project-continuum-computer-senza-app.md, raw/controrumore/controrumore20261014-diario-ai-sicurezza-lavoro-e-nuovi.md, raw/tldr/tldr20261013.md, raw/pillitteri/pillitteri20261027-genie-4-google-deepmind-world-model.md]
---

# World Models

## Introduzione

Modelli che apprendono e simulano la dinamica del mondo (reale o virtuale) in tempo reale, usati per robotica, generazione video e pianificazione.

## Attori coinvolti

- [[jing]]
- [[video-ai]]
- [[world-labs]]
- [[worldmodelgym]]
- [[xgen-labs]]

## Timeline delle notizie

- **2026-07-22** — Decart LUCY 2.5 generava video in tempo reale in base all'input dell'utente: l'AI costruiva lo spazio virtuale al volo, senza game engine. [Fonte: raw/puntate/ainews20260722.md]
- **2026-07-25** — Bifrost ha rilasciato un sistema real2sim: da un video di un sito industriale a un ambiente 3D navigabile e fotorealistico in trenta minuti, con 3D Gaussian Splatting e asset articolati. [Fonte: raw/puntate/ainews20260725.md]
- **2026-07-29** — Reka AI ha aperto WorldModelGym, leaderboard che valuta la capacità di prevedere quale azione porta al miglior risultato; Dreamer-v3 ha guidato tre benchmark su quattro. [Fonte: raw/puntate/ainews20260729.md]
- **2026-07-30** — ABot World 0.5B, world model che gira in tempo reale su GPU consumer: gli dai un'immagine iniziale e lo piloti con la tastiera. [Fonte: raw/puntate/ainews20260730.md]
- **2026-09-01** — [[world-labs]], la società di [[fei-fei-li]], presenta [[world-labs-atlas]]: un world model che unisce generazione con controllo della telecamera, ricostruzione spaziale da due o tre foto e simulazione spazio-temporale, con uscita in nuvola di punti o gaussian splat. La stessa azienda dichiara di aver fatto girare cinque piattaforme robotiche per un'ora ciascuna dentro ambienti ricostruiti, il real-to-sim che toglierebbe di mezzo la scarsità di dati di addestramento realistici per i robot, ma il dato resta senza verifica indipendente. [Fonte: raw/pillitteri/pillitteri20260904-world-labs-atlas-world-model-3d.md]
- **2026-09-10** — Da nove foto sgranate di uno studio, GPT-6 Astra di OpenAI ricostruisce lo spazio, capisce come sono disposti gli oggetti e genera un modello 3D completamente interattivo: quello che richiedeva scanner professionali da cinquantamila dollari ora si fa con un telefono. [Fonte: raw/puntate/ainews20260910.md]

- **2026-09-17** — [[relateanything]] stima in tempo reale le relazioni tra gli oggetti di una scena con 53 milioni di parametri: 474.000 immagini e 4,3 milioni di relazioni in addestramento, oltre diecimila tipi di relazione coperti e circa venti millisecondi per fotogramma. [Fonte: raw/puntate/ainews20260917.md]
- **2026-09-19** — [[xgen-labs]] presenta un'IA che simula un mondo intero dove ti muovi in prima persona: il modello JING è già numero uno nel ranking mondiale WBench e viene letto come il primo passo verso un OASIS tipo Ready Player One. [Fonte: raw/puntate/ainews20260919.md]

- **2026-09-21** — [[gavel]] porta Qwen3-8B dal 41,2 al 91,8 per cento sui task robotici a lungo orizzonte senza toccare il modello: il guadagno viene da un grafo del mondo con relazioni fra oggetti e precondizioni delle azioni, che intercetta gli errori di stato prima dell'esecuzione e corregge le violazioni semplici senza richiamare il modello. [Fonte: raw/puntate/ainews20260921.md]

- **2026-09-21** — [[tripo]] lancia [[tripo-p2-0]], primo modello del settore con topologia quad nativa, e il settore passa dalla fase dimostrativa a quella in cui servono capitali seri per addestrare modelli sempre più grandi: World Labs ha raccolto oltre un miliardo di dollari, Tripo circa 446 milioni in un solo round. [Fonte: raw/pillitteri/pillitteri20260923-tripo-ai-p2-finanziamento-quad.md]
- **2026-10-01** — Runway presenta Praxis-1, modello world action open-weight che trasforma il pre-training video in controllo per robot reali, in test con i primi partner sul loro hardware e con rilascio pubblico previsto nei mesi successivi. [Fonte: raw/tldr/tldr20261001.md]
- **2026-10-06** — Il team dietro [[jepa-anything]] presenta un world model unificato che funziona attraverso molecole, cellule, fluidi, pazienti, robot e meteo, con codice e paper disponibili. [Fonte: raw/puntate/ainews20261006.md]
- **2026-10-12** — Con Project Continuum, Runway porta Solaris dall'interfaccia singola alla shell intera: Solaris è un world model applicato a un'interfaccia anziché a un mondo fisico, presentato a fine agosto nella famiglia Interface World Models e costruito secondo CMSWire sul video Gen-4.5 con un modello linguistico che decide come cambia l'interfaccia. Runway dichiara 720p e frame in meno di 500 millisecondi e uno studio interno con 250 partecipanti che preferisce le interfacce generate a quelle scritte in codice da Claude Opus 5, ma sono numeri dell'azienda su un test dell'azienda. [Fonte: raw/pillitteri/pillitteri20261012-runway-project-continuum-computer-senza-app.md]
- **2026-10-13** — Arriva Helix World, world model audio-visivo in tempo reale interattivo, capace di generare scene esplorabili con colonna sonora spaziale. [Fonte: raw/tldr/tldr20261013.md]



- **2026-10-14** — Artificial Analysis presenta AA-3D, benchmark per 21 modelli nella costruzione di scene tridimensionali interattive da istruzioni testuali, con giudici umani che confrontano i risultati alla cieca e agenti che correggono il lavoro via screenshot: Claude Sonnet 5.5 guida la classifica iniziale ma il vantaggio sui rivali immediati non è statisticamente significativo, e qualità percepita, spesa e velocità non coincidono. [Fonte: raw/controrumore/controrumore20261014-diario-ai-sicurezza-lavoro-e-nuovi.md]
- **2026-10-28** — [[google-deepmind]] presenta [[genie-4]], world model in tempo reale che secondo l'azienda è il primo del suo genere a generare audio nativo, con rumori ambientali, musica e personaggi che parlano, oltre a mondi esplorabili e modificabili con un prompt mentre la simulazione gira: sotto lavora la famiglia Gemini, con Gemini Omni che ancora aspetto e comportamento della scena al mondo reale. Google ammette deriva visiva e perdita di permanenza degli oggetti nelle sessioni lunghe, il testo leggibile compare solo se scritto nel prompt e la coerenza «fino a due minuti» è la cifra riportata da TechCrunch, mentre la pagina di DeepMind parla più prudentemente di alcuni minuti di interazione continua. Il rilascio resta in anteprima di ricerca per tester selezionati, con lista d'attesa per Project Genie e accesso futuro per gli abbonati Google AI Ultra e per i partner dell'API Gemini e di AI Studio, senza Paesi né prezzo annunciati. [Fonte: raw/pillitteri/pillitteri20261027-genie-4-google-deepmind-world-model.md]
















## Collegamenti

- [[fei-fei-li]]
- [[gavel]]
- [[gpt-6-astra]]
- [[jing]]
- [[relateanything]]
- [[rsi-anything]]
- [[xgen-labs]]
- [[video-ai]]
- [[world-labs]]
- [[world-labs-atlas]]
- [[worldmodelgym]]
- [[project-continuum]]
- [[index]]
- [[image-blaster]]

