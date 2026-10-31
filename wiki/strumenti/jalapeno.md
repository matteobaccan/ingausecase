---
title: "Jalapeño"
category: strumento
tags: [3nm, broadcom, chip, hbm4, inferenza, openai]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
sources: [raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]
---

# Jalapeño

## Introduzione

Primo chip custom di [[openai]] per l'inferenza, progettato insieme a Broadcom e presentato mercoledì 24 giugno 2026: l'obiettivo dichiarato è ridurre la dipendenza dalle GPU [[nvidia]] e abbattere i costi di esecuzione dei modelli, perché l'inferenza è la fase che si ripete miliardi di volte al giorno e dove si accumulano i costi reali di un servizio AI di massa. L'architettura riduce lo spostamento dei dati e bilancia calcolo, memoria e rete per avvicinare l'utilizzo reale al picco teorico, cioè più lavoro utile per ogni watt consumato. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]

## Funzionalità principali

- A Hot Chips 2026 OpenAI ha mostrato i primi risultati: 13,4 petaflop in calcolo a 4 bit, 232 GB di memoria HBM4 e 15,4 TB/s di banda, con una latenza fino a 3,6 volte inferiore rispetto a Nvidia GB300, secondo i dati riportati da IEEE Spectrum. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]
- Il dettaglio più citato riguarda il software: su un kernel di attenzione latente multi-testa di DeepSeek i modelli AI interni di OpenAI hanno portato le prestazioni dallo 0,31 all'88,94 per cento del picco teorico in circa quaranta ore, e nella progettazione fisica l'AI ha ridotto del 10 per cento l'area delle unità di moltiplicazione matriciale rispetto a una base umana ottimizzata. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]
- Tempi dichiarati: meno di venti mesi dall'idea al primo silicio e nove mesi dal primo RTL al tape-out, con un processo di co-sviluppo hardware-software in cui gli stessi modelli dell'azienda hanno accelerato parti della progettazione. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]
- Il limite lo mette Richard Ho, vicepresidente hardware di OpenAI: il design di un chip non si automatizza del tutto, servono un team piccolo (meno di cento persone) e tempi stretti. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]

## Disponibilità

- Non è ancora in produzione di massa: è un chip in fase di test pensato per i carichi di inferenza di OpenAI, con dispiegamento previsto a partire dalla fine del 2026 come primo tassello di una piattaforma di calcolo multi-generazione che combina gli acceleratori di OpenAI, il silicio e le tecnologie di rete di Broadcom e l'esperienza di system integration di Celestica. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]

## Timeline delle notizie

- **2026-06-27** — OpenAI presenta Jalapeño, il primo chip custom per l'inferenza costruito con Broadcom: progetto pronto per la fabbricazione in nove mesi e meno di venti dall'idea al primo silicio, con i modelli interni usati per accelerare il design e un dispiegamento previsto dalla fine del 2026. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]
- **2026-09-20** — A Hot Chips 2026 arrivano i primi numeri: 13,4 petaflop a 4 bit, 232 GB di HBM4, 15,4 TB/s di banda e latenza fino a 3,6 volte inferiore a Nvidia GB300, con un kernel di attenzione latente multi-testa di DeepSeek portato dallo 0,31 all'88,94 per cento del picco teorico in circa quaranta ore dai modelli interni di OpenAI. [Fonte: raw/pillitteri/pillitteri20260627-openai-jalapeno-chip-custom-inferenza-broadcom.md]

## Collegamenti

- [[nvidia]]
- [[openai]]
- [[index]]
