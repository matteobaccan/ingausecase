---
title: "Gemini Robotics 2"
category: modello
tags: [google-deepmind, physical-ai, robotica, vla]
related_puntate: []
created: 2026-09-19
updated: 2026-10-28
---

# Gemini Robotics 2

## Introduzione

Famiglia di tre modelli pubblicata da [[google-deepmind]] il 30 luglio 2026 che porta il controllo di un robot umanoide sotto un'unica policy addestrata: gambe, busto, braccia e mani a cinque dita. Fino alla versione precedente il modello governava solo la parte superiore del corpo, quindi il robot lavorava fermo davanti a un tavolo.

## Capacità e performance

- I tre livelli lavorano su scale temporali diverse: Gemini Robotics 2 è il modello VLA (Vision-Language-Action) che traduce immagini e istruzioni in comandi motori, Gemini Robotics ER 2 è il modello di ragionamento incarnato costruito su [[gemini-3-5-flash]] con 128.000 token in ingresso e fino a 64.000 in uscita, e Gemini Robotics On-Device 2 è la versione compatta che gira sul computer di bordo senza cloud, appoggiandosi ai modelli Gemma.
- Lo stesso checkpoint pilota tre configurazioni hardware diverse: Apollo 2 di Apptronik con le mani [[sharpa-robotics]] SharpaWave a 22 gradi di libertà, Apollo 2 con mani Inspire e la piattaforma a due bracci Franka Duo con pinza Robotiq.
- I tassi di successo pubblicati raccontano una manipolazione fine ancora aperta: svitare una lampadina 92%, inserimento di precisione 89,6%, preparazione di un kit di attrezzi 78,9%, prelievo da scaffale 76,3%, presa e posa generica 74,2%, prelievo da tavolo 68,4%, prelievo da pavimento 45,7%, chiudere un sacco della spazzatura 44%, sigillare una busta ziplock 40%, avvitare una lampadina 36%, usare la paletta per la polvere 32%.
- ER 2 consente a macchine di costruttori diversi di condividere una rappresentazione semantica della scena e passarsi un compito a metà, ed è integrato nella Gemini Live API con un endpoint di streaming bidirezionale; riconosce il fotogramma critico di un video con il 91,3% di accuratezza e uno scarto medio di 0,96 secondi, mentre classifica lo stato di avanzamento di un compito su cinque livelli con il 57,4%.
- On-Device 2 si adatta a una piattaforma robotica mai vista prima con meno di 200 esempi e poche ore di addestramento: sulla piattaforma SO101 passa dal 6,7% di Gemini Robotics 1.5 al 53,3%, su Dexmate dal 33,3% al 75,6%.

## Disponibilità

- Distribuzione a tre velocità: ER 2 è in anteprima pubblica su Google AI Studio e tramite le API Gemini (e in anteprima privata su Gemini Enterprise Agent Platform), il VLA Gemini Robotics 2 è in anteprima privata per partner selezionati con lista d'attesa pubblica, On-Device 2 è riservato al programma trusted tester.

## Azienda di riferimento

- [[google-deepmind]]

## Timeline delle notizie

- **2026-07-31** — Google DeepMind introduce ASIMOV-Agentic, banco di prova per la sicurezza dei robot autonomi che misura l'orchestrazione delle azioni sotto incertezza, il rifiuto delle chiamate a strumenti pericolose e il rilevamento di una persona nelle vicinanze con arresto in tempo. Carolina Parada, che guida la divisione robotica, riconosce che la questione diventa più pressante man mano che i robot escono dai laboratori, mentre i robot delle dimostrazioni restano addestrati per compiti specifici con teleoperazione, esempi video e simulazioni.
- **2026-10-28** — Gemini Robotics Embodied Reasoning 2 diventa disponibile su Google Cloud, portando nel servizio il ragionamento spazio-temporale e la pianificazione su orizzonti lunghi per i robot.




## Collegamenti

- [[gemini-3-5-flash]]
- [[google-deepmind]]
- [[physical-ai]]
- [[sharpa-robotics]]
- [[index]]
