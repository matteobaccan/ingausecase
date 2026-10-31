---
title: "DeepSeek-v4-flash"
category: modello
tags: [agent, cina, coding, deepseek, gratis, llm, locale, moe, open-weight, reasoning, vision]
related_puntate: [20260611, 20260621, 20260627, 20260801, 20260802, 20260803, 20260804, 20260805, 20260806, 20260807, 20260812, 20260824, 20260920]
created: 2026-08-12
updated: 2026-10-08
sources: [raw/pillitteri/pillitteri20260509-ds4-antirez-motore-inferenza-deepseek-v4-flash.md, raw/puntate/ainews20260611.md, raw/puntate/ainews20260621.md, raw/puntate/ainews20260627.md, raw/puntate/ainews20260801.md, raw/puntate/ainews20260802.md, raw/puntate/ainews20260803.md, raw/puntate/ainews20260804.md, raw/puntate/ainews20260805.md, raw/puntate/ainews20260806.md, raw/puntate/ainews20260807.md, raw/puntate/ainews20260812.md, raw/puntate/ainews20260824.md, raw/pillitteri/pillitteri20260802-deepseek-v4-flash-0731-api-ufficiale.md, raw/pillitteri/pillitteri20260901-ds4-antirez-visione-locale-deepseek-v4-flash.md, raw/pillitteri/pillitteri20260911-deepseek-v41-flash-748-miliardi-vision.md, raw/pillitteri/pillitteri20260913-streaming-disco-modelli-moe-portatile.md, raw/puntate/ainews20260920.md, raw/pillitteri/pillitteri20261007-deepseek-v4-flash-nemotron-locale-windows-rtx-spark.md]
---

# DeepSeek-v4-flash

## Introduzione

Modello MoE open-weight di DeepSeek da 284 miliardi di parametri totali e 13 attivi, con un milione di token di contesto. Nel periodo è passato in versione API ufficiale, superando V4-Pro-Preview sui benchmark agentici e dimostrandosi estremamente economico in locale.

## Capacità e performance

- DeepSeek-v4-flash è tra i modelli offerti gratuitamente da NVIDIA per un anno, con quaranta richieste al minuto.
- DeepSeek V4 Flash è tra i cinque modelli cinesi di frontiera resi accessibili gratuitamente da NVIDIA con una sola chiave API, senza carta di credito.
- Tra i modelli accessibili tramite FreeLLMAPI, che aggrega i tier gratuiti di 16 provider dietro un singolo endpoint, con oltre 100 modelli disponibili.
- Supporta nativamente il formato Responses API e l'integrazione con [[codex]] tramite un unico file ~/.codex/config.toml, valido per la CLI, per l'app desktop di ChatGPT e per l'estensione VS Code; la build 0731 aggiunge il modulo di decodifica speculativa DSpark e porta il conteggio a 304 miliardi di parametri nel pacchetto completo. [Fonte: raw/pillitteri/pillitteri20260802-deepseek-v4-flash-0731-api-ufficiale.md]

## Azienda di riferimento

- [[amd-token-factory]]
- [[deepseek]]
- [[nvidia]]
- [[roundtable-space]]

## Strumenti correlati

- [[ai-locale]]
- [[codex]]
- [[dspark]]
- [[ds4]]
- [[freellmapi]]
- [[ollama]]
- [[vulcanbench]]

## Timeline delle notizie

- **2026-05-09** — La ricetta di quantizzazione di [[antirez]] dentro [[ds4]] porta il MoE da 284 miliardi di parametri in circa 76 GB: scendono a 2 bit solo gli esperti instradati, mentre esperti condivisi, proiezioni di attenzione, router ed embedding restano in Q8. Su un MacBook Pro M3 Max da 128 GB la Q2 fa 58,52 token al secondo in prefill su prompt corto e 26,68 in generazione, con 250,11 token al secondo di prefill su un prompt da 11.709 token, e il merito è anche dell'addestramento QAT con cui DeepSeek lo ha rilasciato: sparsità estrema e pesi già preparati alla compressione rendono la perdita di qualità contenuta anche sotto i 4 bit. La variante Q4 richiede almeno 256 GB. [Fonte: raw/pillitteri/pillitteri20260509-ds4-antirez-motore-inferenza-deepseek-v4-flash.md]
- **2026-06-11** — DeepSeek-v4-flash è tra i modelli offerti gratuitamente da NVIDIA per un anno, con quaranta richieste al minuto. [Fonte: raw/puntate/ainews20260611.md]
- **2026-06-21** — DeepSeek V4 Flash è tra i cinque modelli cinesi di frontiera resi accessibili gratuitamente da NVIDIA con una sola chiave API, senza carta di credito. [Fonte: raw/puntate/ainews20260621.md]
- **2026-06-27** — Tra i modelli accessibili tramite FreeLLMAPI, che aggrega i tier gratuiti di 16 provider dietro un singolo endpoint, con oltre 100 modelli disponibili. [Fonte: raw/puntate/ainews20260627.md]
- **2026-08-01** — Rilasciato da DeepSeek in versione ufficiale API: supera V4-Pro-Preview sui benchmark agentic, con 284 miliardi di parametri totali e 13 attivi, contesto da un milione di token; ora è eseguibile anche in locale. [Fonte: raw/puntate/ainews20260801.md]
- **2026-08-02** — In un test comparativo con Kimi K3 e GLM 5.2 è ultimo ma 150 volte più economico; la versione 0731 su M5 Max con Metal genera tra 35 e 39 token al secondo (quantizzata da 91 GB); un endpoint pubblico gratuito (nessun account, compatibile OpenAI) riporta 82,7 su terminal-bench e 54,4 su SWE-bench, con limite di 12 richieste al minuto per IP. [Fonte: raw/puntate/ainews20260802.md]
- **2026-08-02** — DeepSeek apre la beta pubblica dell'API ufficiale di V4-Flash nella build 0731: architettura e dimensioni restano identiche alla preview (284 miliardi di parametri totali, 13 attivi) e tutto il salto viene dal re-post-training. Nei nove benchmark agentici dichiarati dal produttore il modello piccolo batte V4-Pro-Preview, con 82,7 contro 72,1 su Terminal Bench 2.1 e 54,4 contro 12,8 su DeepSWE, restando però sotto Claude Opus 4.8 su tutte le voci; Artificial Analysis lo colloca a 50 punti di Intelligence Index contro i 51 di GPT-5.6 Luna e sul benchmark GDPval il punteggio Elo passa da 1.189 a 1.559. Il listino resta a 0,14 dollari per milione di token in input a cache fredda e 0,28 in output, con 2.500 richieste simultanee, ma DeepSeek ha annunciato una tariffazione peak e off-peak che raddoppia i prezzi nelle fasce 9:00-12:00 e 14:00-18:00 di Pechino. I pesi sono su Hugging Face con licenza MIT e il modello base ha superato i 2,8 milioni di download nell'ultimo mese; per l'esecuzione locale servono circa 110 GB di memoria a 3 bit oppure un nodo con quattro GB300. I numeri restano dichiarazioni del produttore, perché le valutazioni sono state eseguite con il DeepSeek Harness in modalità minimal e con sforzo di ragionamento massimo, e quello strumento non è stato rilasciato. [Fonte: raw/pillitteri/pillitteri20260802-deepseek-v4-flash-0731-api-ufficiale.md]
- **2026-08-03** — DeepSeek V4 Flash 0731 gira su Mac da centoventotto GB e ha preso la prima posizione su VulcanBench con effort medio, superando Grok 4.5 medio secondo, con Fable fuori dal podio e ChatGPT fuori dai primi cinque. [Fonte: raw/puntate/ainews20260803.md]
- **2026-08-04** — DeepSeek V4 Flash 0731 gira su una singola RTX quattro zero nove zero: dodici token al secondo in decode, seicentocinquanta in prefill e duecentocinquantamila token di contesto. [Fonte: raw/puntate/ainews20260804.md]
- **2026-08-05** — DeepSeek V4 Flash 0731 e' gratis sei ore al giorno in ogni paese su Roundtable Space; Ollama riporta che e' il modello a crescita piu' rapida di sempre per uso token, con over cento token al secondo e zero data retention. [Fonte: raw/puntate/ainews20260805.md]
- **2026-08-06** — Roundtable ha aggiunto la visione a DeepSeek V4 Flash: l'agent legge mockup e screenshot, rendendo il debug frontend molto piu' preciso; una skill installa tutto. [Fonte: raw/puntate/ainews20260806.md]
- **2026-08-07** — Test comparativo di DeepSeek V4 Flash su quattro harness (Claude Code, Codex, OpenCode, Oh My Pi) su trenta task agentici: ogni harness ha vinto su una metrica diversa; DSpark lo accelera del doppio in locale a centoventi token al secondo senza perdita di accuratezza, e Codex lo integra come sub-agent nativo. [Fonte: raw/puntate/ainews20260807.md]
- **2026-08-12** — DeepSeek V4 Flash e Qwen3.6 sono gratis su AMD Token Factory con dieci dollari di utilizzo al giorno: il contatore si resetta quotidianamente e tutto cio' che e' fuori lista gira su crediti Firework AI. [Fonte: raw/puntate/ainews20260812.md]

- **2026-08-24** - DeepSeek V4 Flash da 284 miliardi di parametri gira a ventidue token al secondo su una RTX 5090 con FreeToken di UC Berkeley, piu' veloce di Ollama. [Fonte: raw/puntate/ainews20260824.md]

- **2026-09-01** — La visione arriva in locale su [[ds4]] di [[antirez]]: DeepSeek V4 Flash analizza un'immagine su un Mac M5 Max senza connessione a un cloud, con il motore portato su Metal, CUDA e ROCm, e la variante Vision-Exp rilasciata il 21 agosto 2026 (comprensione delle immagini senza perdite sul testo, immagini contate come token fino a 384 per immagine, prestazioni multimodali dichiarate vicine a Claude Opus 4.8). I benchmark su M5 Max con 128 GB e quantizzazione a 2 bit danno 39,35 token al secondo in generazione a contesto corto e 27,64 con 65.536 token; la versione a 2 bit occupa circa 81 GB e l'encoder visivo aggiunge 0,9 GiB. [Fonte: raw/pillitteri/pillitteri20260901-ds4-antirez-visione-locale-deepseek-v4-flash.md]

- **2026-09-11** — La versione 0731 viene sostituita: il 10 settembre [[deepseek]] rilascia [[deepseek-v4-1-flash]], che prende il posto sia di questo modello sia del ramo sperimentale Vision, con i vecchi nomi API che puntano automaticamente alla nuova versione. [Fonte: raw/pillitteri/pillitteri20260911-deepseek-v41-flash-748-miliardi-vision.md]
- **2026-09-13** — Nel confronto sui motori a streaming da disco è tra i modelli che [[colibri]] fa girare in locale senza GPU (284B, con la variante compressa REAP a 150B che scende a circa 85 GB), mentre la variante successiva 4.1 Flash resta per ora solo su [[ds4]] con Metal. [Fonte: raw/pillitteri/pillitteri20260913-streaming-disco-modelli-moe-portatile.md]

- **2026-09-20** — Un ingegnere giapponese distilla DeepSeek V4 Flash in un modello da quattro miliardi di parametri: ventisei ore su [[dgx-spark]] per comprimere centosettanta gigabyte di pesi in un modello che supera la modalità rapida del teacher, con ventidue millisecondi per decisione, un ventesimo delle dimensioni originali e tutto in locale. [Fonte: raw/puntate/ainews20260920.md]
- **2026-10-07** — DeepSeek V4 Flash è il modello che Microsoft porta in locale su Windows: 284 miliardi di parametri totali e 13 miliardi attivi, quantizzati a 1,6 bit per stare in 60 GB di memoria, un livello che sta in un PC con memoria unificata ampia come RTX Spark da 128 GB ma non in un portatile da 16 o 32 GB; a 4 bit gli stessi pesi sarebbero circa 142 GB. Il prezzo della compressione è la qualità e «near-frontier» resta una formula del produttore, in attesa di test indipendenti. [Fonte: raw/pillitteri/pillitteri20261007-deepseek-v4-flash-nemotron-locale-windows-rtx-spark.md]




## Collegamenti

- [[ai-locale]]
- [[amd-token-factory]]
- [[chatgpt]]
- [[claude-opus-4-8]]
- [[codex]]
- [[colibri]]
- [[deepseek]]
- [[deepseek-harness]]
- [[dspark]]
- [[ds4]]
- [[fable-5]]
- [[freellmapi]]
- [[glm-5-2]]
- [[glm-5-5]]
- [[gpt-5-6]]
- [[gpt-oss-120b]]
- [[grok-4-5]]
- [[kimi-k3]]
- [[nvidia]]
- [[ollama]]
- [[qwen-3-6]]
- [[roundtable-space]]
- [[vulcanbench]]
- [[freetoken]]
- [[index]]

