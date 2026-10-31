---
title: "Qwen 3.8 27B"
category: modello
tags: [alibaba, cina, edge, llm, open-weight]
related_puntate: [20260804, 20260807, 20260810, 20260825, 20260907, 20260918, 20260920, 20261003, 20261009, 20261010, 20261014, 20261021]
created: 2026-08-12
updated: 2026-10-24
sources: [raw/puntate/ainews20260804.md, raw/puntate/ainews20260807.md, raw/puntate/ainews20260810.md, raw/puntate/ainews20260825.md, raw/puntate/ainews20260907.md, raw/puntate/ainews20260918.md, raw/puntate/ainews20260920.md, raw/puntate/ainews20261003.md, raw/pillitteri/pillitteri20261004-installare-modello-uncensored-locale-mac-windows.md, raw/puntate/ainews20261009.md, raw/puntate/ainews20261010.md, raw/puntate/ainews20261014.md, raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md, raw/puntate/ainews20261021.md, raw/controrumore/controrumore20261024-diario-ai-sicurezza-regole-e-nuovi.md]
---

# Qwen 3.8 27B

## Introduzione

Modello compatto della famiglia Qwen 3.8 di Alibaba, progettato per girare su diciassette GB di RAM. Rilasciato in contemporanea con Qwen 3.8 Max.

## Capacità e performance

- Qwen 3.8 27B, parte del rilascio della famiglia Qwen 3.8, è progettato per girare su diciassette GB di RAM insieme ai pesi aperti annunciati per la settimana successiva.
- Grande notizia per la community LocalAI: Qwen tre punto otto ventisette B sara' rilasciato con pesi aperti il dodici agosto alle dieci UTC+8; per la prima volta Qwen aprira' i pesi di un modello Max-class, il Qwen tre punto otto due punto quattro T-A novantacinque B.
- Qwen tre punto otto da ventisette miliardi arriva il dodici agosto con pesi aperti: dovrebbe girare localmente con circa diciassette GB RAM/VRAM quantizzato.

## Azienda di riferimento

- [[alibaba]]

## Timeline delle notizie

- **2026-08-04** — Qwen 3.8 27B, parte del rilascio della famiglia Qwen 3.8, è progettato per girare su diciassette GB di RAM insieme ai pesi aperti annunciati per la settimana successiva. [Fonte: raw/puntate/ainews20260804.md]
- **2026-08-07** — Grande notizia per la community LocalAI: Qwen tre punto otto ventisette B sara' rilasciato con pesi aperti il dodici agosto alle dieci UTC+8; per la prima volta Qwen aprira' i pesi di un modello Max-class, il Qwen tre punto otto due punto quattro T-A novantacinque B. [Fonte: raw/puntate/ainews20260807.md]
- **2026-08-10** — Qwen tre punto otto da ventisette miliardi arriva il dodici agosto con pesi aperti: dovrebbe girare localmente con circa diciassette GB RAM/VRAM quantizzato. [Fonte: raw/puntate/ainews20260810.md]
- **2026-08-25** — Qwen 3.8 27B è alla base di tre modelli annunciati oggi: Carnice V3 27B (open source, batte modelli dieci volte più grandi in Hermes-agent), Huihui-Qwen3.8-27B-abliterated-GGUF (multimodale, quasi zero rifiuti, locale) e SuperQwen3.8-27b-abliterated (uncensored, un milione di contesto). [Fonte: raw/puntate/ainews20260825.md]
- **2026-09-07** — Qwen 3.8 27B gira in BF16 completo su TPU gratuito Kaggle senza quantizzazione (circa 130 token/s decode, 10k token/s prefill, 262k contesto) ed è esponibile come endpoint compatibile OpenAI. [Fonte: raw/puntate/ainews20260907.md]
- **2026-09-18** — Qwen 3.8 27B è la base di Ternary Bonsai 2 27B di PrismML: la versione ternary è nove volte più piccola della controparte full-precision e mantiene il 98,2% delle performance aggregate, con footprint di 5,9 gigabyte. [Fonte: raw/puntate/ainews20260918.md]

- **2026-09-20** — [[inco-splash]] è il motore di inferenza open source costruito attorno a Qwen 3.8 27B per Apple silicon: 144 token al secondo su MacBook Pro M5 Max, tre volte Ollama, il doppio di oMLX, quasi quattro volte quando un agente si scompone in sotto-agenti e integrato in LM Studio dal giorno zero. [Fonte: raw/puntate/ainews20260920.md]
- **2026-10-02** — Esce MLX-Serve 26.10.1 con aumenti di velocità su tutta la linea: Qwen 3.8 27B con drafter guadagna il 66% su M5 Ultra, il 28% su M4 Max e il 37% su M1 Pro, mentre Qwen Flash Next segna +11% in decode su M4 Max e +51% in prefill su M5 Ultra; i modelli GGUF girano su un engine MLX proprietario in Zig e Metal e Qwen-Image 2.1 modifica immagini da istruzioni. [Fonte: raw/puntate/ainews20261002.md]
- **2026-10-03** — Una RTX 3090 spinge Qwen 3.8 27B a 381 token al secondo con speculative decoding a blocchi di verifica più lunghi e context lookup, che sui documenti lunghi predice i token dal contesto già presente; su chat normali segna 133 token al secondo. [Fonte: raw/puntate/ainews20261003.md]
- **2026-10-04** — Le versioni uncensored di Qwen3.8-27B sono ormai il caso di studio dell'ecosistema locale: la sola variante GGUF di JonathanColetti supera i 2,1 milioni di download e quella di orcarouter i 135.000, con rifiuti sulle richieste dannose dichiarati in calo dal 64-99% del modello base allo 0-6%; il file Q4_K_M pesa 16,8 GB e chiede circa 20 GB di memoria totale. [Fonte: raw/pillitteri/pillitteri20261004-installare-modello-uncensored-locale-mac-windows.md]
- **2026-10-09** — Underdog rilascia Saluki 27B, compresso da Qwen 3.8 27B: quasi sette volte più piccolo della controparte full-precision, mantiene il 96 per cento delle prestazioni sui benchmark e batte Qwen nel tool calling, open source e sotto gli otto gigabyte. [Fonte: raw/puntate/ainews20261009.md]

- **2026-10-09** — Lithos Metal esegue Qwen 3.8-27B a oltre duecento token al secondo per utente su un Apple M5 Max con megakernels e speculative decoding DSpark. [Fonte: raw/puntate/ainews20261009.md]
- **2026-10-10** — Qwen 3.8-27B riceve un upgrade pesante con 390.000 sample di codice nel post-training: LiveCodeBench sale da 83 a 90, GPQA arriva a 89,9 per cento e MMLU al 90 per cento, il pensiero si accorcia del 44-53 per cento e la licenza resta Apache 2.0. [Fonte: raw/puntate/ainews20261010.md]
- **2026-10-14** — Qwen3.8-27B passa da 82 a 381 token al secondo sulla stessa RTX 3090 da 24 GB con sole ottimizzazioni software: DFlash2 con context lookup propone blocchi di testo già presenti nel contesto e il modello verifica sedici token alla volta invece di sette, portando un documento da 25.000 token da 260 a 382 token al secondo, mentre il prefix caching taglia il tempo al primo token da ventidue secondi a 0,56. [Fonte: raw/puntate/ainews20261014.md]
- **2026-10-14** — Gira a circa 20 token al secondo sulla GPU di una PlayStation 5 con jailbreak grazie a PS5LM Plus, il fork che porta il progetto di llama.cpp per console da payload ad app nativa con 11,44 GiB di memoria: la variante UD-Q2_K_XL a 2 bit (9,2 GiB) fa 20,3 token al secondo con 32k di contesto e la IQ2_XXS 20,7 con 64k, al prezzo di una precisione che allucina più di una versione meno compressa. [Fonte: raw/pillitteri/pillitteri20261014-qwen-27b-ps5-jailbreak-gpu-20-token-secondo.md]
- **2026-10-21** — Con [[eagle-4|EAGLE-4]] e TokenSpeed raggiunge 961,6 token al secondo su quattro GPU Nvidia B300 in parallelo, secondo il benchmark del progetto EAGLE. [Fonte: raw/puntate/ainews20261021.md]
- **2026-10-24** — È stato usato come base per il fine-tuning del sistema di Microsoft e Hugging Face che valuta gli agenti software sullo stato finale del database: dopo l'addestramento su 187 attività il successo medio su 507 compiti è salito di 9,08 punti percentuali rispetto al modello senza fine-tuning, con almeno sette attività comunque non risolte. [Fonte: raw/controrumore/controrumore20261024-diario-ai-sicurezza-regole-e-nuovi.md]




























## Collegamenti

- [[bonsai-27b]]

- [[alibaba]]
- [[carnice-v3-27b]]
- [[huihui-qwen3-8-27b-abliterated-gguf]]
- [[qwen-3-8-max]]
- [[superqwen3-8-27b-abliterated]]
- [[inco-splash]]
- [[index]]
- [[ps5lm]]

