---
title: "Alternative open source ai software a pagamento"
category: trend
tags: [alternativa, gratis, open-source, saas]
related_puntate: [20260531, 20261013]
created: 2026-08-12
updated: 2026-10-15
---

# Alternative open source ai software a pagamento

## Introduzione

Ondata di alternative open source gratuite a software a pagamento: Parchis al posto di ElevenLabs, Graphite di Photoshop+Illustrator, PDF-Tools di Acrobat, Notesnook di Notion, Docmost di Confluence, Tuta di Gmail, Beszel di Datadog, Reactive Resume, Shotcut e LocalAI delle API OpenAI.

## Timeline delle notizie

- **2026-05-31** — È comparsa un'ondata di alternative gratuite a software a pagamento, tutte open source e funzionali: Parchis Text-to-Speech al posto di ElevenLabs, Graphite al posto di Photoshop più Illustrator, PDF-Tools al posto di Acrobat, Notesnook al posto di Notion, Docmost al posto di Confluence, Tuta al posto di Gmail, Beszel al posto di Datadog, Reactive Resume al posto dei resume builder a pagamento, Shotcut al posto degli editor video premium e LocalAI al posto delle API OpenAI.

- **2026-04-17** — [[salesforce]] Enterprise costa a un team commerciale di dieci persone circa 21.000 dollari l'anno di sole licenze e HubSpot CRM Suite Professional parte da 1.781 dollari al mese con un onboarding fee fino a 4.500, con dati, automazioni e integrazioni che restano prigionieri della piattaforma: è il lock-in il vero prodotto. Twenty CRM si presenta come l'alternativa open source, 44.000 stelle su GitHub, licenza AGPL-3.0, self-hosted gratis per sempre, scritto in TypeScript con 11.590 commit e oltre 300 contributori, sostenuto da Y Combinator (batch S23) e da un round seed da 5 milioni nel novembre 2024 guidato da Runa Capital. Il modello dati si personalizza a runtime senza migrazioni SQL, le viste tabella e Kanban hanno filtri e viste salvate, il motore di workflow copre trigger, azioni e logica condizionale, l'email si sincronizza con Gmail e Outlook via OAuth, ogni oggetto è esposto in REST e GraphQL e i permessi sono granulari a livello di oggetto, record e campo; il cloud costa 9 dollari per utente al mese e il self-hosted solo il costo di un server da 20-50 dollari, con circa il 19.200 dollari di risparmio annuo su un team di dieci rispetto a Salesforce Enterprise. L'AI entra dalle API, per arricchimento dei contatti, scoring delle opportunità e riassunti dei call report, ed è anche il terreno su cui si gioca la visibilità: gli utenti scoprono il progetto chiedendo a ChatGPT alternative open source a Salesforce.
- **2026-09-16** — L'outage globale di [[salesforce]] del 16 settembre riporta Twenty sotto i riflettori: il disservizio che blocca login, API e perfino l'apertura di un ticket riaccende la domanda sulle alternative, ma il progetto viene indicato anche con la sua avvertenza, cioè che cambiare piattaforma per un CRM aziendale resta tutto tranne che indolore.
- **2026-10-08** — Brandon Thomas, fondatore dello studio ArtCraft, pubblica su GitHub sette app open source scritte in Rust con l'aiuto di Claude Opus 5.5 che ricalcano Photoshop, Illustrator, Premiere, Lightroom, After Effects, InDesign e Acrobat Pro (licenza MIT o Apache 2.0), con PhotoCraft a 23.303 stelle su 42.000 complessive in otto giorni e altre due app, un foglio di calcolo e presentazioni, comparse il 7 ottobre; il progetto si presenta come «clean-room», ricostruito da specifiche pubbliche e comportamento osservato, e lo stesso autore lo descrive come un'alpha molto acerba, con FilmCraft che stima la propria prontezza per il lavoro reale al 50-60 per cento e l'ecosistema di plugin allo 0-10 per cento.
- **2026-10-08** — Le Crafting Apps di ArtCraft crescono: LightCraft, alternativa a Lightroom in Rust, ha otto giorni di vita e oltre 5.200 stelle (roadmap al 60-70 per cento di parità con Lightroom, 85 per cento per chi scatta JPEG o DNG, 45 per cento per Canon CR3 e RAW compressi Olympus), mentre VectorCraft (alternativa a Illustrator, oltre 3.200 stelle, circa 221.000 righe di Rust e 2.840 test) è nato il 30 settembre insieme a PhotoCraft; le roadmap contano i tempi di lavoro come sviluppo continuo di quattro-sei agenti AI in parallelo.
- **2026-10-10** — Alla famiglia di cloni di ArtCraft si aggiungono WordCraft, GridCraft e DeckCraft, cloni open source di Word, Excel e PowerPoint scritti in Rust con Claude Opus 5.5: in quattro giorni WordCraft raccoglie 2.302 stelle, GridCraft 1.412 e DeckCraft 1.098, e la v0.4.0 porta installer per Windows, macOS, Linux e FreeBSD. Le coperture dichiarate dai README (87 per cento dei comandi del nastro in WordCraft, 89 per cento dei comandi e 93 per cento delle funzioni in GridCraft, 79 per cento delle funzioni in DeckCraft) sono stime degli autori, e le tre app si presentano come pre-alpha: nel DOCX vengono scartati grafici, SmartArt e oggetti OLE, in GridCraft manca VBA e il PPTX è stato provato solo su presentazioni fatte in casa. Nella puntata del 13 ottobre WordCraft ricompare fra i rilasci della famiglia: revisione delle modifiche, commenti, citazioni bibliografiche, sommario automatico e stampa unione, supporto a Windows, macOS, Linux e browser e un server MCP nativo che permette a agenti come Claude Code di controllare l'editor per generare e modificare documenti, con il progetto ancora in fase pre-alpha. Le tre guide di approfondimento del 13 ottobre ne danno i numeri aggiornati: WordCraft a 9.597 stelle con 487 dei 502 comandi della barra di Word per Mac e circa 88.700 righe di Rust, GridCraft a 3.977 stelle con 1.013 commit e 57 contributori ma nessuna misura della compatibilità con i file Excel altrui, DeckCraft a 2.676 stelle con il 79 per cento delle funzioni contato sul codice e il 53 per cento di prontezza stimata: in tutti e tre il corpus di file reali mai provato resta il bloccante della beta.
- **2026-10-12** — Alla famiglia ArtCraft si aggiunge CADCraft, alternativa gratuita e open source ad AutoCAD scritta in Rust, nata il 7 ottobre e a 3.108 stelle al 12: la prima versione, 51.000 righe e 290 comandi, è costata circa 11,5 ore di agente Claude Opus 5.5, e il progetto si dichiara pre-alpha con quattro dei cinque flussi base di AutoCAD ancora fuori dall'alpha. Il DXF è letto e scritto, il DWG passa per conversione con prove solo sintetiche e nessun file di AutoCAD usato come campione, alla licenza MIT o Apache-2.0 del codice si affianca la MPL 2.0 della libreria acadrust.
- **2026-10-13** — Alla famiglia ArtCraft si aggiunge FigCraft, clone di Figma in Rust nato il 9 ottobre e a 327 stelle al 14: si dichiara alpha pronta al 53 per cento per il lavoro reale, con 211 voci del menu di Figma che hanno un comando funzionante, apertura dei file .fig in modalità best effort mai provata su file reali, motore interamente in Rust senza Electron e server MCP che porta i comandi dell'editor dentro un agente.
- **2026-10-13** — Le 13 app della suite Craft vengono provate tutte con Claude Code: ognuna espone il proprio server MCP, che gira headless sui file o si aggancia all'app aperta, e i tredici compiti assegnati finiscono senza toccare il mouse; sei app espongono cinque strumenti comuni mentre le altre sette usano ancora nomi storici.
- **2026-10-14** — EffectCraft, clone di After Effects in Rust nato il 1 ottobre, è a 6.316 stelle al 14 con la versione 0.9.2 del 12 ottobre: 306 effetti, import ed export in formato Lottie, nessuna apertura dei progetti .aep di Adobe, circa 361.000 righe di Rust scritte quasi interamente da agenti e il 75,8 per cento dei commit con Claude fra i coautori.
- **2026-10-14** — Alla suite Craft si aggiunge DesignCraft, alternativa gratuita e open source a InDesign scritta in Rust, nata il 1° ottobre e a 4.031 stelle al 15 con 1.025 commit e 76 contributori: il progetto si presenta come reimplementazione clean-room con doppia licenza MIT o Apache-2.0, dichiara il 69 per cento di copertura delle voci di menu di InDesign 2026 e circa il 47 per cento di prontezza stimata per il lavoro reale, con 420-750 ore di lavoro di agenti AI indicate come distanza dalla beta. Esporta PDF/X-4, EPUB e IDML, che legge e scrive con 49 test su file sintetici, ma non apre i documenti .indd, il formato nativo di InDesign, e il compositore di paragrafi usa l'algoritmo di Knuth e Plass con sillabazione solo in inglese e spagnolo.

- **2026-10-14** — SoundCraft, alternativa gratuita e open source a Pro Tools scritta in Rust, arriva alla 0.7.0 del 14 ottobre con il repository nato il 7 ottobre, 2.890 stelle, 682 commit e 39 contributori: il progetto si presenta come reimplementazione clean-room con interfaccia in egui e dichiara 482 delle 512 voci di menu di Pro Tools Ultimate 2026.4.1 (94,1 per cento), circa il 70 per cento delle funzioni e circa il 40 per cento di prontezza per il lavoro professionale, con 478 comandi pilotabili da script in JSON. Non apre le sessioni .ptx e .ptf né i formati AAF e OMF, l'area hardware è stimata al 12 per cento perché manca uno strato per le periferiche MIDI, quindi una tastiera collegata non suona e non registra, mentre l'esportazione scrive WAV, AIFF o FLAC a 16, 24 o 32 bit con dither, picco, true peak e loudness in LUFS.

- **2026-10-14** — Le tredici app della suite Craft si installano con ArtCraft Launcher (craft-launcher), app nativa in Rust con interfaccia egui e doppia licenza MIT o Apache 2.0, arrivata alla 0.4.1: sceglie il pacchetto giusto per sistema e processore, ne verifica lo SHA-256, installa le app dove le tiene il sistema e propone gli aggiornamenti di quelle già presenti, con build firmate e notarizzate da Apple (Developer ID di Learning Machines LLC) e 25 file per release. Gira su macOS 11 o successivi, Windows 10 e 11 (anche Arm), Linux con glibc 2.35 o successiva e FreeBSD 14, l'interfaccia è tradotta in dieci lingue ma non in italiano, e tra il 13 e il 14 ottobre il repository ha raccolto decine di segnalazioni proprio su installazione e avvio.

- **2026-10-15** — ElixirOffice, suite per ufficio libera con licenza AGPL v3 lanciata da Gaël Duval (creatore di Mandrake Linux e fondatore di /e/OS), entra in beta il 13 ottobre 2026 con una versione desktop per Windows, macOS (solo Apple Silicon) e Linux e una versione server in Docker: il motore è quello di ONLYOFFICE passato per il fork Euro-Office e sopra c'è un'interfaccia che riprende nastro, KeyTips e 228 scorciatoie di Word su Windows e 171 su macOS, con apertura di DOCX, XLSX, PPTX, ODT, ODS e ODP ed export in PDF. L'app desktop lavora offline con un modulo WebAssembly da 3,1 MB compressi e dichiara zero telemetria, ma nella beta mancano stampa unione, confronto tra documenti, cronologia delle versioni, macro, firme digitali, modifica dei PDF ed editor collaborativo, e la versione server non ha ancora un sistema di utenti proprio; il README dichiara che il progetto è supervisionato da Duval ma sviluppato con agenti di codice basati su modelli linguistici, con test automatici e revisioni a ogni modifica.

























## Collegamenti

- [[salesforce]]
- [[index]]

