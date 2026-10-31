---
title: "vLLM-Omni"
category: strumento
tags: [inferenza, llm, multimodale, omni, open-source, serving, tts]
related_puntate: [20260509, 20260609]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260509.md, raw/puntate/ainews20260609.md]
---

# vLLM-Omni

## Introduzione

Servizio di inferenza open source per modelli multimodali (Qwen3-Omni, TTS) basato su vLLM upstream, con scalabilità su H20 e NPU.

## Funzionalità principali

- vLLM-Omni v0.20.0, allineato con vLLM upstream v0.20.0, offre Qwen3-Omni throughput +72% su H20 via multi-replica talker/code2wav, TTS più veloce e leggero (VoxCPM2 RTF da 0,946 a 0,106, Fish Speech Fast AR latency -53%, Qwen3-TTS/Voxtral-TTS Code2Wav risparmia circa 3,2GB), diffusion dynamic step-level batching +7,8% throughput e -5,8% latency, e Wan2.2 su NPU production-ready con +50-60% performance.
- vLLM-Omni 0.22.0 ha supporto day-zero per Cosmos 3 di NVIDIA (testo, immagini, audio, video e azioni in entrata e uscita), serving robotica con DreamZero e OpenPI, TTS con Qwen3-TTS, Qwen3-Omni e VoxCPM2; trecentotrentanove commit e centoventiquattro contributor.

## Azienda / Autore

- [[nvidia]]

## Timeline delle notizie

- **2026-05-09** — vLLM-Omni v0.20.0, allineato con vLLM upstream v0.20.0, offre Qwen3-Omni throughput +72% su H20 via multi-replica talker/code2wav, TTS più veloce e leggero (VoxCPM2 RTF da 0,946 a 0,106, Fish Speech Fast AR latency -53%, Qwen3-TTS/Voxtral-TTS Code2Wav risparmia circa 3,2GB), diffusion dynamic step-level batching +7,8% throughput e -5,8% latency, e Wan2.2 su NPU production-ready con +50-60% performance. [Fonte: raw/puntate/ainews20260509.md]
- **2026-06-09** — vLLM-Omni 0.22.0 ha supporto day-zero per Cosmos 3 di NVIDIA (testo, immagini, audio, video e azioni in entrata e uscita), serving robotica con DreamZero e OpenPI, TTS con Qwen3-TTS, Qwen3-Omni e VoxCPM2; trecentotrentanove commit e centoventiquattro contributor. [Fonte: raw/puntate/ainews20260609.md]

## Collegamenti

- [[nvidia]]
- [[index]]

