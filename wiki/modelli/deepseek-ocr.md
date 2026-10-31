---
title: "DeepSeek-OCR"
category: modello
tags: [cina, deepseek, efficienza, ocr, open-source]
related_puntate: [20260626, 20260628]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260626.md, raw/puntate/ainews20260628.md]
---

# DeepSeek-OCR

## Introduzione

Modello OCR di DeepSeek che legge un'immagine compressa del testo: 64 vision token per pagina con accuratezza del 97%.

## Capacità e performance

- DeepSeek-OCR legge documenti usando dieci volte meno token: il modello legge un'immagine compressa del testo invece del testo stesso; una pagina diventa sessantaquattro vision token con accuratezza del novantasette percento, a duemilacinquecento token al secondo su vLLM.
- Serve come base per Unlimited OCR, che lo usa con ottimizzazioni dell'attenzione per ottenere memoria costante e 93% sui benchmark standard.

## Azienda di riferimento

- [[deepseek]]

## Strumenti correlati

- [[vllm]]

## Timeline delle notizie

- **2026-06-26** — DeepSeek-OCR legge documenti usando dieci volte meno token: il modello legge un'immagine compressa del testo invece del testo stesso; una pagina diventa sessantaquattro vision token con accuratezza del novantasette percento, a duemilacinquecento token al secondo su vLLM. [Fonte: raw/puntate/ainews20260626.md]
- **2026-06-28** — Serve come base per Unlimited OCR, che lo usa con ottimizzazioni dell'attenzione per ottenere memoria costante e 93% sui benchmark standard. [Fonte: raw/puntate/ainews20260628.md]

## Collegamenti

- [[deepseek]]
- [[unlimited-ocr]]
- [[vllm]]
- [[index]]

