---
title: "Deepfake"
category: trend
tags: [deepfake, sicurezza, regolamentazione, disinformazione]
related_puntate: []
created: 2026-09-12
updated: 2026-10-19
---

# Deepfake

## Introduzione

Genere di contenuti sintetici generati o alterati con sistemi di intelligenza artificiale che riproducono l'immagine, la voce o il video di una persona reale: non una manipolazione fotografica tradizionale, ma pixel prodotti da un modello generativo, quindi molto più difficili da analizzare a livello forense.

## Evoluzione nel tempo

- Il caso che ha portato il tema al centro del dibattito italiano è il deepfake a sfondo sessuale della premier Giorgia Meloni, che il 5 maggio 2026 ha pubblicato sul proprio profilo X una delle immagini sintetiche che la ritraevano in biancheria intima, denunciando il fenomeno con la frase "oggi capita a me, domani può capitare a chiunque".
- Il salto rispetto al precedente del 2024 è tecnico: dai video con volto sostituito su corpi reali si è passati a immagini interamente generative, con produzione più rapida e un bacino di autori molto più ampio, perché non servono competenze di video editing.
- Il Regno Unito ha esteso l'Online Safety Act ai deepfake non consensuali e un uomo è stato condannato a 26 mesi per deepfake sessuali di donne creati con l'AI; negli Stati Uniti operano il TAKE IT DOWN Act federale e leggi statali in California, Texas e Tennessee, la Corea del Sud ha varato una delle normative più severe dopo lo scandalo dei canali Telegram nelle università e la Cina richiede etichettatura visibile e watermarking sulle piattaforme domestiche dal 2023.

## Numeri

- Uno studio del 2023 confermato dai monitoraggi successivi rileva che il 98% dei deepfake online ha contenuto sessuale e il 99% delle vittime sono donne; il rapporto di UN Women del 30 aprile 2026, curato con la City St George's University di Londra e il laboratorio TheNerve, documenta il 24% di ansia o depressione legate alla violenza online, il 13% con diagnosi clinica di disturbo da stress post-traumatico, il 41% che si autocensura sui social e il 19% sul lavoro.
- I politici sono coinvolti nel 36% degli incidenti deepfake registrati dal 2017, con 143 casi documentati e il 76% degli utilizzi a fini di propaganda o disinformazione.
- Il "liar's dividend" è il danno collaterale: quando tutto può essere falso, anche il contenuto autentico perde forza probatoria e chiunque può dichiarare falso ciò che lo riguarda scaricando l'onere della prova sull'accusatore.

## Attori coinvolti

- YouTube, con Likeness Detection: un sistema di scansione che funziona dentro YouTube Studio come una versione specializzata di Content ID, ma applicata al volto di chi si iscrive, che confronta i nuovi caricamenti con il modello biometrico estratto dalla verifica iniziale e segnala i video sospetti senza rimuoverli in automatico.
- Il Politecnico di Milano, con due progetti di ricerca europei: FF4ALL, che riconosce volti artificiali in foto e video combinando informazioni geometriche tridimensionali e caratteristiche strutturali e ha prodotto il dataset WILD con immagini sintetiche di circa venti modelli generativi, e FUN-Media, che affronta i deepfake vocali con modelli Mixture of Experts, anomaly detection addestrata solo su voci autentiche e attribuzione della tecnologia generativa responsabile, fino al livello dei singoli fonemi.
- Il legislatore italiano, con l'articolo 612-quater del codice penale introdotto dalla Legge 132/2025 e in vigore dal 10 ottobre 2025: punisce con la reclusione da 1 a 5 anni chi diffonde senza consenso immagini, video o voci falsificati con l'AI che cagionino un danno ingiusto, con procedibilità d'ufficio quando la vittima è una pubblica autorità.
- Le piattaforme, chiamate a meccanismi di rimozione rapidi: sul fronte europeo la risoluzione presentata a Bruxelles il 6 maggio 2026 dal gruppo dei Conservatori e Riformisti europei chiede alla Commissione un'applicazione rigorosa degli obblighi di trasparenza dell'AI Act su etichettatura, watermarking e responsabilità delle piattaforme.
- Gli strumenti di verifica: Content Authenticity Initiative di Adobe e Microsoft, le API di rilevamento di Hive AI e Sensity, l'analisi forense di InVID-WeVerify e lo standard di provenance C2PA, nessuno dei quali sostituisce il cross-check della fonte.
- [[apple]], con Apple Reference Image: la firma crittografica nasce dentro il sensore dell'iPhone 18 Pro nell'istante dello scatto, anziché nei metadati aggiunti dopo, e la certificazione resta anonima invece di legare la foto a un'identità. Lo standard C2PA che l'azienda ha scartato è lo stesso usato da Google sui Pixel 10 e da Leica, Sony e Nikon.
- Sul fronte difensivo, YouTube ha aperto Likeness Detection a tutti i creator dai 18 anni, offrendo uno strumento contro i deepfake AI accessibile anche ai non-VIP.
- Chi sfrutta la clonazione vocale: nell'ondata di agosto 2026 contro i fondi di Wall Street l'obiettivo non era il bonifico ma credenziali, reset di password, codici del secondo fattore e sblocchi di accesso ai sistemi interni, con l'help desk al posto del dirigente come bersaglio reale; per il resto bastano pochi secondi di audio pubblico di dirigenti e responsabili tra interviste, podcast e conference call.

## Notizie rilevanti

- Il quadro normativo italiano è il primo nell'Unione europea a prevedere una fattispecie penale specifica sul deepfake; la cornice europea è completata nel giugno 2026 dai primi due decreti attuativi dell'AI Act.
- Il vettore vocale si sposta dalla frode sul singolo dirigente alla raccolta di identità digitali: nel vishing di agosto 2026 il payload è la voce clonata ma la vulnerabilità è il processo di verifica, e la voce al telefono è stata trattata nella pratica come un fattore di autenticazione che non è mai stata.

## Timeline delle notizie

- **2026-05-07** — Il caso Meloni riapre il dibattito su deepfake, art. 612-quater e applicazione dell'AI Act, con i dati di UN Women su vittime e autocensura e l'apertura di Likeness Detection di YouTube a tutti i creator.
- **2026-05-21** — YouTube annuncia che Likeness Detection diventa accessibile a chiunque abbia un account e almeno 18 anni, senza requisiti di iscritti o monetizzazione: l'iscrizione richiede un documento di identità e un selfie video, la scansione è continua ma non automatica, la copertura riguarda solo la somiglianza facciale e non le clonazioni vocali, e la rimozione passa dalla moderazione umana. Il percorso era partito nel 2024 con un'anteprima, era arrivato ai creator partner nel 2025, ai giornalisti a marzo 2026 e all'industria dell'intrattenimento (CAA, UTA, WME, Untitled) ad aprile.
- **2026-06-16** — Il Politecnico di Milano presenta i software che smascherano immagini, video e voci artificiali nati da due progetti europei: FF4ALL per i volti sintetici e il dataset WILD, FUN-Media per le voci con rilevazione e attribuzione della tecnologia generativa. Il caso di partenza è la frode con la voce clonata del ministro Guido Crosetto, costata a un imprenditore circa un milione di euro bonificato verso Hong Kong prima del congelamento; gli attacchi basati su voci sintetiche sono cresciuti di oltre dieci volte nel 2025 e le persone distinguono una voce clonata solo in circa sei casi su dieci.
- **2026-06-20** — Uno studio di UNICEF, ECPAT e INTERPOL in undici Paesi rileva che almeno 1,2 milioni di minori hanno dichiarato di aver subito nell'ultimo anno la manipolazione delle proprie immagini in deepfake a sfondo sessuale; i dati sullo sharenting indicano che un bambino europeo medio ha circa 1.500 foto online prima dei cinque anni, terreno ideale per la creazione di deepfake.



- **2026-08-08** — Un'ondata di vishing con voci clonate colpisce Citadel, Point72, Two Sigma, Millennium Management e diverse società di private equity: le telefonate, arrivate quasi in contemporanea su gestori concorrenti, chiedevano credenziali, reset di password, codici del secondo fattore e sblocchi di accesso ai sistemi interni invece di un bonifico. Per reggere la conversazione serve voice cloning speech-to-speech in tempo reale con latenza bassa, capacità passata in pochi anni dal laboratorio all'abbonamento mensile e che ha moltiplicato la scala delle campagne; il CrowdStrike 2026 Threat Hunting Report registra il raddoppio delle intrusioni via vishing nel primo semestre 2026 e una crescita dell'89% delle minacce con strumenti di AI.
- **2026-09-02** — Anthropic apre claude.com/check-files, lo strumento gratuito che verifica se un file contiene una Content Credential C2PA firmata dall'azienda, cioè se è passato da Claude, e segnala eventuali manomissioni: è la versione operativa dello standard che il settore usa per certificare la provenienza di un'immagine, e ne mostra il limite, perché i metadati spariscono con uno screenshot, un ritaglio o una conversione di formato, spesso senza che nessuno abbia voluto rimuoverli. Il watermark statistico sul testo è più tenace ma cede a parafrasi, traduzione o riscrittura con un altro modello, e nella documentazione Anthropic scrive che l'assenza di un marchio non significa che il contenuto non sia stato generato dall'AI: trovarlo dice qualcosa, non trovarlo non dice quasi nulla, e chi usa un rilevatore come giudice automatico rischia di punire innocenti.

- **2026-09-12** — Il deepfake esce dal perimetro delle celebrità e diventa violenza contro donne comuni: il caso britannico di Lewis Davison, 26 anni, condannato a 26 mesi per immagini sessuali generate di donne e di una ragazza diffuse in gruppi Telegram con didascalie che incitavano allo stupro, arriva in una cronaca ormai mensile, da Strood a Bolton fino all'Essex. Il denominatore comune è che l'autore conosceva le vittime e prendeva le loro foto dai social: la barriera tecnica non esiste più. Sul fronte del rilevamento Google ha esteso a tutti gli utenti il sistema di somiglianze su YouTube e il Politecnico di Milano ha messo a punto un software che smaschera video e voci falsi, ma i generatori restano avanti e i gruppi privati sfuggono ai filtri automatici.
- **2026-09-12** — In India il volto e la voce delle star di Bollywood diventano materia prima per deepfake, endorsement mai concessi e merchandising abusivo, e gli attori passano ai tribunali: il 29 aprile 2026 Arjun Kapoor ottiene dall'Alta Corte di Delhi una tutela provvisoria contro l'uso non autorizzato di nome, voce e immagine, con un'ordinanza mirata a fermare i contenuti "aberranti" e sessualmente espliciti generati con l'AI, mentre l'Alta Corte di Bombay ordina la rimozione dei contenuti che sfruttavano l'identità di Shruti Haasan. La lista di chi ha fatto causa comprende Aishwarya Rai Bachchan, Abhishek Bachchan, Amitabh Bachchan, Karan Johar, Anil Kapoor, Jackie Shroff, Akshay Kumar e i cantanti Asha Bhosle e Kumar Sanu; il diritto indiano chiama questa tutela "personality rights", il diritto a controllare lo sfruttamento commerciale della propria immagine, e i giuristi si aspettano che il 2026 e il 2027 siano gli anni in cui l'ondata di cause diventa una valanga.
- **2026-09-16** — Il 15 settembre 2026 [[apple]] racconta l'architettura di Apple Reference Image, la prima certificazione che parte dal silicio: sull'iPhone 18 Pro e Pro Max il sensore ridisegnato firma i pixel con ECDSA P-256 e SHA-256 subito dopo l'acquisizione e impedisce al firmware di alterarli, il Secure Enclave firma i metadati che il sensore non copre, e lo sviluppo su Private Cloud Compute chiude il file con uno schema ibrido RSA-3072 e ML-DSA-87 pensato per durare oltre l'arrivo dei computer quantistici. La funzione risponde al problema opposto a quello del watermarking: marcare un file è facile, la parte difficile è fare in modo che il marchio resista, come mostra il caso del rilevatore aperto da [[anthropic]] sui propri contenuti e la fragilità di un watermark che si toglie con un semplice salvataggio; il tema della provenienza digitale è segnalato da Gartner tra le tendenze della fiducia digitale (vedi [[digital-provenance]]). La cattura non è disponibile nell'Unione Europea al lancio e il sistema è opzionale: funziona solo se chi scatta ha attivato la modalità prima, e non recupera un'immagine già fatta.
- **2026-09-26** — Sabato 26 settembre 2026 Roberto Vannacci, leader di Futuro Nazionale, ha pubblicato su Facebook una foto della sottosegretaria Matilde Siracusano ritoccata con l'IA: la maglietta bianca dell'originale sparisce e sotto la giacca resta una scollatura profonda. L'immagine non mostra nudità, ma scopre una scollatura che nell'originale non esisteva; Siracusano annuncia la denuncia, Vannacci nega di aver modificato la foto e sostiene di averla presa da un blog calabrese, e il caso esplode alla vigilia delle elezioni suppletive di Reggio Calabria.
- **2026-09-26** — Il fronte legale poggia sull'articolo 612-quater del codice penale, introdotto dalla legge 132/2025 entrata in vigore il 10 ottobre 2025: punisce con la reclusione da uno a cinque anni chi diffonde senza consenso immagini o voci alterate con l'IA e idonee a indurre in inganno, se ne deriva un danno ingiusto, e si procede a querela. La difficoltà è concreta, perché serve un'alterazione capace di ingannare e soprattutto sapere chi ha diffuso cosa; l'AI Act prevede obblighi di marcatura che però non toccano una foto ritoccata a mano e rilanciata sui social, e nessuna difesa tecnica basata sulla provenienza avrebbe aiutato, perché i metadati si perdono passando da un blog e da un social.
- **2026-10-01** — A Singapore un uomo è accusato di aver usato Gemini per creare un falso avvistamento di un coccodrillo in un bacino pubblico, facendo sospendere le attività in acqua e avviare due giorni di ricerche; dopo aver cancellato le prove affronta accuse di diffusione di informazioni false e ostruzione della giustizia, con pene combinate che possono arrivare a dieci anni di reclusione più multe.
- **2026-10-02** — Uno studio peer-reviewed analizza 88 siti che ospitavano immagini intime non consensuali generate con AI e individua Cloudflare, Google, Namecheap, WordPress e Proton tra i fornitori infrastrutturali dominanti, tra hosting, CDN, DNS, certificati, pubblicità, CMS e posta: il lavoro sposta l'attenzione dalla sola generazione dei deepfake alla catena tecnica che ne consente distribuzione e monetizzazione.
- **2026-10-02** — La Corte d'Appello dell'Arizona annulla la condanna a dieci anni per omicidio colposo di Gabriel Paul Horcasitas e ordina una nuova determinazione della pena perché durante l'udienza era stato mostrato un video generato con AI che raffigurava la vittima deceduta mentre parlava al giudice: il collegio ha ritenuto il contenuto inaffidabile perché non documentava eventi o parole reali.
- **2026-10-04** — La corte d'appello dell'Arizona ha annullato il 30 settembre 2026 all'unanimità la pena di Gabriel Horcasitas per l'omicidio colposo di Christopher Pelkey perché in aula era stato mostrato un video generato con l'IA in cui la vittima perdonava l'imputato: la condanna resta, la pena va rifatta. L'opinione qualifica l'ammissione come fundamental error e precisa che resta aperto l'uso dell'IA per ripristinare registrazioni autentiche.
- **2026-10-04** — La Commissione europea conferma il divieto delle app di nudificazione dal 2 dicembre 2026, senza periodo transitorio e con sanzioni fino a 35 milioni di euro o al 7 per cento del fatturato mondiale: la spinta politica era arrivata dalle immagini sessuali false di Giorgia Meloni, e il divieto non risparmia i generatori di immagini generici quando il fornitore non impedisce l'uso per produrre contenuti sessuali di persone reali senza consenso.



- **2026-10-05** — Una corte d'appello federale sospende la legge del Minnesota contro le immagini intime sintetiche realistiche di persone identificabili, accogliendo la richiesta cautelare di [[xai]]: lo Stato difende la norma come tutela contro i deepfake sessuali, l'azienda invoca il Primo Emendamento.

- **2026-10-05** — Tavus presenta Griffin, modello video-to-video per conversazioni faccia a faccia: in uno studio con partecipanti negli Stati Uniti e in Europa 26 persone su 54, il 48 per cento, hanno dichiarato dopo una videochiamata di un minuto di avere creduto di parlare con una persona reale. Con la piattaforma precedente della stessa azienda l'inganno era riuscito a 1 persona su 41, il 2,4 per cento, e lo studio resta condotto da Tavus, su 54 partecipanti e senza gruppo di controllo umano.

- **2026-10-05** — Immagini generate o ritoccate con l'AI entrano in comunità come pesca, skateboard, ciclismo e arrampicata, dove foto e video valgono come prova pubblica di abilità: quando ogni prova visiva diventa sospetta, anche i risultati autentici perdono forza.
- **2026-10-05** — Giorgia Meloni deposita all'Euipo la propria voce come marchio sonoro, quattro secondi con due volte la frase «Io sono Giorgia Meloni», per tutelare timbro e inflessioni dalle clonazioni AI: la domanda è in esame e il marchio copre il timbro, non il diritto d'autore sulla frase, il che lo rende una difesa lenta contro un problema veloce e poco utile contro le truffe anonime. Il fatto è ripreso da Controrumore il 6 ottobre 2026.
- **2026-10-05** — I dati raccolti dall'ANSA il 5 ottobre spostano il baricentro del deepfake verso l'audio: con tre-cinque secondi di parlato pulito un modello moderno restituisce un clone all'85% dell'originale, un deepfake audio costa trenta dollari e la clonazione vocale pesa il 10,5% del totale secondo IdentifAI, ma è la fetta più pericolosa perché aggira la fiducia telefonica, il canale su cui si confermano i bonifici. McAfee misura un aumento complessivo dei deepfake del 900% in un anno, con il 3.000% in più sui tentativi di frode, e Kaspersky un più 1.300% sui crimini di clonazione vocale; il 70% delle persone non si sente sicuro di distinguere una voce reale da una clonata. L'AI Act europeo prevede l'etichettatura dei contenuti sintetici all'articolo 50, ma l'obbligo è stato posticipato dal pacchetto Digital Omnibus.



- **2026-10-06** — L'Internet Watch Foundation rileva nei primi sei mesi del 2026 più immagini fotorealistiche di abuso sessuale su minori generate con AI di quante ne avesse registrate nell'intero 2025: gli analisti hanno valutato 6.310 immagini, circa il 40 per cento in più delle 4.512 dell'anno precedente, comprese manipolazioni di fotografie reali. Il fenomeno aumenta il carico su piattaforme, hotline e forze dell'ordine e spinge l'IWF a chiedere regole più vincolanti e maggiori responsabilità per i fornitori di sistemi generativi.
- **2026-10-07** — Sony Music chiede la rimozione di oltre 260.000 brani deepfake che imitavano artisti reali senza autorizzazione, quasi il doppio delle richieste di marzo, segnale di quanto l'enforcement su copie vocali e attribuzioni false sia diventato industriale.
- **2026-10-08** — Una rete di oltre venti app di incontri gestita da uno studio con base in Cina avrebbe usato numerose personas AI senza dichiarare che non appartenevano a persone reali: secondo un'analisi citata da Channel NewsAsia circa il 75 per cento dei profili dell'ecosistema era generato o gestito con AI, con operatori umani nelle videochiamate, e chat a pagamento e crediti incentivano interazioni prolungate.

- **2026-10-08** — Il Wesleyan Media Project ha tracciato quasi 170 annunci politici generati con AI per circa 80 milioni di dollari di spesa nelle elezioni di metà mandato 2026: candidati e gruppi repubblicani pesano per l'80 per cento degli annunci e l'83 per cento della spesa, appena il 31 per cento ha dichiarato l'uso dell'AI, e il quadro delle regole statali resta frammentato.
- **2026-10-12** — Il disegno di legge danese L 49, presentato l'8 ottobre da Zenia Stampe al Folketing, renderebbe illegale pubblicare imitazioni digitali realistiche di volto, voce e movimenti di una persona senza consenso, con l'onere della prova a carico di chi pubblica e la tutela che dura per tutta la vita e 50 anni dopo la morte. Satira, parodia, caricatura e critica restano consentite finché non diventano disinformazione capace di mettere a rischio diritti essenziali, e l'eventuale entrata in vigore al 1° gennaio 2027 dipende dall'approvazione del Parlamento.
- **2026-10-16** — [[openai]] e [[meta]] portano ai giudici federali USA il problema dell'autenticità delle prove nell'era dei deepfake: possibili regole di verifica in discussione, tracciabilità aperta. Rilevazione citata: 15 giudici su 931 con casi riconducibili a manipolazioni.
- **2026-10-19** — [[apple]] ha aggiornato le linee guida dell'App Store per proteggere le persone dalla diffusione di immagini intime non consensuali, comprese quelle generate con AI, chiedendo agli sviluppatori strumenti per filtrare e segnalare contenuti sessuali espliciti e riservandosi di rimuovere materiali e account; la misura non misura quante violazioni saranno individuate né l'efficacia dell'applicazione.





































## Collegamenti

- [[anthropic]]
- [[apple]]
- [[digital-provenance]]
- [[disinformazione-ai]]
- [[cybersicurezza]]
- [[regolamentazione]]
- [[sicurezza-ai]]
- [[voce-ai]]
- [[griffin]]
- [[index]]
