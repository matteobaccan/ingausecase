---
title: "parakeet.cpp"
category: strumento
tags: [asr, cpp, inferenza, nvidia]
related_puntate: [20260601, 20260607]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260601.md, raw/puntate/ainews20260607.md]
---

# parakeet.cpp

## Introduzione

Implementazione C++ di inferenza per i modelli Parakeet di NVIDIA, senza dipendenze Python, con output identico a NeMo.

## Funzionalità principali

- parakeet.cpp offre inferenza nativa C++ per i modelli Parakeet di NVIDIA, senza Python, con output identico byte per byte a NeMo ma più veloce; gira su CPU e GPU e i modelli GGUF quantizzati sono su Hugging Face.
- parakeet.cpp esegue Nemotron 3.5 ASR su CPU normale, due volte e mezzo più veloce del runtime ufficiale di NVIDIA con lo stesso output byte per byte.

## Azienda / Autore

- [[hugging-face]]
- [[nvidia]]

## Modelli supportati / correlati

- [[nemotron-3-5-asr]]
- [[parakeet]]

## Timeline delle notizie

- **2026-06-01** — parakeet.cpp offre inferenza nativa C++ per i modelli Parakeet di NVIDIA, senza Python, con output identico byte per byte a NeMo ma più veloce; gira su CPU e GPU e i modelli GGUF quantizzati sono su Hugging Face. [Fonte: raw/puntate/ainews20260601.md]
- **2026-06-07** — parakeet.cpp esegue Nemotron 3.5 ASR su CPU normale, due volte e mezzo più veloce del runtime ufficiale di NVIDIA con lo stesso output byte per byte. [Fonte: raw/puntate/ainews20260607.md]

## Collegamenti

- [[hugging-face]]
- [[nemo]]
- [[nemotron-3-5-asr]]
- [[nvidia]]
- [[parakeet]]
- [[index]]

