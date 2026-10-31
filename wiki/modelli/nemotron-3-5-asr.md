---
title: "Nemotron 3.5 ASR"
category: modello
tags: [asr, cpu, nvidia, open-weight, speech, streaming]
related_puntate: [20260607, 20260611, 20260617, 20260624]
created: 2026-08-12
updated: 2026-10-03
sources: [raw/puntate/ainews20260607.md, raw/puntate/ainews20260611.md, raw/puntate/ainews20260617.md, raw/puntate/ainews20260624.md, raw/pillitteri/pillitteri20260617-nemotron-3-5-asr-nvidia-trascrizione-40-lingue.md]
---

# Nemotron 3.5 ASR

## Introduzione

Modello NVIDIA di speech recognition da 0.6 miliardi di parametri, multilingue e a esecuzione su CPU pura.

## Capacità e performance

- Nemotron 3.5 ASR ha seicento milioni di parametri, copre oltre quaranta lingue e funziona in streaming; parakeet.cpp lo esegue su CPU normale a due volte e mezzo la velocità del runtime ufficiale con lo stesso output.
- Nemotron-3.5-ASR ha zero virgola sei miliardi di parametri, oltre quaranta lingue e streaming real-time: richiede solo CPU ed è due punto cinque volte più veloce del runtime NeMo ufficiale con risultati identici; offline.
- NVIDIA ha rilasciato Nemotron-3.5-ASR, modello di speech recognition da zero punto sei miliardi di parametri: oltre quaranta lingue supportate, output streaming real-time, gira su CPU pura senza GPU ed è due punto cinque volte più veloce del runtime Nemo ufficiale con risultati identici.

## Azienda di riferimento

- [[nvidia]]

## Strumenti correlati

- [[nemo]]
- [[parakeet-cpp]]

## Timeline delle notizie

- **2026-06-07** — Nemotron 3.5 ASR ha seicento milioni di parametri, copre oltre quaranta lingue e funziona in streaming; parakeet.cpp lo esegue su CPU normale a due volte e mezzo la velocità del runtime ufficiale con lo stesso output. [Fonte: raw/puntate/ainews20260607.md]
- **2026-06-11** — Nemotron-3.5-ASR ha zero virgola sei miliardi di parametri, oltre quaranta lingue e streaming real-time: richiede solo CPU ed è due punto cinque volte più veloce del runtime NeMo ufficiale con risultati identici; offline. [Fonte: raw/puntate/ainews20260611.md]
- **2026-06-17** — NVIDIA ha rilasciato Nemotron-3.5-ASR, modello di speech recognition da zero punto sei miliardi di parametri: oltre quaranta lingue supportate, output streaming real-time, gira su CPU pura senza GPU ed è due punto cinque volte più veloce del runtime Nemo ufficiale con risultati identici. [Fonte: raw/puntate/ainews20260617.md]
- **2026-06-17** — NVIDIA pubblica su Hugging Face i pesi aperti di Nemotron 3.5 ASR: architettura Cache-Aware FastConformer-RNNT, 40 combinazioni lingua-locale su tre fasce di qualità (19 transcription-ready, 13 broad-coverage, 8 adaptation-ready), latenza sotto i 100 millisecondi con finestre di contesto regolabili da 80 a 1120 millisecondi e WER del 4,25% sull'italiano. Su una singola GPU H100 sostiene circa 240 stream alla finestra da 80 ms contro i 14 di un Parakeet RNNT da 1,1 miliardi. [Fonte: raw/pillitteri/pillitteri20260617-nemotron-3-5-asr-nvidia-trascrizione-40-lingue.md]



- **2026-06-17** — L'esecuzione su CPU senza GPU riguarda il modello solo inglese nemotron-speech-streaming-en-0.6b, portato su ONNX Runtime da un gruppo di Microsoft CoreAI con quantizzazione a 4 bit (da 2,47 a 0,67 GB): le varianti ONNX superano un RTFx di 6 su CPU e la versione a 4 bit ottiene WER 8,20% contro 8,03% della FP32, non il modello a 40 lingue e non una velocità di 2,5 volte il runtime NeMo. [Fonte: raw/pillitteri/pillitteri20260617-nemotron-3-5-asr-nvidia-trascrizione-40-lingue.md]

- **2026-06-24** — Nemotron-3.5-ASR di NVIDIA è un modello speech recognition da zero virgola sei miliardi di parametri: oltre quaranta lingue, latenza configurabile fino a ottanta millisecondi e diciassette volte più stream concorrenti rispetto ai modelli precedenti da uno virgola uno miliardi. [Fonte: raw/puntate/ainews20260624.md]

## Collegamenti

- [[nemo]]
- [[nvidia]]
- [[parakeet-cpp]]
- [[index]]

- [[nemotron-3-5-transcribe]]
