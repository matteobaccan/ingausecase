---
title: "Qwen 3.8 27B"
category: modello
tags: [alibaba, llm, locale, open-weight]
related_puntate: [20260826, 20260827, 20260902, 20260907, 20261001]
created: 2026-08-26
updated: 2026-10-26
---

# Qwen 3.8 27B

## Introduzione

Modello della famiglia Qwen da ventisette miliardi di parametri, pensato per girare in locale su hardware consumer.

## Capacità e performance

- Genera scene Minecraft, città neon e siti web completi.
- In alcuni test ha battuto [[claude-opus-4-6]].
- È denso (27,78 miliardi di parametri, niente MoE), multimodale in ingresso su testo, immagini e video, con contesto nativo di 262.144 token estendibile fino a un milione con YaRN: un'attenzione ibrida in cui 48 delle 64 layer usano attenzione lineare e solo 16 attenzione piena porta la KV cache da 256 KB a 64 KB per token, così una sessione da 128.000 token occupa circa 8 GB di cache invece dei 32 GB di un'architettura densa classica.
- Le quantizzazioni Unsloth Dynamic 2.0 in formato GGUF vanno da 9,0 GB (UD-IQ2_XXS, con perdita di qualità visibile) a 53,8 GB (BF16): su 16 GB entrano interi UD-Q3_K_XL (13,4 GB) e IQ4_XS (15,7 GB), mentre il Q4_K_M da 17,1 GB richiede l'offload di qualche layer sulla CPU; la community misura 26-30 token al secondo a 4 bit su una RTX 3090 e circa 45 a Q5 su una RTX 5090.
- È rilasciato con licenza Apache 2.0 su Hugging Face e ModelScope e gira in locale senza restrizioni geografiche, il che per chi tratta dati sensibili semplifica il rispetto del GDPR perché i contenuti non lasciano la macchina.

## Disponibilità

- Locale: gira su GPU da otto GB con quantizzazione IQ4_XS, Q4 KV cache e settantamila token di contesto.
- Kaggle TPU: gira in BF16 completo su TPU gratuito Kaggle senza quantizzazione, circa 130 token/s in decode, 10.000 token/s in prefill e 262.000 token di contesto; esponibile come endpoint compatibile OpenAI per Claude Code, Codex e OpenCode.

## Azienda di riferimento

- [[qwen]]

## Strumenti correlati

- [[unsloth]]: fine-tuning gratuito in locale su ventiquattro GB di VRAM, una virgola cinque volte più veloce con cinquanta percento di VRAM in meno.

## Timeline delle notizie

- **2026-08-15** — Il team Qwen di Alibaba pubblica i pesi aperti di Qwen3.8-27B il 14 agosto alle 15:00 UTC: 27,78 miliardi di parametri in architettura densa e multimodale, licenza Apache 2.0 su Hugging Face e ModelScope, con le quantizzazioni Unsloth Dynamic 2.0 che scendono fino a 9 GB per farlo girare su una macchina da 16 GB. Su [[llama-cpp]] il flag `--jinja` non è opzionale e la sua assenza è la prima causa delle segnalazioni di quantizzazioni "rotte"; su Windows, macOS e Linux il percorso più rapido è LM Studio, che scarica il modello, riconosce da solo il template di chat e sfrutta la memoria unificata di Apple Silicon. Unsloth indica temperatura 0,7, top-p 0,80 e top-k 20 in modalità istruzioni e temperatura 1,0 con top-p 0,95 in modalità ragionamento; i benchmark ufficiali sono misurati a piena precisione e non si riproducono su una build a 4 bit.
- **2026-08-21** — Alibaba pubblica i benchmark ufficiali, forti per un modello aperto che gira in locale: 89,2 su GPQA Diamond per il ragionamento scientifico, 90,3 su LiveCodeBench v6, 61,7 su SWE-bench Pro e 73,0 su Terminal-Bench 2.1, terzo posto mondiale su CodeArena dietro solo ai grandi modelli chiusi e Artificial Analysis Intelligence Index di 52, con una variante FP8 ufficiale che dimezza la memoria senza perdite pratiche. Il confronto diretto è con [[muse-glimmer]]: Qwen3.8-27B dichiara di superarlo su tutti e otto i benchmark pur avendo tre miliardi di parametri in meno.
- **2026-08-22** — La famiglia è tra le più usate come base per i modelli "decensurati": i pesi di Qwen 3.8 27B circolano su Hugging Face con i suffissi *abliterated* o *uncensored*, e il canale più noto è il profilo huihui-ai, che mantiene versioni abliterated di quasi ogni Qwen recente con i file GGUF già pronti per [[llama-cpp]], LM Studio, Jan e [[ollama]]. L'abliteration non riaddestra il modello ma rende ortogonali alla *refusal direction* alcune matrici del transformer, e con lo strumento [[heretic]] l'operazione è accessibile a chi sappia lanciare un comando da terminale.
- **2026-08-26** — Qwen 3.8 27B gira in locale su GPU da otto GB (IQ4_XS, Q4 KV cache, settantamila token di contesto): genera scene Minecraft, città neon e siti web completi, e in alcuni test ha battuto Claude Opus 4.6.

- **2026-08-27** — Versioni MLX quantizzate di Qwen 3.8 27B per Mac: dodici virgola sette gigabyte, ottimizzate per girare su macchine da sedici gigabyte.
- **2026-09-07** — Qwen 3.8 27B gira in BF16 completo su TPU gratuito Kaggle senza quantizzazione: circa 130 token/s in decode, 10.000 token/s in prefill, 262.000 token di contesto, esponibile come endpoint compatibile OpenAI per Claude Code, Codex e OpenCode.

- **2026-08-25** — Qwen 3.8 27B quantizzato a 3 bit è uno dei due modelli locali di [[portable-computer]] di [[perplexity]]: circa 17,4 GB di download e 32 GB di RAM richiesti.
- **2026-09-01** — HYBRID COMPUTE su Mac usa tre modelli locali tra cui Qwen 3.8 27B riaddestrato da Perplexity con il nome PPLX Qwen 3.8 27B, scelto di default.
- **2026-09-14** — La versione post-addestrata da Perplexity per [[portable-computer]] arriva già pronta nell'app Windows, ottimizzata per le GPU RTX.
- **2026-10-01** — SGLang trasforma Qwen3.8-27B in un modello multimodale di decisione: batte l'élite dei quattro e il campione di Pokémon FireRed con decisioni sotto i cento millisecondi dallo stato di gioco live, sfruttando l'endpoint nativo /v1/decisions che trasforma LLM e VLM in modelli di classificazione e scoring.
- **2026-10-24** — Il laboratorio cinese Nanbeige pubblica [[nanbeige-4-3-33b]], modello open da 33,1 miliardi di parametri con licenza Apache 2.0 che nei test della sua scheda dichiara di superare questo modello in 18 prove su 20, con il distacco maggiore sul coding agentico (65,5 contro 42,5 su DeepSWE) e margini di pochi decimi quasi ovunque altrove; sono numeri del laboratorio, senza test di terzi.







## Collegamenti

- [[claude-opus-4-6]]
- [[celeris-magnus]]
- [[qwen]]
- [[qwen3-8-flash-next]]
- [[unsloth]]
- [[sglang]]
- [[index]]
