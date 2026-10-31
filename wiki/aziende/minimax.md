---
title: "MiniMax"
category: azienda
tags: [minimax, cina, llm, multimodale, video, video-ai]
related_puntate: [20260801, 20260804, 20260805, 20260827, 20260828, 20260830, 20260901, 20260902, 20260904, 20260905, 20260908, 20261001, 20261002, 20261003, 20261013]
created: 2026-08-12
updated: 2026-10-23
sources: [raw/puntate/ainews20260905.md, raw/puntate/ainews20260830.md, raw/puntate/ainews20260801.md, raw/puntate/ainews20260805.md, raw/puntate/ainews20260827.md, raw/puntate/ainews20260901.md, raw/puntate/ainews20260902.md, raw/puntate/ainews20260904.md, raw/puntate/ainews20260908.md, raw/puntate/ainews20260804.md, raw/puntate/ainews20260828.md, raw/pillitteri/pillitteri20260601-minimax-m3-open-weights-coding-1m-context.md, raw/puntate/ainews20261001.md, raw/puntate/ainews20261002.md, raw/puntate/ainews20261003.md, raw/puntate/ainews20261013.md, raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md, raw/pillitteri/pillitteri20261023-minimax-m3-1-flash-pesi-hugging-face-licenza.md]
---

# MiniMax

## Introduzione

Azienda cinese di modelli multimodali (audio, video e agentici), attiva anche con modelli open-weight come M2.7. Nel periodo ha rilasciato H3, modello generativo unificato con video fino a 15 secondi a risoluzione 2K e audio stereo nativo.

## Modelli

- [[minimax-h3]]
- [[minimax-m3]]

## Strumenti

- [[minimax-agent]]

## Timeline delle notizie

- **2026-06-01** — Rilascia MiniMax M3, presentato come il primo open weights con coding di frontiera, contesto da un milione di token e multimodalità nativa, con pesi e report tecnico promessi entro circa dieci giorni. Il titolo alla Borsa di Hong Kong, quotato con il ticker 00100.HK, sale di oltre il 5% fino a 907,5 dollari di Hong Kong e poi perde il 12,38% nella stessa mattinata con 1,49 miliardi di dollari di Hong Kong di scambi: il classico "sell the news" dopo settimane di attesa. [Fonte: raw/pillitteri/pillitteri20260601-minimax-m3-open-weights-coding-1m-context.md]
- **2026-08-01** — Ha rilasciato H3, modello multimodale generativo con architettura unificata per testo, immagini, video e audio: genera video fino a 15 secondi a risoluzione 2K con audio stereo nativo; pesi aperti e disponibile su fal. [Fonte: raw/puntate/ainews20260801.md]
- **2026-08-04** — MiniMax ha rilasciato H3 come open source, modello che genera video da testo, immagini, audio e video come contesto unico. [Fonte: raw/puntate/ainews20260804.md]
- **2026-08-05** — MiniMax ha pubblicato la variante uncensored del modello video H3, costruita per creator e studi indipendenti, senza filtri. [Fonte: raw/puntate/ainews20260805.md]

- **2026-08-27** — MiniMax H3 Director Cut Studio è un editor video locale per H3: timeline stile Premiere, gestisce shot e prompt e si integra con ComfyUI per generare video fino a centoventi secondi da un singolo prompt. [Fonte: raw/puntate/ainews20260827.md]

- **2026-08-30** — Arriva MiniMax H3 Fast, versione distillata di MiniMax H3 con accelerazioni fino a quattordici volte; progetto in fase iniziale, senza versione quantizzata e con supporto solo text-to-video. [Fonte: raw/puntate/ainews20260830.md]
- **2026-08-28** — Comfy diventa il primo distributore commerciale delle licenze per i modelli generativi di MiniMax: quasi venti milioni di download open weight tramite Comfy, ora ottenibile licenza commerciale completa (audio, musica, video) con piano Professional ed Enterprise. [Fonte: raw/puntate/ainews20260828.md]
- **2026-09-01** — MiniMax H3 Max ora offre quindici generazioni giornaliere gratuite al login, clip da dieci secondi, modalità T2V e I2V. MiniMax Fast H3 genera video full HD in cinque minuti su RTX 470. ComfyUI-Spectrum-MiniMax-H3 accelera la generazione H3 senza training. [Fonte: raw/puntate/ainews20260901.md, raw/puntate/ainews20260902.md]
- **2026-09-02** — Un generatore di giochi interattivi (Video Con) costruito su H3Max: da script e immagini di prodotti produce giochi con ramificazioni narrative, latenza quasi zero, orientato anime galgame in realtime. [Fonte: raw/puntate/ainews20260902.md]
- **2026-09-03** — Video Delta Net, sistema hybrid attention open source per text-to-video live con qualità quasi lossless, accelera H3 di settantacinque-novanta volte; il modello di MiniMax è citato come base accelerata. Checkpoint, codice di training e inference rilasciati open source.
- **2026-09-05** — Minimax H3 gira ora in locale: modelli di sessantacinque gigabyte, dodici gigabyte di VRAM su RTX 4070 Ti, con text-to-video completo dentro ComfyUI eseguito in un’unica macchina, senza cloud. [Fonte: raw/puntate/ainews20260905.md]
- **2026-09-08** — Playtime-AI ha addestrato un LoRA per MiniMax H3 basato su Sydney Sweeney (155 MB su Hugging Face, patch di identità) e ha già caricato 70 modelli simili di personaggi pubblici. [Fonte: raw/puntate/ainews20260908.md]
- **2026-09-04** — BlendiByl ha costruito il primo servizio di streaming video completamente IA usando MiniMax H3 Max Turbo: si possono guardare film interi e crearli. Inoltre, tecnica con MiniMax H3: girare una stanza a 360° in un’unica ripresa continua prima di estrarre i singoli tagli migliora drasticamente la coerenza della scena. [Fonte: raw/puntate/ainews20260904.md]
- **2026-10-01** — MiniMax introduce RefMod su H3: la tecnica fissa la faccia di un personaggio senza LoRA training, con un file da circa un megabyte creato in pochi minuti che mantiene la faccia coerente nei video generati. [Fonte: raw/puntate/ainews20261001.md]
- **2026-10-03** — FreeVideo porta MiniMax H3 e Video DeltaNet su un laptop con otto gigabyte di VRAM più sedici di RAM, con integrazione ComfyUI, LoRA e workflow personalizzati. [Fonte: raw/puntate/ainews20261003.md]
- **2026-10-13** — MiniMax trasforma H3 Ref2VA in un renderer neurale streaming real-time con StreamRender-H3: due step di denoising, ventiquattro frame al secondo e circa 273 millisecondi per chunk su otto GPU GB200, con il motore di gioco che gestisce fisica e interazioni mentre H3 genera le immagini. [Fonte: raw/puntate/ainews20261013.md]
- **2026-10-19** - MiniMax lancia [[minimax-m3-1-flash|M3.1 Flash]] a 0,15 dollari per milione di token in ingresso e 0,60 in uscita, con cache a 0,015, contesto da un milione di token, cinque livelli di sforzo e pesi annunciati per il 23 ottobre senza licenza n\u00e9 dimensioni; l'azienda conferma che Space Bunny era una versione precedente del modello. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- **2026-10-23** — Pubblica i pesi di [[minimax-m3-1-flash|M3.1 Flash]] su Hugging Face con licenza MiniMax Community, 252,4 GB di file e 23 miliardi di parametri attivi: uso non commerciale gratuito, dicitura e notifica per quello commerciale, autorizzazione scritta oltre i 20 milioni di dollari di ricavi annui. Nelle stesse ore un account affiliato alla CCTV, ripreso dal South China Morning Post, sostiene che DeepSeek e MiniMax avrebbero completato le procedure di registrazione per l'export previste dalle nuove regole cinesi, ancora in bozza. [Fonte: raw/pillitteri/pillitteri20261023-minimax-m3-1-flash-pesi-hugging-face-licenza.md]
















## Collegamenti

- [[minimax-agent]]
- [[minimax-h3]]
- [[minimax-h3-director-cut-studio]]
- [[minimax-h3-fast]]
- [[minimax-m3]]
- [[modelscope]]
- [[video-con]]
- [[refmod]]
- [[index]]
