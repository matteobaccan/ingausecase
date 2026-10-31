---
title: "Heretic"
category: strumento
tags: [abliteration, locale, open-source]
related_puntate: [20260714]
created: 2026-08-12
updated: 2026-10-25
sources: [raw/puntate/ainews20260714.md, raw/pillitteri/pillitteri20260822-qwen-senza-censura-abliterated-heretic.md, raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md, raw/pillitteri/pillitteri20261004-installare-modello-uncensored-locale-mac-windows.md, raw/pillitteri/pillitteri20261025-hugging-face-banna-modelli-uncensored-kimi-k27-code.md]
---

# Heretic

## Introduzione

Repository open source che rimuove la censura dai modelli in quarantacinque minuti, con un comando e nessuna configurazione.

## Funzionalità principali

- Heretic è un repository che rimuove la censura dai modelli in quarantacinque minuti con un comando e nessuna configurazione: funziona con Llama, Qwen e Gemma, tutto in locale.
- È il progetto dello sviluppatore noto come p-e-w, con licenza AGPL-3.0, e ha superato le 28.000 stelle su GitHub in meno di un anno: con questo strumento la community ha già pubblicato oltre 5.000 modelli decensurati. [Fonte: raw/pillitteri/pillitteri20260822-qwen-senza-censura-abliterated-heretic.md]
- Automatizza l'abliteration con un ottimizzatore di parametri basato su Optuna e sull'algoritmo TPE: cerca la configurazione che minimizza insieme i rifiuti residui e la divergenza di Kullback-Leibler rispetto al modello originale. Su Gemma-3-12B l'originale rifiuta 97 richieste dannose su 100, le abliteration manuali scendono a 3 con divergenza 1,04 (mlabonne) e 0,45 (huihui-ai), e Heretic ottiene lo stesso 3 con divergenza 0,16: stessa soppressione del rifiuto, quasi un terzo del danno. [Fonte: raw/pillitteri/pillitteri20260822-qwen-senza-censura-abliterated-heretic.md]
- Si installa da PyPI con `pip install -U heretic-llm` e si lancia con un comando (`heretic Qwen/Qwen3-4B-Instruct-2507`), con l'opzione `--quantization bnb_4bit` per la poca VRAM e la variante `heretic-llm[research]` per analizzare i vettori residui strato per strato. Richiede Python 3.10 o superiore, PyTorch 2.2 o superiore e una GPU NVIDIA: su una RTX 3090 un Qwen3-4B viene processato in circa 20-30 minuti. [Fonte: raw/pillitteri/pillitteri20260822-qwen-senza-censura-abliterated-heretic.md]

## Modelli supportati / correlati

- [[deepseek-v4-1-flash-abliterated]]
- [[superglm-5-2-abliterated]]
- [[huihui-qwen3-8-27b-abliterated-gguf]]
- [[superqwen3-8-27b-abliterated]]

## Timeline delle notizie

- **2026-07-14** — Heretic è un repository che rimuove la censura dai modelli in quarantacinque minuti con un comando e nessuna configurazione: funziona con Llama, Qwen e Gemma, tutto in locale. [Fonte: raw/puntate/ainews20260714.md]
- **2026-08-22** — Guida al meccanismo dell'abliteration, la tecnica che toglie la capacità fisica di rifiutare senza riaddestrare nulla: il comportamento di rifiuto è mediato in gran parte da una singola direzione nello spazio delle attivazioni (la *refusal direction* individuata dal lavoro di Arditi e colleghi del 2024), e rendere ortogonali a quella direzione le matrici di proiezione dell'attenzione e di discesa del blocco MLP elimina la strada neurale del rifiuto, lasciando intatte le conoscenze del modello. Heretic non aggiunge nulla di diverso dall'abliteration manuale se non l'automatizzazione del dosaggio; per chi vuole solo usare i modelli senza fabbricarli, il canale di riferimento è il profilo huihui-ai su Hugging Face, con Ollama e LM Studio come vie più semplici su Mac e Windows. Restano i rischi dichiarati: un modello senza filtri è a doppio uso, e scaricare pesi da profili sconosciuti espone a casi documentati come il GGUF malevolo di Bleeding Llama. [Fonte: raw/pillitteri/pillitteri20260822-qwen-senza-censura-abliterated-heretic.md]
- **2026-09-13** — Il caso di [[deepseek-v4-1-flash]] mostra le due strade dell'abliteration a confronto: quella a livello di pesi (dealignai, distributedcognition, s-zaizen) scrive nel file la rimozione dei rifiuti e non si torna indietro, mentre il **control vector** di Matt Suiche, un file da 800 KB applicato solo durante l'inferenza, lascia il modello ufficiale intatto ed è reversibile. Il secondo è la scelta migliore per chi studia i rifiuti, perché misura l'effetto senza distruggere l'originale, il primo per chi vuole solo un modello sbloccato da usare. Suiche avverte anche che il vettore ha un comportamento non lineare: alzare alpha oltre una certa soglia riduce l'effetto invece di aumentarlo. Anche qui un GGUF passa da [[heretic]] per girare su [[ds4]]. [Fonte: raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md]
- **2026-10-04** — Una guida all'installazione locale cita Heretic (33.116 stelle, licenza AGPL-3.0) come lo strumento che automatizza l'abliteration e cerca il compromesso tra rifiuti residui e distanza dal modello originale. [Fonte: raw/pillitteri/pillitteri20261004-installare-modello-uncensored-locale-mac-windows.md]
- **2026-10-25** — Il ritmo delle versioni senza rifiuti non si è fermato con i primi ritiri: tra il 18 e il 24 ottobre nascono 454 repository con abliterated, uncensored o heretic nel nome, 280 dei quali in un formato di conversione come GGUF, MLX, FP8 o FP4, e da inizio settembre le stesse ricerche ne contano più di 2.700, di cui 158 solo per GLM-5.3. [Fonte: raw/pillitteri/pillitteri20261025-hugging-face-banna-modelli-uncensored-kimi-k27-code.md]







## Collegamenti

- [[superglm-5-2-abliterated]]
- [[index]]

