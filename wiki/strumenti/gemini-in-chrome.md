---
title: "Gemini in Chrome"
category: strumento
tags: [browser, gemini, skills, auto-browse, agenti]
related_puntate: []
created: 2026-09-25
updated: 2026-10-09
sources: [raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md, raw/pillitteri/pillitteri20261009-gemini-chrome-legge-scheda-aperta-default.md]
---

# Gemini in Chrome

## Introduzione

Pannello laterale con cui Gemini vive dentro Chrome desktop e iOS invece che in una scheda a parte: si apre dall'icona in alto a destra, eredita il contesto della pagina attiva e, su richiesta, lo estende alle altre schede aperte fino a dieci. L'assistente non parte da zero come sul sito di Gemini, perché ha già visibilità su testo, link, DOM e contenuti incorporati — video YouTube, prodotti di Google Shopping, voli su Google Flights — ed è costruito su Gemini 3 con Nano Banana per le immagini e sulle connected app che includono Gmail, Google Calendar, YouTube, Maps, Shopping e Flights. La posta in gioco è competitiva: browser come Arc, Dia, Comet e ARC Search avevano conquistato gli utenti avanzati integrando l'assistente nel motore di navigazione, e Google, che con Chrome copre circa il 65 per cento del mercato, ha risposto portando l'AI sul proprio terreno invece di lasciarla alle estensioni di terze parti. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]

## Funzionalità principali

- Skills è il livello che rende ripetibile un prompt che funziona: si salva una conversazione dalla cronologia chat con nome ed emoji e la si richiama digitando lo slash nel pannello, e la Skill non è solo testo perché porta con sé i riferimenti al contenuto della pagina, alla cronologia della scheda e all'output delle connected app. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- La libreria ufficiale sta su chrome://skills/browse e raccoglie oltre cinquanta prompt preconfezionati in cinque categorie — Learning, Research, Shopping, Writing, Productivity — più una sezione Health & Wellness con casi come il calcolo dei macronutrienti: fra gli esempi citati dalla stampa internazionale ci sono Protein Maximizer, Gift Concierge, Document Speed-Read, Vegan Recipe Converter e Spec Comparator. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- Le Skills di Google ricevono aggiornamenti silenziosi con il browser, mentre quelle personali si sincronizzano via account Google e compaiono su tutti i Chrome desktop dove si è fatto l'accesso; il pattern è documentato anche lato API nel repository google-gemini/gemini-skills, 3.547 stelle, creato il 6 febbraio 2026. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- L'auto-browse è il livello agentico: riceve un obiettivo in linguaggio naturale, per esempio prenotare un tavolo per due sabato sera, apre il sito, cerca, sceglie data e ora, compila i dati dal Password Manager e si ferma all'ultimo click chiedendo conferma. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- I limiti pratici pesano più di quanto sembri: le Skills funzionano solo con la lingua del browser impostata su English (US), le schede analizzabili insieme sono al massimo dieci — quindi una ricerca su quindici fonti va spezzata in più sessioni — e la modalità in incognito disattiva del tutto il pannello perché il contesto delle conversazioni richiede la sincronizzazione con l'account. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- Il divieto geografico è applicato lato server, quindi una VPN con IP statunitense può sbloccare il pannello ma viola i termini di servizio e rischia il blocco dell'account in caso di violazioni ripetute. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]

## Requisiti

- Desktop: Chrome aggiornato all'ultima release stabile (sotto la 132 il pannello non c'è), Mac, Windows o Chromebook Plus; Linux non è supportato e i Chromebook non Plus restano fuori dal perimetro. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- Account: login con un account Google personale, almeno 18 anni e lingua di sistema fra le cinquanta supportate; gli account Workspace richiedono l'abilitazione dell'amministratore dalla Admin Console. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- Android: l'integrazione completa arriva da fine giugno 2026, inizialmente negli Stati Uniti e su dispositivi con almeno 4 GB di RAM e Android 12 o superiore. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- Auto-browse: serve essere fisicamente negli Stati Uniti e avere un piano Google AI Pro (19,99 dollari al mese) o AI Ultra (249,99 dollari al mese), con termini specifici che includono clausole di responsabilità per le azioni dell'agente. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]

## Azienda / Autore

- [[google]]

## Timeline delle notizie

- **2026-05-23** — Al 23 maggio 2026 l'Italia non è ancora nella lista ufficiale dei paesi serviti. Il rilascio è avvenuto per ondate: Stati Uniti il 28 gennaio 2026 su Mac, Windows e Chromebook Plus, poi India, Canada e Nuova Zelanda il 10 marzo con il supporto per le cinquanta lingue principali, quindi Australia, Indonesia, Filippine, Singapore, Corea del Sud e Vietnam il 20 aprile su desktop e iOS, con il Giappone che ha ricevuto l'app iOS in ritardo per ragioni regolatorie locali. Il ritardo europeo è attribuito agli obblighi di trasparenza algoritmica, audit dei dati di training e divieto di profilazione dei minori imposti da Digital Services Act, Digital Markets Act e AI Act, la stessa dinamica che aveva rallentato di sei mesi il rollout europeo di Gemini Nano nel browser; il comunicato del 10 marzo sul blog di Workspace Updates dà però l'italiano già attivo a livello di interfaccia, segno che l'infrastruttura linguistica è pronta e manca solo il via libera geografico. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- **2026-05-23** — Le Skills erano state annunciate sul blog ufficiale di Google il 14 aprile 2026 e nascono da un problema concreto: la maggior parte degli utenti riusa gli stessi prompt centinaia di volte ed è costretta a riscriverli o a ripescarli nella cronologia. Il flusso di creazione in tre minuti è pensato perché la Skill nasca da un prompt già testato e non da un editor astratto — si scrive la richiesta nel pannello, si verifica che l'output abbia il formato voluto, si salva il messaggio dalla cronologia con i tre puntini e la voce Save as Skill, poi la si richiama con lo slash applicandola a una nuova pagina. [Fonte: raw/pillitteri/pillitteri20260523-gemini-in-chrome-skills-come-funzionano-disponibilita-paesi.md]
- **2026-10-09** — Google documenta il comportamento predefinito di Gemini in Chrome: all'apertura del pannello o di una nuova chat l'assistente riceve il testo e l'URL della scheda aperta senza chiedere nulla, e si possono condividere fino a 10 schede recenti; l'opzione "Condividi la scheda corrente per impostazione predefinita" (Impostazioni, Innovazioni dell'AI, Gemini in Chrome) la disattiva. Sulle pagine Workspace l'accesso può estendersi all'intero documento, parte del contenuto ricevuto può non essere visibile a schermo e la pagina di supporto consultata il 9 ottobre non elenca l'Italia né gli altri paesi UE tra le regioni servite. [Fonte: raw/pillitteri/pillitteri20261009-gemini-chrome-legge-scheda-aperta-default.md]




## Collegamenti

- [[google]]
- [[gemini-intelligence]]
- [[agent-skills]]
- [[agenti-ai]]
- [[index]]
