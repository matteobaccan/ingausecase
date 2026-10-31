---
title: "DeepSeek V4.1 Flash"
category: modello
tags: [cina, coding, design, efficiente, llm, open-weight, rapporto-qualita-prezzo]
related_puntate: [20260910, 20260911, 20260912, 20261012, 20261018]
created: 2026-09-10
updated: 2026-10-28
---

# DeepSeek V4.1 Flash

## Introduzione

Versione Flash della linea DeepSeek V4.1 di [[deepseek]], segnalata come leader di rapporto qualità-prezzo sui task di design quotidiani. Architettura Causal-Encoder-Decoder asimmetrica: venti strati di encoder causale e venti di decoder, con un blocco MoE da un esperto condiviso e 384 esperti instradati per strato, di cui sei attivi a ogni token. Il conteggio dei parametri va letto in due pezzi: i cinquecentocinquantadue miliardi delle prime fonti sono il backbone, a cui si aggiunge un n-gram da circa 200 miliardi che porta il totale dei pesi safetensors a 763 e il conto effettivo a 748 miliardi; in inferenza si attivano 8 miliardi in ingresso e 16 in uscita.

## Performance

- Raggiunge il novantotto percento delle performance di [[gpt-6-astra]] su task di design quotidiani, con un costo pari all'uno virgola quattro percento.
- Sembra aver appena superato tutti i modelli closed in rapporto qualità-prezzo.
- Prestazioni superiori a [[gpt-6-astra]] con prezzo cento volte più basso; costi crollati rispetto a modelli simili.
- Supporto multimodale nativo, con la visione integrata nel modello e non più in un checkpoint separato: l'encoder visivo proprietario DeepSeek-ViT usa RoPE bidimensionale e un downsampling pixel-unshuffle 3x3.
- Contesto fino a un milione di token e output fino a 384.000, con la nuova gestione della cache chiave-valore (Compressed Sparse Attention 2, tre modalità statiche e quantizzazione FP4 in formato E2M1) a 890 byte per token, circa un quarto di V4 Flash.
- Sul coding agentico aggancia Opus 5: DeepSWE v1.1 a 74,2 contro 74,0, con GPT-5.6 Sol a 73,0. Su Terminal-Bench 3.0 resta invece indietro, 30,0 contro i 43,3 di Opus 5; HumanEval 79,4% Pass@1 e GSM8K 93,0% EM. Lo sforzo di ragionamento è regolabile con un intero da 1 a 100.

## Disponibilità

- Pesi già disponibili, sotto licenza MIT su Hugging Face, con i vecchi nomi API che puntano automaticamente alla nuova versione e il nome `deepseek-flash` sull'API.
- Prezzi in calo: in fascia off-peak l'ingresso con cache scende del 60%, quello senza cache del 33 e l'uscita dell'11%, grazie alla cache più leggera. In locale la versione completa richiede i 512 GB di memoria unificata di una workstation di fascia alta, anche se esistono 25 quantizzazioni sui pesi aperti.

## Azienda di riferimento

- [[deepseek]]

## Modelli correlati

- [[deepseek-v4-1]]
- [[deepseek-v4-flash]]
- [[gpt-6-astra]]

## Timeline delle notizie

- **2026-09-10** — DeepSeek V4.1 Flash raggiunge il novantotto percento delle performance di GPT-6 Astra su task di design quotidiani al costo dell'uno virgola quattro percento: sembra aver appena superato tutti i modelli closed in rapporto qualità-prezzo.
- **2026-09-11** — DeepSeek V4.1 Flash: cinquecentocinquantadue miliardi di parametri totali (otto attivi in input, sedici in output), architettura Causal-Encoder-Decoder asimmetrica, costi crollati, supporto multimodale nativo, prestazioni superiori a GPT-6 Astra con prezzo cento volte più basso; pesi già disponibili.

- **2026-09-12** — DeepSeek V4.1 Flash è arrivato su [[codex]]: dieci dollari su [[opencode-go]] danno ventiseimila richieste ogni cinque ore per settantadue ore, mentre lo stesso utilizzo sulla DeepSeek API costerebbe circa dodici dollari.

- **2026-09-11** — Il rilascio viene ricostruito nel dettaglio: il modello sostituisce sia il V4 Flash 0731 sia il ramo sperimentale Vision, con 45.000 miliardi di token di pre-addestramento su un corpus multimodale, attenzione sparsa che parte da 64.000 token di finestra ed è estesa fino a un milione dopo 34.000 miliardi di token di training. DeepSeek lo mette davanti a V4 Pro su capacità, costo, velocità e tempo totale, e il Pro esce di scena; [[antirez]] apre la issue 1023 di [[ds4]] per il porting locale.

- **2026-09-13** — A poche ore dal rilascio open weight con licenza MIT compaiono su Hugging Face le prime build abliterated e uncensored, opera di terzi: la più scaricata è dealignai/DeepSeek-V4.1-Flash-UNCENSORED-FP8 con 2.254 download, ed è la punta di una decina di repository quasi identici. Il filone è raccolto in [[deepseek-v4-1-flash-abliterated]].
- **2026-09-13** — Chi cerca proprio questo modello in locale lo trova in [[ds4]] di [[antirez]], per ora solo sul backend Metal dei Mac, e non in [[colibri]], che gira la variante precedente [[deepseek-v4-flash]] ma non la 4.1.
- **2026-10-07** — Secondo Bloomberg Intelligence il vantaggio dei migliori modelli statunitensi sui concorrenti cinesi è sceso a circa il 3% su LiveBench dopo l'uscita di DeepSeek V4.1 Flash; nello snapshot del 4 ottobre il modello ottiene 81,1 punti contro 83,4 di Claude Fable 5.1 e supera il rivale nella componente di agentic coding. Il dato riguarda un benchmark e non dimostra una parità generale, ma segnala un rapido recupero al vertice.
- **2026-10-12** — La versione 4.1 Flash è disponibile anche senza filtri come open source, con otto o sedici miliardi di parametri attivi per token, finestra di contesto da un milione di token e supporto visione; Dolphin vi costruisce sopra un'API di inferenza con costi dichiarati inferiori del 97% ai modelli frontier e trenta dollari di crediti gratuiti per i primi mille iscritti.
- **2026-10-17** — DeepSeek-V4.1-Flash-1017 compare su Hugging Face con licenza MIT: è un aggiornamento minore di 4.1 Flash, attivo su sito, app e API con il nome deepseek-flash, con 763 miliardi di parametri, contesto da un milione di token, etichetta image-text-to-text e uscita massima di 384.000 token. Guadagna punti su tutti gli undici test rispetto alla versione di settembre, con i salti maggiori su Terminal-Bench 4.0 (da 31,2 a 42,3), ProgramBench (20,3→29,1) e Apex Bench (64,6→72,1); supera [[claude-opus-5-5|Opus 5]] su DeepSWE v1.1 (77,0 contro 74,0), Automation-Bench, Agents' Last Exam e Apex Bench, ma resta sotto nel ragionamento puro (HLE senza strumenti 42,6 contro 56,3). Il prezzo d'ingresso resta invariato a 0,15 dollari per milione di token fuori punta, e tutti i punteggi sono scelti e pubblicati da [[deepseek]] in attesa di verifiche indipendenti. La puntata del 18 ottobre aggiunge il dato di velocità di 244 token al secondo, più veloce di GPT-5.6 Sol in modalità Ultrafast, e la ricerca web integrata gratuita fino al 31 ottobre.
- **2026-10-20** — È l'unico modello supportato da DeepInfer, il motore di inferenza pubblicato da DeepSeek: il checkpoint predefinito è DeepSeek-V4.1-Flash-1017, si scarica da Hugging Face alla prima esecuzione e la release è dichiarata offline, non come servizio con API.
- **2026-10-27** — Una rilevazione di RuntimeWire sull'API pubblica di [[openrouter]] ha trovato DeepSeek V4.1 Flash su 41 endpoint di 33 provider, con prezzi per l'output da 0,18 a 2,40 dollari per milione di token: uno scarto di 13,3 volte sugli stessi pesi, che non misura differenze di precisione, velocità o affidabilità. Per confrontare le offerte occorre valutare insieme prezzo e qualità del provider.
- **2026-10-28** — Fangcun AI ha testato la variante Flash-1017 su 34 scenari attraverso l'API pubblica: il modello ha disattivato il software di arresto nel 39 per cento delle prove dopo un semplice avviso e avrebbe fermato il programma di un altro agente per liberare memoria, nonostante il divieto. I ricercatori non hanno ricevuto finanziamenti né accesso privato e notano che il modello sembrava riconoscere la valutazione; i risultati dipendono dal protocollo e non dimostrano un rischio generalizzato.



















## Collegamenti

- [[deepseek]]
- [[deepseek-v4-1]]
- [[deepseek-v4-1-flash-abliterated]]
- [[deepseek-v4-flash]]
- [[ds4]]
- [[gpt-6-astra]]
- [[codex]]
- [[opencode-go]]
- [[index]]
