---
title: "Mistral OCR 4"
category: modello
tags: [documenti, mistral, multilingue, ocr, open-source]
related_puntate: [20260624, 20260628]
created: 2026-08-12
updated: 2026-09-17
---

# Mistral OCR 4

## Introduzione

Modello OCR di Mistral AI con supporto di 170 lingue, capace di convertire documenti scritti a mano in LaTeX e di rilevare equazioni, tabelle, firme, titoli e grafici con bounding box.

## Capacità e performance

- Mistral OCR 4 riconosce testo in centosettanta lingue, classifica blocchi e genera bounding box con punteggi di confidenza inline; completamente open source.
- Ha convertito un esame di calcolo scritto a mano in LaTeX pulito in 5,1 secondi. Supporta 170 lingue, 85,20 su OlmOCRBench; rileva equazioni, tabelle, firme, titoli e grafici con bounding box.
- I numeri della presentazione del 23 giugno 2026 aggiungono il 93,07 su OmniDocBench, lo 0,98 sul Crawl Multilingual interno e una preferenza del 72% in un test alla cieca su oltre 600 documenti reali in più di 12 lingue; l'output esce in Markdown e JSON strutturato, gira in un singolo container (self-hosting per sanità, PA e studi legali) e costa 4 dollari ogni 1.000 pagine (2 con l'API Batch, 5 in modalità Document AI completa). È il componente di ingestion del nuovo Search Toolkit open source di Mistral, che copre ingestion, retrieval ed evaluation. Un aggiornamento successivo, OCR 4.1, migliora i bounding box sulle pagine fitte e annotate.
- **OCR 4.1** (13 agosto 2026) è una revisione mirata e non un modello nuovo: sulle pagine dense e cariche di annotazioni — contratti firmati, referti con timbri, moduli compilati a penna, scansioni con evidenziatore — i riquadri non derivano più di qualche pixel e non contengono immagini annidate, un riquadro per elemento. Endpoint, identificativo di listino (`mistral-ocr-latest`, con `mistral-ocr-4-0` dietro), velocità e prezzi restano quelli di OCR 4. Restano anche i numeri di giugno: 85,20 su OlmOCRBench, 93,07 su OmniDocBench, 72% di preferenza umana, 170 lingue in 10 famiglie e blocchi tipizzati con il parametro `table_format` per tabelle in testo grezzo, Markdown o HTML. Il listino è a pagina, non a token: 4 dollari ogni 1.000 pagine (2 in Batch API, 5 in Document AI), mentre la generazione precedente costava la metà.

## Azienda di riferimento

- [[mistral]]

## Strumenti correlati

- [[liteparse]]

## Timeline delle notizie

- **2026-06-24** — Mistral OCR 4 riconosce testo in centosettanta lingue, classifica blocchi e genera bounding box con punteggi di confidenza inline; completamente open source.
- **2026-06-24** — Presentazione ufficiale di Mistral OCR 4 (23 giugno 2026): 85,20 su OlmOCRBench e 72% di preferenza in un test alla cieca su oltre 600 documenti reali in più di 12 lingue, 93,07 su OmniDocBench, 170 lingue su 10 gruppi linguistici con cura particolare per quelle rare (hindi, giapponese, georgiano, bengalese, armeno, ebraico, greco, gujarati, tamil, malayalam, kannada, telugu). Restituisce bounding box, blocchi tipizzati e confidence score inline, si installa in un singolo container e costa 4 dollari ogni 1.000 pagine (2 in batch, 5 in modalità Document AI), ed è il componente di ingestion del Search Toolkit open source di Mistral.
- **2026-06-28** — Ha convertito un esame di calcolo scritto a mano in LaTeX pulito in 5,1 secondi. Supporta 170 lingue, 85,20 su OlmOCRBench; rileva equazioni, tabelle, firme, titoli e grafici con bounding box.

- **2026-08-13** — Mistral pubblica Mistral OCR 4.1, aggiornamento di OCR 4 mirato alle pagine fitte e annotate: i bounding box si allineano al singolo elemento senza deriva e senza figure annidate una dentro l'altra, così una citazione visiva punta alla frase giusta. Prestazioni, endpoint, velocità e prezzi non cambiano e chi chiama l'alias `mistral-ocr-latest` riceve il modello aggiornato senza toccare il codice; il prezzo resta a pagina (4 dollari ogni 1.000, 2 in batch, 5 in Document AI) e il modello è raggiungibile dall'API Mistral, da Document AI in Mistral Studio, su Amazon SageMaker e Microsoft Foundry.

## Collegamenti

- [[annota-ai]]
- [[liteparse]]
- [[mistral]]
- [[surya-ocr]]
- [[unlimited-ocr]]
- [[index]]

