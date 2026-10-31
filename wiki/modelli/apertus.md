---
title: "Apertus"
category: modello
tags: [llm, open-source, svizzera, multilingue]
related_puntate: []
created: 2026-09-12
updated: 2026-09-12
---

# Apertus

## Introduzione

Modello linguistico open source su larga scala sviluppato in Svizzera da EPFL, ETH Zurich e dal Centro Nazionale Svizzero di Supercalcolo (CSCS), lanciato il 2 settembre 2025. È addestrato su 15 trilioni di token in oltre 1.000 lingue sul supercomputer Alps di Lugano, con oltre 10 milioni di ore GPU e più di 4.000 GPU NVIDIA GH200, ed è il primo grande modello linguistico presentato come conforme all'EU AI Act.

## Capacità e performance

- Due versioni, Apertus-8B e Apertus-70B, entrambe decoder-only Transformer con contesto massimo di 65.536 token, attivazione xIELU, ottimizzatore AdEMAMix e post-training SFT più allineamento QRPO.
- Il 40% dei dati di addestramento è in lingue diverse dall'inglese, incluse lingue sottorappresentate come svizzero tedesco, romancio e centinaia di lingue africane, asiatiche e indigene.
- Benchmark dichiarati: Apertus-70B segna 69,6% su MMLU, 62,7% su Global-MMLU, 77,6% su GSM8K, 73,0% su HumanEval e 80,6% su RULER a 32k; il punto di forza è la traduzione multilingue, dove supera Llama nelle lingue a basse risorse.
- Limiti dichiarati: resta dietro ai modelli proprietari in matematica e coding, non è multimodale (solo testo) e le performance su lingue minoritarie come svizzero tedesco e romancio sono state definite "praticamente inutilizzabili" in alcuni test.

## Disponibilità

- Pesi scaricabili da Hugging Face (organizzazione swiss-ai), in versione base e Instruct, compatibili con Transformers, vLLM, SGLang, llama.cpp e MLX.
- Deployment anche su Amazon SageMaker JumpStart, sulla piattaforma AI sovrana di Swisscom e sulla rete Public AI; il modello 8B gira su un laptop con circa 16 GB di RAM in quantizzazione Q4.
- La conformità dichiarata si regge su dati di training pubblici, filtraggio delle richieste di opt-out, rimozione dei dati personali e pubblicazione di architettura, pesi e ricette di addestramento.

## Casi d'uso

- Il Canton Ticino usa dalla primavera 2026 un sistema di traduzione basato su una versione fine-tuned di Apertus-8B, sviluppata dall'azienda ticinese Artificialy (guidata da Luca Gambardella, CEO e professore di AI all'USI), con il 94% di accuratezza dopo il fine-tuning contro il 90% prima, cento dipendenti cantonali in test e GPU dedicate installate nel data center cantonale.
- Meditron, modello verticale per la medicina costruito sull'ecosistema Apertus dall'iniziativa Swiss AI, è in test all'Ospedale Universitario di Losanna (CHUV) da maggio 2026.

## Azienda di riferimento

- Progetto della Swiss National AI Initiative: EPFL, ETH Zurich e CSCS, senza una pagina nella wiki.

## Timeline delle notizie

- **2026-03-23** — Il modello svizzero open source Apertus, sviluppato da EPFL, ETH Zurich e CSCS, viene usato dal Canton Ticino per la traduzione AI dei documenti ufficiali con una versione fine-tuned di Apertus-8B realizzata da Artificialy: 94% di accuratezza, dati che non lasciano il data center cantonale.

## Collegamenti

- [[hugging-face]]
- [[nvidia]]
- [[open-source]]
- [[regolamentazione]]
- [[index]]
