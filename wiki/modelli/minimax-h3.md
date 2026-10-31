---
title: "H3"
category: modello
tags: [cina, consumer, efficienza, locale, minimax, multimodale, open-source, open-weight, video, video-ai]
related_puntate: [20260801, 20260804, 20260805, 20260806, 20260810, 20260825, 20260826, 20260828, 20260830, 20260831, 20260901, 20260903, 20260904, 20260905, 20260908, 20260915, 20261001, 20261005, 20261013]
created: 2026-08-12
updated: 2026-10-29
sources: [raw/puntate/ainews20260905.md, raw/puntate/ainews20260831.md, raw/puntate/ainews20260830.md, raw/puntate/ainews20260801.md, raw/puntate/ainews20260804.md, raw/puntate/ainews20260805.md, raw/puntate/ainews20260806.md, raw/puntate/ainews20260810.md, raw/puntate/ainews20260825.md, raw/puntate/ainews20260826.md, raw/puntate/ainews20260828.md, raw/puntate/ainews20260901.md, raw/puntate/ainews20260903.md, raw/puntate/ainews20260904.md, raw/puntate/ainews20260908.md, raw/puntate/ainews20260915.md, raw/puntate/ainews20261001.md, raw/puntate/ainews20261005.md, raw/puntate/ainews20261013.md, raw/pillitteri/pillitteri20260801-minimax-h3-video-ai-2k-pesi-aperti.md, raw/pillitteri/pillitteri20261029-migliori-generatori-video-ai-confronto.md]
---

# H3

## Introduzione

Modello multimodale generativo di MiniMax con architettura unificata per testo, immagini, video e audio: video fino a 15 secondi a risoluzione 2K con audio stereo nativo, pesi aperti.

## Capacità e performance

- Da MiniMax arriva H3, modello multimodale generativo con architettura unificata per testo, immagini, video e audio: genera video fino a 15 secondi a risoluzione 2K con audio stereo nativo; pesi aperti e disponibile su fal.
- H3 di MiniMax genera video da testo, immagini, audio e video come contesto unico, con clip fino a quindici secondi a duemila pixel e ventiquattro FPS con audio stereo già nel file.
- ModelScope permette di far girare MiniMax-H3 in locale anche su Mac, con versione quantizzata a quattro bit via DiffSynth-Studio, minimo otto gigabyte di VRAM e funzionamento su Mac da sedici giga in modalita' estrema.

## Azienda di riferimento

- [[fal]]
- [[minimax]]
- [[modelscope]]

## Strumenti correlati

- [[clipproj]]

## Timeline delle notizie

- **2026-08-01** — Da MiniMax arriva H3, modello multimodale generativo con architettura unificata per testo, immagini, video e audio: genera video fino a 15 secondi a risoluzione 2K con audio stereo nativo; pesi aperti e disponibile su fal. [Fonte: raw/puntate/ainews20260801.md]
- **2026-08-03** — I pesi sono stati pubblicati su Hugging Face: in locale il modello arriva a 768p mentre il 2K resta riservato all'API, e la licenza esclude Unione europea, Regno Unito, Corea del Sud e Stati Uniti, quindi in Italia i pesi non si possono usare senza un permesso separato dell'azienda. L'app Hailuo e l'API restano invece utilizzabili. [Fonte: raw/pillitteri/pillitteri20260801-minimax-h3-video-ai-2k-pesi-aperti.md]

- **2026-10-29** — Nel confronto di fine ottobre è l'unico generatore che dichiara dialoghi stabili in italiano, tra le 11 lingue della scheda ufficiale, con clip da 4 a 15 secondi e audio stereo a 32 kHz: il listino a consumo chiede 0,13 dollari al secondo in 2K e 0,08 a 768p, con la variante Lite a 0,04, quindi una clip 2K da 15 secondi costa 1,95 dollari. [Fonte: raw/pillitteri/pillitteri20261029-migliori-generatori-video-ai-confronto.md]



- **2026-08-04** — H3 di MiniMax genera video da testo, immagini, audio e video come contesto unico, con clip fino a quindici secondi a duemila pixel e ventiquattro FPS con audio stereo già nel file. [Fonte: raw/puntate/ainews20260804.md]
- **2026-08-05** — ModelScope permette di far girare MiniMax-H3 in locale anche su Mac, con versione quantizzata a quattro bit via DiffSynth-Studio, minimo otto gigabyte di VRAM e funzionamento su Mac da sedici giga in modalita' estrema. [Fonte: raw/puntate/ainews20260805.md]
- **2026-08-06** — MiniMax H3 gira su hardware consumer: validato su RTX 3060 da duecentottanta dollari, sedici GB di VRAM sufficienti e MacBook offline funzionante, peso open source. [Fonte: raw/puntate/ainews20260806.md]
- **2026-08-10** — ClipProj riduce MiniMax H3 da quindici virgola sette GB a cinque virgola due GB di VRAM sostituendo il text encoder con Qwen3-VL-4B, con qualche perdita di qualita'. [Fonte: raw/puntate/ainews20260810.md]
- **2026-08-25** — Custom nodes per ComfyUI generano video MiniMax-H3 lunghi fino a centoventi secondi con audio sincronizzato da un singolo prompt. [Fonte: raw/puntate/ainews20260825.md]

- **2026-08-26** — L'ecosistema MiniMax H3 cresce: un indice raccoglie tutto ciò che è stato costruito attorno a H3, da setup locali ComfyUI da ventiquattro GB di VRAM a deployment enterprise con SGLang e vLLM-Omni, con guide di quantizzazione, stack multi-GPU, skill per agenti nativi e nodi di contesto motion multi-shot; nella pipeline Flova H3 gestisce le scene live action. [Fonte: raw/puntate/ainews20260826.md]
- **2026-08-30** — MiniMax H3 Fast, versione distillata di H3 con accelerazioni fino a quattordici volte, e supporto per H3 FastVideo aggiunto a ComfyUI da Kijai. Il modello H3 è stato ottimizado da Fal per generare video più velocemente di quanto si possa guardarli. [Fonte: raw/puntate/ainews20260830.md]
- **2026-08-28** — MiniMax H3 è stato ottimizado da NVIDIA con Nvidia Super Acceleration: generazione video fino a tre volte più veloce (166 contro 550 secondi) su RTX 4060 Ti 16 GB, senza upscaling LTX; altri test su GPU più potenti in corso. [Fonte: raw/puntate/ainews20260828.md]
- **2026-08-31** — fal ha reso gratuito MiniMax H3 Max: cinque generazioni al giorno senza registrazione, clip fino a quindici secondi, velocità estrema. [Fonte: raw/puntate/ainews20260831.md]
- **2026-09-01** — MiniMax Fast H3: generazione video full HD in cinque minuti su RTX 470. Base H3 ventistep richiedeva sessantaquattro minuti, LightX due V quattrostep quattordici, Kijai Fast H3 VSA solo cinque. [Fonte: raw/puntate/ainews20260901.md]

- **2026-09-04** — Tecnica con MiniMax H3: girare una stanza a 360° in un’unica ripresa continua prima di estrarre i singoli tagli migliora drasticamente la coerenza della scena. [Fonte: raw/puntate/ainews20260904.md]
- **2026-09-05** — H3 gira ora interamente in locale: modelli di sessantacinque gigabyte, dodici gigabyte di VRAM su RTX 4070 Ti, con l’intero pipeline text-to-video eseguito dentro ComfyUI senza connessioni al cloud. [Fonte: raw/puntate/ainews20260905.md]
- **2026-09-03** — Video Delta Net, sistema hybrid attention per text-to-video live con qualità quasi lossless, accelera H3 di settantacinque-novanta volte, generando quattordici secondi di video a settecentosessantotto pixel in undici secondi su otto GPU NVIDIA B duecento; checkpoint, codice di training e inference rilasciati come open source. [Fonte: raw/puntate/ainews20260903.md]
- **2026-09-08** — Playtime-AI ha addestrato un LoRA per MiniMax H3 basato su Sydney Sweeney: 155 MB su Hugging Face, funziona come patch di identità (H3 genera movimenti, espressioni, lip-sync e suono, il LoRA aggiunge le caratteristiche fisiche). Playtime-AI ha già caricato 70 modelli simili di personaggi pubblici. [Fonte: raw/puntate/ainews20260908.md]

- **2026-09-15** — La community open source accelera MiniMax H3: FastH3 con distillazione a quattro step, Sol-H3 che genera quindici secondi di video a settecentosessantotto pixel più audio in sei secondi e sei su otto GPU B300, VDN con attenzione ripensata per l'inferenza e varie LoRA accelerate. [Fonte: raw/puntate/ainews20260915.md]
- **2026-10-01** — MiniMax H3 introduce RefMod, tecnica che fissa la faccia di un personaggio senza LoRA training: un file da circa un megabyte creato in pochi minuti mantiene la faccia coerente nei video generati. [Fonte: raw/puntate/ainews20261001.md]
- **2026-10-05** — FreeVideo porta H3 su PC con otto gigabyte di VRAM, integrazione ComfyUI, LoRA e workflow personalizzati adattati all'hardware. [Fonte: raw/puntate/ainews20261005.md]
- **2026-10-13** — StreamRender-H3 usa H3 Ref2VA come motore di generazione di un renderer neurale streaming real-time: due step di denoising, 24 frame al secondo e 273 millisecondi per chunk su otto GPU GB200, con lo stesso mondo interattivo e aspetti visivi completamente diversi cambiando immagine di riferimento e prompt. [Fonte: raw/puntate/ainews20261013.md]










## Collegamenti

- [[comfyui]]
- [[clipproj]]
- [[flux-3]]
- [[minimax]]
- [[modelscope]]
- [[video-delta-net]]
- [[refmod]]
- [[sglang]]
- [[index]]
