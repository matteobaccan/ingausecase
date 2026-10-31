---
title: "Telegram"
category: strumento
tags: [messaggistica, bot, privacy, censura, sicurezza]
related_puntate: []
created: 2026-09-21
updated: 2026-10-17
---

# Telegram

## Introduzione

Applicazione di messaggistica che nel 2026 ha aperto la propria piattaforma agli agenti automatizzati degli sviluppatori e, nello stesso periodo, è stata al centro di blocchi nazionali, di un ricatto coordinatosi con l'App Store, di un'inchiesta della Polizia Postale e di un'accusa penale del servizio di sicurezza russo al suo fondatore. Il filo comune delle vicende è la stessa caratteristica che la distingue dalle altre app: canali e gruppi pubblici enormi, bot che chiunque può creare e una gestione dei contenuti che delega molto agli amministratori.

## Funzionalità principali

- **Secretary Mode**: gli sviluppatori di bot possono collegare i propri agenti agli account personali degli utenti, leggere i messaggi in entrata e rispondere per conto del titolare nelle chat selezionate, appoggiandosi all'API Business Connections introdotta nel 2024. Per il destinatario non c'è alcuna marcatura "inviato da bot", quindi l'effetto pratico è quello di un assistente personale invisibile.
- L'attivazione richiede il flag "Business Mode" sul bot via @BotFather, un account abilitato come Telegram Business, permessi granulari su lettura, risposta, gestione di contenuti multimediali e invio di pagamenti, e un solo business bot connesso per volta; le chat in cui un bot ha operato negli ultimi 30 giorni mantengono i metadati di connessione anche dopo la disconnessione.
- Il limite operativo è la finestra delle 24 ore di attività recente di una chat: il bot può scrivere come se fosse l'utente solo dove c'è stato uno scambio reale nell'ultimo giorno, altrimenti l'invocazione fallisce.

## Azienda / Autore

- [[pavel-durov]]

## Timeline delle notizie

- **2026-05-23** — Il pacchetto "AI Bot Revolution: 11 New Features" pubblicato sul blog ufficiale contiene la mossa più radicale: Telegram non fornisce un'AI proprietaria ma apre la piattaforma a chi vuole costruire segretari AI, filtri anti-spam, gestori di lead e autoresponder commerciali, con un consenso utente granulare. La differenza con WhatsApp Business e iMessage è netta, perché gli altri ecosistemi impongono limitazioni o non permettono affatto la delega completa.
- **2026-06-16** — Dal 16 e fino al 22 giugno in India non si riesce ad aprire Telegram: il governo impone un blocco temporaneo per spegnere il mercato nero delle prove d'esame attorno al NEET, il test di ammissione a medicina, dopo l'annullamento della prova di maggio per una fuga di notizie che ha coinvolto oltre due milioni di candidati. Le misure sono due e hanno scadenze diverse: blocco completo dell'app fino al 22 giugno, giorno successivo al re-esame fissato per il 21, e disattivazione della funzione che permette di modificare i messaggi già inviati fino al 30 giugno, per quasi cento milioni di utenti indiani.
- **2026-07-29** — Il Servizio federale per la sicurezza russo annuncia di avere incriminato in contumacia [[pavel-durov]] per favoreggiamento dell'attività terroristica, articolo 205.1 parte 1.1 del codice penale russo, e di avere avviato la procedura per inserirlo nella lista dei ricercati internazionali; il giorno dopo il Rosfinmonitoring aggiunge il suo nome al registro ufficiale di terroristi ed estremisti. L'accusa riguarda il rifiuto di rimuovere canali, chat e bot che i servizi ucraini avrebbero usato per coordinare sabotaggi e attentati, ma tutte le cifre dei comunicati russi, compresi i 46 arresti di persone tra i 12 e i 22 anni in 16 regioni, non sono verificabili in modo indipendente: nelle stesse ore il Comitato investigativo parlava di 19 adolescenti fermati, con uno scarto di oltre il doppio.
- **2026-08-03** — Nella notte [[apple]] rimuove Telegram dall'App Store per circa quaranta minuti, dopo che una revisione dei contenuti aveva trovato materiale pedopornografico in una chat pubblica; entro quaranta minuti Telegram rimuove il contenuto e sospende l'account responsabile, e Apple ripristina l'app. Il giorno seguente Durov pubblica una ricostruzione sostenendo che il materiale è stato piazzato deliberatamente da un estorsore che ricatta i proprietari dei gruppi, modificato con strumenti di intelligenza artificiale e inserito modificando un messaggio vecchio, e che la segnalazione ad Apple era parte dello schema.
- **2026-09-15** — L'operazione Fly Trap della Polizia Postale, coordinata dalla Direzione distrettuale antimafia di Roma, porta a 17 arresti per detenzione e diffusione di materiale pedopornografico: la rete battezzata New Saga riuniva oltre mille utenti in gruppi privati e si teneva in piedi con donazioni in criptovalute. Le ordinanze scattano in tredici sedi con oltre cento operatori, 23 perquisizioni e circa 200 dispositivi sequestrati, e l'indagine del Centro nazionale per il contrasto alla pedopornografia online parte nel 2024 da una segnalazione di Homeland Security Investigations.
- **2026-09-21** — Per due anni e quattro mesi Telegram Desktop ha scritto nei file HTML delle chat esportate il testo dei pulsanti inline dei bot senza filtrarlo, così un bot poteva nascondere uno script che partiva da solo all'apertura del file nel browser: è un XSS memorizzato, vale 8,2 su 10 nella scala CVSS ed è chiuso dal 14 luglio 2026 con la versione 7.0.1. I file già prodotti con le versioni vecchie restano però com'erano, perché l'aggiornamento dell'app non li tocca, e la funzione che avrebbe protetto i messaggi esisteva da tempo senza essere chiamata su quel campo.
- **2026-10-17** — Una lettera depositata in un tribunale federale statunitense mostra la prima risposta concreta di Telegram a una richiesta delle autorità: ID utente, numero di telefono e indirizzo IP con data e ora, tre righe di dati e nulla sui messaggi. La sezione 8.3 della privacy policy consente dal settembre 2024 (dopo l'arresto di Durov in Francia) di comunicare IP e numero di telefono su un valido ordine dell'autorità giudiziaria che indichi l'utente come sospettato; nel 2024 le richieste soddisfatte agli Stati Uniti sono passate da 14 nei primi nove mesi a 900 nell'anno, con 2.253 utenti coinvolti e quasi tutte nell'ultimo trimestre.




## Collegamenti

- [[apple]]
- [[cybersicurezza]]
- [[pavel-durov]]
- [[regolamentazione]]
- [[signal]]
- [[index]]
