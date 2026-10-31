---
title: "Annota AI"
category: strumento
tags: [annotazione, dati, italia, mcp, ocr, training]
related_puntate: []
created: 2026-09-17
updated: 2026-09-17
sources: [raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]
---

# Annota AI

## Introduzione

Piattaforma italiana per preparare i dati destinati all'AI: converte documenti con l'OCR, annota immagini, addestra modelli e costruisce basi di conoscenza aziendali, il tutto con un server MCP verso gli agenti di coding e con l'infrastruttura tenuta in Europa. L'ha sviluppata in dieci mesi una startup di cinque persone con sede a Grosseto, Annota S.r.l., e la tesi di partenza è che i modelli siano ormai una commodity mentre i dati propri no, visto che l'80% del tempo di un progetto AI se ne va a preparare, pulire ed etichettare i dati. [Fonte: raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]

## Funzionalità principali

- **OCR**: trasforma PDF e scansioni in Markdown strutturato, capisce il layout a più colonne, estrae le immagini in una cartella a parte lasciando nel testo il riferimento a dove stanno e scrive le formule in LaTeX; le tabelle restano tabelle.
- **LLM Wiki**: da un mucchio di documenti compila una base di conoscenza esportabile come grafo, con una cartella raw, una cartella wiki con l'indice e i file di istruzioni che spiegano all'agente come costruirlo; si esporta, si apre il coding agent preferito (Claude Code, Codex, Antigravity, OpenCode), si chiede l'ingestion e l'agente indicizza da solo. Obsidian serve solo a guardare il grafo.
- **Data labeling**: poligoni a mano oppure Magic Select, dove si clicca l'oggetto e il segmento appare da solo, e Magic Annotate, che dato un dataset, una classe e una soglia di confidenza etichetta in blocco tutte le immagini non ancora annotate, con un ripasso umano dopo. Le classi vanno scritte in inglese e devono essere cose che il modello ha plausibilmente già visto in addestramento.
- **Addestramento**: il modello si allena in locale passando dataset e istruzioni a un coding agent (gira anche sulla CPU), oppure nel cloud della piattaforma con versionamento del dataset, scelta dell'architettura, numero di epoche e metriche; alla fine si scaricano pesi, manifest JSON e README.
- **Server MCP**: caricare file, etichettare, esportare e addestrare si chiedono al proprio agente collegando la piattaforma come connettore personalizzato in Claude, Codex o OpenCode. [Fonte: raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]

## Casi d'uso

- Il progetto mostrato nella demo: un'azienda con più cantieri vuole un modello che dalle telecamere conti quanti operai indossano il caschetto. Si parte da 200 immagini scaricate da Hugging Face, Magic Annotate etichetta in blocco persone e caschetti, un umano ripassa, poi il dataset passa a un coding agent che addestra in locale un modello da circa 9 MB, capace di girare su CPU a 30 fotogrammi al secondo. La fonte registra il confronto con un modello visione-linguaggio grande come Gemini o GPT: funziona, ma richiede GPU e non regge il tempo reale su una telecamera. [Fonte: raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]

## Installazione e uso

- Si usa dal web a crediti: piano Free gratuito con 500 crediti al mese che si ricaricano da soli, Pro a 18 euro al mese (3.000 crediti, 4 membri, 40 dataset), Scale a 90 euro (20.000 crediti, 6 membri, 60 dataset) ed Enterprise su misura con opzioni on-premise e SLA. Per dare la misura: mille pagine di OCR costano circa 4 euro di crediti, mille immagini auto-annotate circa 10. [Fonte: raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]

## Limiti

- Magic Annotate dipende da un modello di frontiera e non è perfetto sulle immagini complesse: le classi fuori dal vocabolario noto al modello vanno disegnate a mano.
- L'alternativa fai-da-te esiste ed è tutta open source, ma si paga in tempo di integrazione: Tesseract, Docling e [[marker]] per l'OCR, CVAT e Label Studio per l'etichettatura, [[ultralytics|YOLO]] per l'addestramento, un RAG fatto in casa per la base di conoscenza. [Fonte: raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]

## Dati e certificazioni

- Infrastruttura e storage restano in region europee grazie al partner Scaleway, i contenuti dei clienti non addestrano modelli di terze parti e sui piani a pagamento non addestrano nemmeno i modelli di Annota; la startup dichiara di puntare a GDPR e AI Act e di avere in corso l'ottenimento delle certificazioni SOC 2, ISO 27001 e ISO 42001, ed è nel programma NVIDIA Inception. [Fonte: raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]

## Timeline delle notizie

- **2026-09-17** — Nasce Annota AI, piattaforma italiana che unisce OCR, annotazione dei dati, addestramento e base di conoscenza in un unico ambiente, con un server MCP per pilotare tutto dall'agente di coding. Sviluppata in dieci mesi da una startup di cinque persone con sede a Grosseto e infrastruttura in Europa, parte da un piano gratuito con 500 crediti al mese e piani a pagamento da 18 e 90 euro, con la tesi che i modelli siano ormai sostituibili e i dati no. [Fonte: raw/pillitteri/pillitteri20260917-annota-ai-startup-italiana-dati.md]

## Collegamenti

- [[hugging-face]]
- [[marker]]
- [[mcp]]
- [[mistral-ocr-4]]
- [[obsidian]]
- [[ultralytics]]
- [[index]]
