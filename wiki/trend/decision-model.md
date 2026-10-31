---
title: "Decision Model"
category: trend
tags: [decision-model, agenti, inferenza, latenza, open-source]
related_puntate: [20261010, 20261012, 20261014]
created: 2026-10-04
updated: 2026-10-25
---

# Decision Model

## Introduzione

Categoria di modelli che non scrive testo ma sceglie una risposta dentro un elenco chiuso, restituendo una probabilità per ogni opzione. Nasce con [[jev]] di TypeSafe il 16 settembre 2026 e in tre settimane conta almeno cinque modelli dello stesso tipo, più i cloni open source del capostipite.

## Perché contano

- La differenza con un LLM sta nel modo in cui arriva la risposta: un LLM genera token dopo token, un decision model fa un solo passaggio in avanti e legge i punteggi delle sole opzioni consentite, quindi il tempo di risposta non cresce con la lunghezza di un testo da scrivere.
- Il caso d'uso è lo strato di controllo degli agenti: instradare un ticket, bloccare un bot, decidere il passo successivo o fermare un agente fuori controllo in pochi millisecondi, come nella Open Agent Safety Platform di [[nvidia]] presentata il 28 settembre 2026.
- La cautela è che quasi tutti i numeri di velocità arrivano dai produttori o dai loro test interni, non da benchmark indipendenti; sulle cifre di Jev TypeSafe dichiara 70-500 millisecondi mentre Cloudflare misura una mediana di 524 millisecondi nel proprio confronto.

## Timeline delle notizie

- **2026-10-04** — Un articolo di sintesi mette a confronto i primi cinque decision model: Jev di TypeSafe (16 settembre, API chiusa), CLM-8B di Stanford e [[nvidia]] (open source), la Decisions API di [[openai]] su GPT-6 Luna (29 settembre, anteprima limitata), [[clef]] e Clef-flash di [[cloudflare]] e [[strands-decider-2b]] di AWS (entrambi il 1 ottobre, open source).
- **2026-10-04** — Il quadro conta anche i cloni open source di Jev — [[semif]], [[kev]], [[jevlike]] e [[laya]], quest'ultimo portato su Apple Silicon con [[laya-mlx]] — che replicano l'interfaccia ma non i pesi né i dati di addestramento di TypeSafe.
- **2026-10-10** — [[microsoft]] presenta Decision-1, modello costruito per le decisioni rapide che nei test interni batterebbe sia gli LLM generalisti sia gli altri decision model su latenza e precisione. [[unsloth]] rilascia nello stesso giorno un notebook gratuito per addestrare decision model personalizzati: [[qwen]] 3.5-4B può generare decisioni invece di testo su otto GB di VRAM, con preparazione dei dati, training e serving inclusi.
- **2026-10-10** — Microsoft-Decision-1 costa 0,042 dollari per milione di token in ingresso con l'output gratuito, le stesse cifre di [[jev]] di TypeSafe, e l'azienda dichiara 2,8 volte la velocità di Jev nel proprio test di latenza; il modello è post-addestrato su Qwen3.5-9B, quindi deriva da un transformer, mentre Jev viene descritto come un design non-transformer. Nessuna delle cifre è stata riprodotta da terzi, il post non elenca i 36 benchmark usati per l'accuratezza e The Register ricorda che i decision model possono sbagliare, con errori che si amplificano quando le decisioni si concatenano.
- **2026-10-12** — Arriva Decision 3.0, famiglia di decision model multimodali open source da 0,6 a 27 miliardi di parametri che si pone al primo posto su entrambe le classifiche Jev Decision Index. Nello stesso giorno Microsoft-Decision-1 entra in Microsoft Foundry e su OpenRouter per routing, classificazione, priorità, verifica e controllo del flusso, mentre [[perplexity]] pubblica [[pplx-decider-v1-1-27b]] e [[cloudflare]] rende multimodale la famiglia di [[clef]] con Clef-omni.
- **2026-10-13** — Un esperimento su Hugging Face affida a [[jev]] i controlli di completamento e le decisioni delimitate di un agente su 360 casi di benchmark: le chiamate al LLM dell'agente scendono del 29,6 per cento, i costi API stimati del 26,6 per cento e la latenza del 19,7 per cento.



- **2026-10-14** — Arriva Amos 1: quattro decision model open-weight da 0,5 a 27 miliardi di parametri che dichiarano il 94,9 per cento su Decision Bench, dieci punti sopra [[jev]] su JevBench hard e davanti a Perplexity e Gemini; leggono foto e rispondono con bounding box, decidono in 27-122 millisecondi e arrivano con API gratuita e licenza Apache 2.0.
- **2026-10-20** — [[jev]] 1.14 aggiunge le domande Box, che restituiscono i quattro bordi di un singolo riquadro come frazioni dell'immagine più una confidenza, e lascia le immagini dietro l'header sperimentale TypeSafe-Danger-Zone-Images: una domanda Box non risponde mai "non trovato", quindi va affiancata a una domanda Noul di controllo sulla presenza dell'oggetto.
- **2026-10-22** — Base Labs presenta due decision model di frontiera, [[mammoth-1]] ed [[elephant-1]], che secondo il blog dell'azienda sono in cima a classifiche come la Jev Decision Index e la Artificial Analysis Decision Index: punteggi e test indipendenti non sono indicati.
- **2026-10-24** — OpenAI apre a tutti i clienti la Decisions API, il modello per scegliere rapidamente tra opzioni che era in accesso limitato, dichiarando risposte passate da uno-tre secondi a circa 100-180 millisecondi, e il cliente Speak misura una riduzione da 1,4 a 0,13 secondi; la concorrenza sul filone dei decision model si intensifica. I dati vengono dall'azienda e dai primi clienti e non coprono costo e accuratezza sulle singole attività.
- **2026-10-24** — Con Decider for Mac [[perplexity]] porta un decision model da 4 miliardi di parametri sul computer dell'utente e lo confeziona in un .dmg con menu, porta configurabile ed esempio curl pronto, dove quasi tutti i concorrenti si scaricano da un repository o si chiamano via API. La stessa richiesta JSON funziona in locale e in hosting cambiando l'URL e aggiungendo la chiave, a 0,01 dollari per milione di token in ingresso nella versione ospitata.

























## Collegamenti

- [[jev]]
- [[clef]]
- [[clm-8b]]
- [[strands-decider-2b]]
- [[laya]]
- [[agenti-ai]]
[[pplx-decider-v1-1-27b]]
- [[index]]
