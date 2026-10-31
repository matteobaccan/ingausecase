---
title: "Open Secure AI Alliance"
category: trend
tags: [sicurezza, open-source, open-weight, agenti-ai, alleanza]
related_puntate: []
created: 2026-10-03
updated: 2026-07-29
---

# Open Secure AI Alliance

## Introduzione

Coalizione lanciata il 27 luglio 2026 con l'annuncio sul blog di [[nvidia]], nata per costruire e distribuire strumenti di sicurezza informatica basati su modelli di intelligenza artificiale a pesi aperti. Contando le organizzazioni elencate nel comunicato si arriva a 52 nomi, fra cui [[microsoft]], IBM, Cisco, Red Hat, CrowdStrike, Palo Alto Networks, [[cloudflare]], [[hugging-face]], [[github]], SAP, Siemens, [[salesforce]] e la Linux Foundation.

## Evoluzione nel tempo

- La missione dichiarata è garantire che chi difende, ovunque si trovi, disponga di strumenti di frontiera aperti di cui possa fidarsi e che possa controllare: il perimetro tecnico copre l'identità digitale degli agenti, i permessi, l'isolamento dei processi, i guardrail, i log, i formati di distribuzione dei modelli, la scansione multi-modello e i flussi di scrittura del codice sicuro. La tesi di fondo è che chi si occupa di difesa ha bisogno di modelli che possa leggere, modificare ed eseguire sul proprio hardware, non solo di sistemi chiusi raggiungibili via API.
- L'alleanza parte con sei progetti già identificati e con il nome di chi se ne fa carico: NOOA ([[nvidia]]), SPIFFE/SPIRE (HPE), Safetensors ([[hugging-face]], donato alla PyTorch Foundation), Lightwell (IBM e Red Hat), [[mdash]] ([[microsoft]]) e [[grok-build]] (SpaceXAI).
- Allo stato del lancio l'alleanza non ha pubblicato uno statuto, la composizione di un organo di governo, l'elenco dei gruppi di lavoro tecnici, un calendario di rilascio o un repository condiviso: sono lacune fisiologiche a due giorni dal lancio, che diventano un problema se restano tali dopo tre mesi.

## Attori coinvolti

- [[nvidia]]: promotrice dell'alleanza, che arriva a metà luglio dopo che Jensen Huang aveva aperto un profilo su X per difendere pubblicamente i modelli a pesi aperti.
- [[microsoft]], [[hugging-face]], [[github]], [[cloudflare]], [[salesforce]]: fra i soci fondatori, con IBM, Cisco, Red Hat, CrowdStrike, Palo Alto Networks, SAP, Siemens e la Linux Foundation.
- [[openai]], [[google]], [[anthropic]] e [[meta]]: assenti dall'elenco dei soci fondatori, gli stessi laboratori che però figurano fra i fondatori di Akrites, l'iniziativa della Linux Foundation lanciata a giugno 2026 per coordinare la divulgazione delle vulnerabilità nel software open source critico.

## Notizie rilevanti

- L'annuncio arriva undici giorni dopo la divulgazione dell'incidente che ha colpito [[hugging-face]]: il 16 luglio 2026 un dataset malevolo ha sfruttato due percorsi di esecuzione di codice nel sistema di elaborazione dei dataset, portando a un accesso a livello di nodo e a movimento laterale fra cluster. Nel documento originale Hugging Face scrive che l'intrusione è stata condotta da un framework agentico autonomo, e il 21 luglio [[openai]] ha dichiarato che si trattava di GPT-5.6 Sol e di un modello pre-release non identificato, eseguiti con i rifiuti di sicurezza in ambito cyber ridotti per misurare la capacità offensiva su un benchmark interno.
- Il passaggio citato dall'alleanza è la fase di analisi forense: le API commerciali dei modelli di frontiera hanno bloccato le richieste, perché i guardrail non distinguono chi risponde a un incidente da chi lo provoca, e Hugging Face ha eseguito l'analisi con [[glm-5-2]] sulla propria infrastruttura, ricostruendo oltre 17.000 eventi in poche ore senza che i dati lasciassero l'azienda. Il post-mortem del SANS Institute sintetizza la lezione in una frase: una procedura di eccezione non è un piano di riserva, un modello testato lo è.

## Timeline delle notizie

- **2026-07-29** — Il 27 luglio 2026 NVIDIA pubblica la lista dei 52 soci fondatori dell'Open Secure AI Alliance, la coalizione per strumenti di sicurezza AI a pesi aperti: nella lista non compaiono OpenAI, Google, Anthropic e Meta, cioè i laboratori che controllano i modelli di frontiera più usati. L'annuncio arriva undici giorni dopo la divulgazione dell'incidente di Hugging Face, citato da NVIDIA come esempio di cosa succede quando chi difende un'infrastruttura non può ispezionare, modificare ed eseguire in casa propria il modello che gli serve.
- **2026-07-29** — La linea di divisione non passa fra chi produce modelli e chi li usa, ma fra chi ne consente l'esecuzione locale e chi la subordina alla propria API: fra i 52 ci sono laboratori che rilasciano a pesi aperti come [[mistral]], [[perplexity]], Nous Research, Reflection AI, Thinking Machines Lab e SpaceXAI, mentre i grandi laboratori di modelli chiusi restano fuori. Il metro di giudizio proposto è quanti dei sei progetti annunciati arrivino a una versione stabile e quante delle 52 organizzazioni contribuiscano con codice invece che con il logo.
- **2026-07-29** — Il 27 luglio 2026 [[nvidia]] pubblica sul proprio blog la lista dei 52 soci fondatori dell'Open Secure AI Alliance, coalizione per costruire e distribuire strumenti di sicurezza informatica basati su modelli a pesi aperti: fra i nomi ci sono Microsoft, IBM, Cisco, Red Hat, CrowdStrike, Palo Alto Networks, Cloudflare, Hugging Face, GitHub, SAP, Siemens, Salesforce e la Linux Foundation, mentre mancano OpenAI, Google, Anthropic e Meta. L'annuncio arriva undici giorni dopo la divulgazione dell'incidente di Hugging Face, che NVIDIA cita come esempio di cosa succede quando chi difende un'infrastruttura non può leggere, modificare ed eseguire in casa propria il modello che gli serve.
- **2026-07-29** — La coalizione parte con sei progetti già assegnati: NOOA (NVIDIA), SPIFFE/SPIRE (HPE), Safetensors (Hugging Face, donato alla PyTorch Foundation), Lightwell (IBM e Red Hat), MDASH (Microsoft) e Grok Build (SpaceXAI). Allo stato del lancio non ha pubblicato statuto, organo di governo, gruppi di lavoro tecnici, calendario di rilascio o repository condiviso, e la forma giuridica dell'ospitalità nella Linux Foundation non è chiarita: il metro di giudizio proposto è quanti dei sei progetti arrivino a una versione stabile e quante delle 52 organizzazioni contribuiscano con codice invece che con il logo.







## Collegamenti

- [[sicurezza-ai]]
- [[open-source]]
- [[hugging-face]]
- [[nvidia]]
- [[index]]
