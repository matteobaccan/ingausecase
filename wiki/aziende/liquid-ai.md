---
title: "Liquid AI"
category: azienda
tags: [liquid-ai, efficiente, efficienza, lfm, llm, modello, open-source, startup, usa, vlm]
related_puntate: [20260528, 20260607, 20260611, 20260620, 20260626, 20260701, 20260708, 20260722, 20260729, 20260805, 20260806, 20261008, 20261016]
created: 2026-08-12
updated: 2026-10-28
sources: [raw/puntate/ainews20260528.md, raw/puntate/ainews20260607.md, raw/puntate/ainews20260611.md, raw/puntate/ainews20260620.md, raw/puntate/ainews20260626.md, raw/puntate/ainews20260701.md, raw/puntate/ainews20260708.md, raw/puntate/ainews20260722.md, raw/puntate/ainews20260729.md, raw/puntate/ainews20260805.md, raw/puntate/ainews20260806.md, raw/tldr/tldr20261006.md, raw/puntate/ainews20261008.md, raw/tldr/tldr20261008.md, raw/puntate/ainews20261016.md, raw/pillitteri/pillitteri20261019-lfm25-24b-a2b-ram-liquid-ai.md, raw/tldr/tldr20261028.md]
---

# Liquid AI

## Introduzione

Azienda AI statunitense specializzata in modelli efficienti e architetture non-transformer, con la famiglia LFM. Nel periodo ha raddoppiato il tokenizer di LFM 2.5-8B-A1B e ha rilasciato gli encoder bidirezionali LFM 2.5 da 230M e 350M.

## Modelli

- [[eney]]
- [[lfm-2-5]]
- [[lfm-2-5-230m]]
- [[lfm-2-5-26b]]
- [[lfm-2-5-24b-a2b]]
- [[lfm-2-5-audio-1-5b]]
- [[lfm-2-5-colbert]]
- [[lfm-2-5-vl-1-6b]]
- [[lfm3]]

## Strumenti

- [[antidoom]]
- [[claude-code]]
- [[ifstruct]]

## Timeline delle notizie

- **2026-05-28** — Liquid AI ha rilasciato LFM 2.5 VL 1.6B: visual language model piccolo, fine-tuned su dataset custom, con accuratezza pari a GPT-5, costo cinquanta volte inferiore ed esecuzione locale full speed via llama.cpp. [Fonte: raw/puntate/ainews20260528.md]
- **2026-06-07** — Liquid AI ha presentato due nuovi modelli giapponesi: LFM 2.5 Audio 1.5B e LFM 2.5 1.2B. [Fonte: raw/puntate/ainews20260607.md]
- **2026-06-11** — Liquid AI presenta LFM2.5-1.5B specializzato in giapponese. [Fonte: raw/puntate/ainews20260611.md]
- **2026-06-20** — Liquid AI ha mostrato come LFM due punto cinque-ColBERT riduce la latenza filtrando i tool meno rilevanti: su centocinquantuno opzioni disponibili seleziona solo i cinque più utili prima di passarli al modello. [Fonte: raw/puntate/ainews20260620.md]
- **2026-06-26** — Liquid AI lancia LFM due punto cinque-duecentotrenta M, modello compatto per robotica ed e-commerce. [Fonte: raw/puntate/ainews20260626.md]
- **2026-07-01** — Ha rilasciato IFStruct, benchmark per output strutturati, dove un modello da 350 milioni di parametri addestrato su di esso supera modelli dieci volte più grandi. [Fonte: raw/puntate/ainews20260701.md]
- **2026-07-08** — Ha rilasciato Antidoom, metodo open source che rimuove il doom loop nei modelli di ragionamento. [Fonte: raw/puntate/ainews20260708.md]
- **2026-07-22** — Ha raddoppiato il tokenizer di LFM 2.5-8B-A1B: da 65.000 a 128.000 token. Il thai ora richiede quattro volte meno token e il vietnamita 2,6 volte meno. [Fonte: raw/puntate/ainews20260722.md]
- **2026-07-29** — Ha rilasciato gli encoder LFM 2.5-Encoder da 230M e 350M: encoder bidirezionali veloci su contesti lunghi anche su CPU; il modello da 230M è 3,7 volte più veloce di ModernBERT-base su CPU a 8.192 token. [Fonte: raw/puntate/ainews20260729.md]
- **2026-08-05** — Liquid AI ha rilasciato il modello agentico LFM due punto cinque-due punto sei B, che gira completamente on-device con dati mai fuori dal dispositivo. [Fonte: raw/puntate/ainews20260805.md]
- **2026-08-06** — Liquid AI entra in partnership con MacPaw per modelli foundation specializzati per macOS: il modello Eney arrivera' a fine anno, con dati sul dispositivo, risposte veloci e niente cloud. [Fonte: raw/puntate/ainews20260806.md]
- **2026-09-30** — Il decision model d1 dichiara di superare Jev sul Decision Index di Hugging Face ed è disponibile sull'API di Liquid, con l'arrivo su OpenRouter in arrivo. [Fonte: raw/tldr/tldr20260930.md]
- **2026-10-06** — Il decision model d1 acquisisce il supporto alle immagini: accetta immagini, testo o entrambi, costa da 19 a 200 volte meno di GPT-6.1 Sol e Claude Opus 5.5 e risponde in 200-300 millisecondi sulle decisioni testuali, senza generare token. [Fonte: raw/tldr/tldr20261006.md]
- **2026-10-08** — Liquid AI rilascia Open d1, due modelli multimodali open-weight della famiglia d1 pensati per le decisioni in tempo reale: d1-3B supporta testo e visione, d1-OMNI-600M testo più immagine o testo più audio, e possono girare dai sistemi NVIDIA DGX alle workstation RTX e ai dispositivi Jetson edge. [Fonte: raw/puntate/ainews20261008.md] [Fonte: raw/tldr/tldr20261008.md]
- **2026-10-16** — d-uno-ultra, il modello decisionale più potente della casa: multimodale in 44 lingue, primo sul Decision Index di Artificial Analysis con 65 punti e primo in tutte le 8 categorie della suite da 112 valutazioni. [Fonte: raw/puntate/ainews20261016.md]
- **2026-10-20** — Le misure sul campo di LFM2.5-24B-A2B su un Mac con M4 e 32 GB danno 47-50 token al secondo con la versione MLX a 4 bit e un picco di 14,5 GB su un prompt da 2.596 token, contro i 184 token al secondo dichiarati dall'azienda su un M5 Max; la licenza LFM Open v1.0 esclude l'uso commerciale per chi supera i 10 milioni di dollari di ricavi annui. [Fonte: raw/pillitteri/pillitteri20261019-lfm25-24b-a2b-ram-liquid-ai.md]
- **2026-10-28** — Lancia [[lfm3]], famiglia open weight costruita su un backbone tri-hybrid condiviso fra testo, visione, audio, omni e modelli decisionali: il modello di testo da 1,7 miliardi di parametri batte il predecessore da 2,6 miliardi con il 35 per cento in meno di parametri, sta in circa un gigabyte a 4 bit e regge 256.000 token di contesto per agenti on-device. LFM3-VL-2B aggiunge l'input video e pareggia Gemma 4 12B su 62 benchmark di visione, e ogni modello della famiglia si fine-tuna su una singola GPU. [Fonte: raw/tldr/tldr20261028.md]



















## Collegamenti

- [[antidoom]]
- [[claude-code]]
- [[eney]]
- [[ifstruct]]
- [[lfm-2-5]]
- [[lfm-2-5-230m]]
- [[lfm-2-5-26b]]
- [[lfm-2-5-24b-a2b]]
- [[lfm-2-5-audio-1-5b]]
- [[lfm-2-5-colbert]]
- [[lfm-2-5-vl-1-6b]]
- [[macpaw]]
- [[d-uno-ultra]]
- [[index]]

