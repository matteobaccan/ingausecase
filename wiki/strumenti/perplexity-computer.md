---
title: "Perplexity Computer"
category: strumento
tags: [perplexity, agent, cloud, finanza, orchestrazione]
related_puntate: [20261016, 20261021]
created: 2026-09-15
updated: 2026-10-21
sources: [raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md, raw/pillitteri/pillitteri20260620-perplexity-brain-memoria-agente-computer.md, raw/pillitteri/pillitteri20260828-perplexity-nvidia-portable-computer-agente-locale.md, raw/pillitteri/pillitteri20260902-perplexity-hybrid-compute-mac.md, raw/tldr/tldr20260923.md, raw/puntate/ainews20261016.md, raw/puntate/ainews20261021.md]
---

# Perplexity Computer

## Introduzione

Agente AI di [[perplexity]] presentato il 25 febbraio 2026 e presentato dal CEO Aravind Srinivas come "lavoratore digitale di uso generale": non un dispositivo fisico ma un servizio cloud che unisce in un'unica interfaccia ragionamento profondo, ricerca web, generazione di documenti, scrittura di codice, esecuzione in browser e automazione di flussi ripetuti nel tempo. La differenza rispetto a una chat è di natura semantica: una chat risponde a una domanda, l'agente porta a termine un obiettivo dichiarato in linguaggio naturale e consegna un artefatto pronto all'uso. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]

## Funzionalità principali

- L'orchestrazione coordina diciannove modelli di frontiera scegliendo per ogni sotto-compito quello più adatto: [[claude-opus-4-6]] come motore di ragionamento e coordinatore dei sub-agenti, [[gemini]] per la ricerca web profonda, [[gpt-5-2]] per i contesti estesi, [[grok]] per le operazioni leggere ad alto throughput, Nano Banana e Veo 3.1 per immagini e video. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]

- Ogni sub-agente lavora dentro una microVM Firecracker, la stessa tecnologia di sandbox usata da AWS per Lambda, con avvio sotto i centoventicinque millisecondi: l'isolamento serve a contenere i comportamenti anomali del modello e a impedire che una sessione interferisca con i file dell'utente o con la rete locale. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- Tre modalità di esecuzione: one-shot per un singolo task, recurring per ripetere lo stesso flusso a intervalli definiti e watch per restare in ascolto e attivare un sotto-agente solo al verificarsi di una condizione esplicita. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- Computer for Professional Finance dà accesso diretto a oltre quaranta strumenti dati live (SEC EDGAR, FactSet, S&P Global, Coinbase, LSEG, Quartr, Polymarket, Crunchbase, Financial Modeling Prep) senza chiavi API separate, con ogni cifra cliccabile verso il documento originale; la connessione a Plaid collega i conti di intermediazione e costruisce dashboard con cost basis, volatilità storica, beta e Sharpe ratio aggiornati. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- Si appoggia al browser [[comet]] per vedere e interagire con il web, con sidebar contestuale sulla pagina e Background Assistants per i task lunghi. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- Dalla presentazione di [[perplexity-brain]] l'agente parte con il contesto dei progetti, delle decisioni prese e delle fonti già consultate invece di ripartire da zero. [Fonte: raw/pillitteri/pillitteri20260620-perplexity-brain-memoria-agente-computer.md]
- Con Hybrid Compute, attivo sull'app per Mac dal 1 settembre 2026, i compiti si spezzano tra i modelli di frontiera nel cloud e un modello locale: il cloud si occupa di ricerca web, pianificazione e ragionamento lungo, il modello sul Mac gestisce file privati e dati sensibili senza farli uscire dal dispositivo, con il passaggio a metà task e senza perdere il contesto. [Fonte: raw/pillitteri/pillitteri20260902-perplexity-hybrid-compute-mac.md]

## Installazione e uso

- Il prompt è un obiettivo in linguaggio naturale, con deliverable atteso, fonti da consultare, formati di consegna e approvazioni intermedie da chiedere prima dei passaggi delicati. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- Il framework AGENT riassume i cinque elementi minimi di un prompt produttivo: Assignment, Guardrails, Engine, Notify, Target; i prompt vaghi generano sub-agenti inutili che consumano crediti senza aggiungere valore. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]

## Repository

- Prodotto proprietario: nessun repository pubblico.

## Azienda / Autore

- [[perplexity]]

## Modelli supportati / correlati

- [[claude-opus-4-6]]
- [[gemini]]
- [[gpt-5-2]]
- [[grok]]

## Timeline delle notizie

- **2026-02-25** — Perplexity presenta Computer: servizio cloud che orchestra diciannove modelli di frontiera dentro microVM Firecracker e consegna artefatti finiti (memo, PDF, dashboard, deploy) da un obiettivo scritto in linguaggio naturale; il confronto con il Bloomberg Terminal da 24.000-30.000 dollari l'anno per posto regge su un abbonamento da 200 dollari al mese. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- **2026-02-25** — Computer for Professional Finance estende l'agente ai dati professionali: oltre quaranta strumenti live, tracciabilità della fonte di ogni numero e connessione Plaid ai conti di intermediazione. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- **2026-06-18** — Brain debutta in research preview proprio su Computer, come memoria del lavoro dell'agente e non dell'utente. [Fonte: raw/pillitteri/pillitteri20260620-perplexity-brain-memoria-agente-computer.md]
- **2026-08-25** — Il runtime dell'agente viene spostato sul dispositivo con [[portable-computer]], senza costi di token per il lavoro locale. [Fonte: raw/pillitteri/pillitteri20260828-perplexity-nvidia-portable-computer-agente-locale.md]
- **2026-09-01** — Su Mac arriva Hybrid Compute, con il Privacy Gate che decide se tenere in locale, mascherare i tratti sensibili, rifiutare l'azione o chiedere un consenso esplicito. [Fonte: raw/pillitteri/pillitteri20260902-perplexity-hybrid-compute-mac.md]

- **2026-09-23** — Per addestrare il modello di Computer, Perplexity combina il fine-tuning con rejection sampling e la self-distillation guidata da indizi, così il modello impara sia dalle sessioni riuscite sia dagli errori corretti dagli utenti. [Fonte: raw/tldr/tldr20260923.md]
- **2026-10-16** — SPACE, la sandbox che lo alimenta, diventa open source per l'ecosistema per iniziativa di [[perplexity]]. [Fonte: raw/puntate/ainews20261016.md]
- **2026-10-21** — Gira ora completamente in locale su Mac, senza inferenza cloud e senza connessione WiFi. [Fonte: raw/puntate/ainews20261021.md]







## Collegamenti

- [[comet]]
- [[perplexity]]
- [[perplexity-brain]]
- [[portable-computer]]
- [[index]]
