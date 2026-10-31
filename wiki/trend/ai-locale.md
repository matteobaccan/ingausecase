---
title: "AI locale"
category: trend
tags: [edge, hardware, locale, on-device, open-source]
related_puntate: [20260925, 20260927, 20261008, 20261009, 20261010, 20261013, 20261015]
created: 2026-09-12
updated: 2026-10-29
---

# AI locale

## Introduzione

Tema trasversale sull'inferenza che gira sulla macchina dell'utente invece che su un server: modelli on-device, motori di esecuzione, requisiti di memoria e il confine mobile tra locale e cloud. La spinta è doppia: i dati non lasciano il dispositivo e il costo per token scende a zero dopo l'hardware.

## Evoluzione nel tempo

- Il collo di bottiglia si sposta dalla potenza di calcolo alla memoria. Con la quantizzazione a 4 bit, il formato che quasi tutti usano perché taglia l'occupazione di circa il 75% perdendo meno dell'1% di qualità, un modello da 7-8 miliardi di parametri sta in circa 8 GB, uno da 14B intorno ai 16 GB, un 30B su 24 GB e i 70B chiedono 48 GB o più; sui Mac conta la memoria unificata, non una VRAM separata.
- I numeri dei runtime non sono più da nicchia: Ollama ha superato le 179.918 stelle su GitHub e llama.cpp le 126.680, il motore C++ che sta sotto quasi tutti gli altri; vLLM, oltre 90.000 stelle, è il riferimento per servire molti utenti in parallelo.
- La qualità dei modelli locali medi ha quasi agganciato quella dei modelli chiusi: sull'Artificial Analysis Index di settembre 2026 il divario per i compiti quotidiani si sente poco, e resta netto solo sul ragionamento lunghissimo e sui progetti di codice enormi.
- Sul fronte mobile la barra si alza: l'AI di sistema più evoluta chiede hardware recente, e il supporto alle funzioni AI on-device segue regole proprie, diverse dagli aggiornamenti di sistema.
- La visione smette di essere una funzione solo cloud: con DS4 un modello multimodale quasi di frontiera analizza immagini in locale su Mac, NVIDIA e AMD con lo stesso motore.
- Sul desktop l'AI locale diventa una categoria di prodotto: Apple apre i preordini del Mac Studio M5 Ultra con 512 GB di memoria unificata e 1,2 TB/s di banda (il 50% in più dell'M3 Ultra) e presenta lo stesso giorno il Mac mini M6, mentre Xiaomi mostra l'AI Cube con tre chip. Il parametro che conta resta la banda, non la RAM: ogni token generato rilegge i pesi attivi, quindi il collo di bottiglia è quanti gigabyte al secondo la memoria sposta.
- Sul ferro il parametro che decide è la memoria per euro, non i teraflops: per l'inferenza quantizzata il modello deve stare tutto nella VRAM, quindi comprare gigabyte costa meno che comprare potenza di calcolo e le vecchie GPU da datacenter rottamate vendono proprio i gigabyte a sconto. In Europa, però, alla scheda va aggiunta la bolletta: un acceleratore da 250 watt acceso qualche ora al giorno supera i 100 euro l'anno a 0,30 euro per kilowattora, e le schede da datacenter consumano molto anche da ferme.

## Attori coinvolti

- Runtime: [[ollama]], [[llama-cpp]], [[vllm]], [[ds4]] e [[strata]], più LM Studio per chi vuole un'interfaccia grafica e Jan per chi non vuole configurare nulla.
- Modelli: [[gemma-4]] e [[gemini-nano-4b]] sul fronte on-device, [[qwen-3-8-27b]] con le sue quantizzazioni GGUF, [[qwen3-8-flash-next]], [[deepseek-v4-flash]] con la sua variante Vision-Exp, e per la memoria ridotta phi-4-mini di Microsoft e i gpt-oss di OpenAI.
- Persone e aziende: [[antirez]], [[apple]], [[xiaomi]], [[nvidia]], [[hugging-face]].

## Notizie rilevanti

- Un modello locale non è un modello di frontiera, e conviene dirlo: serve bene per chat, riassunti, correzione, riscrittura e codice normale, inciampa su matematica e ragionamento dove un modello grande non sbaglierebbe. Il vantaggio non è la potenza, è il posto in cui gira: i dati non escono, la funzione lavora offline e non c'è latenza di rete.
- In produzione il discorso cambia: un modello sul portatile serve una persona alla volta, mentre un server che risponde a un ufficio deve reggere decine di richieste insieme, e per questo si passa da Ollama a vLLM e a GPU da datacenter. Il motivo per cui un'azienda si mette in casa tutto questo è quasi sempre uno, i dati: un modello on-premise semplifica il rispetto del GDPR.
- La scelta pratica per l'utente è tenere entrambe le cose, un modello locale per il grosso del lavoro e la privacy e un abbonamento cloud per quando serve la potenza vera.

## Timeline delle notizie

- **2026-05-23** — Il Flipper One annunciato il 21 maggio è un cyberdeck Linux tascabile con un acceleratore NPU da 6 TOPS in INT8 dichiaratamente pensato per eseguire piccoli LLM e modelli di visione sul dispositivo senza passare dal cloud: SoC Rockchip RK3576 octa-core, 8 GB di RAM, Debian 13, due porte Gigabit Ethernet, Wi-Fi 6E e slot M.2 per modem 5G, SSD o moduli SDR, a meno di 350 dollari nella configurazione base. Le radio storiche del Flipper Zero non sono integrate e diventano accessori, e il progetto è aperto alla community per firmware, driver e applicazioni.
- **2026-06-07** — Lo stack dell'inferenza locale su un PC normale è ormai a tre strati: [[ollama]] come runtime (oltre 173.000 stelle su GitHub al 7 giugno 2026, API compatibile OpenAI su localhost:11434), [[gemma-4]] come modello (famiglia sotto Apache 2.0 rilasciata il 2 aprile 2026: E2B/E4B edge, 12B encoder-free che gira su 16 GB, 26B MoE con 3,8 miliardi di attivi e contesto a 256.000 token, 31B dense) e [[hermes-agent]] come agente, che rifiuta all'avvio i modelli con meno di 64.000 token di contesto. La quantizzazione Q4_K_M taglia l'ingombro di circa il 75% perdendo tra il 2 e il 5% di qualità: 8 GB reggono Gemma 4 E4B, 16 GB il 12B (circa 6,7 GB), 24 GB il 26B MoE e 32 GB il 31B.
- **2026-06-15** — [[amd]] porta al CES 2026 il **Ryzen AI Max+ 395** (nome in codice Strix Halo) e fa girare in locale un modello da 235 miliardi di parametri su un mini PC da un chilo e mezzo, 1.499 dollari; il 10 luglio 2026 arriva il mini PC ufficiale Ryzen AI Halo con 128 GB di LPDDR5x a 3.999,99 dollari, in esclusiva Micro Center negli Stati Uniti.
- **2026-06-19** — La HP ZGX Nano AI Station è una workstation da scrivania di 150 millimetri di lato costruita sul chip [[nvidia]] GB10 Grace Blackwell: carica in memoria un modello da 200 miliardi di parametri e due unità collegate arrivano a 405 miliardi, senza cloud e senza far uscire i dati dalla stanza.
- **2026-07-03** — L'inferenza on-device arriva nel browser: Gemma 4 gira a 255 token al secondo su un Mac M4 grazie a kernel WebGPU scritti da un modello di Anthropic, con i pesi scaricati una volta (circa 2,9 GB) e nessun prompt che lascia il computer. Il valore va letto nel contesto: uno sciame di agenti su una A10G da datacenter aveva raggiunto 508 token al secondo e una implementazione di riferimento su RTX 5090 si ferma intorno ai 125, ma il punto è che un modello da qualche miliardo di parametri oggi gira in una scheda senza server, con un vantaggio diretto in ottica GDPR.

- **2026-07-04** — Il confronto sui siti web 3D chiude sulle stesse tecnologie dell'AI on-device: WebGL è supportato dal 97,5 per cento dei browser, WebGPU è il successore capace di superare i 120 fotogrammi al secondo e Three.js, con 113.502 stelle su GitHub, è lo standard di fatto per usarle senza programmare la pipeline grafica. Sono le stesse basi su cui girano i kernel di Gemma 4 nel browser e Gemini Nano in Chrome, il che fa del browser una piattaforma di rendering 3D e di inferenza insieme.



- **2026-08-29** — Google elenca i primi sette telefoni con Gemini Nano 4, costruito su Gemma 4: i quattro Pixel 11 e i tre pieghevoli Galaxy Z8, con Pixel 10 e Galaxy S26 che restano a Nano 3. Nano 4 Fast (Gemma 4 E2B, circa 2 miliardi di parametri, 4,2 GB) punta alla velocità e Nano 4 Full (Gemma 4 E4B, circa 4 miliardi, 5,9 GB) alla qualità, entrambi con almeno 12 GB di RAM richiesti; i test indipendenti di Android Authority misurano 19,14 token al secondo per Fast e 5,3 per Full, contro i 9,6 di Nano 3, ridimensionando la promessa di quattro volte la velocità.
- **2026-09-01** — antirez mostra DeepSeek V4 Flash con la visione in locale su un Mac M5 Max e annuncia che il supporto Metal, CUDA e ROCm del suo motore DS4 è pronto: Metal per i Mac, CUDA per le schede NVIDIA incluso il DGX Spark e ROCm per le AMD come il Framework Desktop con Strix Halo. I benchmark su M5 Max con 128 GB e quantizzazione a 2 bit danno 790,18 token al secondo in prefill a contesto corto e 39,35 in generazione, che scendono a 398,50 e 27,64 con 65.536 token di contesto; la versione a 2 bit occupa circa 81 GB, quindi la fascia comoda parte da 96 GB, e la visione aggiunge un encoder da 0,9 GiB.
- **2026-09-02** — Guida ai migliori LLM locali del 2026: Qwen3 come tuttofare (licenza Apache 2.0, taglie da 1,7B a 235B), Gemini... il riferimento per il ragionamento è DeepSeek, Gemma 3 è la famiglia meglio ottimizzata per Apple Silicon via MLX, Devstral e Qwen3-Coder per gli agenti di codice, phi-4-mini e gpt-oss per chi ha poca memoria. Lo strumento con cui si lancia il modello conta quasi quanto il modello: Ollama per il terminale, LM Studio per l'interfaccia, llama.cpp per il controllo totale, vLLM per la produzione.

- **2026-09-11** — Il paradosso del modello "leggero": [[deepseek-v4-1-flash]] si chiama Flash ma pesa 748 miliardi di parametri totali (552 di backbone MoE più un n-gram da circa 200), attiva 8 miliardi in ingresso e 16 in uscita e per girare in casa chiede i 512 GB di memoria unificata di una macchina di fascia alta. Chi ce l'ha ottiene un modello multimodale di frontiera che gira offline, senza mandare un byte fuori casa, con la cache scesa a 890 byte per token; per tutti gli altri restano l'API DeepSeek e HuggingChat. Il porting su [[ds4]] è in lavorazione.
- **2026-08-12** — Guida al mercato europeo delle GPU usate per l'inferenza locale: la AMD Instinct MI50 con 32 GB HBM2 e 1.024 GB/s si trova intorno ai 220 euro (circa 7 euro per gigabyte) ma vive di ROCm, la Tesla V100 da 32 GB sotto i 500 euro è il compromesso più equilibrato fra le datacenter, la Tesla P40 illude coi suoi 24 GB perché la GDDR5 a 347 GB/s la rende lenta, e la RTX 3090 da 24 GB (600-900 euro, NVLink per 48 GB) resta la scelta per chi non vuole smanettare; due MI50 o due V100 portano a 64 GB complessivi sotto i 500 euro di schede. [[llama-cpp]] gira su ROCm e su un modello da 70 miliardi quantizzato la community riporta generazioni intorno ai 100 token al secondo.
- **2026-08-15** — Il team Qwen di Alibaba pubblica [[qwen-3-8-27b]] con pesi aperti e licenza Apache 2.0: 27,78 miliardi di parametri densi e multimodali che, con le quantizzazioni Unsloth Dynamic 2.0, scendono fino a 9 GB e girano su una macchina da 16 GB, mentre l'attenzione ibrida (48 layer lineari su 64) riduce la KV cache da 256 KB a 64 KB per token. Le varianti senza censura compaiono nel giro di poche ore tramite abliterazione (JonathanColetti, Blackfrost-AI) e col metodo automatico Heretic (trohrbaugh), mentre il gruppo huihui-ai non ha ancora portato la sua serie oltre Qwen3.6-27B.
- **2026-08-22** — I modelli "senza censura" diventano un filone a sé dell'inferenza locale: il repository di [[heretic]] supera le 28.000 stelle e la community ha già pubblicato oltre 5.000 modelli decensurati, molti dei quali partono da Qwen e arrivano su Hugging Face con i suffissi *abliterated* o *uncensored*. L'abliteration non riaddestra nulla e non si può patchare da remoto, perché il modello modificato vive sul disco di chi lo ha scaricato; su Mac e Windows la via più semplice per usarli resta [[ollama]] o LM Studio.
- **2026-08-25** — [[apple]] apre i preordini del **Mac mini M6** (899 dollari il modello base, 1.699 la versione M5 Pro) dichiarando un'AI fino a quattro volte più veloce del Mac mini con M4; è l'ultimo hardware importante presentato con Tim Cook amministratore delegato, perché dal 1 settembre 2026 il ruolo passa a John Ternus.
- **2026-08-26** — Il confronto misurato di Mickaël Villers tra un Mac Studio M5 Max da 128 GB con un Qwen da 27 miliardi in locale e un abbonamento [[claude]] Max da 200 dollari al mese separa velocità e qualità: il locale vince il cronometro (614 GB/s di banda, circa 58 token al secondo) ma si ferma al 30,9% su Terminal-Bench 2.0 contro il 53,9% di Claude Opus 4.5. Il Mac da 4.800 dollari più 25-35 dollari al mese di elettricità si ripaga in poco più di due anni, mentre il noleggio di un Mac nel cloud a 257 dollari al mese è la peggiore delle tre strade.
- **2026-08-26** — Il 25 agosto Apple apre i preordini del **Mac Studio M5 Ultra**: 5.499 dollari, CPU fino a 36 core, GPU fino a 80 e Neural Engine a 32, ma il dato che pesa per l'inferenza è la banda di memoria unificata a 1,2 TB/s contro gli 819 GB/s dell'M3 Ultra, con configurazioni da 96 a 512 GB e nessuna opzione da 1 TB (consegne dal 22 settembre, il taglio da 512 GB verso fine ottobre). La tesi di [[antirez]] sposta il giudizio dalle specifiche alla domanda pratica — quante sessioni parallele con GLM 5.3 — e indica il batching come il vero discrimine: su Apple Silicon MLX non regge il confronto con [[vllm]], quindi senza un motore che raggruppa le richieste la macchina resta ferma ad aspettare un solo utente. Il tetto a 512 GB è una scelta onesta: GLM 5.3 da 753 miliardi di parametri (8 attivi per token) entra quantizzato a circa 239 GB, mentre [[kimi-k3]] da 2,8 trilioni con 104 miliardi attivi non ci sta con una velocità usabile.
- **2026-09-11** — La guida pratica a [[omnivoice]] mostra come la clonazione vocale in locale sia alla portata di un portatile: pesi da 3,3 GB, Python 3.10-3.13, PyTorch con backend MPS e nessuna scheda NVIDIA, con il trucco di scaricare i pesi via curl e lavorare in modalità offline quando il downloader Xet si impunta.
- **2026-09-13** — Il filone abliterated di [[deepseek-v4-1-flash-abliterated]] mostra dove finisce il confine del "modello senza censura in locale": la build MLX per Apple Silicon pesa 458,7 GB e la versione su 48 shard arriva a 510 GB, quindi servono workstation con 256 o 512 GB di memoria unificata o server multi-GPU, non un portatile. La via realistica per sperimentare l'idea resta un modello piccolo, come nella guida a [[qwen3-8-27b]] che gira su 16 GB con LM Studio.
- **2026-09-13** — Lo streaming da disco, la terza via per l'inferenza locale senza GPU, ha ora un confronto a tre: [[colibri]] tiene in RAM solo la parte densa e legge gli esperti dall'NVMe (GLM-5.2 in 4 bit sono circa 370 GB, a ogni token ne servono una manciata), [[ds4]] sposta sul disco soprattutto la cache KV con quantizzazione a 2 bit ed è il più maturo sui Mac, [[ktransformers]] tiene gli esperti nella RAM di sistema e la parte densa sulla GPU (21-28 token al secondo, il solo uso interattivo serio). Classifica GitHub: 28.756, 22.318 e 19.505 stelle; la regista della gara è il numero di modelli che un motore sa far girare bene, non la trovata tecnica iniziale.
- **2026-09-13** — Guida ai mini PC per l'AI locale: la scelta si riduce a due architetture, la memoria unificata del Ryzen AI Max+ 395 (fino a 96 dei 128 GB assegnabili alla GPU, banda 256 GB/s, GMKtec EVO-X2 sotto i 2.000 dollari e Beelink GTR9 Pro per l'home lab) e la GPU discreta dei FEVM FN80G e FA80G con RTX 5090 mobile da 24 GB, veloce ma con il tetto dei 24-32 miliardi di parametri. Un 70B in Q4_K_M gira intorno ai 14-18 token al secondo sul Ryzen AI Max, mentre i modelli Mixture-of-Experts salgono a 18-70 token al secondo perché leggono pochi miliardi di pesi per token; i 50 TOPS della NPU non generano testo e servono solo ai compiti brevi.
- **2026-09-18** — Il Geekom A9 Max è un mini PC da 0,78 litri e meno di 700 grammi con AMD Ryzen AI 9 HX 370 (dodici core fino a 5,1 GHz, GPU Radeon 890M) e una NPU da circa 80 TOPS totali: la configurazione base parte da 999 euro con 32 GB di DDR5 e 2 TB di SSD. È un altro segnale del fatto che la fascia dei mini PC per l'inferenza locale si sta allargando oltre le piattaforme di punta.
- **2026-06-15** — Autonomous, l'azienda nota per le scrivanie regolabili e le poltrone ergonomiche, pubblica su GitHub la guida autonomous-computer con licenza MIT per costruirsi in casa un computer che fa girare l'IA in locale: tre configurazioni pronte, Home con due schede RTX 5090 e 64 GB di VRAM, Team con quattro RTX PRO 6000 Blackwell e 384 GB e Business con otto schede fino a 256 GB, ognuna con lista materiali e prezzi, file 3D per lo chassis, schema di cablaggio, regolazioni del BIOS e foto di montaggio. Lato software la guida copre sistema operativo, driver NVIDIA e tre motori di inferenza, [[ollama]], [[vllm]] e [[llama-cpp]], fino al collegamento di un agente in locale, e la filosofia è riassunta in "Own your intelligence": un modello affittato nel cloud può essere spento dall'oggi al domani, uno che gira in casa no. Al 15 luglio 2026 il repository è passato da 184 a 810 stelle.
- **2026-08-25** — La regola pratica per capire cosa gira su un computer è che il vincolo è la memoria, non la potenza di calcolo: un modello a 4 bit occupa circa mezzo gigabyte per miliardo di parametri, uno a 8 bit circa un gigabyte e uno a piena precisione circa due, con un 15-20 per cento da aggiungere per la cache del contesto. Un modello da 13 miliardi a 4 bit chiede quindi intorno agli 8 GB di VRAM, e un modello da 7 miliardi a 4 bit circa 4 GB; la quantizzazione è la leva che cambia tutto, perché passare da FP16 a 4 bit taglia la memoria di quattro volte con una perdita quasi impercettibile nell'uso quotidiano.
- **2026-08-25** — Esistono otto strumenti gratuiti che rispondono alla domanda prima di scaricare venti gigabyte di pesi, alcuni leggendo la scheda grafica direttamente dal browser e altri stimando la memoria di qualsiasi modello prima di toccarlo, e il criterio resta quello della scheda da 16 GB che oggi regge un modello da 27 miliardi di parametri, cosa impensabile due anni fa.
- **2026-09-21** — [[linux-ai-os|Linux-AI OS 1.0 Star]] porta l'IA locale fino al sistema operativo, con un desktop Cinnamon e un assistente che esegue [[ollama]] e i modelli Llama sulla macchina, e il caso mostra quanto la verifica delle fonti primarie conti su questi progetti, perché le pagine ufficiali si contraddicono sulla base della distribuzione, sui requisiti e perfino sulla dimensione dell'immagine.
- **2026-09-21** — [[contabo]] lancia la GPU VPS a 999 euro al mese con una RTX PRO 6000 da 96 GB dedicata, quasi 200 euro sotto il GEX131 di Hetzner a 1.197,30 più 599 di setup: il canone fisso per una scheda della stessa classe diventa un'alternativa al computer in casa, con la scheda riservata a un solo cliente e la macchina proposta per inferenza, rendering, calcolo scientifico su un singolo nodo e fine-tuning LoRA, mentre restano fuori i cluster multi-nodo con NVLink.
- **2026-09-25** — La versione senza limiti di Qwen-Image si sblocca su Hugging Face con tre file da scaricare (modello di generazione, encoder di testo e rewriter di prompt) e soglie di memoria dichiarate per fascia: otto gigabyte di VRAM con la quantizzazione UC-Q4_K_M da quattro e sei gigabyte su GPU oppure Heretic Q4 da sei e due gigabyte in RAM, dodici gigabyte per Q6_K o Q8_0, sedici per INT8, ventiquattro e oltre per BF16 a precisione piena. Su Mac funziona ma è lento: un M1 Pro da trentadue gigabyte impiega sedici minuti per quaranta step.

- **2026-09-25** — La guida a LM Studio con Gemma 4 per i documenti aziendali mostra la coppia come via all'inferenza locale: il modello è un file sul disco, il calcolo avviene sul computer e il documento non lascia la macchina, sparisce l'anello del fornitore esterno che vede i dati. Il GDPR resta valido per il resto, ma il vincolo sul fornitore esterno cade alla radice.
- **2026-10-01** — La generazione di immagini in locale su Mac ha una guida passo passo con ComfyUI, che supera le 135.757 stelle su GitHub: i motivi per installarlo invece di usare un servizio cloud sono quattro, la paternità del risultato resta interamente dell'utente, i dati restano sul disco e non transitano su server di terzi, il costo marginale di ogni immagine dopo l'investimento iniziale è zero e il controllo sui parametri dal numero di step al modello di sampling è granulare come nessuna app cloud replica. Il prezzo è la configurazione iniziale da Terminale, con la parte più difficile nel primo avvio di PyTorch con il supporto Metal.
- **2026-10-02** — Ajax è un modello da 9 miliardi di parametri progettato per girare su un singolo PC da casa dentro l'ambiente self-hosted Odysseus, con requisiti dichiarati di almeno 22 GB di VRAM in BF16 che scendono a 11 GB in FP8, più una build quantizzata Q4 per GPU consumer annunciata ma non ancora pubblicata. È il capitolo più recente del filone «liberarsi del cloud», che in questo caso porta con sé un costo che non è tecnico ma contrattuale: le regole d'uso dei modelli di frontiera usati per generare i dati di addestramento.
- **2026-10-02** — Il rincaro dei Raspberry Pi da 2GB incide su uno dei modi più economici di fare AI e servizi in locale: per un server domestico leggero come Home Assistant, un adblocker DNS o un piccolo NAS il taglio da 2GB resta sufficiente, ma chi deve far girare più container Docker, un database o un modello linguistico compresso trova il 2GB stretto e con il divario di prezzo ormai ridotto a pochi euro rispetto all'8GB ha poco senso risparmiare. La Fondazione ha introdotto ad aprile un taglio intermedio da 3GB per il Raspberry Pi 4 a 83,75 dollari, segnale che considera il taglio minimo ormai al limite per molti usi concreti.
- **2026-10-03** — Con l'SDK Linux di Muse Gadgets un Raspberry Pi 5 o un'altra macchina Linux diventa un gadget collegato all'agente di Meta e può eseguire comandi personalizzati, con il sito che cita due usi concreti: l'integrazione con Home Assistant, la piattaforma open source per la domotica, e le operazioni di amministrazione di sistema come controllare un server domestico. Il vantaggio rispetto all'ESP32 è la potenza di calcolo disponibile per i comandi personalizzati, mentre il firmware ESP32 collega schede da pochi euro a Muse.
- **2026-10-04** — Le varianti senza filtri di Qwen3.8-27B dominano il download locale (oltre 2,1 milioni sulla sola GGUF di JonathanColetti) e si installano con Ollama, LM Studio, llama.cpp e MLX; una guida ricorda che togliere il rifiuto dal modello non toglie la legge dal mondo e che un GGUF costruito ad hoc resta un rischio di supply chain.
- **2026-10-05** — Le parole del CEO di [[micron]] indicano che la memoria resterà scarsa e cara fino al 2028, con la HBM per i server AI che sottrae wafer alla DRAM di PC e telefoni: per chi pianifica acquisti o hardware locale significa prezzi più alti e disponibilità più incerta, e gli analisti consigliano di bloccare i prezzi con accordi pluriennali.
- **2026-10-06** — [[openeurollm]] pubblica Qwen3.5-9B-EU-SFT, variante di Qwen3.5-9B ottimizzata per seguire istruzioni e ragionare in oltre 24 lingue europee, addestrata sul supercomputer LUMI con circa 400.000 esempi multilingue: migliora nettamente nei test dichiarati di instruction following, ma la model card la definisce un primo bootstrap SFT, con tool calling e formattazione locale ancora deboli e ulteriori fasi di preference optimization e reinforcement learning previste.
- **2026-10-07** — Al keynote Windows di San Francisco Microsoft annuncia che DeepSeek V4 Flash gira in locale su Windows in 60 GB con i suoi 284 miliardi di parametri quantizzati a 1,6 bit, che llama.cpp entra in Windows ML portando i modelli in formato GGUF nel runtime ufficiale senza conversione a ONNX, che HydraFusion supporta i modelli locali dal 15 ottobre e che NVIDIA lancerà un Nemotron locale da oltre 70 miliardi di parametri sempre il 15 ottobre.

- **2026-10-07** — Sempre nello stesso evento, Copilot per Windows ottiene l'accesso ai file del PC e ai modelli locali dietro un interruttore «Hybrid Intelligence» che governa accesso ai file, azioni e uso dei modelli locali: nella demo rinomina file e sposta i documenti fiscali in una cartella con un modello locale, cercando in Download, Documenti, Desktop, OneDrive e Immagini, e si ferma su «Nothing will be sent until you approve it», mentre Microsoft Execution Containers passa in disponibilità generale e Agent 365 viene collegato a Windows per il governo aziendale degli agenti.



- **2026-10-08** — Tony Fadell spiega il fallimento della prima ondata di gadget AI, dal Rabbit R1 all'assistente Muse di Meta, con l'incapacità di rispondere a bisogni reali e di costruire fiducia, e sostiene che gli assistenti di successo dovranno girare on-device per garantire la privacy: in quest'ottica Apple è ben posizionata per hardware e fiducia dei consumatori anche senza un modello proprietario.
- **2026-10-09** — Lithos Metal, progetto open source, esegue Qwen 3.8-27B a oltre duecento token al secondo per utente su un Apple M5 Max con megakernels e speculative decoding DSpark, compatibile con qualsiasi coding agent in un comando.
- **2026-10-09** — Google presenta Google AI Edge Foresight per Mac Apple Silicon: trascrizione di riunioni, note e ricerca nei file con EmbeddingGemma 2 e Gemma 4 eseguiti in locale, senza mandare l'audio fuori dal computer per dichiarazione di Google; è il primo ingresso di Big G nelle app locali per le riunioni.

- **2026-10-09** — Minisforum presenta il mini PC MS-S1 MAX-P495, con 192 GB di memoria unificata (160 GB assegnabili alla grafica) e AMD Ryzen AI Max+ PRO 495, a 7.399 dollari in preordine (7.799 euro sul negozio europeo): secondo il produttore farebbe girare DeepSeek V4 Flash a circa 12 token al secondo e due unità in cluster eseguirebbero Qwen3.5-397B a circa 16 token al secondo.
- **2026-10-10** — La puntata raccoglie cinque rilasci pensati per girare in locale: l'app Modly per le mesh 3D su GPU locale, Living Weights di TensorFold che porta con sé i pesi aggiornati da una macchina all'altra, il metodo per usare Qwen 3.8-27B gratis da terminale via SSH, l'engine vocale Speech.cpp su ggml e il notebook Unsloth per addestrare decision model su otto GB di VRAM.
- **2026-10-11** — Qualcomm racconta per voce del suo amministratore delegato Cristiano Amon di aver ricevuto da alcune aziende di AI una richiesta precisa: telefoni capaci di far girare in modo continuo un modello da almeno 100 miliardi di parametri entro il 2028, senza nomi dei clienti né promesse su chip o date di prodotto.
- **2026-10-12** - [[intel]] presenta la GPU D-series per l'inferenza, con 160 GB di LPDDR5X sulla scheda Intel e la possibilit\u00e0 di 480 GB sulle versioni dei partner ODM: punta sulla capacit\u00e0 pi\u00f9 che sulla banda (1,5 TB/s contro i 4 TB/s di AMD MI350P) e su un consumo di 350 watt, pensando ai server raffreddati ad aria che devono ospitare modelli aperti senza rifare il data center.

- **2026-10-19** - La guida ai migliori OCR locali del 2026 indica tre modelli sotto il miliardo e mezzo di parametri in testa a OmniDocBench v1.6 - PaddleOCR-VL-1.6, MinerU2.5-Pro e GLM-OCR - e Tesseract con OCRmyPDF per i PC senza scheda video; i modelli da 0,9B girano su RTX 30 o successive e su Apple Silicon via MLX-VLM, ma nessun benchmark misura l'italiano.



- **2026-10-13** — RustGIS 0.1.0 è il primo rilascio di un GIS open source scritto in puro Rust: oltre mille strumenti di geoprocessing che girano su Windows, macOS, Linux e nel browser, con un assistente IA opzionale e dati che restano sulla macchina a meno che l'utente non li invii a un modello IA di sua scelta.
- **2026-10-13** — Il rincaro della memoria ridisegna i confronti: su Amazon.it il Raspberry Pi 5 da 16 GB costa 349 euro, quanto il nuovo Apple TV 4K, dopo che è passato dai 120 dollari di novembre 2025 ai 305 dopo il rincaro di aprile e la sua LPDDR4 è rincarata di sette volte; la causa è la riconversione delle linee DRAM sui moduli per i server di addestramento dell'AI, che richiederà anni.
- **2026-10-13** — Una guida del 13 ottobre passa in rassegna i generatori di immagini gratuiti distinguendo locale e online: in locale Draw Things per i dispositivi Apple con edizione Free, ComfyUI a 137.205 stelle con la v0.39.0 del 5 ottobre, InvokeAI (28.595 stelle, Apache-2.0), Krita AI Diffusion, Fooocus ancora alla v2.5.5 del 2024 in sola manutenzione e DiffusionBee fermo dal 2024; online Leonardo AI con 150 token al giorno, Playground con 3 crediti al mese e Mage.space con 300 gemme alla registrazione. In locale niente coda né tetto di immagini e nessun prompt che esce dalla macchina, ma i modelli vanno scaricati a parte.
- **2026-10-14** — Qwen 3.8 27B gira a circa 20 token al secondo sulla GPU di una PlayStation 5 con jailbreak grazie a PS5LM Plus, che trasforma il port di llama.cpp in un'app nativa con 11,44 GiB di memoria; il modello ci sta solo quantizzato a 2 bit e l'elaborazione dell'input va a 35-50 token al secondo, quindi un prompt da 20.000 token di un agente di programmazione richiede minuti prima della prima parola.

- **2026-10-15** — NVIDIA presenta Nemotron 3.5 Bolt 74B A9B, MoE da 74 miliardi di parametri e 9 attivi compresso a 2 bit in 24 GB per gli agenti locali sui portatili RTX Spark, con cinque runtime supportati al lancio (llama.cpp, vLLM, Ollama, Unsloth e LM Studio) e due agenti, Hermes e OpenClaw.



- **2026-10-15** — AMD propone una macchina da 1.599 dollari con Ryzen AI Max+ e 128 gigabyte di memoria unificata tra CPU e GPU, capace di far girare in locale modelli fino a 235 miliardi di parametri su un singolo dispositivo.
- **2026-10-16** — Un confronto tra Mac Studio M5 Max e [[nvidia]] [[dgx-spark]] mette la banda di memoria al centro della scelta per l'AI locale: il Mac di [[apple]] dichiara fino a 614 GB/s contro i 273 GB/s del DGX Spark, un vantaggio teorico di 2,25 volte sui modelli densi (un 70B a 4 bit, circa 40 GB, resta intorno ai 15 token al secondo contro i 7). Il DGX Spark (chip GB10 Grace Blackwell, 128 GB unificati, ConnectX-7 a 200 Gbps, fino a quattro unità in cluster) recupera su modelli MoE, richieste in parallelo (circa 2.451 token al secondo aggregati con 256 richieste) e prefill, e resta l'unica via per CUDA e fine-tuning; il Mac Studio M5 Max, aggiornato il 25 agosto 2026 con consegne dal 22 settembre, parte da 2.999 euro su Amazon.it con soli 36 GB, insufficienti per un 70B a 4 bit. I prezzi del DGX Spark da 128 GB vanno da 5.999,99 euro (derivato ASUS GX10) a 8.350 euro, con un rincaro statunitense a circa 6.950 dollari per il costo della memoria.
- **2026-10-18** — Violoop è un box da 399 dollari in prevendita su Kickstarter che si presenta al computer come una tastiera USB e legge lo schermo, con un modello locale Qwen 8B quantizzato a 4 bit su un processore RK3576 con acceleratore da 26 TOPS; per i compiti pesanti si collega la propria chiave API di Claude, OpenAI o Gemini. Le funzioni locali non richiedono abbonamento, e il video dello schermo resta nel box mentre ai cloud arriva un riassunto testuale già filtrato.
- **2026-10-22** — [[recursive-flint]] porta il coding agentico su hardware locale: mixture-of-experts da 40 miliardi di parametri con 2,5 attivi per token, oltre 150 token al secondo su un RTX Spark da 64 GB e nessun dato inviato a un server remoto.
- **2026-10-25** — Con 128 GB di memoria unificata un laptop sottile carica modelli che su una scheda dedicata da 16 o 24 GB di memoria video non entrerebbero, ed è la ragione per cui RTX Spark ha senso per chi sviluppa agenti o lavora con modelli da 70 miliardi di parametri; per giocare, un desktop x86 con una GeForce costa meno e non ha dubbi sull'anti-cheat. Le prime prove sull'autonomia parlano di 55 minuti a giocare, con modello e gioco non precisati, e i giochi x86 passano dall'emulatore Prism di Windows 11, dove anti-cheat e DRM restano il terreno da verificare.
- **2026-10-25** — GPU-Unlock, modulo del kernel Linux per le GeForce RTX serie 30, sblocca le istruzioni FP16 e BF16 senza toccare il driver: i report del progetto danno dal 14 al 36 per cento in più sul prefill dei modelli locali, mentre il decode resta identico perché dipende dalla banda di memoria e gli output restano gli stessi bit per bit. Wccftech riporta intanto un rincaro delle 3090 usate, da circa 1.000 a oltre 2.000 dollari, senza confronto con uno storico dei prezzi.
- **2026-10-27** — [[lenovo]] mostra in anteprima l'AI Host P7, una macchina da circa 300 grammi che dichiara modelli fino a 125 miliardi di parametri in locale con contesto da 256K, chip Houmo M50 e CIX P1 e un software che espone i modelli locali come API a strumenti di programmazione e agenti. Prezzo e data non sono stati comunicati, e il confronto con la banda di memoria di un modello denso da 122 miliardi a 4 bit mette in dubbio i 50 token al secondo dichiarati a maggio.
- **2026-10-27** — Con i fork turing-unlock e gpu-unlock-ada lo sblocco dei tensor core arriva anche alle GeForce RTX 20 e 40, dopo il modulo per le RTX 30: il guadagno riguarda il prefill, cresciuto del 14-36 per cento sulle Ampere, mentre la generazione dei token resta uguale perché dipende dalla banda di memoria, e su un MoE quantizzato con una 4090 da 48 GB non si è visto alcun miglioramento. Restano fuori le RTX 50, che l'autore dice fuori portata per questo metodo.
- **2026-10-28** — [[giotto-ai]] presenta Giotto Solo come «il modello più intelligente che gira su una sola GPU», pensato per workstation e server in sede dove i dati non escono: si installa tramite integratori certificati con licenza annuale o pluriennale calcolata sul numero e sul tipo di GPU, e i pesi non sono pubblici. L'azienda non ha comunicato parametri né finestra di contesto e descrive l'architettura come una rete coordinata di modelli più piccoli e specializzati, non un unico modello gigante.
- **2026-10-29** — Per chi compra hardware da AI locale il Black Friday del 27 novembre arriva in un mercato che sale: TrendForce prevede per il quarto trimestre rincari del 10-15 per cento sui contratti DRAM e del 15-20 per cento sulla NAND, quindi uno sconto su un SSD o su un kit DDR5 può solo riportare il prezzo a quello di settembre. Il criterio pratico resta la memoria e non il chip — un Mac da 24 GB, una scheda con 16 GB di VRAM o un mini PC con 128 GB condivisi decidono quale modello si carica — mentre sui Mac M6 usciti il 6 novembre i tagli saranno rari perché il confronto dei 30 giorni si regge su poco.
- **2026-10-29** — La guida ai requisiti di memoria per un LLM locale dà la formula pratica: parametri per bit per peso diviso otto, più la memoria del contesto (la KV cache), quindi un modello da 8 miliardi di parametri pesa 16 GB in FP16 e scende a 4,9 GB in Q4_K_M, la quantizzazione che Ollama scarica di default. Ridurre la precisione dei pesi fino a 4 bit costa una perdita di qualità misurabile ma piccola, che sopra i 4 bit diventa evidente.

- **2026-10-29** — Per trascrivere e generare voce in italiano senza mandare un secondo di audio nel cloud bastano due modelli gratuiti: [[whisper|Whisper]] large-v3-turbo, o Parakeet v3 di NVIDIA, per la trascrizione e [[kokoro|Kokoro]] o Chatterbox per la sintesi vocale. Girano su un Mac con 16 GB di memoria o su un PC con una scheda video da 8 GB.

- **2026-10-30** — [[openai|Sam Altman]] ha definito «piuttosto terribile» che ogni utente tenga nel proprio PC una fetta della scarsa DRAM mondiale, usata a suo dire il 5 per cento del tempo, e ne ha concluso che con l'offerta così ridotta conviene la massima utilizzazione nel cloud: è la posizione contro l'inferenza locale espressa nella puntata del podcast Cheeky Pint di Stripe uscita il 29 ottobre.














































































## Collegamenti

- [[violoop]]
- [[amd]]
- [[anthropic]]
- [[apple]]
- [[claude]]
- [[cybersicurezza]]
- [[deepseek-v4-flash]]
- [[deepseek-v4-1-flash-abliterated]]
- [[ds4]]
- [[ktransformers]]
- [[gemini-intelligence]]
- [[gemini-nano-4b]]
- [[gemma-4]]
- [[llama-cpp]]
- [[ollama]]
- [[open-source]]
- [[qwen-3-8-27b]]
- [[qwen3-8-flash-next]]
- [[strata]]
- [[vllm]]
- [[xiaomi]]
- [[index]]
- [[ps5lm]]
