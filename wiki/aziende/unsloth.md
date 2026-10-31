---
title: "Unsloth"
category: azienda
tags: [unsloth, amd, efficienza, fine-tuning, libreria, llm, open-source, ottimizzazione, quantizzazione, startup, usa]
related_puntate: [20260513, 20260602, 20260604, 20260613, 20260616, 20260629, 20260715, 20260718, 20260721, 20260724, 20260728, 20260731, 20260826, 20260905, 20260929, 20261009, 20261010]
created: 2026-08-12
updated: 2026-10-29
sources: [raw/puntate/ainews20260905.md, raw/puntate/ainews20260513.md, raw/puntate/ainews20260602.md, raw/puntate/ainews20260604.md, raw/puntate/ainews20260613.md, raw/puntate/ainews20260616.md, raw/puntate/ainews20260629.md, raw/puntate/ainews20260715.md, raw/puntate/ainews20260718.md, raw/puntate/ainews20260721.md, raw/puntate/ainews20260724.md, raw/puntate/ainews20260728.md, raw/puntate/ainews20260731.md, raw/puntate/ainews20260826.md, raw/pillitteri/pillitteri20260815-qwen3-8-27b-locale-16gb-lm-studio-unsloth.md, raw/puntate/ainews20260929.md, raw/puntate/ainews20261009.md, raw/puntate/ainews20261010.md, raw/pillitteri/pillitteri20261029-unsloth-browser-use-qwen3-8-27b-locale.md]
---

# Unsloth

## Introduzione

Azienda open source specializzata in fine-tuning e quantizzazione efficiente di modelli. Nel periodo ha rilasciato Gemma 4 26B A4B QAT per GPU da 8 GB, ha firmato la lettera Open Weights e ha portato Inkling-Small, il più grande open model per dimensione, su hardware consumer.

## Modelli

- [[diffusiongemma]]
- [[gemma-4]]
- [[inkling-small]]
- [[kimi-k2-7-code]]

## Strumenti

- [[axolotl]]
- [[llama-factory]]
- [[nativ]]

## Persone chiave

- [[andrew-ng]]

## Timeline delle notizie

- **2026-05-13** — Unsloth ha aperto il fine-tuning di Gemma 4 gratis nel browser: notebook Colab, scegli modello e dataset, avvii, con barriera a zero. [Fonte: raw/puntate/ainews20260513.md]
- **2026-06-02** — Unsloth ha pubblicato una guida sull'uso di MCP con LLM locali, collegando Qwen3.6 e Gemma 4 per accesso controllato a strumenti, file e API con workflow automatizzati privati. [Fonte: raw/puntate/ainews20260602.md]
- **2026-06-04** — Unsloth ha reso Gemma 4 12B eseguibile localmente con soli otto GB di RAM tramite Dynamic GGUF, con immagini, audio e duecentocinquantasei K di contesto; disponibile anche su Unsloth Studio per training. [Fonte: raw/puntate/ainews20260604.md]
- **2026-06-13** — Unsloth ha ottimizzato DiffusionGemma per inferenza locale: oltre duemila token al secondo, uno punto otto volte più veloce della versione base, con diciotto gigabyte di RAM. [Fonte: raw/puntate/ainews20260613.md]
- **2026-06-16** — Unsloth ha reso Kimi K2.7 Code eseguibile in locale: il modello da un terabyte è stato compresso a trecentoventicinque gigabyte, con quaranta token al secondo su configurazioni con trecentotrenta gigabyte di RAM o VRAM. [Fonte: raw/puntate/ainews20260616.md]
- **2026-06-29** — Tra le quattro librerie segnalate per accelerare il fine-tuning: raddoppia la velocità e riduce la VRAM del 70%. [Fonte: raw/puntate/ainews20260629.md]
- **2026-07-15** — Unsloth rilascia Gemma 4 quant NVFP4: uno virgola cinque volte più veloce su GPU, Gemma-4-12B funziona su undici GB di VRAM e un modello 26B-M-A4B raggiunge tredicimila token al secondo su B200. [Fonte: raw/puntate/ainews20260715.md]
- **2026-07-18** — Unsloth ha pubblicato le versioni quantizzate GGUF, MLX e NVFP4 aggiornate di Gemma 4, dopo l'aggiornamento Google con miglioramenti a tool-calling, accuratezza chat e velocità. [Fonte: raw/puntate/ainews20260718.md]
- **2026-07-21** — Unsloth collabora con AMD per abilitare training e inferenza di oltre cinquecento modelli su GPU AMD: funziona su Windows, WSL e Linux, addestra Qwen e Gemma con tre gigabyte di VRAM, due volte più veloce con il settanta per cento di VRAM in meno. [Fonte: raw/puntate/ainews20260721.md]
- **2026-07-24** — Ha rilasciato Gemma 4 26B A4B QAT, ottimizzato per girare su schede con 8 GB di VRAM: con cache KV a 8 bit raggiunge 180.000 token di contesto su RTX 4060. [Fonte: raw/puntate/ainews20260724.md]
- **2026-07-28** — Ha firmato la lettera Open Weights perché crede che il futuro dell'IA debba essere accessibile a tutti. [Fonte: raw/puntate/ainews20260728.md]
- **2026-07-31** — Porta Inkling-Small: 276 miliardi di parametri, il più forte open model per dimensione, gira locale su 128 GB di RAM con licenza Apache-2.0 e supporto a immagini, audio e un milione di token di contesto. [Fonte: raw/puntate/ainews20260731.md]

- **2026-09-05** — Unsloth ha ottimizzato l'inferenza GGUF di GLM 5.3-Flash per la esecuzione locale: ora gira tre punto tre volte più veloce grazie a decodifica migliorata e predizione multi-token, e mette a disposizione una versione a tre bit utilizzabile su configurazioni da centoventi gigabyte di RAM. [Fonte: raw/puntate/ainews20260905.md]
- **2026-08-15** — Il gruppo Unsloth (71.902 stelle su GitHub) distribuisce [[qwen-3-8-27b]] in formato GGUF con la quantizzazione Dynamic 2.0, che calibra i livelli sui dati d'uso reale e mantiene a precisione più alta le layer più sensibili, così un 4-bit Unsloth regge meglio di un 4-bit generico: le varianti vanno da 9,0 GB a 53,8 GB e su 16 GB di memoria entrano interi UD-Q3_K_XL e IQ4_XS. [Fonte: raw/pillitteri/pillitteri20260815-qwen3-8-27b-locale-16gb-lm-studio-unsloth.md]
- **2026-08-26** — Con Unsloth il fine-tuning di Qwen 3.8 27B è gratuito e gira in locale su ventiquattro GB di VRAM: l'addestramento è una virgola cinque volte più veloce con cinquanta percento di VRAM in meno; Unsloth lavora anche al supporto day zero di Qwen 3.8 Flash-Next. [Fonte: raw/puntate/ainews20260826.md]
- **2026-09-29** — Unsloth Desktop fa girare Laya Decision in locale con quattro gigabyte di RAM su CPU, Mac, Windows, Linux e GPU, servendo il modello tramite API compatibile Jev. [Fonte: raw/puntate/ainews20260929.md]
- **2026-10-09** — Unsloth collabora con Windows per aggiungere il sandboxing a livello di sistema operativo tramite mxc, il repository di [[microsoft]] per l'esecuzione sandboxed di codice, con meno di cento millisecondi di overhead. [Fonte: raw/puntate/ainews20261009.md]
- **2026-10-10** — Unsloth pubblica un notebook gratuito per addestrare decision model personalizzati: Qwen 3.5-4B può generare decisioni invece di testo su otto GB di VRAM, con data prep, training e serving nello stesso flusso. [Fonte: raw/puntate/ainews20261010.md]
- **2026-10-29** — Il 28 ottobre Unsloth ha pubblicato la prova del proprio browser use con [[qwen3-8-27b]]: il modello locale controlla il browser integrato in Unsloth Desktop e porta a termine da solo compiti come una partita a scacchi e un disegno, senza intervento umano, secondo l'annuncio dell'azienda. La funzione è arrivata per gradi, dal browser dentro l'app il 6 ottobre (0.1.903) al clic su coordinate e al trascinamento sui canvas il 13 ottobre (0.1.907), fino all'interruttore nella pagina Nuova scheda nella 0.1.912 del 28 ottobre; per il 27B a 4 bit servono 16-19 GB fra RAM e VRAM, 31 GB a 8 bit e 56 GB in BF16. [Fonte: raw/pillitteri/pillitteri20261029-unsloth-browser-use-qwen3-8-27b-locale.md]










## Collegamenti

- [[andrew-ng]]
- [[axolotl]]
- [[diffusiongemma]]
- [[gemma-4]]
- [[inkling-small]]
- [[kimi-k2-7-code]]
- [[llama-factory]]
- [[nativ]]
- [[nvidia]]
- [[open-source]]
- [[index]]

