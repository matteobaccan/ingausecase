---
title: "vLLM"
category: strumento
tags: [inference, inferenza, llm, multi-utente, open-source, performance, serving]
related_puntate: [20260509, 20260626, 20260627, 20260702, 20260703, 20260713, 20260719, 20260730, 20261019]
created: 2026-08-12
updated: 2026-10-22
sources: [raw/puntate/ainews20260509.md, raw/puntate/ainews20260626.md, raw/puntate/ainews20260627.md, raw/puntate/ainews20260702.md, raw/puntate/ainews20260703.md, raw/puntate/ainews20260713.md, raw/puntate/ainews20260719.md, raw/puntate/ainews20260730.md, raw/tldr/tldr20260923.md, raw/tldr/tldr20261015.md, raw/puntate/ainews20261019.md, raw/tldr/tldr20261020.md, raw/tldr/tldr20261022.md]
---

# vLLM

## Introduzione

Framework open source di inferenza LLM ad alte prestazioni sviluppato da UC Berkeley, standard de facto per il serving di modelli open-weight in produzione.

## Funzionalità principali

- vLLM-Omni v0.20.0 è allineato con vLLM upstream v0.20.0 per throughput e latenza migliorati sui modelli multimodali.
- vLLM è il runtime su cui DeepSeek-OCR raggiunge duemilacinquecento token al secondo, ed è il motore locale di Hyper-Extract.
- Oltre 100 agenti hanno collaborato per una settimana e accelerato Gemma 4 su vLLM di 5 volte, sviluppando autonomamente norme di comunicazione, pooling di quote, divisione del lavoro computazionale e debug kernel cross-agent.

## Azienda / Autore

- [[nvidia]]
- [[prime-intellect]]

## Modelli supportati / correlati

- [[deepseek-ocr]]
- [[deepseek-v4]]
- [[gemma-4]]
- [[kimi-k3]]
- [[minimax-m3]]

## Timeline delle notizie

- **2026-05-09** — vLLM-Omni v0.20.0 è allineato con vLLM upstream v0.20.0 per throughput e latenza migliorati sui modelli multimodali. [Fonte: raw/puntate/ainews20260509.md]
- **2026-06-26** — vLLM è il runtime su cui DeepSeek-OCR raggiunge duemilacinquecento token al secondo, ed è il motore locale di Hyper-Extract. [Fonte: raw/puntate/ainews20260626.md]
- **2026-06-27** — Oltre 100 agenti hanno collaborato per una settimana e accelerato Gemma 4 su vLLM di 5 volte, sviluppando autonomamente norme di comunicazione, pooling di quote, divisione del lavoro computazionale e debug kernel cross-agent. [Fonte: raw/puntate/ainews20260627.md]
- **2026-07-02** — Versione 0.25 con 571 commit da 256 contributori: supporto per MiniMax M3 con FP8 e MXFP4, tuning AMD esteso, DeepSeek V4 matura con cache indice sparso FlashInfer, nuovo Streaming Parser Engine unificato per chiamate tool e ragionamento, DiffusionGemma e DeepEP v2 per parallelismo esperto ampio. [Fonte: raw/puntate/ainews20260702.md]
- **2026-07-03** — Ora supporta DSpark di DeepSeek: speculative decoding che propone più token in parallelo e li verifica in un passo. Su 8 B300 produce circa 250 token al secondo. [Fonte: raw/puntate/ainews20260703.md]
- **2026-07-13** — vLLM versione 0.25 porta il Model Runner V2 come default per tutti i modelli densi, ritira l'implementazione legacy di PagedAttention e introduce un motore di parsing unificato; aggiunge speculative decoding universale con i nuovi drafter DSpark e DFlash e supporto per modelli Hy3 e Unlimited OCR. [Fonte: raw/puntate/ainews20260713.md]
- **2026-07-19** — Il chunked prefill di vLLM divide le richieste lunghe in blocchi piccoli per evitare che un singolo utente monopolizzi la GPU: ogni chunk viene processato insieme ad altre richieste, mantenendo il throughput alto e servendo più utenti contemporaneamente. [Fonte: raw/puntate/ainews20260719.md]
- **2026-07-30** — Con vLLM su Kimi-K3 sono stati raggiunti 464 token al secondo in batch uno con 4x4 GB300, benchmark completamente riproducibile. [Fonte: raw/puntate/ainews20260730.md]

- **2026-09-23** — Introduce layer hardware-agnostici per servire i modelli su hardware diverso mantenendo alte prestazioni: raggiungono fino al 96,6 per cento dell'efficienza delle implementazioni native su GPU NVIDIA H100 restando compilabili con torch ed estensibili, così vLLM si adatta ai nuovi acceleratori senza abbandonare quelli vecchi e di nicchia. [Fonte: raw/tldr/tldr20260923.md]
- **2026-10-15** — Un connettore NIXL push-based sposta fuori dal percorso critico il coordinamento e il setup del trasferimento post-prefill nell'inferenza disaggregata, migliorando la reattività dell'applicazione soprattutto ad alte frequenze di richieste. [Fonte: raw/tldr/tldr20261015.md]
- **2026-10-19** — vLLM 0.32.0 introduce un endpoint strutturato `/v1/systemone`, compressione KV a bassa precisione ovunque e Model Runner V2 ora di default su ROCm, con tempi di avvio più rapidi e throughput aumentato dal quarantatré all'ottantacinque per cento con worker multi-API; aggiunge supporto per EmbeddingGemma 2, MiniCPM-V 4.7 e Nemotron 3.5 ASR, oltre a tre patch di sicurezza. [Fonte: raw/puntate/ainews20261019.md]
- **2026-10-20** — vLLM introduce un trasferimento KV push-based per ridurre il tempo al primo token e il tempo per token in uscita nelle configurazioni di inferenza disaggregata. [Fonte: raw/tldr/tldr20261020.md]
- **2026-10-22** — Il progetto annuncia Humming, libreria di kernel generica per l'inferenza quantizzata, con supporto ampio a dispositivi e tecniche di quantizzazione e un'architettura unica che rende semplice regolare i parametri di esecuzione e raccogliere pipeline per carichi diversi. [Fonte: raw/tldr/tldr20261022.md]













## Collegamenti

- [[bitnet-cpp]]
- [[deepseek-ocr]]
- [[deepseek-v4]]
- [[dflash]]
- [[dspark]]
- [[gemma-4]]
- [[hyper-extract]]
- [[kimi-k3]]
- [[minimax-m3]]
- [[nvidia]]
- [[ollama]]
- [[open-source]]
- [[prime-intellect]]
- [[index]]

