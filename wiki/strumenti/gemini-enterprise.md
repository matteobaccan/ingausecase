---
title: "Gemini Enterprise"
category: strumento
tags: [agent, enterprise, finanza, google, legale, mcp, verticale]
related_puntate: []
created: 2026-09-12
updated: 2026-10-14
sources: [raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md, raw/pillitteri/pillitteri20260901-gemini-enterprise-rooms-goal-playbook.md, raw/pillitteri/pillitteri20260426-gemini-enterprise-2026-agent-designer-inbox-esempi-pratici.md, raw/pillitteri/pillitteri20260423-gemini-enterprise-agent-platform-google-next-2026.md, raw/pillitteri/pillitteri20260606-google-agentic-rag-gemini-enterprise.md]
---

# Gemini Enterprise

## Introduzione

Piattaforma di [[google]] Cloud per agenti AI e ricerca aziendale, presentata al Next 2026 e specializzata il 25 agosto 2026 in due versioni verticali: Gemini Enterprise per i servizi finanziari e Gemini Enterprise per il settore legale, le prime confezionate per un singolo mestiere invece che per un uso generico. Sopra la piattaforma di base, che resta il motore, Google impacchetta quattro strati costruiti attorno a un mestiere preciso: competenze pronte all'uso, connettori verso i sistemi di quel settore, agenti già addestrati e un ecosistema di partner che li estende. La tesi dichiarata da Thomas Kurian, amministratore delegato di Google Cloud, è che i professionisti vogliono un'AI che non li leghi a un solo modello o ecosistema, si connetta ai sistemi IT che usano ogni giorno e sia sicura e conforme. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]

## Funzionalità principali

- **Financial Research agent**, agente gestito da Google con spiegabilità completa: ogni risposta arriva con punteggio di confidenza, metodologia usata, istantanea dei dati e citazione precisa della fonte. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Oltre 50 competenze per ruoli finanziari specifici, dalla valutazione del rischio di credito al monitoraggio di portafoglio, dalla sintesi delle notizie di mercato alla ricerca investigativa. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- 13 connettori verso fonti sotto licenza: CoinDesk Data & Indices, Daloopa, Dun & Bradstreet, FactSet, Finnhub, Fiscal.ai, Guidepoint, LSEG, Moody's, MSCI, PitchBook, S&P Global e SEC Edgar, che coprono dati di mercato, flussi di notizie, depositi regolamentari e archivi interni. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Agenti di terze parti innestati sulla piattaforma: D&B Business Verification Agent, gli agenti FlowX, l'Obin Financial Agent e due agenti di S&P Global per il reperimento dati e per lo scenario energetico. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Sul fronte legale le competenze coprono revisione e redlining dei contratti, creazione di playbook, ricognizione dell'orizzonte normativo, ricerca legale, evasione delle richieste di accesso ai dati personali (le DSAR previste dal GDPR) e redazione di NDA, più la redazione automatica dei documenti per le istanze di segretazione, che individua termini sensibili e dati personali da oscurare. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- I connettori legali passano dal protocollo MCP: gestori documentali iManage e NetDocuments, firma Docusign, piattaforme di e-discovery Everlaw e RelativityOne, ricerca con Thomson Reuters HighQ e CourtListener del Free Law Project, assistenti legali Harvey, Legora e Solve Intelligence. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Agenti partner per il legale: Deloitte con Contract Summarize Pro Agent e Clause Guard, Eudia con un agente che unisce ricerca legale, analisi documentale e screening di conformità. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]

## Installazione e uso

- L'amministratore attiva la soluzione verticale sul tenant Google Cloud dell'organizzazione: le politiche di sicurezza VPC e le chiavi di cifratura gestite dal cliente (CMEK) restano quelle aziendali e i dati del cliente non vengono usati per addestrare i modelli di Google. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Si collegano i connettori pertinenti, i 13 finanziari o le integrazioni MCP legali: l'agente non copia i dati altrove, si collega ai sistemi ereditando permessi e controlli di accesso già in vigore, quindi chi non può vedere un documento non lo vede nemmeno tramite l'agente. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Il professionista richiama una competenza (per esempio valutare il rischio di credito di una controparte o confrontare un contratto con il playbook dello studio) e l'agente esegue citando le fonti; chi vuole spingersi oltre compone agenti personalizzati con l'Agent Designer visivo di Gemini Enterprise. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]

## Casi d'uso

- Finanza: Deutsche Bank, partner di progettazione dell'agente di ricerca, CME Group, BNY, Citi Wealth, Lloyds Banking Group e Macquarie Bank. Marie-Jeanne Deverdun di Deutsche Bank indica l'obiettivo di ridurre lo sforzo manuale di ricerca e migliorare coerenza e verificabilità degli output. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Legale: adozione anticipata per Cleary Gottlieb, Freshfields, Weil e Williams & Connolly; Weil ha costruito sulla piattaforma uno strumento proprio, Benchmark, dedicato agli insight giudiziari, e Freshfields la inquadra in una partnership pluriennale con Google Cloud. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Il perimetro dichiarato è ricerca e automazione documentale: il Financial Research agent produce ricerca ancorata alle fonti e non esegue ordini di mercato. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]

## Prezzi

Le due soluzioni verticali sono in anteprima e il prezzo si concorda con le vendite, perché include connettori sotto licenza e agenti gestiti; la piattaforma di base ha invece un listino pubblico per utente al mese.

| Edizione | Prezzo per utente al mese | A chi serve |
| --- | --- | --- |
| Gemini Business | circa 21 dollari | Piccoli team, con limiti d'uso (fino a 500 utenti) |
| Enterprise Standard | circa 30 dollari (35 senza impegno annuale) | Uso pieno, libreria completa dei connettori |
| Enterprise Plus | circa 50-60 dollari | Massima capacità e più spazio di archiviazione |
| Enterprise Frontline | tariffa ridotta a consumo | Chi usa l'AI in modo occasionale (blocchi da 150 posti) |

Al costo per posto si aggiunge la spesa a consumo degli agenti personalizzati, con i token del modello che vanno da pochi centesimi per milione sui modelli Flash fino a cifre più alte sui modelli Pro, più il calcolo e l'archiviazione; la fatturazione di Memory Bank e Sessions sull'Agent Platform parte dal 1 settembre 2026. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]

## Azienda / Autore

- [[google]]

## Modelli supportati / correlati

- [[gemini]]

## Disponibilità in Italia

- Entrambe le soluzioni sono in anteprima dal 25 agosto 2026, con priorità su capital markets e corporate banking per la parte finanziaria; la piattaforma Gemini Enterprise è già disponibile in Italia e i connettori legali (Docusign, iManage, Thomson Reuters, NetDocuments) sono diffusi anche negli studi italiani medio-grandi. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]
- Il nodo per una realtà italiana non è tecnico ma di conformità: verificare che l'uso degli agenti su dati personali regga il vaglio del GDPR e del Garante privacy, aspetto su cui la funzione DSAR e la pista di controllo con citazioni giocano a favore. Google ha annunciato pacchetti successivi per sanità, scienze della vita e altri servizi professionali. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]

## Timeline delle notizie

- **2026-04-23** — Al Next '26 Google Cloud presenta il Gemini Enterprise Agent Platform, evoluzione di Vertex AI che unifica Model Garden (oltre 200 modelli, fra cui Gemini 3.1 Pro, Gemma 4 e Claude di Anthropic), Agent Studio, ADK, runtime per agenti long-running, Memory Bank, Agent Identity, Registry e Gateway, più la suite di simulazione e osservabilità; arrivano anche il Data Agent Kit, che vive dentro VS Code, Gemini CLI e Claude Code, e un fondo da 750 milioni di dollari per i partner. [Fonte: raw/pillitteri/pillitteri20260423-gemini-enterprise-agent-platform-google-next-2026.md]

- **2026-04-26** — Google Cloud aggiorna Gemini Enterprise il 25 aprile 2026 con Agent Designer V2 (canvas drag-and-drop, controllo passo-passo, anteprima e test integrati), un Inbox unificato, un Data Insights Agent nativo e Deep Research e Deep Research Max basati su Gemini 3.1 Pro, più l'apertura ad agenti di partner tramite Agent Gallery. [Fonte: raw/pillitteri/pillitteri20260426-gemini-enterprise-2026-agent-designer-inbox-esempi-pratici.md]

- **2026-06-06** — Google Research con Google Cloud presenta Agentic RAG, workflow multi-agente dentro Gemini Enterprise Agent Platform in public preview: cinque agenti (Orchestrator, Planner, Query Rewriter, RAG Agent e Sufficient Context Agent) continuano a cercare finché non c'è contesto a sufficienza, con accuratezza fino al 34 per cento in più del RAG a singolo passaggio sui dataset di fattualità. [Fonte: raw/pillitteri/pillitteri20260606-google-agentic-rag-gemini-enterprise.md]

- **2026-08-25** — Google Cloud apre in anteprima Gemini Enterprise per i servizi finanziari e per il settore legale, le prime versioni verticali della piattaforma: il Financial Research agent con confidenza, metodologia e citazioni, oltre 50 competenze di ruolo e 13 connettori sotto licenza per la finanza, e per il legale revisione contrattuale, playbook, sorveglianza normativa, DSAR, NDA e oscuramento per la segretazione sopra i connettori MCP di iManage, NetDocuments, Docusign, Everlaw, RelativityOne, Thomson Reuters, CourtListener, Harvey, Legora e Solve Intelligence. Entrambe sono in anteprima, la disponibilità generale non è annunciata e il prezzo dei pacchetti verticali si concorda con le vendite. [Fonte: raw/pillitteri/pillitteri20260825-gemini-enterprise-finanza-studi-legali.md]

- **2026-09-01** — Il 31 agosto 2026 Alexey Shabanov di TestingCatalog trova nelle build di Gemini Enterprise i riferimenti a Rooms, spazi di lavoro condivisi dove un team collabora con l'AI attorno a un obiettivo dichiarato: ogni Room si costruisce su un goal, un playbook che detta come Gemini deve comportarsi e una knowledge base di file collegati. Le Rooms estendono Projects — mostrato a marzo 2026 e ufficializzato al Cloud Next di aprile — spostando obiettivo e metodo da contenuto implicito a configurazione dichiarata e verificabile, il che rende possibili le revisioni di conformità e gli audit che con una chat privata non si possono fare. Resta un prototipo trovato nel codice, che Google non ha annunciato, non ha datato e potrebbe cambiare forma o sparire. [Fonte: raw/pillitteri/pillitteri20260901-gemini-enterprise-rooms-goal-playbook.md]

## Collegamenti

- [[chatgpt-financial-services]]
- [[claude-financial-services]]
- [[gemini]]
- [[google]]
- [[index]]
