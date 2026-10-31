---
title: "Nanbeige4.3-33B"
category: modello
tags: [cina, llm, open-weight, coding, apache-2-0, agenti]
related_puntate: []
created: 2026-10-26
updated: 2026-10-26
sources: [raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]
---

# Nanbeige4.3-33B

## Introduzione

Modello linguistico open da 33,1 miliardi di parametri con licenza Apache 2.0 e finestra di contesto da 524.288 token, pubblicato il 24 ottobre 2026 su Hugging Face dal laboratorio cinese Nanbeige, che è la divisione di modelli linguistici di BOSS Zhipin (Kanzhun), piattaforma di recruiting online quotata al Nasdaq con la sigla BZ e a Hong Kong. Il laboratorio lo presenta come flagship teacher model della serie 4.3, cioè il modello da cui distillare versioni più piccole. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]

## Capacità

- La scheda indica 524.288 token di contesto, ragionamento attivo di default (si spegne con `enable_thinking` impostato a False) e l'opzione `preserve_thinking`, che conserva i ragionamenti dei turni precedenti: il laboratorio la consiglia accesa per flussi con strumenti e agenti di codice e spenta per la chat. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]
- Le chiamate a strumenti passano da un template dedicato con formato XML consigliato e JSON supportato; le lingue dichiarate sono inglese e cinese. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]
- Il rilascio comprende due repository: Nanbeige4.3-33B, già rifinito per chat e ragionamento con gli strumenti, e Nanbeige4.3-33B-Base, la versione grezza da cui partire per un proprio post-addestramento. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]

## Performance

- Nei test della scheda supera [[qwen3-8-27b]] in 18 prove su 20 e ne perde due, SWE-Bench Pro (60,3 contro 61,7) e GDPval (84,8 contro 86,4); il distacco maggiore è sul coding agentico, con DeepSWE a 65,5 contro 42,5, Terminal-Bench 4.0 a 23,8 contro 6,3 e Terminal-Bench 2.1 a 80,9 contro 73,0. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]
- Sui compiti d'ufficio Automation Bench segna 54,2 contro 38,3 e DeepPlanning 63,3 contro 49,2; su Tau3-Bench, GPQA Diamond e AIME 2026 i margini sono di pochi decimi, e su GPQA Diamond Gemma4-31B resta davanti a tutti con 91,3. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]
- Sul Base il laboratorio riporta il confronto con Gemma4-31B-Base: GPQA 62,0 contro 41,5 e MMLU-Pro 66,9 contro 59,3. Tutti i numeri sono misurati da chi vende il modello, senza rapporto tecnico né dati di addestramento, e il banco di prova è scelto dal laboratorio. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]

## Disponibilità

- I pesi sono su Hugging Face con licenza Apache 2.0, senza lista d'attesa; servono circa 66 GB di memoria in BF16 o intorno ai 20 GB con una quantizzazione a 4 bit, più la KV cache, che per questo modello costa circa 208 KB per token: 32.768 token occupano circa 7 GB e i 524.288 dichiarati intorno a 112 GB. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]
- Le istruzioni ufficiali per vLLM e SGLang parlano di quattro schede in parallelo, con i parser di Qwen3 (`--reasoning-parser qwen3` e `--tool-call-parser qwen3_coder`), temperatura 1,0 e top_p 0,95 fino a 65.536 token per l'uso agentico, temperatura 0,6 fino a 262.144 per ragionamento e chat. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]

## Rilasci e aggiornamenti

- La serie Nanbeige4 è nata con il modello da 3 miliardi di parametri di dicembre 2025, seguito dalle revisioni 4.1 e 4.2 di luglio 2026, che ha introdotto un Looped Transformer; il 4.3-33B torna a un'architettura LlamaForCausalLM dichiarata nel `config.json`, con 52 strati, 8 teste per chiavi e valori e 128 dimensioni per testa, senza attenzione sparsa o ibrida. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]
- La scheda del 4.2 annuncia che le novità dell'architettura a cicli confluiranno nel Nanbeige4.5, in addestramento per la fine del 2026, e indica il Nanbeige4.3-3B come prossimo allievo della distillazione, per ora senza data. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]

## Azienda di riferimento

- Nanbeige, laboratorio di BOSS Zhipin (Kanzhun): nessuna delle due ha una pagina in wiki. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]

## Timeline delle notizie
- **2026-10-24** — Nanbeige pubblica su Hugging Face Nanbeige4.3-33B e la versione Base: 33,1 miliardi di parametri in BF16, licenza Apache 2.0, 524.288 token di contesto e ragionamento attivo di default, con l'obiettivo dichiarato di farne il modello insegnante per distillare versioni più piccole della serie 4.3. [Fonte: raw/pillitteri/pillitteri20261025-nanbeige-4-3-33b-open-source.md]




## Collegamenti

- [[qwen3-8-27b]]
- [[gemma-4-31b]]
- [[muse-glimmer]]
- [[open-source]]
- [[index]]
