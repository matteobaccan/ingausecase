---
title: "Indra"
category: modello
tags: [ocr, efficienza, locale, open-weight, vision]
related_puntate: [20261014, 20261017, 20261020]
created: 2026-10-14
updated: 2026-10-20
sources: [raw/puntate/ainews20261014.md, raw/puntate/ainews20261017.md, raw/puntate/ainews20261020.md, raw/pillitteri/pillitteri20261020-indra-ocr-1-1-80-lingue-cpu.md]
---

# Indra

## Introduzione

Modello OCR da un milione di parametri che gira su CPU: quarantanove pagine al secondo, undici volte più veloce di [[paddleocr]] e diciassette volte di [[tesseract]].

## Performance

- Su OmniParseBench batte entrambi i confronti: quarantuno punto tre contro trentacinque punto otto di PaddleOCR e diciannove punto tre di Tesseract. [Fonte: raw/puntate/ainews20261014.md]
- Layout completo e bounding box delle righe inclusi, con inferenza su CPU. [Fonte: raw/puntate/ainews20261014.md]

## Timeline delle notizie

- **2026-10-14** — Arriva Indra, modello OCR da un milione di parametri che gira su CPU a quarantanove pagine al secondo: undici volte più veloce di [[paddleocr]] e diciassette volte di [[tesseract]], e su OmniParseBench li batte entrambi (41,3 contro 35,8 e 19,3) con layout completo e bounding box delle righe. [Fonte: raw/puntate/ainews20261014.md]
- **2026-10-17** — Indra, modello OCR da un milione di parametri, è quindici volte più veloce di [[tesseract]] su CPU e molto più accurato, secondo il suo autore sorpreso dalle prestazioni. [Fonte: raw/puntate/ainews20261017.md]
- **2026-10-20** — Indra OCR 1.1 legge 44 pagine al secondo su CPU, sta a quattro punti da DeepSeek OCR 2 su OmniParseBench, è quindici volte più veloce di Tesseract, supporta oltre ottanta lingue e riconosce la scrittura a mano. [Fonte: raw/puntate/ainews20261020.md] Le note di rilascio aggiungono il 66,7 complessivo su OmniParseBench (era 62,3), la scrittura a mano al 25,2% (era 8,3%), 212 millisecondi a pagina su 4 core e una licenza divisa: codice Apache 2.0, pesi OpenRAIL-M modificata gratuiti solo per ricerca, uso personale e startup sotto i 20 milioni di dollari, con il divieto di concorrenza con l'API di Datalab. [Fonte: raw/pillitteri/pillitteri20261020-indra-ocr-1-1-80-lingue-cpu.md]







## Collegamenti

- [[paddleocr]]
- [[tesseract]]
- [[index]]
