---
title: "Computer History"
category: strumento
tags: [openai, chatgpt, memoria, macos, privacy, prompt-injection]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
---

# Computer History

## Introduzione

Funzione dell'app desktop di [[chatgpt]] per macOS, attivata da [[openai]] il 13 agosto 2026, che trasforma quello che si fa sul computer in una cronologia consultabile dal modello: registra clic, digitazione, scorciatoie da tastiera e i passaggi da un'app all'altra, poi ne ricava promemoria testuali che ChatGPT e [[codex]] possono usare nelle conversazioni successive. È spenta di default, si attiva app per app e al debutto non è disponibile nello Spazio Economico Europeo, quindi neanche in Italia.

## Funzionalità principali

- Costruisce una timeline delle attività raccolte dalle app e dai siti autorizzati: da lì si può chiedere cosa si stava facendo prima della pausa pranzo, ritrovare un documento aperto due ore prima o farsi riassumere la mattinata di lavoro.
- Quando il sistema nota che un flusso di lavoro si ripete, la timeline propone di trasformarlo in una skill o in un'automazione da far costruire a [[codex]] partendo dal flusso registrato.
- Sostituisce l'approccio di Chronicle, l'anteprima che catturava screenshot dello schermo a intervalli regolari e li leggeva con l'OCR: Computer History legge gli eventi di interazione esposti dalle API di accessibilità di macOS, lo stesso canale dei software per non vedenti, e questo abbassa molto il consumo di token.
- Restano fuori screenshot, registrazione dello schermo, microfono e audio di sistema, e la navigazione in modalità privata non viene mai inclusa.
- Gli eventi grezzi restano sul Mac in file temporanei per un massimo di 48 ore, mentre i riassunti inviati ai server di OpenAI tornano sul computer come file Markdown in chiaro nella cartella `~/.codex/memories/extensions/skysight/`, dove "skysight" è un residuo del progetto Chronicle; OpenAI dichiara che gli eventi non vengono conservati dopo l'elaborazione né usati per addestrare i modelli.

## Limiti e rischi

- I file di memoria restano sul disco in chiaro e non cifrati e altri programmi in esecuzione con lo stesso utente macOS potrebbero leggerli: OpenAI consiglia di spegnere la funzione durante le comunicazioni con altre persone se non hanno dato il consenso.
- La documentazione riconosce che la funzione aumenta il rischio di [[sicurezza-ai|prompt injection]], perché istruzioni malevole nascoste in un sito o in un'app possono finire per influenzare le risposte del modello; la stampa tecnica ha ribattezzato l'approccio "keylogging amichevole", leggendolo come un meccanismo più profondo di quello di Microsoft Recall, non necessariamente un miglioramento della privacy.
- Richiede la funzione Memories attiva e non funziona con chiavi API o Amazon Bedrock.
- I controlli di cancellazione sono granulari: si può mettere in pausa la raccolta, escludere app e siti, ispezionare le singole voci della timeline, aprire il file di memoria nel Finder e cancellare gli ultimi dieci minuti, un'ora, un giorno o tutto.

## Azienda / Autore

- [[openai]]

## Timeline delle notizie

- **2026-08-14** — Computer History è riservata ai piani ChatGPT Pro, Business ed Enterprise e solo all'app desktop per macOS: sui piani aziendali un amministratore deve abilitarla perché i singoli membri possano attivarla, su Pro l'utente la accende da solo dalle impostazioni sotto integrazioni e controlli dati.
- **2026-08-14** — Al lancio la funzione non è disponibile in Italia perché il Paese rientra nello Spazio Economico Europeo, escluso insieme a Svizzera e Regno Unito; OpenAI ha detto che l'accesso arriverà nelle settimane successive senza una data precisa, e l'esclusione iniziale è letta come regolatoria, perché una registrazione continua dell'attività dell'utente tocca il GDPR e l'AI Act, lo stesso schema già visto con altre novità AI bloccate nell'Unione Europea al debutto.
- **2026-08-14** — La funzione è il tassello che mancava alla strategia agentica di OpenAI dopo la chiusura del browser Atlas: la memoria conversazionale non basta a un agente che deve agire sul computer, che ha bisogno di sapere cosa è stato fatto, con quali app e in che ordine, ed è il motivo per cui la funzione vive nell'app desktop e non nel web.

## Collegamenti

- [[agenti-ai]]
- [[chatgpt]]
- [[codex]]
- [[memoria-ai]]
- [[openai]]
- [[sicurezza-ai]]
- [[index]]
