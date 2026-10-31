---
title: "Jumper"
category: strumento
tags: [robotica, open-source, robot, cina, simulazione]
related_puntate: []
created: 2026-10-12
updated: 2026-10-12
---

# Jumper

## Introduzione

Robot esapode a forma di granchio (跳跳, Tiaotiao) di KingKong Technology, azienda di Pechino che produce encoder e servo oltre ai robot, reso open source su GitHub il 28 settembre 2026 con licenza Apache-2.0. Misura 400 x 400 x 200 millimetri, pesa 1,8 chilogrammi e ha 22 servo tattili proprietari con due encoder magnetici ciascuno.

## Funzionalità principali

- Calcolo su Rockchip RK3576 con otto core, NPU da 6 TOPS, 4 GB di memoria e 64 GB di storage; sensori: IMU a sei assi, dToF da 54 x 42 punti, camera da 5 megapixel e quattro microfoni; Wi-Fi 5 e Bluetooth 5.0, batteria rimovibile da 25,2 V e 3.000 mAh con ricarica USB-C PD 3.1 fino a 140 W.
- Il repository KingKongRobotics/jumper contiene il modello di simulazione MuJoCo con le mesh STL, l'addestramento per rinforzo con PPO costruito su mjlab e rsl_rl (MuJoCo Warp come motore fisico) e la catena di esportazione verso la scheda di bordo; al 12 ottobre conta 2.385 stelle e 232 fork, con un file CLAUDE.md, un AGENTS.md e una cartella di skill per [[claude-code]].
- Per addestrare e far muovere il robot in simulazione bastano Python da 3.10 a 3.13 e un portatile, anche senza GPU NVIDIA: il robot fisico non serve e per ora non si compra.

## Limiti

- Gli stessi autori dichiarano che l'inferenza sulla NPU non è ancora verificata su hardware reale e che il ciclo di controllo a 1 kHz non ha mai pilotato il bus dei motori; il salto di 400 millimetri del sito resta una dichiarazione dell'azienda, mentre nelle note di versione la simulazione misura 0,159 metri di elevazione netta.

## Timeline delle notizie

- **2026-10-11** — KingKong pubblica in open source Jumper, granchio da 40 cm e 1,8 kg con 22 giunti, toolkit completo di simulazione MuJoCo, addestramento PPO ed esportazione verso il robot, licenza Apache-2.0 e nessun disegno di produzione nel repository; dal 30 settembre un concorso con Douyin mette in palio 100 unità ingegneristiche, giudicate per il 60% sulla popolarità e per il 40% da una giuria.

## Collegamenti

- [[physical-ai]]
- [[claude-code]]
- [[open-source]]
- [[index]]
