---
title: "DeepSeek V4 Pro"
category: modello
tags: [cina, coding, deepseek, llm, locale, open-weight, reasoning, traduzione]
related_puntate: [20260508, 20260510, 20260518, 20260623, 20260807]
created: 2026-08-12
updated: 2026-10-08
---

# DeepSeek V4 Pro

## Introduzione

Modello di coding e reasoning di DeepSeek, ora eseguibile completamente in locale con quantizzazione 2 bit su hardware Mac Studio.

## Capacità e performance

- DeepSeek V4 Pro chiude la top five della nuova classifica di coding dei modelli cinesi, dietro Kimi K2.6, GLM-5.1, MiMo V2.5 Pro e MiniMax 2.7.
- ERNIE 5.1 di Baidu supera DeepSeek-V4-Pro su tau3-bench e SpreadsheetBench-Verified con solo il 6% del costo di pretraining di modelli simili.
- DeepSeek V4 PRO gira su Mac Studio M3 Ultra con 512 GB RAM: quantizzazione 2 bit, file GGUF da 433 GB, 130 token al secondo in prefill e 13 in generazione, tutto locale senza cloud.

## Azienda di riferimento

- [[deepseek]]

## Strumenti correlati

- [[deepseek-sparse-attention]]
- [[violin]]

## Timeline delle notizie

- **2026-04-24** — Il rilascio open-weight con licenza MIT: 1,6 trilioni di parametri totali, 49 miliardi attivi, contesto da un milione di token e architettura Hybrid Attention con Compressed Sparse Attention e Heavily Compressed Attention. DeepSeek dichiara che V4-Pro richiede solo il 27% dei FLOPs di inferenza per token rispetto a V3.2 e il 10% della KV cache a parità di contesto, grazie anche alle Manifold-Constrained Hyper-Connections e all'ottimizzatore Muon. Nei benchmark pubblicati segna 87,5 su MMLU-Pro, 90,1 su GPQA Diamond, 93,5 su LiveCodeBench, 3.206 punti di rating Codeforces e 76,8 su HumanEval. Sul listino ufficiale costa 1,74 dollari per milione di token in input e 3,48 in output, contro i 15 e 75 di Claude Opus 4.7.
- **2026-05-08** — DeepSeek V4 Pro chiude la top five della nuova classifica di coding dei modelli cinesi, dietro Kimi K2.6, GLM-5.1, MiMo V2.5 Pro e MiniMax 2.7.
- **2026-05-10** — ERNIE 5.1 di Baidu supera DeepSeek-V4-Pro su tau3-bench e SpreadsheetBench-Verified con solo il 6% del costo di pretraining di modelli simili.
- **2026-05-18** — DeepSeek V4 PRO gira su Mac Studio M3 Ultra con 512 GB RAM: quantizzazione 2 bit, file GGUF da 433 GB, 130 token al secondo in prefill e 13 in generazione, tutto locale senza cloud.
- **2026-05-31** — Dal 22 maggio 2026 il prezzo di V4-Pro è permanente e non più uno sconto a tempo: 0,435 dollari per milione di token in input e 0,87 in output, con SWE-bench Verified a 80,6% contro l'80,8 di Claude e un divario di circa 11,5 volte in input e fino a 28-34 volte in output. Su un carico di dieci milioni di token di output al giorno la differenza dichiarata è 261 dollari al mese contro i 7.500 di Claude; sul mercato compare anche MiniMax M3, open weights con contesto da un milione di token uscito il 1° giugno 2026.
- **2026-06-23** — DeepSeek V4 Pro è il modello di traduzione usato da Violin nel pipeline di doppiaggio automatico video.
- **2026-08-07** — I nuovi modelli Qwen 9B e 4B sono addestrati interamente su tracce di DeepSeek V4 Pro, ottimizzati per matematica e STEM, e su hardware consumer raggiungono duecentoquaranta token al secondo.

- **2026-08-12** — DeepSeek V4 Pro esce dalla preview durata quasi quattro mesi: MoE da 1,6 trilioni di parametri totali e 49 miliardi attivi per token, contesto da un milione di token e output fino a 384.000, con 80,6 per cento su SWE-bench Verified a un decimo di punto da Claude Opus 4.6 (80,8) e pari a Gemini 3.1 Pro, 93,5 per cento su LiveCodeBench e rating Codeforces di 3.206, mentre resta indietro sul ragionamento agentico a lungo orizzonte con 67,9 su Terminal Bench 2.0 contro il 75,1 di GPT-5.4.

- **2026-09-06** — DeepSeek V4 Pro segna 53,2 sull'[[artificial-analysis-intelligence-index]]: ultimo della fascia alta aperta, ma sopra quota 50, la soglia che dodici mesi prima sembrava lontana.
## Collegamenti

- [[deepseek]]
- [[ernie-5-1]]
- [[glm-5-1]]
- [[kimi-k2-6]]
- [[mimo-v2-5-pro]]
- [[minimax-m2-7]]
- [[qwen-9b]]
- [[deepseek-sparse-attention]]
- [[violin]]
- [[index]]

