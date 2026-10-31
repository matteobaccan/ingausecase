---
title: "MAI Realtime"
category: modello
tags: [full-duplex, microsoft, realtime, tts, voce]
related_puntate: []
created: 2026-09-12
updated: 2026-09-12
sources: [raw/pillitteri/pillitteri20260802-mai-realtime-microsoft-voce-full-duplex.md]
---

# MAI Realtime

## Introduzione

Modello vocale conversazionale di [[microsoft]], il primo costruito internamente per l'audio in tempo reale: ascolta e parla nello stesso istante (full-duplex) invece di alternarsi a turni. È stato individuato il 2 agosto 2026 da TestingCatalog dentro il MAI Playground come elemento in early access, riservato a un gruppo ristretto di partner e mai annunciato con un comunicato ufficiale, senza benchmark pubblicati né data di apertura al pubblico. [Fonte: raw/pillitteri/pillitteri20260802-mai-realtime-microsoft-voce-full-duplex.md]

## Capacità

- Full-duplex nativo: l'audio è trattato come un flusso continuo nelle due direzioni, quindi il modello può iniziare a formulare la risposta mentre l'utente parla e gestire le sovrapposizioni di voce; nelle pipeline STT-LLM-TTS a turni, invece, interrompere l'assistente lo manda in confusione e il silenzio prima della risposta tradisce la macchina.
- Diciassette lingue, due in più delle 15 di [[mai-voice-2]]: inglese, tedesco, spagnolo, francese, italiano, portoghese, giapponese, coreano, cinese, olandese, hindi, indonesiano, arabo, russo, turco, vietnamita e thai.
- Due voci di partenza, Victoria e Grant; il nome Grant non è inedito, perché nella documentazione di Azure Speech esiste già en-US-Grant:MAI-Voice-2, segno di un'identità vocale mantenuta tra i modelli della famiglia.
- Due modalità di turn-taking: Switchboard, che si appoggia all'endpointer MAI-Ears e intuisce la fine dell'intervento da contenuto e prosodia come farebbe un interlocutore umano, e una modalità deterministica che combina il rilevamento del silenzio con un endpointer semantico basato su Whisper, meno naturale ma più prevedibile nei centralini automatici e nei flussi IVR.
- Pannello di debug con latenza in diretta, passaggi di elaborazione e stato interno del ragionamento durante la conversazione; la condivisione dei campioni audio è indicata come funzione in arrivo.
- Il modello non canta e non produce suoni diversi dal parlato: una scelta di sicurezza che riduce la superficie di abuso, coerente con l'accesso approvato richiesto per la clonazione vocale della famiglia [[mai-voice-2]].

## Performance

Nessun benchmark pubblicato, a differenza dei numeri su CyberGym diffusi per MAI-Cyber-1-Flash. Il resoconto di TestingCatalog riferisce interruzioni gestite in modo pulito e latenza di risposta bassa, senza però una cifra end-to-end confrontabile con i circa 200 millisecondi di Moshi di Kyutai o con [[gpt-live-1]]. [Fonte: raw/pillitteri/pillitteri20260802-mai-realtime-microsoft-voce-full-duplex.md]

## Disponibilità

- Preview interna con accesso riservato ai partner: nel MAI Playground la voce non è selezionabile dagli utenti comuni e non esiste una data di apertura comunicata.
- Il MAI Playground è testabile solo dagli Stati Uniti; per l'accesso operativo le aziende passano da Microsoft Foundry, disponibile globalmente.
- Prezzo non comunicato: nella conversazione continua il costo si calcola sui minuti di audio in entrambe le direzioni, non sui caratteri sintetizzati come per [[mai-voice-2]].
- L'uso degli strumenti esterni durante la conversazione è indicato come previsto ma non documentato in caso di sovrapposizione di voci.

## Rilasci e aggiornamenti

- 2 agosto 2026: comparsa in early access nel MAI Playground, senza annuncio ufficiale.

## Azienda di riferimento

- [[microsoft]]

## Strumenti correlati

- [[gpt-live-1]]
- [[mai-transcribe-1-5]]
- [[mai-voice-2]]

## Timeline delle notizie

- **2026-08-02** — TestingCatalog individua MAI Realtime nel MAI Playground: full-duplex, 17 lingue con l'italiano, le voci Victoria e Grant, due modalità di turn-taking e un pannello di debug con la latenza in diretta; nessun benchmark, nessun prezzo e nessuna data di rilascio. Il modello chiude la catena vocale della famiglia MAI dopo MAI-Transcribe-1 (ascoltare) e MAI-Voice-1 e 2 (parlare), nello stesso disegno di verticalizzazione applicato al codice con MAI-Code-1-Flash e alla sicurezza con MAI-Cyber. Per il mercato italiano il dato che conta è la presenza dell'italiano tra le 17 lingue, a cui si aggiungono le voci italiane già esistenti nella preview di Azure Speech (it-IT-Luca:MAI-Voice-2 e it-IT-Rosa:MAI-Voice-2); sul fronte GDPR resta decisiva la regione di deployment di Speech, che determina dove viene elaborato l'audio. [Fonte: raw/pillitteri/pillitteri20260802-mai-realtime-microsoft-voce-full-duplex.md]

## Collegamenti

- [[gpt-live]]
- [[gpt-live-1]]
- [[mai-transcribe-1-5]]
- [[mai-voice-2]]
- [[microsoft]]
- [[voce-ai]]
- [[index]]
