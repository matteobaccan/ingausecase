---
title: "Unlimited-OCR"
category: modello
tags: [baidu, cina, documenti, ocr, open-source, paddlepaddle, pdf]
related_puntate: [20260623, 20260624, 20260628, 20260720, 20260727, 20260901, 20261012, 20261016, 20261019]
created: 2026-08-12
updated: 2026-10-19
---

# Unlimited-OCR

## Introduzione

Modello OCR cinese da tre miliardi di parametri che legge interi PDF da cento pagine in un'unica passata, con finestra di contesto da 32.000 token e il 93% di accuratezza, eseguibile localmente.

## Capacità e performance

- Unlimited-OCR di PaddlePaddle gestisce centinaia di pagine in un solo passaggio mantenendo velocità costante: novantatré percento su OmniDocBench; la chiave è R-SWA, che tiene la cache KV costante durante la decodifica.
- Unlimited-OCR di Baidu ha tre miliardi di parametri totali con solo cinquecento milioni attivi: elabora documenti interi in una passata unica, gestisce oltre quaranta pagine senza perdere contesto o rallentare e ottiene risultati SOTA su OmniDocBench.
- OCR dalla Cina basato su DeepSeek OCR con ottimizzazione dell'attenzione: memoria costante indipendentemente dalla lunghezza del documento, 93% su benchmark standard e meno di 0,11 di errore su 40 pagine.

## Azienda di riferimento

- [[baidu]]
- [[paddlepaddle]]

## Strumenti correlati

- [[marker-2]]
- [[r-swa]]

## Timeline delle notizie

- **2026-06-23** — Unlimited-OCR di PaddlePaddle gestisce centinaia di pagine in un solo passaggio mantenendo velocità costante: novantatré percento su OmniDocBench; la chiave è R-SWA, che tiene la cache KV costante durante la decodifica.
- **2026-06-24** — Unlimited-OCR di Baidu ha tre miliardi di parametri totali con solo cinquecento milioni attivi: elabora documenti interi in una passata unica, gestisce oltre quaranta pagine senza perdere contesto o rallentare e ottiene risultati SOTA su OmniDocBench.
- **2026-06-24** — La guida al rilascio chiarisce i contorni: pubblicato il 18 giugno 2026 con licenza MIT e pesi aperti su Hugging Face e ModelScope, pesa 3 miliardi di parametri in BF16, cioè circa 6 GB su disco, e usa una finestra di contesto da 32.768 token. Il meccanismo dichiarato tiene l'intero documento visibile come contesto ma trasporta in avanti solo una finestra scorrevole del testo generato, così la memoria non cresce a ogni token in uscita; i credit del repository citano DeepSeek-OCR, DeepSeek-OCR-2 e PaddleOCR.
- **2026-06-24** — Si usa in due modi: la libreria Transformers per la singola immagine o lo script `infer.py` per cartelle e PDF multipagina, con PyMuPDF a convertire le pagine e il supporto a SGLang per volumi alti; le modalità gundam (ritaglio a 640, pagine dense) e base (1024 sulla pagina intera, layout complessi) scelgono il compromesso tra velocità e precisione. L'aggiornamento del 15 luglio 2026 porta le stelle da 4.663 a 14.259.
- **2026-06-28** — OCR dalla Cina basato su DeepSeek OCR con ottimizzazione dell'attenzione: memoria costante indipendentemente dalla lunghezza del documento, 93% su benchmark standard e meno di 0,11 di errore su 40 pagine.
- **2026-07-20** — Unlimited-OCR processa PDF da cento pagine in un colpo solo: trentaduemila token di contesto, multilingua, zero costi e un virgola nove milioni di download.
- **2026-07-27** — Progetto cinese Unlimited-OCR: tre miliardi di parametri, legge interi PDF da cento pagine in un'unica passa senza tagliare pagina per pagina; finestra di contesto da 32.000 token, 93% di accuratezza, gira localmente, gratis per sempre.
- **2026-09-01** — Unlimited-OCR di Baidu ha raggiunto 24.000 stelle: elabora PDF lunghi centinaia di pagine in un'unica passa. Disponibile su Hugging Face, ModelScope e Baidu Cloud. Supporta Transformers, vLLM e SGLang.
- **2026-10-12** — Unlimited-OCR di Baidu resta a tre miliardi di parametri e legge PDF fino a cento pagine in un'unica passata con 32.000 token di contesto: 94 per cento di accuratezza sui test standard e costo zero per mille pagine contro i quindici dollari dei servizi cloud tradizionali.
- **2026-10-16** — Unlimited-OCR di [[baidu]]: 1,2 milioni di download in un mese, pesi aperti con licenza MIT, testo pulito con tabelle e formule da documenti, foto e PDF multipagina. Processa PDF interi in una passata, da 3.000 milioni di parametri su GPU normale.
- **2026-10-19** — [[unlimited-ocr|Unlimited-OCR]] è un modello da tre miliardi di parametri di un team cinese che legge interi PDF da cento pagine in una sola passata mantenendo il contesto tra le pagine, con accuratezza del novantatré per cento sui benchmark standard e tasso di errore sotto lo zero virgola undici su documenti oltre le quaranta pagine. Funziona interamente in locale e supporta Transformers, vLLM, SGLang, Docker, Ollama e llama.cpp; su Hugging Face ha superato un milione novecentomila download.










## Collegamenti

- [[baidu]]
- [[deepseek-ocr]]
- [[marker-2]]
- [[mistral-ocr-4]]
- [[paddlepaddle]]
- [[r-swa]]
- [[surya-ocr]]
- [[index]]

