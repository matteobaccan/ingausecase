---
title: "Voce AI"
category: trend
tags: [asr, tts, voice]
related_puntate: [20260722, 20260724, 20260728, 20260729, 20260731, 20260813, 20260906, 20260907, 20260911, 20260912, 20260913, 20260924, 20261010, 20261012, 20261015, 20261018, 20261021]
created: 2026-08-12
updated: 2026-10-31
---

# Voce AI

## Introduzione

Tendenza nei modelli e strumenti di sintesi e riconoscimento vocale: clonazione della voce, TTS emotivi in realtime e ASR verbatim, sempre più locali.

## Attori coinvolti

- [[audio8]]
- [[auk]]
- [[auk-flash]]
- [[crisperwhisper-2-0]]
- [[luxtts]]
- [[mai-realtime]]
- [[microsoft]]
- [[netease-youdao]]
- [[omnivoice]]
- [[openai]]
- [[tencent]]
- [[vibevoice-asr-streaming-7b]]
- [[voicebox]]

## Timeline delle notizie

- **2026-07-09** — OpenAI annuncia GPT-Live, la voce full-duplex che ascolta e parla nello stesso istante: il modello valuta di continuo se intervenire, inserisce backchannel come "mhmm" e "yeah" mentre l'utente parla e delega ricerche e ragionamenti complessi a GPT-5.5. GPT-Live-1 è l'esperienza vocale predefinita dei piani Go, Plus e Pro mentre il piano gratuito riceve GPT-Live-1 mini; i backchannel sono anche il bersaglio principale delle critiche delle prime ore.
- **2026-07-22** — Voicebox ha clonato la voce da dieci secondi di audio, offline e in ventitré lingue, integrandosi con Claude via MCP.
- **2026-07-24** — La modalità voce di Claude è passata ai modelli più capaci con accesso agli strumenti connessi durante la conversazione e molte più lingue: [[anthropic]] ha aggiornato la voice mode in beta aggiungendo la scelta tra [[claude-opus-5]], Sonnet e Haiku e la connessione ad app come Gmail, Google Calendar, Slack, Notion e Canva; già a giugno la modalità vocale di Claude offriva diciotto lingue e un selettore di modello. È la stessa direzione su cui insiste [[openai]] con ChatGPT Voice sul desktop — la voce non come interfaccia di conversazione ma come modo per far eseguire compiti concreti a un agente.
- **2026-07-24** — NeuTTS 2E offriva sintesi vocale emotiva realtime su CPU.
- **2026-07-28** — CrisperWhisper 2.0 ha portato il riconoscimento vocale verbatim production-grade con timing parola a 29 millisecondi su dieci lingue.
- **2026-07-29** — Fish Audio S2.1 Pro per conversazioni AI real-time con clonazione vocale da campioni brevi; VODER ha unificato otto modalità vocali in locale.
- **2026-07-31** — Inflect 2 Nano e Micro (9 e 4 milioni di parametri) abbastanza veloci per real-time su CPU, GPU, browser e Raspberry Pi; un agente vocale locale completo da STT a TTS ha raggiunto 7.800 stelle.
- **2026-08-02** — [[microsoft]] compare nel MAI Playground con MAI Realtime, modello conversazionale full-duplex individuato da TestingCatalog: 17 lingue con l'italiano, due voci (Victoria e Grant), due modalità di turno di parola e un pannello di debug con la latenza, ma nessun benchmark, nessun prezzo e nessuna data di rilascio.
- **2026-08-08** — La clonazione vocale in tempo reale cambia bersaglio: un'ondata di vishing con voci clonate colpisce Citadel, Point72, Two Sigma e Millennium Management, con telefonate che non chiedono bonifici ma credenziali, reset di password, codici del secondo fattore e sblocchi di accesso, prendendo di mira l'help desk invece del dirigente; il CrowdStrike 2026 Threat Hunting Report registra il raddoppio delle intrusioni via vishing nel primo semestre 2026 e una crescita dell'89% delle minacce che incorporano strumenti di AI.
- **2026-08-13** — LuxTTS è un modello text-to-speech leggero che gira su CPU più veloce del parlato reale: audio a 48 kHz con un solo GB di memoria video, qualità di clonazione vocale dichiarata pari a modelli dieci volte più grandi e funzionamento interamente locale.

- **2026-09-05** — Rai 1 porta in studio Ipazia, un avatar AI che dalla puntata del 4 settembre 2026 affianca Barbara Carfagna nel programma Codice: non recita risposte preparate, viene interrogato in diretta, replica agli interlocutori e può rivolgere lui stesso domande agli ospiti, con un sistema RAG che pesca nell'archivio di dieci edizioni del programma. Rai valuta di inserirlo nella pagina di Codice su RaiPlay perché gli spettatori possano interrogarlo; il nodo dichiarato non è l'effetto scenico ma chi risponde di quello che l'avatar dice, tra supervisione giornalistica e trasparenza sulle fonti.

- **2026-09-06** — NVIDIA PersonaPlex 7B: modello conversazionale open source che parla e ascolta allo stesso tempo, gestisce interruzioni naturali, qualsiasi voce e qualsiasi ruolo definiti da prompt testuale.
- **2026-09-07** — Microsoft VibeVoice-ASR-Streaming-7B (10 lingue, hot-word, diarizzazione realtime) e OmniVoice (600+ lingue, zero-shot, 40x realtime, ~10k stelle) mostrano la spinta verso voce AI locale e streaming.
- **2026-09-11** — Tencent ha rilasciato AuK (1,5B, MIT) che sostituisce un intero stack di tool audio separati via istruzioni in linguaggio naturale: clonazione vocale zero-shot, modifica parole, cambio emozione/pitch/velocità/volume, rimozione accenti, parlato-sussurro, riscrittura cantato preservando melodia e voce, denoising, separazione speaker ed estrazione vocali; AuK-Flash è la versione distillata quattro volte più veloce.

- **2026-09-12** — OmniVoice clona voci a partire da registrazioni brevi, supporta oltre seicento lingue con regolazione di età, tono e dialetto e genera quaranta volte più veloce del tempo reale.

- **2026-09-09** — La traduzione in tempo reale arriva su un prodotto di massa: gli AirPods 5 di [[apple]] traducono una conversazione parlata quasi mentre avviene, con la voce tradotta nell'orecchio invece che su uno schermo, appoggiandosi ad [[apple-intelligence]] su un iPhone collegato. Sedici lingue supportate con l'italiano compreso, funzione ancora in beta e legata alla disponibilità geografica di Apple Intelligence: la novità non è la tecnologia in sé ma il prezzo, perché vive dentro un auricolare da 129 dollari.
- **2026-09-11** — La voce clonata diventa un servizio da browser: [[fish-audio]] clona un timbro da circa dieci secondi di campione, copre 83 lingue con emozioni controllabili e latenza in streaming sotto i 300 millisecondi, con un piano gratuito da 8.000 crediti al mese e il modello S2.1 Pro gratuito per gli sviluppatori; sotto c'è Fish Speech, il modello open source con 32.652 stelle su GitHub.
- **2026-09-11** — La guida a [[omnivoice]] sposta il tema sul locale: clonazione zero-shot da 3-10 secondi di audio, 646 lingue, pesi da 3,3 GB che girano sulla GPU integrata di un Mac Apple Silicon, licenza dei pesi CC-BY-NC per uso non commerciale e un voice-prompt da 17 KB per non ripassare dal campione a ogni frase.
- **2026-09-11** — La voce di OpenAI diventa infrastruttura: [[gpt-live-1]] arriva nelle API a 0,05 dollari al minuto per il livello vocale, con supporto alla telefonia, trascrizioni native, turn detection e comprensione di codici alfanumerici, e il ragionamento delegato al modello abbinato. Sul benchmark Tau3 Voice Intelligence passa dal 45,7% di GPT-Realtime-2 all'86,2%, con la latenza di turno scesa da 1,63 a 0,798 secondi.
- **2026-09-13** — [[voicestudio]] si propone come alternativa open source a [[elevenlabs]] che gira interamente in locale: clona voci, doppia video, genera audiolibri e trascrive audio usando quattordici motori text-to-speech diversi, tutto sulla macchina dell'utente.
- **2026-09-09** — Una funzione di trascrizione vocale finisce dentro un orologio che decine di milioni di persone già portano al polso: [[apple]] presenta Audio Intelligence su Apple Watch Series 12 e Ultra 4, con Live Rewind che riavvolge gli ultimi 15 secondi di una conversazione premendo due volte la Digital Crown e Siri Recap che genera un titolo e punti chiave di una conversazione riconosciuta durante la giornata. Live Rewind mostra lo snippet per circa 30 secondi e non memorizza nulla se non lo salvi tu, Siri Recap gira solo quando lo accendi con orari e luoghi configurabili, e dall'orologio esce un suono udibile anche in modalità silenziosa quando Live Rewind cattura una frase.
- **2026-09-24** — Una giornata di rilasci audio: [[qwen]] porta in Audio 3.1 cinque modelli in un'unica suite (ASR-Next multi-speaker con etichette, timestamp e riconoscimento emotivo, TTS-Next che genera voce, effetti sonori e sottofondo in una sola passata) e taglia il listino fino al novantacinque per cento sull'ASR, [[google]] presenta in AI Studio Gemini 3.8 Flash TTS e Flash-Lite TTS, [[nvidia]] rilascia Nemotron 3 Diarization per le voci sovrapposte fino a otto speaker, [[netease-youdao]] pubblica R2T2 per l'ASR in tempo reale e T3PO per la traduzione realtime, e [[audio8]] annuncia ASR Infinite per lo streaming senza drift.
- **2026-09-09** — La differenza tecnica rispetto a un registratore indossabile qualunque sta in dove finisce l'audio: [[apple]] lo lavora sul dispositivo, dentro una zona blindata del chip S11 chiamata Secure Exclave, dove un modello leggero si limita a capire se una conversazione è partita senza trascrivere né registrare, e l'audio grezzo resta in un buffer isolato via hardware che viene continuamente sovrascritto. Il nodo che nessuna protezione tecnica risolve è il consenso di chi ti sta davanti: la persona che ti parla non ha accettato di farsi riassumere, il suono di avviso non è un consenso e in molte giurisdizioni registrare senza il permesso di tutti i presenti è illegale. In Unione europea le due funzioni arrivano inizialmente escluse.

- **2026-09-26** — Truffatori hanno usato l'AI per impersonare dirigenti e clonare la voce di un professionista, inducendo Fideuram, divisione private banking di Intesa Sanpaolo, a trasferire 95 milioni di euro verso conti esteri; circa 53 milioni sono stati recuperati. Parte del denaro resta dispersa dopo passaggi internazionali e conversioni in criptovalute. Il caso mostra come la clonazione vocale diventi uno strumento operativo nelle frodi ad alto valore. Secondo la ricostruzione di ANSA, Sky TG24 e Open, il falso messaggio WhatsApp era attribuito al CEO di Intesa Sanpaolo Carlo Messina e la telefonata di conferma usava la voce replicata dell'avvocato Paolo Nastasi, managing partner di A&O Shearman Italia ed estraneo ai fatti; a ordinare i bonifici fu il presidente di Fideuram Paolo Molesini, che ha lasciato la carica il 12 marzo 2026. Almeno 36 milioni sono stati convertiti in criptovalute prima che qualcuno potesse fermarli.
- **2026-09-27** — [[neuralink]] mostra il 16 settembre 2026 un video di 23 secondi in cui Terry, terzo paziente del trial VOICE con sclerosi laterale amiotrofica a esordio bulbare, dice "ti amo" alla moglie con una voce sintetica generata dai suoi segnali neurali; [[elon-musk]] lo riprende il giorno dopo e il clip supera i 23 milioni di visualizzazioni nelle prime ore. La voce non è generica: è ricostruita da registrazioni dello stesso Terry precedenti alla malattia tramite Grok Voice di [[xai]], e il decoder ha continuato a funzionare anche quando ha iniziato a immaginare la parola senza muovere nulla. L'N1 è sperimentale, coperto dalla sola Breakthrough Device Designation della FDA, e Neuralink non ha pubblicato dati clinici su accuratezza, vocabolario o latenza.

- **2026-09-28** — Il CEO di [[elevenlabs]] [[mati-staniszewski]] sostiene che le aziende dovrebbero dichiarare esplicitamente quando una chiamata è gestita da un agente AI, lasciando all'utente la scelta tra attendere un operatore umano o parlare subito con un sistema automatico: la posizione arriva mentre la società sposta una parte crescente del business verso i voice agent per il customer support, e la trasparenza diventa parte integrante della diffusione commerciale di voci sintetiche sempre più realistiche.
- **2026-10-01** — Un tribunale di Tokyo riconosce il principio di tutela della voce umana dalla clonazione AI nella causa di Kenjiro Tsuda contro TikTok, estendendo il confronto giuridico sui deepfake dalla replica di immagini e volti alle caratteristiche vocali riconoscibili.
- **2026-10-05** — L'ANSA del 5 ottobre, citando Security.org, McAfee e Kaspersky, mette in fila i numeri della clonazione vocale: bastano tre-cinque secondi di parlato pulito per un clone all'85% di somiglianza, un deepfake audio costa trenta dollari (cinquanta con il video) e Kaspersky misura un più 1.300% dei crimini di clonazione vocale in un anno, mentre i rilevatori automatici perdono fino al 45-50% di precisione quando l'audio passa dal canale telefonico. Il cambiamento che pesa di più è la località: OmniVoice, RVC e XTTS v2 girano sulla GPU di casa senza chiamate di rete né log, quindi la generazione del clone è invisibile dall'esterno e l'unico appiglio investigativo resta il canale con cui il risultato viene diffuso.
- **2026-10-05** — Il volto generato in tempo reale si salda alla voce clonata: Griffin di [[tavus]] clona una voce con circa dieci secondi di audio e la sincronizza a un volto in video full-duplex, con 0,43 secondi di ritardo medio su una GPU H100, mentre l'azienda ammette di dover aggiungere funzioni di segnalazione prima di diffonderlo.



- **2026-10-08** — La Federal Communications Commission valuta di allentare i limiti ai robocall politici verso i cellulari, aprendo a chiamate preregistrate e conversazioni con voci artificiali prima delle elezioni di metà mandato: i gruppi per i diritti digitali temono impersonificazioni e dati personali e richiamano il precedente della voce clonata di Joe Biden.

- **2026-10-08** — CarMax, il maggiore rivenditore di auto usate negli Stati Uniti, instrada le chiamate in ingresso ai negozi e all'assistenza clienti attraverso agenti vocali AI che rispondono alle domande di routine e passano le richieste complesse al personale, estendendoli a valutazioni e appuntamenti per i test drive; il CEO Keith Barr dice che l'AI non può sostituire la vendita perché i clienti vogliono vedere e guidare l'auto.
- **2026-10-10** — Esce un modello vocale open source da 1,7 miliardi di parametri che clona qualsiasi voce in pochi secondi e controlla emozione, età, tono, personalità e accento, multilingua e a bassa latenza. Nello stesso giorno il team turco [[antalia]] presenta Antalia-2 Mini, che gira anche su telefoni vecchi ed è dichiarato più veloce di [[elevenlabs]].
- **2026-10-12** — Nvidia rilascia con pesi aperti un modello audio-nativo da due miliardi di parametri che riunisce trascrizione, traduzione, riconoscimento dei suoni, domande sull'audio, text-to-speech e speech-to-speech in un unico sistema; la puntata non ne riporta il nome.
- **2026-10-15** — xAI porta Grok Voice 3.0 sulle chiamate di assistenza clienti: il modello speech-to-speech risponde in meno di un secondo e costa meno di altri modelli di punta.
- **2026-10-17** — OpenAI apre a tutti i clienti delle API la creazione di voci da un prompt (prompt-to-voice) e aggiunge nove preset per GPT-Live in tedesco, francese, hindi, giapponese e coreano: la voce si sceglie all'avvio della sessione, vive anche nelle instructions di sessione e non è garantita unica, con un tetto di 100 voci da prompt per organizzazione.



- **2026-10-18** — La puntata segnala due progetti vocali: [[tyger]], che ascolta microfono e TTS insieme e ogni ottanta millisecondi decide se parlare, lasciare spazio o fare un cenno sonoro, sostituendo il VAD, e [[ahenk]], TTS open source per il turco che legge numeri, date, prezzi e telefoni e segue istruzioni emotive.
- **2026-10-19** — La baronessa Campbell di Surbiton ha usato una voce generata con AI per intervenire alla Camera dei Lord durante la seconda lettura dell'Health Bill del tredici ottobre: il Parlamento britannico presenta l'episodio come il primo uso di questa tecnologia nelle sue due Camere e come strumento di accessibilità per la parlamentare, impegnata sui diritti delle persone con disabilità. Le fonti non indicano che l'AI abbia scritto il discorso o determinato le posizioni politiche.
- **2026-10-21** — Tre lanci nella stessa giornata spostano il fronte della voce: [[voxtral-3]] di [[mistral]] per trascrizione e sintesi dentro una nuova API per voice agent, [[eleven-realtime]] di [[elevenlabs]] in speech-to-speech con mezzo secondo di avvio e 98,8 per cento su Big Bench Audio, e [[phonon-tts]] con una suite di modelli TTS sotto i cinquanta milioni di parametri per l'esecuzione on-device.
- **2026-10-24** — Il filone full-duplex ha due casi pubblici: [[personaplex]], il modello NVIDIA da 7 miliardi di parametri che rifinisce Moshi di Kyutai e parla solo inglese, e [[dessa]] di Block, addestrato da zero su sole conversazioni registrate e ancora chiuso in lista d'attesa; il primo risale al 15 gennaio 2026, il secondo al 23 ottobre.
- **2026-10-29** — La guida a Home Assistant mostra la catena dell'assistente vocale interamente in casa: la versione 2026.10 è uscita il 7 ottobre, il progetto conta 91.830 stelle su GitHub e l'hub ufficiale Green costa 179 euro, con Assist che riconosce le frasi tramite Speech-to-Phrase o Whisper e con uno speaker Voice Preview Edition che non manda l'audio al cloud. Per le frasi libere si aggiunge un modello linguistico locale con Ollama su un mini PC, senza account né abbonamento.
- **2026-10-29** — La voce in locale è ormai alla portata di un PC normale: la guida indica Whisper large-v3-turbo, o Parakeet v3 di NVIDIA, per la trascrizione e Kokoro o Chatterbox per la sintesi, con un Mac da 16 GB di memoria o una scheda video da 8 GB sufficienti a tenere tutto l'audio fuori dal cloud. Il repository di Whisper supera le 111.540 stelle su GitHub al 29 ottobre 2026.
- **2026-10-31** — [[rivian]] ha concesso a Volkswagen una licenza su elementi della tecnologia del proprio assistente vocale AI, dopo aver introdotto Rivian Assistant sui modelli R1 e R2: nel trimestre i ricavi software e servizi sono cresciuti del 45% a 605 milioni di dollari, un dato che include più attività e non isola l'assistente.
- **2026-10-31** — [[deepgram]] ha annunciato l'acquisizione di Daily, creatrice del framework open source [[pipecat]] per agenti conversazionali, per unire modelli vocali e comunicazione in tempo reale: il framework resterà gratuito con licenza BSD V2 e le due aziende preparano una fondazione indipendente per rappresentare l'ecosistema. Il prezzo non è stato comunicato e l'integrazione punta a migliorare affidabilità e latenza senza offrire ancora risultati di produzione misurati.











































## Collegamenti

- [[audio8-asr-infinite]]
- [[gemini-3-8-flash-tts]]
- [[nemotron-3-diarization]]
- [[netease-youdao]]
- [[qwen-audio-3-1]]
- [[r2t2]]
- [[t3po]]
- [[auk]]
- [[voicestudio]]
- [[auk-flash]]
- [[crisperwhisper-2-0]]
- [[luxtts]]
- [[mai-realtime]]
- [[microsoft]]
- [[neuralink]]
- [[omnivoice]]
- [[openai]]
- [[personaplex-7b]]
- [[tencent]]
- [[vibevoice-asr-streaming-7b]]
- [[voicebox]]
- [[deepgram]]
- [[flux-tts]]
- [[index]]
- [[grok-voice-3-0]]

