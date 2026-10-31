---
title: "Intel GPU D-series"
category: strumento
tags: [intel, gpu, inferenza, hardware, data-center, memoria]
related_puntate: []
created: 2026-10-19
updated: 2026-10-19
---

# Intel GPU D-series

## Introduzione

Acceleratore PCIe per l'inferenza AI, nome commerciale del progetto Crescent Island, presentato da [[intel]] il 12 ottobre 2026 all'OCP Global Summit. Il modello di punta è il D270, con 160 GB di memoria LPDDR5X sulla scheda con marchio Intel; i titoli che parlano di 480 GB si riferiscono alle versioni dei partner ODM.

## Specifiche dichiarate

- Architettura Xe3P con 32 core e 256 motori matriciali XMX, 1,3 petaflops in FP8, 1,5 TB/s di banda di memoria, scheda PCIe 5.0 raffreddata ad aria con un limite di 350 watt.
- Modelli fino a 300 miliardi di parametri su una sola scheda e oltre mille miliardi in un sistema a 8 GPU, secondo Intel e senza benchmark indipendenti.
- Il sampling, cioè la consegna dei campioni ai clienti, è già partito; mancano data di lancio commerciale, prezzo e Paesi di vendita.

## Perché LPDDR5X

- Intel sceglie la memoria nata per smartphone e portatili invece della HBM usata da Nvidia e AMD: più economica e capiente per euro speso, ma con una banda molto più bassa.
- Secondo il confronto di XenoSpectrum, i 1,5 TB/s sono il 37,5% dei 4 TB/s dell'AMD Instinct MI350P, che ha 144 GB di HBM3E e arriva a 600 watt; la D-series sta sopra per capacità.
- A 4 bit per parametro, 300 miliardi di parametri occupano circa 150 GB: entrano nei 160 GB solo con quantizzazione spinta e poco spazio per il contesto, e il comunicato non specifica la precisione usata.

## Ecosistema

- Insieme alla GPU Intel ha mostrato rack basati sui Xeon 6+, con configurazioni che superano i 46.000 core per rack e assorbono 133,45 kW, in parte secondo lo standard Open Rack v3 dell'OCP.
- La base software Xe resta comune alle GPU Intel, con supporto upstream ai principali framework e runtime di inferenza e una promessa di supporto day 0 per Muse Glimmer di Meta; il driver Linux è ancora in sviluppo upstream secondo Phoronix.
- Il target dichiarato sono i server aziendali raffreddati ad aria che devono ospitare grandi modelli aperti senza rifare il data center, non i cluster più grandi.

## Limiti

- Non esistono misure indipendenti di token al secondo su modelli reali né un prezzo per scheda: senza questi due numeri i dati dichiarati restano una scheda tecnica.
- I 480 GB valgono solo per le schede dei partner ODM, di cui non c'è ancora un elenco; chi pianifica un acquisto deve contare su 160 GB.

## Timeline delle notizie

- **2025-10-14** - Crescent Island compare all'OCP con 160 GB di LPDDR5X e la promessa di sampling per la seconda metà del 2026.
- **2026-10-12** - Intel presenta la GPU D-series all'OCP Global Summit: il D270 dichiara 1,3 petaflops in FP8, 1,5 TB/s di banda, 350 watt e 160 GB di LPDDR5X, con sampling già avviato ma senza data di lancio né prezzo.

## Collegamenti

- [[intel]]
- [[ai-locale]]
- [[infrastruttura-ai]]
- [[index]]
