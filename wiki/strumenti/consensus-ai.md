---
title: "Consensus AI"
category: strumento
tags: [ricerca, paper-scientifici, citazioni, agenti, mcp]
related_puntate: []
created: 2026-09-28
updated: 2026-09-28
sources: [raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]
---

# Consensus AI

## Introduzione

Motore di ricerca basato sull'intelligenza artificiale dedicato alla letteratura scientifica peer-reviewed, lanciato nel 2022 dalla startup newyorkese fondata da Christian Salem, Eric Olson e Joshua Fayer. Interroga oltre 220 milioni di articoli e restituisce risposte sintetiche con citazioni verificabili, attingendo a Semantic Scholar, OpenAlex e in parte PubMed e ArXiv invece che al web aperto. Otto milioni di ricercatori lo usano, e il 2025 si è chiuso con ricavi otto volte quelli dell'anno precedente. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]

## Funzionalità principali

- **Pipeline in tre fasi**: ricerca ibrida semantica più BM25 su Elastic con il modello ELSER, re-ranking dei primi venti risultati per anno, citazioni, impact factor e tipologia di studio, sintesi finale affidata a [[gpt-5]] di [[openai]] tramite le Responses API, con citazioni inline. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]
- **Consensus Meter**: su domande sì/no mostra quante fonti supportano, contraddicono o danno risultati misti. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]
- **Study Snapshot**: scheda automatica con popolazione, campione, durata, metodologia, risultati e limiti dichiarati. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]
- **Deep Search**: report strutturato con sintesi, sezioni tematiche e research gap in due-cinque minuti. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]
- **Scholar Agent**: sistema multi-agente su GPT-5 con quattro agenti specializzati (Planning, Search, Reading, Analysis). [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]

## Installazione e uso

Nel 2025 l'azienda ha rilasciato un server [[mcp]], così qualsiasi client compatibile — Claude Desktop, [[claude-code]], Cursor o la modalità Deep Research di ChatGPT — può interrogare il corpus dei 220 milioni di paper dalla propria interfaccia. La configurazione richiede un account con piano Pro o superiore e le chiamate si contano nelle quote del piano. I piani vanno dal gratuito (10 Pro Analysis e 10 Study Snapshot al mese) a 8,99 dollari al mese per il Premium e 15 per il Pro, con il piano Teams a 9,99 dollari per posto. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]

## Casi d'uso

Università come Yale, University of Virginia, Loyola Marymount e Oklahoma State lo hanno adottato in trial istituzionali; gli ambiti di uso indicati sono il giornalismo scientifico, la consulenza tecnica, la ricerca medica clinica e l'ingegneria. I limiti documentati sono tre: la sintesi tende a oversemplificare i dibattiti metodologici, il corpus include preprint non revisionati (fisica e informatica in particolare) e non esiste un meccanismo automatico per escludere paper ritirati. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]

## Azienda / Autore

- Christian Salem, Eric Olson, Joshua Fayer

## Timeline delle notizie

- **2026-04-22** — La guida ricostruisce il prodotto e il suo mercato: un benchmark della Hong Kong University of Science and Technology sullo steso quesito ha misurato circa dieci studi citati nelle sintesi di Consensus e Scite, cinque-otto per Scopus AI e quattro per Elicit. [Fonte: raw/pillitteri/pillitteri20260422-consensus-ai-motore-ricerca-paper-scientifici-guida-2026.md]

## Riferimenti

- https://pasqualepillitteri.it/news/1290/consensus-ai-motore-ricerca-paper-scientifici-guida-2026

## Collegamenti

- [[openai]]
- [[gpt-5]]
- [[mcp]]
- [[formazione-ai]]
- [[index]]
