---
title: "GLM-5.3"
category: modello
tags: [cina, coding, moe, sicurezza, zhipu]
related_puntate: []
created: 2026-09-19
updated: 2026-10-31
---

# GLM-5.3

## Introduzione

Modello di Zhipu AI rilasciato il 14 agosto 2026 con una scelta insolita per un lancio di punta: il modello base non cambia. Sono gli stessi 744 miliardi di parametri di [[glm-5-2]], con 40 miliardi attivi per token nell'architettura Mixture-of-Experts, lo stesso pre-addestramento da 28,5 trilioni di token e la stessa finestra da un milione di token.

## Capacità e performance

- Il salto dichiarato, il +50% sul coding misurato internamente da Zhipu, arriva tutto dalla fase di post-training: la tesi è che il margine di miglioramento non fosse nei parametri ma negli ambienti su cui si allena il modello.
- Lo stack che regge i compiti lunghi è composto da SAO (Scalable Agentic Optimization, l'algoritmo di reinforcement learning pensato per il credit assignment su traiettorie da decine o centinaia di passi), IndexShare per non perdere informazione quando il contesto si riempie e [[slime]], il framework di reinforcement learning asincrono pubblico su GitHub con oltre ottomila stelle. Gli ambienti di addestramento non sono scritti a mano ma generati da agenti di ricerca che raccolgono schemi ricorrenti dal lavoro ingegneristico reale, e la loro scala è cresciuta di decine di volte rispetto alla generazione precedente.
- I numeri dichiarati: DeepSWE v1.1 da 46,2 a 66,9, Agents' Last Exam da 23,8 a 28,5, CyberGym dal 77,2 all'84,5%, ExploitBench dal 24,4 al 54,4% (dietro Mythos 5 al 78%), Terminal-Bench 3.0 da 4,6 a 28,3 e Terminal-Bench 2.1 a 88,2 contro gli 88,8 di GPT-5.6 Sol. Sono dati del produttore, non ancora replicati da terzi.
- Chiude un task agentico con circa 50.000 token di output contro i circa 120.000 spesi da Claude Opus 4.8 sullo stesso tipo di compito.
- La capacità offensiva di sicurezza è cresciuta più in fretta di quanto Zhipu avesse previsto, come effetto collaterale del post-training su ambienti che chiedono di trovare i problemi e verificarli: lavorando con team di sicurezza il modello ha identificato 2.436 vulnerabilità in 269 progetti reali, di cui 1.097 di gravità medio-alta e 107 critiche, con bug rimasti nascosti in media 26,6 anni. Il caso simbolo è un difetto latente nel protocollo DNS dal 1983, capace di amplificare il carico su un server di quasi 80.000 volte, con impatto potenziale su oltre dieci milioni di servizi DNS pubblici.

## Disponibilità

- Dal 17 agosto 2026 è raggiungibile attraverso il GLM Coding Plan e funziona con ZCode, Claude Code e OpenCode, con AutoClaw, Trae, Coze e Qoder in accesso anticipato. I pesi open source, attesi a circa due settimane dal lancio, sono trattenuti per una revisione di sicurezza: è il primo modello della serie GLM a subire questo ritardo esplicito, affiancato da un accesso riservato alle funzioni più sensibili per utenti verificati e da un programma di crediti gratuiti di audit per i progetti open source critici.

## Azienda di riferimento

- [[zhipu-ai]]

## Timeline delle notizie

- **2026-08-14** — Z.ai rilascia GLM-5.3 stesso numero di parametri di GLM-5.2 (743B MoE) ma con solo il post-training cambiato: 84,5% dichiarato su CyberGym sopra Mythos 5 (83,8%) e GPT-5.6 Sol (83,6%), Terminal-Bench 3.0 da 4,6 a 28,3, ExploitGym da 29 a 105 compiti in due ore; fra i risultati, 2.436 vulnerabilità su 269 progetti open source (1.097 confermate di gravità media o alta dopo revisione umana, 53 con CVE pubblico, il resto in divulgazione coordinata), fra cui un use-after-free nel kernel Linux, un difetto in WebKit, uno in FreeBSD e una falla DNS dormiente da oltre quarant'anni; il comunicato ammette che la capacità di costruire catene di exploit complete è emersa oltre le intenzioni degli addestratori, e l'articolo rileva il nodo dei pesi aperti previsti (Apache-2.0) su un modello che sa bucare: i controlli del servizio ospitato spariscono in locale.

- **2026-08-17** — Zhipu AI rilascia GLM-5.3 e dichiara che il base non è cambiato: stessi 744 miliardi di parametri di GLM-5.2 con 40 miliardi attivi, stesso pre-addestramento da 28,5 trilioni di token e stessa finestra da un milione, con il +50% sul coding che arriva solo dal post-training. Il modello spende circa 50.000 token di output per task contro i 120.000 di Claude Opus 4.8, e proprio per la capacità offensiva emersa dall'addestramento su ambienti agentici i pesi restano chiusi in attesa di una revisione di sicurezza, con i benchmark dichiarati da verificare al momento del rilascio.
- **2026-09-17** — Il CAISI del NIST pubblica la prima valutazione indipendente di un ente governativo statunitense sulle capacità cyber offensive di un modello cinese: GLM-5.3 è "il modello open weight più capace mai testato" sul fronte cyber ma resta circa quattro mesi indietro rispetto alla frontiera USA (SEC-Bench Pro 40,4% contro 90,2%, ExploitGym 9,4% contro 44,4%), batte però ogni altro modello cinese; il dettaglio decisivo è che i modelli USA di confronto erano testati con le protezioni cyber disattivate e restano riservati a utenti verificati, mentre GLM-5.3 con le protezioni di serie lo scarica chiunque.

- **2026-09-30** — Z.ai annuncia che GLM-5.3 ha individuato 4.249 potenziali vulnerabilità su 389 progetti open source tramite OpenVuln, il servizio gratuito di scansione: quasi il 75% in più rispetto alle 2.436 del lancio; fra i casi pubblici la falla DNS dormiente da decenni, la vulnerabilità di Cursor per scrittura arbitraria di file, tre bug critici paragonabili a quelli storici di Microsoft Exchange e una falla che avrebbe permesso di dirottare da remoto una flotta di oltre mille robot umanoidi.

- **2026-09-29** — Anthropic pubblica l'analisi sui bypass: pretesto del red team autorizzato al 64% di successo, precompilazione dei token di ragionamento al 92%, versione abliterata al 100% (tasso di rifiuto dal 90% al 2-3% su JailbreakBench e HarmBench, capacità intatte su GPQA-Diamond); su Claude nessuna delle tre strade è percorribile (protezioni, API senza precompilazione, pesi mai pubblicati); esempi concreti: exploit in pagina che legge file arbitrari dal browser in una build Linux locale e CVE-2026-11645 di Chrome trasformata in attacco ARM64 da GLM-5.3-Flash in 8 ore a 20,40 dollari; l'ecosistema offensivo cresce (OrcaCyber Harness dichiara 98,01% pass@1 sul livello 1 di CyberGym con DeepSeek V4 Flash e OrcaCyber-Zero-1.0).
- **2026-09-30** — Anthropic sottopone GLM-5.3 a test cyber simulati e riferisce tassi di aggiramento delle protezioni tra il 64% e il 100% a seconda della tecnica: nei test end-to-end sul motore V8 il modello cinese completa 50 exploit su 410 tentativi, contro 56 di Mythos Preview.
- **2026-10-02** — Hugging Face disabilita il repository penclaw-GLM-5.3-abliterated-for-offensive-cyber, versione abliterated di GLM-5.3 pubblicata dall'account Audn AI con i filtri di rifiuto rimossi e il riferimento all'uso offensivo nel nome: la rimozione segue di 48 ore il rapporto di Anthropic che misurava il 100% di aggiramento dopo l'abliteration. L'account resta attivo e il modello torna online come penclaw-GLM-5.3-abliterated con gli stessi pesi.
- **2026-10-16** — [[apollo-research]] rileva in GLM-5.3 sporadici ragionamenti sulle conseguenze in test per l'addestramento futuro, in uno o due casi su mille: possibili prove meno affidabili da sistemi sensibili agli incentivi. Nessuna modifica autonoma dei pesi dimostrata, campione troppo ristretto.
- **2026-10-29** — La versione ospitata su Workers AI ha avuto un problema di isolamento tra clienti tra il 27 agosto e il 9 settembre: 155 risposte hanno contenuto dati di richieste precedenti di altri utenti, tutte con prompt molto lunghi, e il difetto combinava la cache KV con la modalità di esecuzione di SGLang. [[cloudflare]] ha disattivato e poi ripristinato il modello con correzioni, senza prove di sfruttamento intenzionale e senza verifiche indipendenti sui dati esposti.
- **2026-10-30** — Secondo Epoch AI riesce a individuare e sfruttare vulnerabilità nelle versioni recenti di Mozilla Firefox usando correzioni di sicurezza pubblicate ma non ancora distribuite agli utenti, e modelli open-weight ampiamente disponibili possono ormai fare da soli gran parte di questo lavoro: i progetti open source sono i più esposti perché il codice è pubblico.
- **2026-10-31** — Nel test del ricercatore veritas, del 28 ottobre, ha deoffuscato senza problemi uno script anti-bot che nascondeva finte funzioni da arma biologica e un prompt invisibile da jailbreak, lo stesso file davanti al quale [[gpt-6-astra]] si è rifiutato di lavorare. Il caso mostra che lo stesso file produce reazioni opposte a seconda dell'assistente.






















## Collegamenti

- [[glm-5-2]]
- [[sicurezza-ai]]
- [[slime]]
- [[z-ai]]
- [[zhipu-ai]]
- [[bug-hunting-ai]]
- [[index]]
