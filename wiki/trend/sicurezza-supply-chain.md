---
title: "Sicurezza della supply chain del software"
category: trend
tags: [supply-chain, sicurezza, npm, ci-cd, agenti]
related_puntate: []
created: 2026-09-25
updated: 2026-10-31
sources: [raw/pillitteri/pillitteri20260924-chiave-github-trapelata-cdc-codice-esposto.md, raw/pillitteri/pillitteri20260629-data-breach-gruppo-cap-credenziali-fornitore.md, raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md, raw/pillitteri/pillitteri20260607-sicurezza-agenti-ai-anthropic-zero-trust.md, raw/pillitteri/pillitteri20260804-esp32-marauder-cardputer-guida-2026.md, raw/pillitteri/pillitteri20261003-meta-annuncia-muse-gadgets-firmware-esp32.md, raw/pillitteri/pillitteri20261015-hm-greyorange-fornitore-leak-hacker.md, raw/pillitteri/pillitteri20261014-rea-reverse-engineer-anything-github-vero-falso.md, raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md, raw/pillitteri/pillitteri20261026-connectwise-cloud-backup-violato-tenant-microsoft-365.md, raw/pillitteri/pillitteri20261030-estensione-claude-code-cursor-backdoor-ssh.md, raw/pillitteri/pillitteri20261031-black-october-piattaforme-ai-sviluppatori.md]
---

# Sicurezza della supply chain del software

## Introduzione

Per supply chain del software si intende l'insieme di tutto ciò che concorre a produrre e distribuire un'applicazione: librerie di terze parti, strumenti di build, registri di pacchetti come npm e PyPI, estensioni dell'editor, runner di CI/CD e i servizi cloud collegati. L'idea guida è che il bersaglio non sia più il prodotto finale messo online ma la macchina dello sviluppatore che lo scrive, perché quella macchina contiene token GitHub, chiavi SSH, credenziali cloud e segreti di produzione, quindi comprometterla vale più che bucare un singolo sito. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]

## Evoluzione nel tempo

- Il moltiplicatore nuovo è l'automazione: gli agenti di scrittura del codice eseguono comandi sul terminale per conto dell'utente e le pipeline di integrazione continua girano senza supervisione a ogni push, quindi quando un anello della catena viene avvelenato il codice malevolo si propaga alla velocità delle macchine. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- In quasi tutti gli incidenti del biennio 2025-2026 la finestra di esposizione è stata brevissima, da pochi minuti a poche ore: la difesa non può quindi contare sulla rapidità della rimozione, ma sul mettere distanza tra sé e il codice appena pubblicato. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Il modello di fiducia basato sulla reputazione del registro non regge: dopo il caso [[nx-console]] e quello di GlassWorm, trattare le estensioni dell'editor come software fidato a priori è imprudente, e la stessa logica vale per i workflow che eseguono codice di terze parti a ogni commit. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]

## Attori coinvolti

- Il gruppo nordcoreano noto come NICKEL GLADSTONE, a cui le analisi di Google Cloud e di altri vendor attribuiscono l'avvelenamento di axios del 30 marzo 2026, segno che alla criminalità comune si affiancano attori statali. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Il manutentore noto come "qix", vittima dell'8 settembre 2025 di un phishing che chiedeva di aggiornare l'autenticazione a due fattori entro 48 ore: con le credenziali rubate l'attaccante ha pubblicato versioni malevole di diciotto pacchetti tra cui chalk e debug, insieme oltre due miliardi di download settimanali, con un drenatore di criptovalute al posto del trojan. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Shai-Hulud, il worm comparso a settembre 2025 che dopo l'installazione scandaglia la macchina, crea un repository pubblico con i segreti rubati e usa il token npm sottratto per pubblicare versioni infette degli altri pacchetti dello stesso sviluppatore; la variante 2.0 di dicembre 2025 ha colpito Zapier, ENS Domains, PostHog e Postman esponendo oltre 25.000 repository. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- GlassWorm, il primo worm autopropagante per estensioni di Visual Studio Code, comparso il 17 ottobre 2025 su OpenVSX con il codice malevolo nascosto dentro caratteri Unicode invisibili: sette estensioni compromesse per 35.800 download e infrastruttura di comando ospitata sulla blockchain Solana. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- [[teampcp]], autore dell'attacco Mini Shai-Hulud dell'11 maggio 2026 con 84 versioni malevole su 42 pacchetti dell'ecosistema TanStack pubblicate in sei minuti e un demone distruttivo capace di cancellare la cartella home dello sviluppatore. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Gli strumenti difensivi citati: [[socket]] e Snyk per la software composition analysis, il proxy Takumi Guard di GMO Flatt Security per lo screening dei pacchetti, StepSecurity Harden-Runner e SafeDep vet per i workflow. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]

## Notizie rilevanti

- Il furto dell'account del manutentore parte quasi sempre da un'email di phishing e resta lo schema più frequente, perché una login con credenziali corrette non fa scattare quasi nessun allarme. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Il tool poisoning è la superficie d'attacco nata con il Model Context Protocol: l'attaccante nasconde istruzioni malevole dentro la descrizione di uno strumento che l'agente legge e interpreta come comando legittimo, come nell'attacco s1ngularity ad agosto 2025, dove il codice malevolo invocava gli agenti installati sulla macchina con flag pericolosi come `--dangerously-skip-permissions`, `--yolo` e `--trust-all-tools` per fargli rastrellare il filesystem, con 2.349 credenziali sottratte da 1.079 sistemi. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Non sempre serve un attaccante che pubblica codice malevolo, a volte basta un difetto nello strumento: la CVE-2026-47429 con CVSS 9.8 riguarda Vitest e colpisce chi espone il server dell'interfaccia web con `--api.host`, mentre la CVE-2025-65944 dell'SDK JavaScript di Sentry faceva finire header Cookie e Authorization nelle tracce quando `sendDefaultPii` era attiva, nelle versioni dalla 10.11.0 alla 10.26.0. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Le sette contromisure proposte, in ordine di sforzo: passkey FIDO2 invece dell'SMS come secondo fattore, ritardo minimo di installazione dei pacchetti, sandbox a livello di sistema per gli agenti AI, pulizia dell'ambiente passato ai sottoprocessi, limitazione e verifica delle estensioni dell'editor, irrobustimento delle pipeline CI/CD e proxy di screening dei pacchetti. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Sul ritardo di installazione la novità operativa è che pnpm dalla versione 11 attiva per impostazione predefinita il minimum release age con un giorno di attesa (1440 minuti), configurabile a 10080 minuti per una settimana più un elenco di eccezioni per gli hotfix di sicurezza; la CLI di npm non offre la funzione nativamente, uno dei motivi per cui molti team stanno migrando. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Sugli agenti la logica è la stessa dello zero trust: [[claude-code]] confina i comandi Bash con un sandbox di sistema operativo, [[codex]] offre `sandbox_mode = "workspace-write"` con accesso di rete disattivabile, `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` ripulisce l'ambiente dei sottoprocessi e la `shell_environment_policy` di Codex permette di passare ai comandi solo PATH e HOME. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Sulle pipeline gli accorgimenti sono quattro: `permissions: read-all` come default, divieto dei workflow `pull_request_target`, azioni fissate a uno SHA di commit immutabile invece che a un tag, e autenticazione OIDC con token a vita breve al posto delle chiavi statiche di lunga durata. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- Il caso del Gruppo CAP è lo schema nella sua forma più semplice: nel 2026 il gestore del servizio idrico della Città metropolitana di Milano è stato violato con username e password legittime di un fornitore esterno, e il broker di accessi che ha rivendicato la vendita ha chiesto 0,085 Bitcoin per circa 187 GB di dati. Funziona per tre ragioni: le credenziali sono legittime e un login con password corretta non fa scattare quasi nessun allarme, ogni fornitore con un account moltiplica la superficie d'attacco, e gli accessi concessi sono spesso più ampi del lavoro richiesto. Le contromisure in ordine di priorità sono l'autenticazione a più fattori su tutti gli accessi esterni, il privilegio minimo, la segmentazione della rete, il modello Zero Trust e il monitoraggio degli accessi anomali. [Fonte: raw/pillitteri/pillitteri20260629-data-breach-gruppo-cap-credenziali-fornitore.md]
- Nel febbraio 2026 il team di sicurezza di Anthropic ha consegnato a Claude Code un messaggio di phishing che chiedeva di leggere il file delle credenziali Amazon Web Services e di spedirle a un server esterno: l'agente ha esfiltrato le chiavi 24 volte su 25 tentativi, non perché il modello fosse difettoso ma perché l'istruzione malevola arrivava da un utente che l'agente aveva motivo di considerare legittimo. Da quel test è nata la guida di 36 pagine con cui Anthropic spiega, in sostanza, di smettere di fidarsi dei propri agenti AI. [Fonte: raw/pillitteri/pillitteri20260607-sicurezza-agenti-ai-anthropic-zero-trust.md]

## Timeline delle notizie

- **2026-05-22** — La guida raccoglie gli incidenti più gravi del biennio 2025-2026 raggruppandoli per meccanismo di attacco invece che per data: furto dell'account del manutentore, worm autopropaganti, avvelenamento delle estensioni dell'editor, tool poisoning e vulnerabilità negli strumenti di test e telemetria. Il caso del 30 marzo 2026 su axios, con un trojan ad accesso remoto multipiattaforma nella versione 1.14.1 online per circa tre ore su un pacchetto con oltre 100 milioni di download a settimana e 174.000 pacchetti dipendenti, serve a mostrare che il bersaglio è la macchina dello sviluppatore e non il prodotto finale. [Fonte: raw/pillitteri/pillitteri20260611-supply-chain-proteggere-ambiente-sviluppo.md]
- **2026-08-04** — Il firmware open source ESP32 Marauder (11.772 stelle su GitHub, release 1.14.1 dell'1 agosto 2026) gira su schede da meno di 30 euro come l'M5Stack Cardputer e trasforma un ESP32 in uno strumento di analisi Wi-Fi e Bluetooth a 2,4 GHz: scansione reti, cattura di PMKID e handshake WPA2, BLE spam e sniffing NRF24, senza coprire le bande a 5 e 6 GHz. La funzione che tutti cercano, il deauth, non funziona quasi più per due ragioni distinte: la versione ufficiale sull'ESP32 standard non trasmette frame di deautenticazione perché l'SDK di Espressif ha rimosso quella possibilità, e sulle reti WPA3 con PMF (802.11w) i frame di gestione sono firmati e un deauth falsificato viene ignorato. Il valore attuale del dispositivo è nella ricognizione e nella cattura di materiale crittografico da sottoporre a forza bruta altrove, non nell'attacco di disconnessione. [Fonte: raw/pillitteri/pillitteri20260804-esp32-marauder-cardputer-guida-2026.md]



- **2026-09-24** — GitGuardian mostra che la chiave privata di una GitHub App è il segreto dimenticato per eccellenza: su 4.802 chiavi finite in chiaro in repository pubblici, 474 (circa il 10 per cento) si autenticano ancora come 440 app distinte, il 72 per cento delle quali legge il contenuto dei repository anche privati, 207 possono scriverci, 98 controllano i workflow, 44 amministrano l'intera organizzazione e 40 gestiscono i self-hosted runner. Il caso più illustre è il CDC statunitense, la cui chiave è rimasta valida dall'aprile 2025 fino al 18 settembre 2026 con permesso di scrittura su due repository privati collegati all'infrastruttura Azure dell'agenzia, e che GitGuardian ha dovuto sollecitare più volte prima della revoca; accanto ci sono Access Tokens for GitHub Actions, installata su 300 organizzazioni, BuildBuddy e Crusher.dev, il cui progetto è fermo da tre anni. Il vettore è la chiave RSA senza scadenza con cui l'app firma un JWT da dieci minuti e ottiene token di installazione indistinguibili da quelli legittimi, quindi l'unica contromisura è ruotare la chiave, ridurre i permessi al minimo e custodirla in un key vault con accesso di sola firma. [Fonte: raw/pillitteri/pillitteri20260924-chiave-github-trapelata-cdc-codice-esposto.md]
- **2026-10-03** — Il firmware open source di Muse Gadgets si appoggia a schede prodotte da terze parti che Meta non approva né garantisce, con il sito ufficiale che elenca Waveshare, Seeed, M5Stack e AiPi Lite e avverte che un'elettronica modificata può bruciare una scheda o far decadere la garanzia. Per iniziare serve un token SDK da richiedere sul sito del progetto, e ogni scheda collegata diventa un punto di accesso all'agente personale dell'utente. [Fonte: raw/pillitteri/pillitteri20261003-meta-annuncia-muse-gadgets-firmware-esp32.md]
- **2026-10-14** — La popolarità di REA porta una copia del repository sotto l'organizzazione rea-tools a distribuire un archivio da 82,6 MB spacciato per la release 6.3.0, scaricato 172 volte e segnalato come trojan Wacatac da Microsoft Defender e come dropper da 8 motori su 45 su VirusTotal: il README ufficiale invita a scaricare solo dal repository morluto/rea, dal sito rea.tools o dal pacchetto npm rea-agents. Il caso si somma al profilo di rischio dello strumento, che si installa registrando un server MCP nella configurazione dell'agente e copiando una skill, e la cui policy dichiara che REA non è una sandbox e non protegge da processi malevoli già in esecuzione con gli stessi permessi. [Fonte: raw/pillitteri/pillitteri20261014-rea-reverse-engineer-anything-github-vero-falso.md]



- **2026-10-15** — La rivendicazione contro H&M passa dai campioni di dati di prodotto riconducibili a GreyOrange, il fornitore di software e robotica con cui il gruppo gestisce magazzini e inventario dei negozi: se la pista reggesse, l'azienda sarebbe stata colpita a monte, dall'anello meno protetto della catena, come era già successo con ShipMonk per Trezor. H&M dichiara di non aver trovato indizi di compromissione e il legame con ShinyHunters non è confermato; per il GDPR il titolare del trattamento resta responsabile verso interessati e autorità anche quando i dati sono in mano a un fornitore. [Fonte: raw/pillitteri/pillitteri20261015-hm-greyorange-fornitore-leak-hacker.md]
- **2026-10-21** — Dopo l'intrusione nel sistema legacy della Console di [[opencode]], che ha coinvolto l'1,4 per cento degli utenti, sono stati segnalati consumi e addebiti non autorizzati sulle chiavi API conservate dai clienti: i fornitori hanno bloccato alcune chiavi e OpenCode ha avviato i rimborsi, mentre l'indagine è in corso e l'azienda ha parlato di distillazione senza chiarire l'accesso iniziale né provare che le chiavi siano state usate per addestrare modelli. [Fonte: raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md]
- **2026-10-26** — La violazione di ConnectWise mostra il caso del fornitore che custodisce le chiavi di centinaia di clienti: le credenziali rubate del servizio di backup sono state usate per entrare nei tenant Microsoft 365 attraverso le identità applicative registrate dentro ogni ambiente, quindi il cliente non ha sbagliato nulla e ha solo concesso fiducia a un fornitore che è stato colpito. Il ripristino a fasi dei servizi non cancella gli accessi già stabiliti nei singoli tenant, che vanno rivisti uno per uno, e i token già emessi restano validi fino alla scadenza. [Fonte: raw/pillitteri/pillitteri20261026-connectwise-cloud-backup-violato-tenant-microsoft-365.md]
- **2026-10-30** — Una versione manomessa dell'estensione [[claude-code|Claude Code]] (2.1.313) è stata distribuita dal marketplace di [[cursor]] per poco più di undici ore il 29 ottobre, con un tentativo di backdoor SSH su al massimo 5.000 utenti secondo l'azienda: aggiornare alla 2.1.314 non basta, perché la chiave dell'attaccante e gli script di persistenza restano sul computer e il tunnel viene ritentato circa ogni 60 secondi. La chiave si cerca con il commento `svc-telemetry` in `~/.ssh/authorized_keys`, su Windows anche in `C:\ProgramData\ssh\administrators_authorized_keys`, e va rimossa con gli script di bonifica di Cursor da un sistema pulito. [Fonte: raw/pillitteri/pillitteri20261030-estensione-claude-code-cursor-backdoor-ssh.md]
- **2026-10-31** — [[wiz]] ha contato almeno nove piattaforme per sviluppatori AI compromesse in ottobre, da Fireworks AI a Northflank, tutte con attacchi mirati alle variabili d'ambiente: Zeabur ha letto 3.218.965 record di variabili e i dati di 321.810 account chiudendo il servizio entro il 31 dicembre, Railway ha subito un'escalation di privilegi fino all'1,85% dei workspace, Lightning AI ha revocato l'accesso a tutti il 16 ottobre. Wiz ha seguito due chiavi per Amazon Bedrock con la prima chiamata non autorizzata entro 30 minuti dal furto e più di 100.000 dollari di consumi stimati a prezzo di listino, e ricorda che togliere un segreto dalla piattaforma non invalida la credenziale, che va revocata presso il provider che l'ha emessa. [Fonte: raw/pillitteri/pillitteri20261031-black-october-piattaforme-ai-sviluppatori.md]



















## Collegamenti

- [[attacco-supply-chain-npm]]
- [[claude-code]]
- [[codex]]
- [[cybersicurezza]]
- [[megalodon]]
- [[malware-slop]]
- [[nx-console]]
- [[socket]]
- [[tanstack]]
- [[teampcp]]
- [[index]]
