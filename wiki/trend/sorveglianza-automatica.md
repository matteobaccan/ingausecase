---
title: "Sorveglianza automatica: telecamere, targhe e contromisure"
category: trend
tags: [sorveglianza, telecamere, targhe, adversarial, privacy]
related_puntate: []
created: 2026-09-21
updated: 2026-10-21
---

# Sorveglianza automatica: telecamere, targhe e contromisure

## Introduzione

Le telecamere con lettura automatica delle targhe, in gergo ALPR, sono diventate infrastruttura ordinaria delle città americane: la Flock Safety, società che le vende a polizie e amministrazioni locali, fotografa i veicoli che passano, legge la targa e ne isola altri dettagli come gli adesivi sul paraurti. Il punto che trasforma ogni singolo dispositivo in un problema di sistema è che le immagini non restano dentro la telecamera: ad Alpharetta, in Georgia, più di 2.000 agenzie avevano accesso ai registri attraverso la rete nazionale della Flock.

## Attori coinvolti

- Flock Safety, il fornitore delle telecamere, e le polizie e amministrazioni locali sue clienti.
- Collettivi di ricercatori indipendenti, come stegan0gram, e organizzazioni di giornalismo e archiviazione come 404 Media, Distributed Denial of Secrets e WIRED.
- Ricercatori come Bill Swearingen, co-fondatore di SecKC, che lavorano sul lato opposto, quello delle contromisure.

## Notizie rilevanti

- Il software delle telecamere riconosce anche persone e biciclette e gira su un computer di bordo con Android, quindi il perimetro dei dati raccolti è più largo di quello dichiarato dall'etichetta di lettore di targhe.
- Le contromisure esistono e non funzionano schermando le lenti: attaccano il modo in cui l'algoritmo interpreta l'immagine, quindi la telecamera continua a registrare ma il modello non classifica correttamente il mezzo.

## Timeline delle notizie

- **2026-06-24** — Il caso Pokémon Go-Vantor mostra il divario tra consenso giuridico e consenso consapevole: le scansioni erano facoltative e coperte da una licenza trasferibile e sublicenziabile, ma i giocatori difficilmente immaginavano che, anni dopo, la stessa tecnologia avrebbe contribuito a orientare droni e robot militari.

- **2026-08-15** — A DEF CON 34 di Las Vegas, all'inizio di agosto 2026, Bill Swearingen riveste una Toyota Yaris del 2009 con una pellicola adesiva stampata con un disegno astratto e la fa passare davanti a una telecamera Flock: il video viene registrato come sempre ma il software di riconoscimento non riesce a classificare il mezzo come automobile. Il progetto si chiama noRecognition e nasce con l'obiettivo dichiarato di sottrarre le persone al riconoscimento automatico delle telecamere intelligenti, dopo circa un anno di lavoro e circa 31 milioni di test di addestramento secondo quanto raccontato dallo stesso ricercatore.
- **2026-09-16** — Un collettivo di hacker chiamato stegan0gram stacca una telecamera Flock da sopra una strada americana, ne copia l'intera memoria e trova la chiave di cifratura in una partizione non protetta, accanto ai dati che avrebbe dovuto difendere: il materiale arriva a 404 Media e alla no-profit Distributed Denial of Secrets, che lo gira a WIRED, e l'inchiesta congiunta esce il 16 settembre. Il ritrovamento smentisce nel punto più semplice da verificare la promessa fatta ai clienti, cioè che la cifratura sul dispositivo protegge i filmati anche quando qualcuno mette le mani sull'hardware.
- **2026-10-04** — Una giudice federale dell'Oklahoma, Sara Hill, ha stabilito il 1 ottobre 2026 che la ricerca di una targa nel database Flock da parte di un vicesceriffo è stata una perquisizione incostituzionale, definendo la rete di lettori di targhe indiscriminate mass surveillance: i dati Flock e le prove della perquisizione successiva sono stati soppressi. Flock conta più di 5.000 agenzie clienti e tra 120.000 e 138.000 telecamere, e il 2 ottobre Sanders, Merkley e Ocasio-Cortez hanno presentato il Ban Flock Act.
- **2026-10-05** — VIDIZMO ha proposto alle forze dell'ordine di esportare i dati delle telecamere Flock Safety verso sistemi di riconoscimento facciale e strumenti AI per analizzare comportamenti e caratteristiche demografiche, un'integrazione non ancora costruita né usata operativamente.
- **2026-10-06** — [[safedrive]] è la telecamera AI della toscana Sodi Scientifica che analizza l'abitacolo con telecamere ad alta risoluzione e illuminatori a infrarossi, riconosce chi tiene il telefono in mano o viaggia senza cintura e consegna a una pattuglia un'immagine come prova, con i volti in parte sfocati. Dal 21 agosto 2026 è in prova sulla Fi-Pi-Li nel territorio di Lastra a Signa per 90 giorni rinnovabili una sola volta, con la lettura della targa usata anche per i controlli su assicurazione e revisione, e in quella sperimentazione nessuna infrazione comporta multe perché il dispositivo non è omologato dal Ministero delle Infrastrutture e dei Trasporti. Il pilota catalano del Servei Català de Trànsit nell'estate 2026 ha contato oltre 8.500 casi di telefono in mano e circa 4.500 di cintura assente, con un'accuratezza complessiva sopra il 70% e oltre l'84% sul telefono.
- **2026-10-08** — Dopo la copertura di 404 Media, legislatori statunitensi di entrambi gli schieramenti presentano più proposte per limitare l'accesso federale alle reti di telecamere Flock, dal Ban Flock Act che vieterebbe ai lettori di targhe federali fino a un disegno che richiede autorizzazioni scritte, cancellazione dei dati dopo dieci giorni e il divieto di riconoscimento facciale: nessuna misura è ancora legge, ma il confronto sposta privacy, conservazione e sorveglianza algoritmica verso limiti tecnici concreti.
- **2026-10-09** — Un esperimento fai da te rovescia lo sguardo della lettura targhe: lo YouTuber canadese Anthony Sistilli punta una telecamera da 180 dollari e un modello addestrato in venti minuti con l'AI sulle sole auto di polizia, raccogliendo poche decine di rilevamenti, e si ritrova gli agenti della Peel Regional Police a casa il 20 settembre 2026; il confronto con Flock regge solo nella direzione opposta, perché i dispositivi dell'azienda sono oltre 120.000 in 49 stati americani e almeno 153 città hanno rifiutato le telecamere o cancellato i contratti.



- **2026-10-10** — [[flock-safety]], azienda di telecamere con lettura automatica delle targhe, riduce il personale di circa 270 persone, il 18 per cento dell'organico, mentre cresce la polemica sulla sorveglianza AI; l'azienda parla di separazioni volontarie e resta sullo sfondo la preoccupazione per la raccolta e la condivisione dei dati sugli spostamenti dei cittadini.
- **2026-10-12** — Texas Tech University usa un programma AI per individuare nei syllabus i contenuti potenzialmente incompatibili con le nuove regole dell'ateneo e dello Stato: un reportage indica libri e saggi contestati, incluso un testo al quale il sistema avrebbe attribuito affermazioni che una docente non trova nel volume, con restrizioni soprattutto su razza, sesso e discriminazioni.
- **2026-10-12** — Una dipendente da remoto del New Jersey sostiene di essere stata licenziata l'8 settembre 2026 dopo aver rifiutato Sentinel AI, piattaforma di Sutherland Healthcare che scatterebbe una foto dalla webcam del portatile ogni tre minuto (160 in otto ore) usando il riconoscimento facciale per verificarne la presenza: causa depositata il 23 settembre a Atlantic City, l'azienda non commenta e nessun giudice si è espresso. Sul tavolo dei legislatori statali c'è il disegno di legge S4075, passato in commissione il 1 ottobre per 5 a 0, che vieterebbe ai datori di usare IA per monitorare residenza, veicolo personale o proprietà del dipendente e di affidare all'IA le decisioni di assunzione e licenziamento.
- **2026-10-13** — Raven, la piattaforma di geolocalizzazione AI di Graylark Technologies, collega una fotografia degli interni a un indirizzo fisico confrontandola con gli annunci immobiliari pubblicati su servizi come Airbnb e Zillow: in una dimostrazione documentata da 404 Media una lavanderia fotografata viene associata a un immobile di Charlotte. La tecnologia è proposta anche alle forze dell'ordine e solleva interrogativi sulla privacy degli abitanti, anche quando le immagini non contengono coordinate geografiche.
- **2026-10-19** — Documenti interni di una vertenza sindacale canadese rivelano che il sistema AI Atlas di [[amazon]] assegna ai magazzini un punteggio sulla probabilità di organizzazione sindacale o sciopero, attingendo a sondaggi tra i dipendenti, post su Reddit e centinaia di altri segnali, con due magazzini britannici nella categoria a rischio più alto; i sindacati parlano di sorveglianza e Amazon nega di tracciare individui.
- **2026-10-20** — L'Australian Human Technology Institute chiede leggi più forti sulla privacy sul lavoro mentre i datori usano AI, telecamere, tracciamento dei tasti e sorveglianza dei messaggi spesso senza informare i dipendenti: il rapporto cita una cassiera sanzionata per un tasso di errore dello 0,18% e chiede test di equità obbligatori, consultazione dei dipendenti, diritto di reclamo e il divieto degli strumenti di monitoraggio ad alto rischio.
- **2026-10-21** — L'Human Technology Institute dell'Università di Tecnologia di Sydney propone una riforma federale australiana per disciplinare il monitoraggio dei lavoratori, che può includere strumenti AI, videocamere, misure di produttività e controlli delle comunicazioni: il rapporto raccomanda criteri di ragionevolezza, consultazione del personale e un percorso per contestare le pratiche dannose, senza chiedere di eliminare ogni controllo.


































## Collegamenti

- [[cybersicurezza]]
- [[privacy-online]]
- [[regolamentazione]]
- [[riconoscimento-facciale]]
- [[safedrive]]
- [[index]]
