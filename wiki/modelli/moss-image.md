---
title: "MOSS-Image"
category: modello
tags: [diffusione, open-weight, testo-in-immagine, layout, cina]
related_puntate: []
created: 2026-10-27
updated: 2026-10-27
sources: [raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]
---

# MOSS-Image

## Introduzione

Modello text-to-image a pesi aperti da 5 miliardi di parametri di [[openmoss]], pubblicato il 16 ottobre 2026 in due versioni con licenza Apache 2.0: SFT per generare immagini, Base per addestrare LoRA e fare fine-tuning. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]

## Capacità e performance

- Il prompt può essere scritto in prosa, in tag in stile booru oppure come documento JSON: ogni voce di `items` porta etichetta, descrizione, riquadro di posizione (bbox in formato yxyx, coordinate relative al centro dell'immagine) e, per le scritte, il testo esatto da stampare. Il prompt può arrivare a 4.000 token. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]
- Le scritte rese bene sono in inglese e in cinese; per l'italiano non esiste una valutazione pubblicata. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]
- Nel report gli autori dichiarano il 96,3 per cento di copertura media del testo su LongLongTextBench e il secondo posto su RealLayoutArena fra i sistemi valutati, ma entrambi i benchmark li hanno costruiti loro e i modelli di confronto non sono nominati nell'abstract. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]

## Requisiti

- Pipeline ufficiale con Python 3.10 o superiore, GPU NVIDIA con CUDA, PyTorch 2.9 o successivo, diffusers 0.38 e transformers 5.3; valori predefiniti a 50 passi con campionatore Euler, guidance 3, shift 5 e salto del ramo negativo al layer 22, con immagini in dimensioni multipli di 16. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]
- La scheda non indica una memoria video minima; il supporto in [[comfyui]] è nativo dal 16 ottobre e il repository segnala il lancio per SGLang e vLLM-Omni. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]
- Chi non ha una GPU può usare il Playground della MOSI API Platform, attivo dal 20 ottobre, con prezzi non pubblicati. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]

## Timeline delle notizie

- **2026-10-16** — [[openmoss]] pubblica MOSS-Image in due versioni Apache 2.0, SFT e Base, con controllo del layout tramite prompt JSON e coordinate: 5 miliardi di parametri, testo lungo in inglese e cinese, supporto nativo in ComfyUI dallo stesso giorno e nessuna valutazione indipendente sui benchmark dichiarati. [Fonte: raw/pillitteri/pillitteri20261027-moss-image-open-source-base-sft.md]

## Collegamenti

- [[openmoss]]
- [[comfyui]]
- [[qwen-image]]
- [[open-source]]
- [[index]]
