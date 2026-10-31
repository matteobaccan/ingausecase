---
title: "Tesseract OCR"
category: strumento
tags: [ocr, open-source, pdf, cpu, lingue]
related_puntate: []
created: 2026-10-19
updated: 2026-10-19
sources: [raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]
---

# Tesseract OCR

## Introduzione

Motore di riconoscimento ottico dei caratteri open source, uno dei più usati, con oltre 77.000 stelle su GitHub al 19 ottobre 2026 e licenza Apache 2.0. Riconosce più di cento lingue senza addestramento aggiuntivo e dalla versione 4 usa una rete neurale LSTM che lavora per righe di testo; la versione 5 è quella stabile. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Funzionalità principali

- Non ha interfaccia grafica e il README avverte che per ottenere buoni risultati spesso bisogna prima migliorare la qualità dell'immagine. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]
- Legge righe di testo, non tabelle, colonne o formule: il suo limite sta nella struttura, non nella lingua. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]
- Il modo più comodo per usarlo è OCRmyPDF, che aggiunge uno strato di testo ai PDF scansionati, li rende ricercabili, raddrizza le pagine inclinate, produce PDF/A e distribuisce il lavoro su più core; richiede Ghostscript e per l'italiano si usa l'opzione -l ita con il pacchetto lingua installato. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]
- Alcuni plugin di OCRmyPDF sostituiscono Tesseract con altri motori, tra cui PaddleOCR accelerato da GPU, EasyOCR e, solo su macOS, Apple Vision. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Limiti

- Non capisce tabelle, formule né colonne, quindi per documenti complessi serve un modello visione-linguaggio. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]
- Non inventa parole: le parole illeggibili le segnala come incerte o le sbaglia in modo riconoscibile, un vantaggio per testi legali e contabili rispetto ai modelli generativi. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Timeline delle notizie

- **2026-10-19** - La guida ai migliori OCR locali del 2026 conferma Tesseract con OCRmyPDF come scelta per i PC senza scheda video: costa zero, legge oltre cento lingue e produce un PDF ricercabile, ma non capisce tabelle né impaginazione. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Collegamenti

- [[ocr-locale]]
- [[open-source]]
- [[index]]
