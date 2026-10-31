---
title: "Jev"
category: modello
tags: [agent, classificazione, decisioni, inferenza, latenza]
related_puntate: [20260917, 20260918, 20260919, 20260920, 20260921, 20260922, 20260924, 20260925, 20260926, 20260929, 20260930, 20261002, 20261004, 20261016, 20261020]
created: 2026-09-16
updated: 2026-10-20
sources: [raw/puntate/ainews20260917.md, raw/pillitteri/pillitteri20260916-jev-typesafe-non-parla-batte-claude.md, raw/puntate/ainews20260918.md, raw/puntate/ainews20260919.md, raw/puntate/ainews20260920.md, raw/puntate/ainews20260921.md, raw/pillitteri/pillitteri20260921-jev-typesafe-cloni-open-source-gratis.md, raw/puntate/ainews20260922.md, raw/controrumore/controrumore20260922-diario-ai-amazon-chiude-la-porta.md, raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md, raw/puntate/ainews20260924.md, raw/tldr/tldr20260924.md, raw/puntate/ainews20260925.md, raw/puntate/ainews20260926.md, raw/puntate/ainews20260929.md, raw/puntate/ainews20260930.md, raw/tldr/tldr20260930.md, raw/myclaw/myclaw20260930-kennedy-wants-ai-on-health-data.md, raw/pillitteri/pillitteri20260929-openai-decisions-api-jev-typesafe.md, raw/puntate/ainews20261002.md, raw/pillitteri/pillitteri20261002-cloudflare-clef-sfida-jev.md, raw/puntate/ainews20261004.md, raw/pillitteri/pillitteri20261010-microsoft-decision-1-qwen-decision-model.md, raw/tldr/tldr20261015.md, raw/puntate/ainews20261016.md, raw/puntate/ainews20261020.md, raw/pillitteri/pillitteri20261020-jev-1-14-immagini-box-typesafe.md]
---

# Jev

## Introduzione

Modello di [[typesafe-ai]] lanciato in accesso anticipato il 16 settembre 2026: non genera testo e non conversa, riceve dati non strutturati — di solito testo — e restituisce un valore tipizzato scelto fra le opzioni fornite dall'utente, fino a 255 per singola chiamata, con un punteggio di confidenza calibrato. TypeSafe lo definisce il primo "System One Model", per riferimento al Sistema 1 di Kahneman, la mente istintiva che risponde in una frazione di secondo, contrapposta al Sistema 2 lento e ragionato su cui lavorano i modelli linguistici. [Fonte: raw/pillitteri/pillitteri20260916-jev-typesafe-non-parla-batte-claude.md]

## Capacità e performance

- La differenza tecnica sta nel modo di produrre l'output: un LLM genera in modo autoregressivo una parola alla volta, Jev produce l'intero output in un solo passaggio, tutte le uscite in parallelo dentro una singola query, con una latenza dichiarata fra 70 e 500 millisecondi da un capo all'altro.
- Non può inventare una risposta fuori dall'elenco e per costruzione non può produrre un errore di tipo: la forma dell'output è garantita dallo schema, quindi il programma a valle sa sempre cosa aspettarsi. Il limite è che lo zero per cento di allucinazioni vale sulla forma e non sul giudizio, perché il modello può ancora scegliere l'opzione sbagliata fra quelle disponibili.
- Il metodo di addestramento si chiama RLCD (Reinforcement Learning for Calibrated Decisions) e punta a produrre probabilità oneste, cioè che quando il modello dichiara 80% di confidenza ci azzecchi davvero quattro volte su cinque.
- Nella demo più discussa Jev gioca a Doom in tempo reale con circa dieci decisioni al secondo; in un'altra naviga fra i link di Wikipedia scegliendo la strada verso una pagina bersaglio.

## Numeri dichiarati da TypeSafe

- 193,6 volte più veloce di Claude Sonnet 5 sui workflow e 444,6 volte più economico di Claude Opus 5; prezzo di 0,042 dollari per milione di token in ingresso, con output di fatto gratuito perché il modello quasi non ne produce.
- Sono cifre di parte, misurate sulle valutazioni interne di TypeSafe e non su un benchmark indipendente.
- C'è anche una lettura critica: l'ingegnere Sean Goedecke osserva che gran parte del guadagno di velocità si ottiene già con tecniche note come il prefill aggressivo e la decodifica vincolata a un singolo token, aggiunge che i primi tentativi di riprodurre l'effetto sono sembrati riuscire e considera l'immunità dalle allucinazioni più un riposizionamento semantico che un vantaggio nuovo. Il limite di capacità resta: rinunciando al ragionamento a tempo di inferenza, Jev difficilmente supera il livello di un LLM non reasoning.

## Disponibilità

- Accesso anticipato dal 16 settembre 2026 tramite il programma early access di TypeSafe, con input a 0,042 dollari per milione di token e output gratuito.

## Azienda di riferimento

- [[typesafe-ai]]

## Timeline delle notizie

- **2026-09-16** — TypeSafe AI lancia Jev, il modello che sceglie invece di scrivere: classificazione, instradamento, punteggio, estrazione e scelta del prossimo passo sono gli usi indicati, cioè lo strato di controllo che serve agli agenti quando devono decidere quale strumento chiamare, se una risposta va bene, se sono entrati in un loop o se è il momento di passare la palla a un umano. Il confronto con le tariffe dei servizi in tempo reale è esplicito: la logica è la stessa del prezzo aggressivo di [[gpt-live-1]] di OpenAI a cinque centesimi al minuto, dove il vero prodotto è la latenza. [Fonte: raw/pillitteri/pillitteri20260916-jev-typesafe-non-parla-batte-claude.md]
- **2026-09-17** — La puntata riprende il lancio leggendolo come il ritorno del co-inventore di ChatGPT dopo due anni di sviluppo in stealth e aggiunge i propri numeri aggregati: venti volte più veloce dei modelli linguistici standard, quaranta volte più economico, output gratuito per sempre e decisioni tipizzate al posto delle stringhe di testo. La proprietà che considera decisiva è la stessa che TypeSafe rivendica dal giorno prima, l'assenza di allucinazioni, mentre le cifre più precise restano quelle dichiarate dall'azienda il 16 settembre, con le critiche che le accompagnano. [Fonte: raw/puntate/ainews20260917.md]
- **2026-09-18** — La puntata aggiunge i numeri operativi di Jev: latenza mediana di duecentocinquantasei millisecondi per classificare mille paper al costo di otto centesimi, e un browser agent basato su Jev che ha cercato voli in sette secondi per meno di un centesimo. [Fonte: raw/puntate/ainews20260918.md]
- **2026-09-19** — La puntata porta i numeri della verticale PR: Jev legge trecentottantaquattro notizie in ventiquattro secondi e nove decimi e sceglie per quindici brand quali storie sfruttare, al costo di zero virgola diciannove dollari, mentre Claude Opus 5 sullo stesso feed ne individua quattro su trecentottantaquattro a zero virgola settantasette dollari, cioè trecentonovanta volte più caro per headline. Il repository è online con la demo e oltre trenta skill che trasformano un agente in un team PR. [Fonte: raw/puntate/ainews20260919.md]
- **2026-09-19** — Sul fronte degli usi la puntata raccoglie un plugin per Claude Code che sfrutta Jev per cancellare il garbage dei terminali e i log ridondanti, eliminando le pause da dieci secondi quando il contesto si riempie, un controllo vocale su Mac che apre le app mentre l'utente finisce la frase, e un confronto fra Codex standard e Codex potenziato da Jev, risultato più fluido sullo stesso task. Un test su ricerca voli reali chiude in sette secondi a zero virgola zero zero trentanove dollari e, con Browser Use integrato, il costo per azione cala di circa quattrocentocinquanta volte. [Fonte: raw/puntate/ainews20260919.md]
- **2026-09-19** — In coppia con Mercury 2.5 e WebMCP risolve il cento per cento dei task del benchmark WebMCP, con un costo modello centododici volte più basso di GPT-6 Astra con computer use e code execution e duecentoquarantacinque volte più basso rispetto ad Astra con screenshot; il benchmark è aperto e riproducibile. [Fonte: raw/puntate/ainews20260919.md]

- **2026-09-20** — Due progetti della puntata partono da Jev: Bespoke Nimble, la versione open source basata su Qwen3.5-9B, arriva al 90,12 per cento sul test set contro il 93,21 dell'originale con due giorni di lavoro, 2.676 esempi di training e una sola sessione LoRA, senza distillazione da Jev, e semgrep usa il modello per la ricerca semantica sul codice, trovando trenta righe in una richiesta e duecento in meno di un secondo. [Fonte: raw/puntate/ainews20260920.md]

- **2026-09-21** — Sul modello arrivano due concorrenti e una lettura architetturale: [[laya]] dichiara 86,5 decisioni al secondo contro 3,2 con nove millisecondi di risposta mediana, [[kev]] propone la stessa idea in tre taglie addestrabili da zero con Kev-8B al 79,6 per cento sui dati mai visti contro l'85,7 di Jev, e Jev Engineering separa il ragionamento dalle decisioni rapide tenendo il modello costoso fuori dal loop, con router strutturati per routing e approvazioni e nei test fino a 193 volte più velocità e 444 volte meno costo. [Fonte: raw/puntate/ainews20260921.md]

- **2026-09-21** — A una settimana dal lancio i cloni open source sono almeno cinque: [[semif]] (2.685 stelle, base Qwen3.5-4B e MiniCPM5-2B nel browser), [[kev]] (1.370 stelle, Qwen3.5 da 0,8 a 9B, compatibile con lo SDK Python di [[typesafe-ai]]) e jevlike (1.122 stelle, encoder byte-level addestrato in casa) sono i tre più seguiti, con openjev e openjev-sglang a seguire. Copiano l'interfaccia e non il modello, perché TypeSafe non ha pubblicato né architettura né dati: sulla stessa RTX 3090 SemIf risponde a 21 criteri in 1,023 secondi contro 5,332 della generazione JSON, con concordanza di 18 criteri su 21. [Fonte: raw/pillitteri/pillitteri20260921-jev-typesafe-cloni-open-source-gratis.md]
- **2026-09-21** — Un'analisi esterna di Archer Hume, "Jev's Architecture Unmasked", ricostruisce il funzionamento su circa 10.000 chiamate all'API e separa tre livelli: dichiarato (output in parallelo e addestramento RLCD), osservato (solo prefill, stato condiviso letto una volta e domande isolate, circa 30.000 token in circa 160 millisecondi, fino a 1.500 domande e 255 opzioni per richiesta) e inferito (un backbone MoE sparso, la parte meno certa), mentre nessuno dei 192 tokenizer pubblici provati corrisponde a quello di Jev. [Fonte: raw/pillitteri/pillitteri20260921-jev-typesafe-cloni-open-source-gratis.md]
- **2026-09-22** — Decine di repository e tool esplosi su GitHub attorno a Jev con automazione browser, compressione contesto per Claude Code, generative UI e integrazione MCP. [Fonte: raw/puntate/ainews20260922.md]
- **2026-09-22** — Unified Harness Protocol esegue Codex, Hermes, Claude Code, DeepSeek Harness e System One powered by Jev sotto un'unica interfaccia compatibile OpenAI Responses in locale. [Fonte: raw/puntate/ainews20260922.md]
- **2026-09-22** — Jev usato per modificare dinamicamente lo sforzo di ragionamento di GPT-6 durante Codex, con 50% meno costi Astra. [Fonte: raw/puntate/ainews20260922.md]
- **2026-09-22** — Debutto pubblico con quasi 13% dei team paid su Vercel AI Gateway in 24 ore per output decisionali strutturati. [Fonte: raw/controrumore/controrumore20260922-diario-ai-amazon-chiude-la-porta.md]
- **2026-09-24** — tev1-4B-experimental è un classificatore nello stile di Jev, fine-tunato su Qwen3.5 4B e servito su Together a 0,042 dollari per milione di token in ingresso e zero in uscita, con la ricetta dei dati e il tutorial di fine-tuning pubblicati e un costo di training di diciassette dollari. [Fonte: raw/tldr/tldr20260924.md]
- **2026-09-24** — Arriva [[clm-8b]], un Contrastive Language Model da otto miliardi pre-addestrato su dati internet-scale che dichiara inferenza fino a nove volte più veloce di Jev con prestazioni comparabili su computer-use, gaming e tool-calling. [Fonte: raw/puntate/ainews20260924.md]
- **2026-09-19** — Il port [[laya-mlx]] porta la stessa idea di Jev sulla memoria unificata di un Mac: decisioni in 7-14 millisecondi contro i 70-500 dichiarati da TypeSafe per una richiesta hostata, da 5 a oltre 60 volte meno, e una demo in cui il modello gioca a Snake a 60 mosse al secondo (75,4 con la compilazione MLX attiva). Il servizio di [[typesafe-ai]] resta hostato, chiuso, non disponibile in Europa e con i dati gestiti sulla costa ovest degli Stati Uniti. [Fonte: raw/pillitteri/pillitteri20260922-laya-mlx-jev-apple-silicon.md]
- **2026-09-25** — Su GitHub esplodono dieci progetti costruiti su JEV: JEV-Trader, bot di trading live su Monad con millenovecentoundici stelle; JEV-Ultrafast, browser agent che decide ogni click con sedicimilasettecentocinquantotto stelle; JEV-Doom-Agent, che gioca a Doom prendendo decisioni tattiche a ogni frame; JEV-T-Rex-Runner, che gioca da solo al dinosauro di Chrome; Typesafe-Chess, che sfida un motore di ricerca scacchistico; JEV-Drone, che pilota un drone simulato fra gli ostacoli; Tax-Doc-Classifier, che classifica moduli IRS a circa zero virgola zero zero uno dollari per pagina; KillMyIdea, che valuta idee di startup restituendo Kill, Fix o Ship; JEV-Curate, che filtra oltre millecinquecento righe di dati al secondo; e PG-JEV, che interroga tabelle Postgres in linguaggio naturale. [Fonte: raw/puntate/ainews20260925.md]

- **2026-09-26** — Un paper dimostra che JEV può fare da giudice per le valutazioni: restituisce un verdetto con un livello di confidenza e, quando questo è alto, mantiene la risposta, mentre quando è basso passa a un modello più costoso, conservando il novantanove per cento dell'accuratezza di GPT-6 con costi ridotti drasticamente. [Fonte: raw/puntate/ainews20260926.md]
- **2026-09-29** — Unsloth Desktop serve Laya Decision in locale tramite un'API compatibile Jev. [Fonte: raw/puntate/ainews20260929.md]
- **2026-09-30** — Due segnali sul mercato dei decision model: la Decisions API di OpenAI (mossa da GPT-6 Luna, con supporto visione) entra come concorrente diretto di Jev, e d1 di Liquid AI dichiara di superare Jev sul Decision Index di Hugging Face; dal lato open source esce Jeff, clone compatibile che gira in locale a 22-26 millisecondi. [Fonte: raw/tldr/tldr20260930.md] [Fonte: raw/puntate/ainews20260930.md]
- **2026-10-02** — Cloudflare prende esplicitamente Jev come riferimento diretto per il lancio di [[clef]], citandolo come il prodotto che ha acceso l'interesse per la categoria dei decision model due settimane prima: Clef è dichiarato pienamente compatibile con l'API di Jev, quindi chi lo ha già integrato può sostituirlo cambiando endpoint e nome del modello. Jev resta avanti su When2Call (80,97 contro 72,37) e su BRIGHT (47,52 contro 45,91), mentre Clef lo supera su gran parte degli altri benchmark del Jev Decision Index e aggiunge la classificazione delle immagini e una finestra di contesto doppia (64.000 contro 32.000 token). [Fonte: raw/pillitteri/pillitteri20261002-cloudflare-clef-sfida-jev.md]



- **2026-10-03** — Viene presentato Jevbox, drive documentale che si organizza da solo tramite Jev: la ricerca è gerarchica su cartella, documento e sezione, ogni risposta cita pagina e sezione, i permessi si applicano al retrieval ed è open source con server MCP integrato. [Fonte: raw/puntate/ainews20261003.md]
- **2026-10-04** — Nel team di agenti di Claude Code descritto da Anthropic uno script layer basato su Jev gestisce i comandi meccanici. [Fonte: raw/puntate/ainews20261004.md]
- **2026-10-10** — Microsoft Decision-1 si prezza 0,042 dollari per milione di token in ingresso, la stessa tariffa di Jev (42 dollari per miliardo), e Microsoft dichiara 2,8 volte la sua velocità nel proprio test di latenza; i numeri disponibili su Jev (70-500 millisecondi dichiarati da TypeSafe, 524 di mediana misurati da Cloudflare) non sono confrontabili con quelle misure perché cambiano hardware, lunghezza dei testi e metodo. [Fonte: raw/pillitteri/pillitteri20261010-microsoft-decision-1-qwen-decision-model.md]
- **2026-10-15** — Esce Jev 1.14.0 con supporto alle immagini, un nuovo tipo e contesto più lungo; la multimodalità è stata attivata anche su Jev 1.13.0 e sia i modelli multimodalità rendono peggio che sul testo puro, mentre scomporre le domande nelle decomposizioni più semplici aiuta molto; il nuovo tipo box restituisce un singolo bounding box ed è un assaggio delle esplorazioni di TypeSafe oltre le decisioni semplici. [Fonte: raw/tldr/tldr20261015.md]
- **2026-10-16** — Jev 1.14 di [[typesafe-ai]] porta supporto sperimentale per immagini, un nuovo tipo box e contesto più lungo: le funzioni visive escono dalla preview, con avviso di cautela agli sviluppatori. [Fonte: raw/puntate/ainews20261016.md]
- **2026-10-20** — Harness² viene integrato in JEV 1.14 senza modifiche ai pesi, con guadagni dichiarati sui benchmark di visione: il sistema riscrive i propri prompt, costruisce i propri tool e distilla la propria esperienza, e il repository JEV-Harness² è annunciato in arrivo. [Fonte: raw/puntate/ainews20261020.md] L'articolo di Pillitteri del 20 ottobre precisa il meccanismo: le immagini passano solo con l'header TypeSafe-Danger-Zone-Images e una mappa assets, ogni file è un PNG o JPEG da 16 MiB con lati tra 280 e 1.568 pixel, una domanda Box restituisce sempre un riquadro anche quando l'oggetto non c'è e va affiancata a una domanda Noul di controllo, il costo resta 0,042 dollari per milione di token di input e il contesto predefinito è di 64.000 token, estendibile a 262.000 con un secondo header. [Fonte: raw/pillitteri/pillitteri20261020-jev-1-14-immagini-box-typesafe.md]






















## Collegamenti

- [[agenti-ai]]
- [[bespoke-nimble]]
- [[clm-8b]]
- [[kev]]
- [[laya]]
- [[laya-mlx]]
- [[browser-use]]
- [[claude]]
- [[gpt-6-astra]]
- [[gpt-live-1]]
- [[mercury-2]]
- [[semgrep]]
- [[semif]]
- [[d1]]
- [[jeff]]
- [[typesafe-ai]]
- [[index]]
- [[decision-model]]
