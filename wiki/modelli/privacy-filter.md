---
title: "Privacy Filter"
category: modello
tags: [on-device, open-source, pii, privacy]
related_puntate: [20260528]
created: 2026-08-12
updated: 2026-09-27
sources: [raw/puntate/ainews20260528.md, raw/pillitteri/pillitteri20260730-rizzo-pii-anonimizzazione-pii-locale-italiano.md, raw/pillitteri/pillitteri20260423-openai-privacy-filter-pii-masking-offline-gpu-cpu.md]
---

# Privacy Filter

## Introduzione

Modello open source di OpenAI (Apache 2.0, 1,5B) che individua e rimuove dati personali, eseguibile interamente nel browser via WebGPU senza server.

## Capacità e performance

- Privacy Filter di OpenAI è il primo modello open-source del 2026: Apache 2.0, 1,5 miliardi di parametri, trova e rimuove dati personali (nome, indirizzo, telefono, email, documenti), gira completamente nel browser via WebGPU con zero server, è multilingua e pensato per compliance e flussi privacy-first.

## Azienda di riferimento

- [[openai]]

## Timeline delle notizie

- **2026-04-23** — Il lancio dietro il modello: pubblicato il 22 aprile 2026 con licenza Apache 2.0, è un classificatore di token bidirezionale con decoder di span, 33 etichette (otto categorie PII per i quattro tag di boundary BIOES), finestra di contesto a 128.000 token e architettura Sparse Mixture-of-Experts da 1,5 miliardi di parametri totali con 50 milioni attivi per token, 128 esperti e routing top-4. OpenAI lo dichiara al 96 per cento di F1 su PII-Masking-300k e al 97,43 su una versione corretta del benchmark. [Fonte: raw/pillitteri/pillitteri20260423-openai-privacy-filter-pii-masking-offline-gpu-cpu.md]
- **2026-04-23** — I requisiti reali sono bassi: da 3 a 4 GB di VRAM in FP16 su GPU, circa 2 GB con quantizzazione INT8, 4-8 GB di RAM su CPU e 2-3 GB via WebGPU nel browser, con oltre 1.500 token al secondo su GPU; si installa con il pacchetto Python `opf` e si può fare fine-tuning su dataset propri. OpenAI chiarisce che il filtro esegue pseudonimizzazione e non anonimizzazione, quindi i dati restano nel perimetro del GDPR, e riconosce che può mancare identificatori insoliti, sovra-redigere sulle frasi brevi ed è più forte in inglese. [Fonte: raw/pillitteri/pillitteri20260423-openai-privacy-filter-pii-masking-offline-gpu-cpu.md]
- **2026-05-28** — Privacy Filter di OpenAI è il primo modello open-source del 2026: Apache 2.0, 1,5 miliardi di parametri, trova e rimuove dati personali (nome, indirizzo, telefono, email, documenti), gira completamente nel browser via WebGPU con zero server, è multilingua e pensato per compliance e flussi privacy-first. [Fonte: raw/puntate/ainews20260528.md]
- **2026-07-30** — Nel confronto tra gli strumenti PII già recensiti, OpenAI Privacy Filter ha il vantaggio dell'architettura sparsa (1,5 miliardi di parametri totali, circa 50 milioni attivi per token) che regge bene i volumi alti, ma copre otto categorie generiche pensate per l'inglese: il codice fiscale semplicemente non esiste nel suo vocabolario, e la verifica di checksum manca. È il confronto che emerge dalla recensione di rizzo-pii, il modello italiano da 0,3 miliardi di parametri con 22 categorie e i cinque identificativi dello studio professionale italiano. [Fonte: raw/pillitteri/pillitteri20260730-rizzo-pii-anonimizzazione-pii-locale-italiano.md]

## Collegamenti

- [[openai]]
- [[index]]

