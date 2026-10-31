---
title: "DeepInfer"
category: strumento
tags: [deepseek, inferenza, open-source, apache-2.0, cina]
related_puntate: []
created: 2026-10-20
updated: 2026-10-21
---

# DeepInfer

## Introduzione

Motore di inferenza di [[deepseek]], pubblicato su GitHub il 20 ottobre 2026 con licenza Apache-2.0: il README lo presenta come il framework che alimenta i servizi di produzione dell'azienda, ma la prima release fa girare un solo modello, [[deepseek-v4-1-flash]], e soltanto in modalità offline.

## Funzionalità principali

- È costruito soprattutto sopra [[vllm]], con spunti da SGLang e TensorRT-LLM, e raccoglie per la prima volta in un unico motore le librerie già pubblicate da DeepSeek: FlashMLA, DeepGEMM, DeepEP, TileKernels, DeepSelect e alcuni kernel in TileLang.
- Porta parallelismo con Attention DP, CP bilanciato per i contesti lunghi, MoE EP con EPLB, decodifica speculativa DSpark con verifica schedulata per confidenza (massimo 5 token di bozza), SWA bounded replay su 140 token, scheduling asincrono, inferenza batch-invariant e campionamento deterministico (solo Nvidia), più output strutturati su regex, JSON o EBNF.
- Dichiara 89.500 token al secondo per GPU in prefill con lotti da 65.536 token su 4 GPU Nvidia SM100 e fino a circa 26.300 token al secondo per GPU in decode su 64 GPU con 256 richieste, accettando che ogni utente veda 103 token al secondo invece di 325.

## Installazione e uso

- Si compila solo su Linux con GCC 13 o successivo e Python 3.12, più CUDA 13 per Nvidia o CANN 9.2 per Huawei; servono GPU Nvidia SM100 oppure NPU Ascend 950, quindi hardware da data center.
- Mancano i pezzi che trasformano un motore in un servizio: cache KV, separazione tra prefill e decode su macchine diverse e bilanciamento del carico tra le repliche, quindi con il solo repository non si apre un'API concorrente a quella di DeepSeek.
- La cartella `eval` porta gli script per AIME 2026, HLE e GPQA Diamond sul percorso offline, con Pass@1 come metrica.

## Repository

- Il repository risulta creato il 16 ottobre e il 20 ottobre contava 4.074 stelle, 307 fork e 35 segnalazioni aperte.

## Azienda/autore

- [[deepseek]]

## Modelli supportati

- [[deepseek-v4-1-flash]]

## Timeline delle notizie

- **2026-10-20** — DeepSeek pubblica DeepInfer con licenza Apache-2.0: il motore supporta solo DeepSeek-V4.1-Flash e solo in modalità offline, richiede Nvidia SM100 o Huawei Ascend 950 e arriva a 4.074 stelle il giorno del primo commit pubblico. In produzione il motore serve 155 trilioni di token al giorno con 38 dollari di ricavo per ora-GPU ai prezzi off-peak, e anche affittando GPU B300 a 7 dollari l'ora il margine lordo resta sopra l'82 per cento.

## Collegamenti

- [[deepseek]]
- [[deepseek-v4-1-flash]]
- [[vllm]]
- [[huawei]]
- [[tilelang]]
- [[index]]
