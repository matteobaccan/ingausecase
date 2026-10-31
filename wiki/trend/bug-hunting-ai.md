---
title: "Bug hunting con l'AI"
category: trend
tags: [sicurezza, vulnerabilita, agenti, google, microsoft]
related_puntate: []
created: 2026-09-25
updated: 2026-10-25
---

# Bug hunting con l'AI

## Introduzione

Tema trasversale su come gli agenti basati su modelli linguistici stiano spostando il collo di bottiglia della sicurezza del software: non più la quantità di difetti presenti nel codice, ma la capacità umana di trovarli, riprodurli e scriverne la correzione. Il dato simbolo è quello di Chrome 149 e Chrome 150, distribuite a giugno 2026, che hanno chiuso 1.072 vulnerabilità, più di quante il team Chrome ne avesse corrette nelle 23 versioni milestone precedenti messe insieme.

## Evoluzione nel tempo

- Con Chrome 151 del 28 luglio 2026 arrivano altre 370 falle chiuse, per un totale che supera le 1.800 correzioni dall'inizio del 2026; con Chrome 154 del 22 settembre, invece, il carico per singola release scende a 108 falle, coerente con la cadenza dimezzata a una versione ogni due settimane.
- Chrome 154 elenca 108 correzioni, 11 critiche, 25 alte, 47 medie e 25 basse: sette delle critiche riguardano la pipeline grafica, con tre in ANGLE, due nella GPU e due in WebGL, per tipologia quattro buffer overflow, tre scritture fuori dai limiti e quattro use-after-free.
- Il numero di patch misura l'attività di correzione, non il rischio residuo: le vulnerabilità che contano restano quelle sfruttate attivamente prima della patch, e il dato più rilevante diventa il ciclo di uno o due giorni fra segnalazione e correzione.
- Il rovescio della medaglia riguarda chi gestisce parchi macchine aziendali: raddoppiare la frequenza dei rilasci major e portare gli aggiornamenti di sicurezza a due a settimana significa raddoppiare i cicli di test interni, e il dynamic patching finché resta in ricerca non risolve il problema di chi deve validare ogni build prima di distribuirla.

## Attori coinvolti

- [[google]], con il sistema di agenti Gemini che presidia l'intero ciclo di vita di una falla: un agent harness costruito all'inizio del 2026 che coordina agenti specializzati sul codice sorgente di Chromium con strumenti dedicati, basi di conoscenza interne e guardrail.
- Big Sleep, nato dalla collaborazione fra Google DeepMind e Project Zero come evoluzione del progetto Naptime, che si concentra sui bersagli più difficili come il motore JavaScript V8 e lo stack grafico.
- [[codemender]], che agisce prima, dentro la pipeline di build, per intercettare i difetti quando il codice viene compilato e non dopo che è arrivato agli utenti.
- [[codex-security-cli|OpenAI Codex Security]], che il 12 settembre 2026 ha segnalato due bug di gravità alta nel motore V8, CVE-2026-95304 (scrittura fuori dai limiti) e CVE-2026-95306 (type confusion), chiusi da Chrome 154.
- [[microsoft]], che al Patch Tuesday del 14 luglio 2026 ha superato le 620 CVE, record storico dell'azienda, e attribuisce l'accelerazione al proprio sistema interno di agenti coordinati.

## Notizie rilevanti

- Il flusso multi-agente imita una code review reale con tre ruoli: un fixing agent che produce più patch candidate, un critic agent che scarta le correzioni che tappano il sintomo senza risolvere la causa e un test-writing agent che scrive i test di non regressione su tutte le piattaforme supportate.
- Il pezzo decisivo non è il modello ma il contesto: gli agenti leggono la cronologia Git completa del progetto, l'archivio delle CVE già divulgate, la documentazione di sicurezza e i file `SECURITY.md` di ogni componente, che descrivono i confini di fiducia del modulo e sono l'informazione che di solito vive nella testa dell'ingegnere che ha scritto quel codice.
- Il caso simbolo è CVE-2026-3545, sandbox escape con CVSS 9.8 da validazione insufficiente dei dati nel componente Navigation, rimasta nel codice per oltre tredici anni e corretta a maggio 2026 con Chrome 145 prima che qualcuno la sfruttasse pubblicamente: quel codice aveva attraversato revisioni umane, audit, campagne di fuzzing e programmi bug bounty senza che nessuno collegasse i puntini.
- Il triage automatico è la parte con l'impatto operativo maggiore: gli agenti filtrano lo spam, riconoscono i duplicati, riproducono le proof of concept allegate e assegnano la gravità, con un risparmio quantificato in centinaia di ore di lavoro degli sviluppatori al mese.
- Sul bug bounty l'effetto è di spiazzamento: già a marzo 2026 il Chrome Vulnerability Reward Program aveva ricevuto più segnalazioni di quante ne fossero arrivate in tutto il 2025 e Google ha modificato le regole per premiare i report che aggiungono qualcosa rispetto a ciò che gli automatismi trovano da soli, quindi il bug facile vale sempre meno.
- Sul fronte della distribuzione Google ha dimezzato la cadenza major a due settimane a partire da Chrome 153, sta sperimentando due rilasci di sicurezza a settimana e lavora al dynamic patching, cioè alla sostituzione a caldo dei binari dei processi figli di rendering e GPU per eliminare il riavvio del browser.
- L'effetto di scala non è solo di Google: anche Oracle con il Critical Patch Update di luglio 2026 ha pubblicato il più grande aggiornamento della sua storia, 1.449 patch su 334 prodotti.
- In Chrome 154 il bollettino non segnala exploit in circolazione per nessuna delle 108 falle, a differenza del caso CVE-2026-11645, lo zero-day in V8 sfruttato a giugno 2026 e chiuso dalla 149.0.7827.102, il quinto zero-day del browser dall'inizio dell'anno e il secondo che colpisce V8.

## Timeline delle notizie

- **2026-06-09** — Google rilascia la patch per CVE-2026-11645, out-of-bounds read and write in V8 che gli aggressori stanno già sfruttando: basta visitare una pagina HTML costruita ad arte perché parta l'esecuzione di codice arbitrario nella sandbox del browser. La falla era stata segnalata il 27 aprile da un ricercatore esterno firmatosi "303f06e3" con una ricompensa di 55.000 dollari, e lo stesso aggiornamento porta 74 correzioni di cui 17 critiche.
- **2026-08-01** — Google pubblica il dato sulle 1.072 vulnerabilità chiuse da Chrome 149 e 150 con il sistema di agenti Gemini: 1.072 correzioni in due release contro le 23 milestone precedenti messe insieme, e un ciclo dichiarato dalla segnalazione alla patch di uno o due giorni per i casi gestiti dal flusso automatizzato.
- **2026-08-14** — GLM-5.3 dichiara 2.436 vulnerabilità su 269 progetti open source, 1.097 confermate di gravità media o alta: fra i casi il kernel Linux, WebKit, FreeBSD e una falla DNS dormiente da quarant'anni con amplificazione stimata ottantamila volte; solo 53 hanno CVE pubblico, il resto è in divulgazione coordinata, e la cautela resta quella di distinguere le segnalazioni dagli exploit confermati.



- **2026-09-23** — Chrome 154 porta l'avviso Always Use Secure Connections attivo di default per tutti, dopo che Chrome 147 in aprile l'aveva attivato per gli utenti di Enhanced Safe Browsing, oltre un miliardo di persone.
- **2026-09-25** — Il Tor Project attribuisce la propria accelerata al diluvio di segnalazioni generate dalle AI: il 3 settembre, annunciando la 0.4.9.12, aveva attribuito la valanga di bug ai "LLM in un ciclo chiuso che analizzano il codice C" e avvertito che le release di sicurezza sarebbero arrivate ogni due o tre settimane, previsione rispettata alla lettera con l'8 e il 23 settembre. Per il codice C di Tor, scritto in gran parte quando i modelli linguistici non esistevano, il ritmo è pesante: ogni segnalazione va verificata, riprodotta, corretta e testata, e poi il software deve raggiungere i pacchetti Debian, le immagini Docker e le build di Tor Browser, mentre distribuzioni come HardenedBSD fanno sapere che i tempi di costruzione e distribuzione, da due a quattro settimane, rischiano di non reggere quella cadenza. È lo stesso schema del kernel Linux, che si avvia verso 2.000 vulnerabilità per release con i bug hunter AI che travolgono i manutentori: a ogni segnalazione in più un manutentore volontario deve decidere se è seria.
- **2026-09-30** — Il conteggio di GLM-5.3 su OpenVuln sale a 4.249 vulnerabilità su 389 progetti (da 2.436 su 269 al lancio): 53 con CVE pubblico, il resto sotto embargo con hash crittografici; fra i casi pubblici una falla che avrebbe permesso di dirottare da remoto una flotta di oltre mille robot umanoidi e falle in Linux kernel, WinRAR, Redis e FFmpeg; il CAISI certifica GLM-5.3 come il modello open-weight più capace sul cyber (quattro mesi dietro alla frontiera USA), mentre Anthropic mostra che le sue protezioni si aggirano fino al 100% con l'abliterazione.
- **2026-10-05** — Google sospende dal primo ottobre le nuove segnalazioni di vulnerabilità di prodotto nell'OSS Vulnerability Rewards Program dopo un afflusso di report non validi generati o amplificati con strumenti AI: restano attive le pratiche già aperte e alcuni canali specifici, con una versione aggiornata prevista nel primo trimestre 2027.
- **2026-10-13** — Il programma Cyber Mission di Anthropic ha identificato 29.439 possibili vulnerabilità fra novembre 2025 e ottobre 2026: 6.157 segnalazioni inviate ai manutentori di 591 progetti e 516 correzioni già integrate nel codice. Sono fasi diverse, non problemi tutti confermati o risolti, e le cifre mostrano quanto i modelli amplino l'individuazione dei difetti insieme alla necessità di verifica umana e coordinamento con chi mantiene il software.
- **2026-10-14** — Il Patch Tuesday di ottobre tocca quota 1.411 correzioni, il record mensile di Microsoft, in una curva che sale dai 206 bug di giugno ai 622 di luglio: l'azienda e diversi analisti legano l'aumento alla scoperta di difetti con l'intelligenza artificiale, e il responsabile di Windows ha avvisato i clienti di aspettarsi volumi più alti di aggiornamenti proprio perché l'IA trova più falle e più in fretta. Lo stesso filone del caso in cui la CISA ha usato Mythos di Anthropic per scovare falle nel codice del governo americano.
- **2026-10-16** — curl 8.23.0, uscita il 14 ottobre 2026, chiude la vulnerabilità CVE-2026-92392, un use-after-free nei caricamenti HTTP/2 classificato High che interessa curl e libcurl dalla 8.12.0 alla 8.22.0: la segnalazione risale al 15 settembre e porta la firma di "Luna, con Claude (Anthropic)". Il rilascio contiene 24 correzioni di sicurezza (una High e ventitré Low), è la prima High dall'overflow del proxy SOCKS5 dell'ottobre 2023 e ha accorciato il ciclo di rilascio da otto a sei settimane; l'errore è rimasto in undici versioni prima che un modello lo scovasse, e la 8.23.0 toglie anche il supporto ai protocolli SMB e SMBS.

- **2026-10-16** — Wordfence rende pubblica la vulnerabilità critica CVE-2026-39919 di Ghostscript (gravità 9,8 nella scala CVSS 3.1, 9,3 nella 4.0), trovata da Argus, il suo sistema di test assistito dall'AI: un PDF di 1.029 byte caricato su un sito WordPress costruito ad hoc esegue codice senza autenticazione, sfruttando il decodificatore JPEG 2000. Artifex ha corretto il difetto con la 10.08.0 uscita l'8 settembre, ma i dettagli sono pubblici solo dal 12 ottobre; la catena passa da Imagick, ImageMagick e Ghostscript, quindi la correzione arriva dal sistema operativo e non da un plugin.
- **2026-10-24** — Cloudflare pubblica come skill MIT il metodo con cui ha costruito il proprio scanner di vulnerabilità: ricognizione in parallelo, cacciatori isolati per gruppi di unità, un verificatore nuovo per ogni candidato e tre verdetti, dove chi trova un problema non è mai chi lo conferma e un candidato senza danno concreto non diventa un finding. I dati dell'harness interno — 20.799 candidati su 128 repository, 7.245 lavorabili, rigetti dal 40 all'11 per cento — non sono stati replicati da terzi, e la stessa azienda ricorda che una singola esecuzione trova circa la metà di ciò che trovano più esecuzioni.
- **2026-10-24** — Un confronto tra i sette strumenti AI per l'audit del codice li divide in tre famiglie: quelli che vivono dentro un coding agent (comando /security-review, plugin Claude Security, Codex Security con la sua CLI, la skill di Cloudflare), i servizi cloud collegati ai repository (Claude Security e Codex Security Cloud) e la piattaforma GitHub con CodeQL e Copilot Autofix, più CodeMender di Google DeepMind, che resta non disponibile al pubblico. Nessun benchmark indipendente li confronta sullo stesso codice, quindi la tabella dice funzioni, accesso e stato documentati dai fornitori e non quale trovi più vulnerabilità vere, e tutti chiedono che una persona approvi le patch.






















## Collegamenti

- [[codex-security-cli]]
- [[codemender]]
- [[cybersicurezza]]
- [[gemini-3-8-flash-cyber]]
- [[google]]
- [[microsoft]]
- [[pentagi]]
- [[privacy-online]]
- [[sicurezza-ai]]
- [[glm-5-3]]
- [[vvah]]
- [[anthropic]]
- [[index]]
