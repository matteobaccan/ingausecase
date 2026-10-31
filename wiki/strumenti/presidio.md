---
title: "Presidio"
category: strumento
tags: [open-source, privacy, pii, gdpr]
created: 2026-10-03
updated: 2026-10-02
source_note: "sources"
sources: [raw/pillitteri/pillitteri20260619-microsoft-presidio-pii-protezione-dati.md, raw/pillitteri/pillitteri20261002-anonimizzare-dati-clienti-ai-gdpr.md]
---

# Presidio

## Introduzione

Framework open source (licenza MIT) per individuare e rimuovere informazioni personali (PII) da testi, immagini e dati strutturati prima che raggiungano un modello. Nato in casa Microsoft e oggi passato all'organizzazione indipendente Data Privacy Stack, gira interamente sulla propria infrastruttura, quindi i dati non escono dai propri server.

## Funzionalità principali

- Si compone di quattro moduli: Analyzer (motore di rilevamento), Anonymizer (trasformazione con operatori configurabili), Image Redactor (OCR e oscuramento sui pixel) e Structured (dati tabellari e semi-strutturati). [Fonte: raw/pillitteri/pillitteri20260619-microsoft-presidio-pii-protezione-dati.md]
- L'Analyzer combina quattro metodi: riconoscimento di entità nominate (spaCy, Transformers o Stanza), espressioni regolari, logica a regole con analisi del contesto e controllo tramite checksum. [Fonte: raw/pillitteri/pillitteri20260619-microsoft-presidio-pii-protezione-dati.md]
- Nella maggior parte dei casi fa pseudonimizzazione e non anonimizzazione ai sensi del GDPR: va inquadrato come misura tecnica a supporto della minimizzazione dei dati e della privacy by design, non come una bacchetta magica che cancella ogni obbligo. [Fonte: raw/pillitteri/pillitteri20260619-microsoft-presidio-pii-protezione-dati.md]

## Timeline delle notizie

- **2026-06-19** — Presidio torna virale sui social presentato come una novità di Microsoft, ma è un progetto open source sviluppato dal 2018 con oltre 9.000 stelle su GitHub e ultima versione 2.2.362 del 18 marzo 2026; con l'esplosione degli assistenti LLM la protezione delle PII verso i sistemi AI è diventata un problema di massa. [Fonte: raw/pillitteri/pillitteri20260619-microsoft-presidio-pii-protezione-dati.md]
- **2026-06-19** — Presidio torna virale sui social presentato come novità di Microsoft, ma è un framework open source sviluppato dal 2018 con oltre 9.000 stelle su GitHub: individua le PII e le sostituisce prima che raggiungano un modello, gira sulla propria infrastruttura e con l'esplosione degli LLM trova una seconda vita nella protezione dei prompt. [Fonte: raw/pillitteri/pillitteri20260619-microsoft-presidio-pii-protezione-dati.md]
- **2026-10-02** — Microsoft Presidio è indicato fra i cinque strumenti per anonimizzare i dati dei clienti prima di incollarli in un chatbot: libreria open source nata in Microsoft, oggi standard de facto per il riconoscimento e la mascheratura di dati personali in testi e documenti, richiede un minimo di competenza tecnica per l'installazione in Python ed è la base su cui molti altri strumenti sono costruiti. [Fonte: raw/pillitteri/pillitteri20261002-anonimizzare-dati-clienti-ai-gdpr.md]







## Collegamenti

- [[microsoft]]
- [[privacy-online]]
- [[index]]
