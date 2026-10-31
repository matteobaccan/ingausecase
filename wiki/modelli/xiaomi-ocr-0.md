---
title: "Xiaomi-OCR-0"
category: modello
tags: [ocr, open-source, documenti, edge, cina]
related_puntate: []
created: 2026-10-31
updated: 2026-10-31
sources: [raw/pillitteri/pillitteri20261030-xiaomi-ocr-0-ocr-open-source.md]
---

# Xiaomi-OCR-0

## Introduzione

Modello open source da 0,8 miliardi di parametri che legge i documenti e restituisce Markdown, tabelle, formule in LaTeX e campi in JSON, oltre a rispondere a domande sul contenuto. Pubblicato da [[xiaomi]] il 30 ottobre 2026 con licenza Apache 2.0, parte da Qwen3.5-0.8B-Base e arriva insieme a un servizio MCP e a una Agent Skill. [Fonte: raw/pillitteri/pillitteri20261030-xiaomi-ocr-0-ocr-open-source.md]

## Capacità e performance

- Tre compiti in un solo modello: parsing della pagina in Markdown con tabelle in OTSL, estrazione di informazioni chiave in JSON e risposta a domande su immagini di testo.
- La scheda dichiara 96,83 su OmniDocBench v1.6, 95,24 su Real5-OmniDocBench e 87,94 su Wild-OmniDocBench, più una media di 83,2 su cinque benchmark di domande sui documenti.
- Nella classifica pubblica di Real5-OmniDocBench lo stesso modello compare con 92,73, secondo dietro PaddleOCR-VL-1.6 a 93,19, perché la versione del codice di valutazione non è la stessa.

## Disponibilità

Pesi su Hugging Face con licenza Apache 2.0 e codice su GitHub, con demo su Hugging Face Spaces; in locale servono SGLang, vLLM o Ollama, mentre con Transformers il modello parte anche su CPU e il pacchetto GGUF della comunità occupa circa 1,8 GB. [Fonte: raw/pillitteri/pillitteri20261030-xiaomi-ocr-0-ocr-open-source.md]

## Azienda di riferimento

- [[xiaomi]]

## Timeline delle notizie

- **2026-10-30** — Xiaomi ha presentato il modello su X insieme a un servizio MCP e a una Agent Skill, mentre i pesi erano già su Hugging Face dal 30 settembre: al 30 ottobre il repository conta 219 stelle e 12 fork. Le etichette dei 170 milioni di esempi di addestramento sono prodotte da otto modelli OCR esperti e tenute solo dove tre concordano, e cinque di quegli otto compaiono fra i modelli del confronto. [Fonte: raw/pillitteri/pillitteri20261030-xiaomi-ocr-0-ocr-open-source.md]

## Collegamenti

- [[xiaomi]]
- [[ocr-locale]]
- [[paddleocr-vl-1-6]]
- [[index]]
