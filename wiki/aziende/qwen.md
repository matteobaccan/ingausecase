---
title: "Qwen"
category: azienda
tags: [qwen, alibaba, cina, llm, open-source, open-weight]
related_puntate: [20260512, 20260603, 20260701, 20260811, 20260826, 20260827, 20260901, 20260904, 20260905, 20260907, 20260919, 20260922, 20260924, 20260928, 20260929, 20261002, 20261005, 20261011, 20261013, 20261020]
created: 2026-08-12
updated: 2026-10-29
---

# Qwen

## Introduzione

Famiglia di modelli open-weight del laboratorio Qwen di Alibaba, molto usata per il coding e gli agenti.

## Modelli

- [[agents-a1]]
- [[qwen-audio-3-1]]
- [[qwen3-8-flash]]
- [[qwen-3-8-max]]
- [[qwen-3-8-omni-flash]]
- [[webworld]]

## Strumenti

- [[e-commerce-bench]]
- [[ollama]]
- [[qwen-intelligence]]
- [[open-webui]]
- [[qwen-mm-plugins]]
- [[qwenwork]]

## Timeline delle notizie

- **2026-05-12** — Qwen ha rilasciato WebWorld, serie di modelli per agenti web da 8B, 14B e 32B con licenza Apache 2.0: +9,9% su MiniWob, +10,9% su WebArena, pareggia Claude Opus 4.1 e Gemini 3 Pro, batte GPT-5 come world model.
- **2026-06-03** — I modelli Qwen sono eseguiti localmente con Ollama e Open WebUI nello stack che sostituisce i servizi a pagamento.
- **2026-07-01** — Ha pubblicato una ricerca su agenti di coding RL: studia i segnali di reward a lungo termine (test pass rate, giudici LLM, tracce di esecuzione) mostrando dove ogni segnale smette di tracciare correttezza e inizia a venire hackerato.
- **2026-08-11** — Qwen ha rilasciato Qwen-MM-Plugins: trasforma gli agenti in entita' multimodali native che leggono immagini, video e documenti, editano video e lavorano con tre D e CAD.

- **2026-08-26** — Qwen 3.8 27B gira in locale su GPU da otto GB con IQ4_XS, Q4 KV cache e settantamila token di contesto, e in alcuni test ha battuto Claude Opus 4.6; annunciato Qwen 3.8 Flash-Next, modello multimodale MoE open-weight costruito sulla nuova architettura Qwen 4, con rilascio previsto per domani.

- **2026-08-27** — Qwen 3.8 Flash: modello multimodale MoE open-weight (centoventicinque miliardi con sei miliardi attivi) che anticipa l'architettura Qwen 4. Lanciato QwenWork, piattaforma di prodittività all-in-one in beta globale.

- **2026-09-05** — Qwopus 3.8 27B Flash: fine-tune del modello base Qwen con chain of thought molto più efficiente (a volte di un fattore dieci), disponibile anche in formato NVFP4 per DGX Spark con fino a un milione di token di contesto e supporto immagini e video.
- **2026-09-04** — Qwen ha lanciato E-Commerce Bench, un benchmark per operations business autonome a lungo termine: gli agenti partono con centomila yuan per gestire negozi online per trecentosessantaquattro giorni, ma quasi nessun modello impara a comprare più economico.
- **2026-09-01** — Qwen 3.8 Flash gira su dodici gigabyte di VRAM tramite llama.cpp con memory mapping, quantizzazione della KV cache e offload degli layer MoE su CPU; FreeToken (UC Berkeley) fa girare Qwen 35 miliardi su 8 GB.
- **2026-09-07** — Qwen 3.8 27B gira in BF16 completo su TPU gratuito Kaggle (130 token/s decode, 10k prefill, 262k contesto) come endpoint OpenAI compatibile; Lium ha fatto girare Qwen 3.6 35B a 14.499 token/s su singola GPU Lium (85% più economico di OpenRouter).
- **2026-09-18** — Nella classifica dei modelli cinesi per il coding, Qwen3.8 Max è secondo con un indice BenchLM di 73,2 e 95 miliardi di parametri attivi su 2,4 trilioni totali, sotto licenza Apache 2.0; il campione di efficienza della famiglia è per la fonte Qwen3-Coder-Next, un MoE da 80 miliardi che ne attiva circa 3 per token, tocca il 70% su SWE-bench Verified e gira su una macchina con 46 GB di memoria unificata.
- **2026-09-19** — Alibaba presenta Qwen 3.8-Omni-Flash, primo modello omnimodale costruito per gli agenti: audio, video, ragionamento e uso di tool in un solo modello, contesto da un milione di token con percezione agente attiva e costi video ridotti dell'ottantanove per cento rispetto a Qwen 3.5-Omni-Plus.

- **2026-09-19** — Il sito ufficiale del Federal Register ha usato Qwen di Alibaba per la ricerca nelle proposte regolatorie e poi lo ha rimosso dopo le polemiche; il caso porta un modello cinese in un servizio governativo USA senza prove di compromissione.
- **2026-09-22** — Qwen-Image 2.1 locale senza restrizioni in varianti Uncensored GGUF e Heretic 4-16 GB.
- **2026-09-22** — Federal Register USA usa brevemente Qwen3 0.6B per ricerca documenti prima di rimuoverlo.
- **2026-09-22** — All'Apsara Conference di Hangzhou (22-24 settembre) il team mostra in anteprima quattro tier della generazione successiva — Qwen 4 Max, Qwen 4 Flash, Qwen 4 Plus e Qwen 4 27B — senza data di rilascio, prezzo, contesto dichiarato né pesi scaricabili: Max come flagship, Flash per la bassa latenza, Plus bilanciato e multimodale, 27B open weight per l'uso locale.
- **2026-09-22** — Il riferimento per prestazioni della famiglia resta Qwen3.8 Max, disponibile dal 3 agosto con 2.400 miliardi di parametri MoE e 95 miliardi attivi, un milione di token di contesto, 2 e 6 dollari per milione di token e il primo posto nelle valutazioni Artificial Analysis Agentic AI e CodeArena per il coding front-end; dei quattro tier mostrati ad Apsara non eredita invece nulla di verificabile.
- **2026-09-24** — Rilascia Audio 3.1, suite di cinque modelli che copre riconoscimento vocale, sintesi, interazione in tempo reale e creazione audio: ASR-Next trascrive multi-speaker con etichette, timestamp e riconoscimento emotivo, TTS-Next genera voce, effetti sonori e sottofondo in un'unica passata, e il listino cala del settanta per cento sul TTS, dell'ottantacinque sul realtime e fino al novantacinque sull'ASR.
- **2026-09-24** — Presenta Qwen Intelligence, tre agenti per dispositivi mobile: Mobile Planner Agent pianifica e orchestra task complessi ed è primo su MobilePA-Bench, Mobile-Use Agent esegue in modalità API-first con 92,2 su MobileWorld-Real e novanta per cento di successo end-to-end, Mobile Creative Agent genera contenuti pronti all'uso in tre secondi.

- **2026-09-28** — Il modello distillato accelerato di [[qwen-image-2-1]] porta la velocità end-to-end a cinque volte quella del modello base a quaranta step: funziona in locale, senza connessione e senza censura, supporta NSFW di default ed è eseguibile anche con bassa VRAM.
- **2026-09-29** — Le prime prove della community vedono Qwen 4 battere Fable 5 e avvicinarsi alla qualità di Fable-Opus, con le varianti da 27B in arrivo per prime.
- **2026-10-05** — Rilascia Consistent Lighting, un LoRA per [[qwen-image-2-1]] che inserisce oggetti nella scena con ombre naturali e highlight speculari, senza riflessi falsi.
- **2026-10-05** — Le build GGUF di [[qwen-image-2-1]] etichettate «uncensored» su Hugging Face sono solo quantizzazioni del modello originale, e la versione davvero senza censure non è ancora pronta: il modello resta sotto Qwen Research License e i rifiuti segnalati stanno nei servizi ospitati, non nei pesi.
- **2026-10-09** — Ecosia sceglie Qwen di Alibaba tra i modelli open-weight con cui sostituire Mistral, serviti dalla piattaforma tedesca Melious su infrastruttura europea.
- **2026-10-10** — Microsoft post-addestra Qwen3.5-9B, modello open-weight da 9 miliardi di parametri, per costruire il decision model Decision-1, e annuncia che a breve lo rifonderà su altri modelli, tra cui la famiglia MAI e quelli di OpenAI, senza spiegare la scelta; anche Cloudflare ha costruito Clef-flash sulla stessa base.
- **2026-10-11** — Qwen4-27 e Qwen4-max usciranno insieme, entrambi open weight: la conferma è arrivata oggi.
- **2026-10-13** — Alibaba presenta QwenGyre, sistema di reinforcement learning elastico per l'addestramento su orizzonti estremamente lunghi: porta NL2RepoBench dal 52,5 al 58,5 per cento in quarantotto step con circa 700.000 token per rollout e riduce del 44 per cento il tempo di training end-to-end rispetto ai sistemi asincroni.
- **2026-10-19** — [[alibaba]] vuole estendere nel 2027 l'uso dell'AI ai flussi di lavoro dei venditori su Taobao e Tmall tramite Qwen Work, in prova per lanciare prodotti, preparare pubblicità e gestire l'assistenza clienti, con la vendita di token AI e computer con modelli Qwen preinstallati.
- **2026-10-20** — Il team Qwen pubblica [[opengcua]], framework open source in cui i modelli decidono quando guardare lo schermo e come agire; su OSWorld-v2 otto modelli guadagnano in media 19,6 punti con il 53% di passi in meno.
- **2026-10-29** — All'Apsara Conference di Amsterdam, prima edizione europea dell'evento, un partecipante ha riportato dal palco la frase «Qwen4 next week» attribuita a Feifei Li, CTO di Alibaba Cloud, mentre una slide di Xudong Guo diceva soltanto «coming soon»: la settimana indicata è quella dal 2 all'8 novembre, ma né Alibaba né il team Qwen hanno confermato una data in un canale ufficiale. L'indizio tecnico è nel codice di Qwen Code, dove il 28 ottobre la modifica 15762 ha assegnato a tutti gli identificativi qwen4 una finestra di contesto da un milione di token (prima il valore di ripiego era 262.144), con l'autore stesso che precisa come il dato sia riferito da un revisore e non misurato; fra i nomi provati compaiono qwen4-max, qwen4-plus, qwen4-coder-plus, qwen4.5-max e qwen4-omni-120b-think.

- **2026-10-29** — La generazione 3.8 servita finora come anteprima dell'architettura di Qwen4: [[qwen3-8-flash]] con pesi aperti, 125 miliardi di parametri più 51 miliardi di embedding N-gram, e il 27B usato in locale; per Max e Plus il precedente è la distribuzione via API, quindi la versione che la community attende su Hugging Face è il Qwen4 27B.




























## Collegamenti

- [[agents-a1]]
- [[qwen3-8-flash]]
- [[ollama]]
- [[open-webui]]
- [[qwen-3-8-max]]
- [[qwen-mm-plugins]]
- [[qwen-intelligence]]
- [[qwen-audio-3-1]]
- [[qwen-3-8-omni-flash]]
- [[qwenwork]]
- [[webworld]]
- [[index]]

