---
title: "GLM-OCR"
category: modello
tags: [zhipu, ocr, documenti, open-source, vision-language]
related_puntate: []
created: 2026-10-19
updated: 2026-10-19
sources: [raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]
---

# GLM-OCR

## Introduzione

Modello OCR visione-linguaggio di Z.ai (Zhipu) da 0,9 miliardi di parametri, con pesi sotto licenza MIT e codice Apache 2.0. Il report tecnico è del marzo 2026 (arXiv 2603.10910). [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Capacità e performance

- Segna 95,22 su OmniDocBench v1.6, terzo posto dietro PaddleOCR-VL-1.6 e MinerU2.5-Pro; sulla versione 1.5 del benchmark il punteggio era 94,62, quindi i numeri di versioni diverse non vanno confrontati. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]
- Si avvia con vLLM 0.19 o successivo, SGLang 0.5.10 o successivo, Ollama e, su Mac, con mlx-vlm; il rilevatore di layout può girare su CPU con l'opzione --layout-device cpu. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Limiti

- Il repository non dichiara né le lingue supportate né la VRAM minima, quindi il test sul proprio hardware va fatto prima di acquistare una scheda o affittare un server. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Timeline delle notizie

- **2026-10-19** - La guida ai migliori OCR locali del 2026 colloca GLM-OCR al terzo posto su OmniDocBench v1.6 con 95,22, con pesi MIT e codice Apache 2.0 e supporto a vLLM, SGLang, Ollama e MLX-VLM, ma senza indicazioni su lingue e memoria minima. [Fonte: raw/pillitteri/pillitteri20261019-migliori-ocr-locali-pc-server.md]

## Collegamenti

- [[ocr-locale]]
- [[z-ai|Z.ai]]
- [[index]]
