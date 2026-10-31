---
title: "DS4"
category: strumento
tags: [deepseek, inferenza, locale, mit, open-source]
related_puntate: []
created: 2026-09-12
updated: 2026-09-13
---

# DS4

## Introduzione

Motore di inferenza specializzato pubblicato su GitHub da [[antirez]] (Salvatore Sanfilippo, il creatore di Redis) il 6 maggio 2026, con licenza MIT. Il nome per esteso è DwarfStar4 e la scelta di fondo è controcorrente: non prova a far girare qualunque modello, ma fa girare bene un modello solo, [[deepseek-v4-flash]], con supporto anche alla variante PRO sulle macchine con moltissima memoria. Al primo settembre 2026 conta 21.984 stelle.

## Funzionalità principali

- Inferenza ottimizzata a mano per DeepSeek V4 Flash, un mixture-of-experts con sparsità estrema (13 miliardi di parametri attivi su 284 miliardi): spremere velocità e qualità da quella forma conviene più con kernel scritti su misura che con un runtime generalista come llama.cpp.
- Supporto a Metal per i Mac Apple Silicon, CUDA per le schede NVIDIA incluso il DGX Spark e ROCm per le AMD come il Framework Desktop con Strix Halo: la stessa immagine, sullo stesso modello, viene analizzata su tutti e tre gli acceleratori senza tre codebase né tre livelli di qualità diversi.
- Visione dalla riga di comando: nella CLI interattiva il comando /read immagine.png passa al modello un file PNG o JPEG, con un encoder visivo separato da 0,9 GiB che si somma ai pesi del modello linguistico.
- Oltre alla visione, cache KV persistente su disco, tool calling, un server con API compatibile OpenAI e Anthropic e un agente di coding integrato.
- Quantizzazione applicata ai soli esperti instradati del MoE, lasciando intatte le altre componenti: è la ragione per cui la qualità regge anche a 2 bit.

## Installazione e uso

- Il codice è su GitHub con licenza MIT, quindi scaricabile, compilabile e utilizzabile anche in progetti commerciali; il supporto alla visione è quello annunciato il 1 settembre 2026, quindi conviene partire dall'ultima versione del ramo principale.
- Requisiti di memoria: circa 81 GB per il modello Flash a 2 bit, con fascia ideale tra 96 e 128 GB. Con meno memoria resta lo streaming dei pesi da SSD, che fa girare modelli più grandi della RAM disponibile a scapito della velocità.
- I benchmark pubblicati su M5 Max con 128 GB e quantizzazione a 2 bit: 790,18 token al secondo in prefill con contesto corto (2.048 token) e 398,50 con contesto lungo (65.536), 39,35 token al secondo in generazione a contesto corto e 27,64 a contesto pieno.

## Repository

- GitHub: `antirez/ds4` — 21.984 stelle al 1 settembre 2026, licenza MIT.

## Azienda / autore

- [[antirez]]

## Modelli supportati / correlati

- [[deepseek-v4-flash]]
- [[deepseek]]

## Timeline delle notizie

- **2026-05-09** — Il rilascio iniziale del 7 maggio 2026 esce come backend Metal-only su Apple Silicon, con un grafo dedicato a un solo modello invece del loader GGUF generalista: quantizzazione asimmetrica, contesto fino a un milione di token, cache KV persistente su disco con header da 48 byte e chiave SHA1 dei token ID, server HTTP con quattro endpoint compatibili OpenAI e Anthropic e CLI interattiva. Solo gli esperti instradati della MoE scendono a 2 bit (IQ2_XXS per up e gate, Q2_K per la proiezione down) mentre esperti condivisi, proiezioni di attenzione, router ed embedding restano in Q8: su un MacBook Pro M3 Max da 128 GB i pesi occupano circa 76 GB e generano 26,68 token al secondo con un picco di 50 watt, mentre la variante Q4 richiede almeno 256 GB. L'11 maggio arriva il refactoring a backend separabili con percorso CUDA di prima classe per l'NVIDIA DGX Spark GB10 e il single-direction activation steering ispirato al paper del 2024 sul rifiuto mediato da un singolo vettore; l'engine viene rinominato DwarfStar4 l'11 maggio e DwarfStar il 25.
- **2026-08-26** — Nel commento al Mac Studio M5 Ultra il batching diventa il terreno su cui si gioca l'inferenza locale: su Apple Silicon lo strumento più diffuso, MLX, non regge il confronto con [[vllm]] sulla capacità di raggruppare le richieste, quindi va bene per un singolo sviluppatore ma non per servire più utenti insieme, ed è il buco che DS4 prova a colmare preassegnando sessioni residenti indipendenti, valutando in un unico passaggio i passi di decodifica pronti e spezzando i prompt lunghi in blocchi controllati perché una richiesta non blocchi tutte le altre.
- **2026-09-01** — antirez mostra DeepSeek V4 Flash con la visione mentre gira in locale su un Mac M5 Max e annuncia il supporto Metal, CUDA e ROCm in uscita nel giro di ore; i commit raccontano la corsa finale, con Vision-Exp aggiunto prima a Metal, poi le due patch del 31 agosto per la build CUDA e ROCm e infine la documentazione e l'irrobustimento della cache multimodale. Il modello a cui DS4 dà la visione è DeepSeek V4 Flash Vision-Exp, rilasciato da DeepSeek il 21 agosto 2026 come versione sperimentale che aggiunge la comprensione delle immagini senza perdere nulla sul testo, con le immagini contate come token fino a 384 per immagine e prestazioni multimodali dichiarate vicine a Claude Opus 4.8. antirez sviluppa DS4 con un aiuto pesante dei modelli, dichiarando nel README l'assistenza di GPT-5.5, 5.6 e Claude Fable, pur restando lui a guidare design e collaudo.

- **2026-09-11** — Il progetto viaggia sopra le 22.000 stelle su GitHub e apre la issue numero 1023 segnalando la disponibilità dei pesi di [[deepseek-v4-1-flash]]: il porting è in corso, ma la richiesta è sul tavolo e antirez ci sta già lavorando.
- **2026-09-13** — Nel confronto a tre motori sullo stesso muro — far girare in locale i MoE che non entrano in VRAM — il progetto è ribattezzato DwarfStar e si ferma a 22.318 stelle, sorpassato da [[colibri]] (28.756) ma davanti a [[ktransformers]] (19.505). La sua strada resta distintiva: sul disco finisce soprattutto la cache KV, sommata a una quantizzazione a 2 bit asimmetrica, ed è il più maturo sui Mac di fascia alta (Metal con almeno 96 GB, poi CUDA e ROCm); gira la famiglia DeepSeek — 4 Flash, 4 PRO e la più recente 4.1 Flash, per ora solo su Metal — più GLM 5.2, 5.3 e la variante Flash.

## Collegamenti

- [[ai-locale]]
- [[antirez]]
- [[colibri]]
- [[deepseek]]
- [[deepseek-v4-flash]]
- [[glm-5-2]]
- [[ktransformers]]
- [[llama-cpp]]
- [[ollama]]
- [[index]]
