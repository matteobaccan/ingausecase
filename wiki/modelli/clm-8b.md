---
title: "CLM-8B"
category: modello
tags: [decisioni, latenza, open-weight, reasoning]
related_puntate: [20260924, 20260927]
created: 2026-09-25
updated: 2026-09-28
sources: [raw/puntate/ainews20260924.md, raw/tldr/tldr20260925.md, raw/puntate/ainews20260927.md, raw/pillitteri/pillitteri20260928-clm-8b-nvidia-stanford-jev.md]
---

# CLM-8B

## Introduzione

Contrastive Language Model da otto miliardi di parametri presentato il 24 settembre 2026 come alternativa a [[jev]] per le decisioni rapide degli agenti: è pre-addestrato su dati internet-scale e offre inferenza fino a nove volte più veloce di Jev, con prestazioni comparabili su computer-use, gaming e tool-calling. [Fonte: raw/puntate/ainews20260924.md]

## Capacità e performance

- Con fine-tuning leggero raggiunge l'ottantuno punto sei per cento su DeepSWE e l'ottantasette punto sei su Terminal-Bench 2.1. [Fonte: raw/puntate/ainews20260924.md]

## Timeline delle notizie

- **2026-09-24** — Arriva CLM-8B, Contrastive Language Model pre-addestrato su dati internet-scale: inferenza fino a nove volte più veloce di Jev con prestazioni comparabili su computer-use, gaming e tool-calling, e con fine-tuning leggero ottantuno punto sei per cento su DeepSWE e ottantasette punto sei su Terminal-Bench 2.1. È pre-addestrato su 60 milioni di coppie Q&A Nemotron, mid-trained su 30 milioni di negativi sintetici e post-trained su 1 milione di traiettorie agentiche, e stabilisce un nuovo stato dell'arte sui benchmark agentici di coding. [Fonte: raw/puntate/ainews20260924.md] [Fonte: raw/tldr/tldr20260925.md]
- **2026-09-27** — La puntata attribuisce il lavoro a [[stanford]] e [[nvidia]] e ne descrive il meccanismo: invece di generare token per token, CLM codifica la situazione corrente e ogni azione candidata come vettori e sceglie il più vicino, con i vettori delle azioni pre-calcolati e cachati. La velocità dichiarata sale fino a tredici volte quella di [[jev]], con sedici millisecondi contro centocinquanta sul dinosaur run, quattro volte più veloce su Super Mario e circa cinque volte su WikiRacing; il limite è che può solo scegliere tra opzioni date, non inventare nuove azioni. [Fonte: raw/puntate/ainews20260927.md]

- **2026-09-28** — Dettagli sul rilascio del 23 settembre: codice e pesi sono pubblici sotto licenza Apache 2.0, il repository ha 2.194 stelle al 28 settembre e l'installazione avviene con `pip install contrastive-lm`, con un client che espone un'API compatibile con quella di [[typesafe-ai]]. L'architettura è un [[qwen|Qwen3-8B]] congelato usato solo come motore di comprensione, sopra cui poggiano due teste di proiezione da circa 20 milioni di parametri ciascuna — le uniche parti addestrate — con la perdita InfoNCE; gli autori rivendicano per questo progetto l'etichetta di Contrastive Language Model e non quella di architettura predittiva alla JEPA di [[yann-lecun]], perché il modello non predice stati futuri ma sceglie tra opzioni note. Il prossimo passo annunciato è CLM-35B-A3B, multimodale e a esperti misti, previsto per l'inizio di ottobre 2026. [Fonte: raw/pillitteri/pillitteri20260928-clm-8b-nvidia-stanford-jev.md]

## Collegamenti

- [[agenti-ai]]
- [[deep-swe]]
- [[jev]]
- [[nvidia]]
- [[stanford]]
- [[terminalbench]]
- [[index]]
