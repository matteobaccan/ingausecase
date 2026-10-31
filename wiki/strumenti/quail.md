---
title: "Quail"
category: strumento
tags: [inferenza, performance, gpu, vllm, modal]
related_puntate: []
created: 2026-09-28
updated: 2026-09-28
---

# Quail

## Introduzione

QUery-Aware Inference Layer: motore di inferenza presentato nel blog di Modal che combina un query planner e un motore di esecuzione per aumentare il throughput su hardware fisso.

## Funzionalità principali

- Supera il miliardo di token processati al minuto su una singola GPU H100.
- Oltre dieci volte più veloce della baseline vLLM sullo stesso hardware.
- Costa meno di 0,06 dollari per miliardo di token su Modal.

## Timeline delle notizie

- **2026-09-28** — Modal presenta Quail, il layer di inferenza che unisce un query planner a un motore di esecuzione e arriva a oltre un miliardo di token al minuto su una singola H100, più di dieci volte la baseline vLLM sullo stesso hardware e sotto i 0,06 dollari per miliardo di token.

## Riferimenti

- https://modal.com/blog/quail-billion-tpm

## Collegamenti

- [[vllm]]
- [[ai-locale]]
- [[index]]
