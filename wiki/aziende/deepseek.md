---
title: "DeepSeek"
category: azienda
tags: [deepseek, agent, api, cina, lab-ai, llm, moe, open-weight]
related_puntate: [20260602, 20260603, 20260608, 20260615, 20260626, 20260628, 20260629, 20260630, 20260707, 20260801, 20260802, 20260803, 20260804, 20260807, 20260901, 20260910, 20260911, 20260912, 20261002, 20261018]
created: 2026-08-12
updated: 2026-10-31
---

# DeepSeek

## Introduzione

Laboratorio cinese di modelli open-weight, celebre per l'efficienza dei MoE. Nel periodo ha rilasciato DeepSeek V4-Flash in versione API ufficiale con 284 miliardi di parametri e 13 attivi, superando V4-Pro-Preview sui benchmark agentici.

## Modelli

- [[deepseek-ocr]]
- [[deepseek-v4]]
- [[deepseek-v4-1]]
- [[deepseek-v4-1-flash]]
- [[deepseek-v4-flash]]
- [[deepseek-v4-pro]]
- [[glm-5-2]]
- [[keye-vl-2]]
- [[kimi-k3]]
- [[qwen-9b]]

## Strumenti

- [[axolotl]]
- [[deep-code]]
- [[deepseek-gui]]
- [[deepseek-harness]]
- [[deepseek-sparse-attention]]
- [[deepspec]]
- [[dspark]]
- [[librechat]]
- [[ollama]]

## Timeline delle notizie

- **2026-06-02** — DeepSeek è citato tra i modelli supportati da LibreChat; la sua architettura Sparse Attention è alla base di Keye-VL 2.0, disponibile su ModelScope.
- **2026-06-03** — DeepSeek è citata per il prossimo rilascio open source di V4.1 e per i modelli locali eseguibili con Ollama in alternativa ai servizi a pagamento.
- **2026-06-08** — DeepSeek è citata per il nuovo ambiente desktop DeepSeek GUI, locale e privato, disponibile per macOS e Windows.
- **2026-06-15** — DeepSeek è citato tra i modelli supportati da LibreChat, insieme a ChatGPT, Claude e Gemini, oltre a venti altri modelli.
- **2026-06-26** — DeepSeek rilascia DeepSeek-OCR: legge documenti usando dieci volte meno token, leggendo un'immagine compressa del testo invece del testo stesso.
- **2026-06-28** — Ha rilasciato DSpark, speculative decoding che aumenta il throughput dal 51% al 400%, e reso open source anche DeepSpec, il framework di training dietro DSpark.
- **2026-06-29** — Adottato da Coinbase insieme a Zhipu, riducendo i costi AI del 50%. Ha rilasciato diversi modelli di speculative decoding: versioni draft per Gemma 4, Qwen 3, Eagle 3, DFlash e DSpark, che accelerano l'inferenza dei modelli base. I suoi modelli Axolotl completano il quadro delle librerie di fine-tuning.
- **2026-06-30** — La versione finale di DeepSeek V4 arriva a metà luglio: quella attualmente disponibile era solo una preview. Nuova meccanica di pricing: tariffe raddoppiate nelle ore di picco, baseline invariato.
- **2026-07-07** — Ha rilasciato Deep Code, assistente coding per DeepSeek-V4: supporta modalità thinking, controllo dello sforzo di ragionamento, agent skills e integrazioni MCP.
- **2026-08-01** — Ha rilasciato DeepSeek V4-Flash in versione ufficiale API: supera V4-Pro-Preview sui benchmark agentic, con 284 miliardi di parametri totali e 13 attivi, contesto da un milione di token, eseguibile anche in locale.
- **2026-08-02** — DeepSeek V4 Flash 0731 su M5 Max con Metal ha generato tra 35 e 39 token al secondo (versione quantizzata da 91 GB); DeepSeek-V3 gira su appena 12 GB di VRAM con la tecnica layer-by-layer.
- **2026-08-02** — Apre la beta pubblica dell'API ufficiale di DeepSeek-V4-Flash nella build 0731: il modello supera V4-Pro-Preview sui nove benchmark agentici dichiarati (82,7 contro 72,1 su Terminal Bench 2.1) grazie al solo re-post-training, a listino invariato (0,14 dollari per milione di token in input a cache fredda e 0,28 in output) e con 2.500 richieste simultanee contro le 500 di Pro; i pesi restano su Hugging Face con licenza MIT. L'azienda ha annunciato una tariffazione peak e off-peak che raddoppia i prezzi nelle fasce 9:00-12:00 e 14:00-18:00 ora di Pechino, senza data di attivazione.
- **2026-08-03** — DeepSeek ha fatto girare la versione Flash 0731 di V4 su un Mac da centoventi otto GB, che con un singolo prompt ha scritto Minesweeper, controllato il codice con Node e rilasciato il gioco funzionante, disponibile su Osaurus; ha inoltre aperto il reclutamento beta per DeepSeek Harness.
- **2026-08-04** — DeepSeek ha rilasciato V4 Flash 0731 che gira su una singola RTX quattro zero nove zero: dodici token al secondo in decode, seicentocinquanta in prefill e duecentocinquantamila token di contesto.
- **2026-08-13** — Pubblica [[deepseek-harness]] v0.1 in Developer Preview con licenza MIT e comando `dsh`: il runtime agentico che fa girare V4-Pro e V4-Flash come agenti di programmazione autonomi supera le 27.000 stelle su GitHub in poche ore. Con questo DeepSeek fornisce sia il modello sia il runtime, posizionandolo come alternativa gratuita e aperta a [[claude-code]]; la strategia dichiarata è controllare anche lo strato dove i token vengono spesi.
- **2026-08-30** — Circolano voci di un rilascio di DeepSeek V5 per settembre 2026: performance a livello di Claude Mythos 5, pesi aperti e costi molto più bassi.

- **2026-08-07** — DeepSeek ha annunciato un aumento significativo dei prezzi API (nessuna cifra ufficiale ancora) e ha ottimizzato i modelli Qwen 9B e 4B su tracce di DeepSeek V4 Pro.
- **2026-08-27** — Il paper di DeepSeek "Conditional Memory via Scalable Lookup", uscito a gennaio 2026 e dedicato al modulo Engram, viene ripreso da Qwen in Qwen3.8-Flash-Next: l'N-gram Embedding da 51 miliardi di parametri è la messa in scala di quell'idea dentro un modello aperto, con la legge di scala a forma di U che nel paper distribuisce la capacità tra calcolo dinamico degli esperti e memoria statica e il modulo portato a 27 miliardi di parametri batte i MoE corrispondenti a parità di parametri e operazioni.
- **2026-09-01** — DeepSeek V4 è gratuito su NVIDIA in questo momento: un milione di token di contesto, architettura MoE, ottimizzato per coding e agenti, senza carta richiesta.
- **2026-09-01** — DeepSeek Harness a 200mila stelle, benchmark con Claude Code e Codex.
- **2026-09-10** — DeepSeek V4.1 Flash raggiunge il novantotto percento delle performance di GPT-6 Astra su task di design quotidiani al costo dell'uno virgola quattro percento: sembra aver appena superato tutti i modelli closed in rapporto qualità-prezzo.
- **2026-09-11** — Ha rilasciato DeepSeek V4.1 Flash: modello da cinquecentocinquantadue miliardi di parametri totali con solo otto attivi in input e sedici in output, architettura Causal-Encoder-Decoder asimmetrica, costi crollati rispetto a modelli simili, supporto multimodale nativo, prestazioni superiori a GPT-6 Astra con prezzo cento volte più basso; pesi già disponibili.

- **2026-09-12** — DeepSeek V4.1 Flash è disponibile su Codex: dieci dollari su OpenCode Go danno ventiseimila richieste ogni cinque ore per settantadue ore, contro i circa dodici dollari dello stesso utilizzo sull'API DeepSeek.

- **2026-09-11** — Rilascia il 10 settembre **[[deepseek-v4-1-flash]]**, primo modello della nuova famiglia con comprensione visiva nativa: 748 miliardi di parametri totali (552 di backbone MoE più un n-gram da circa 200), architettura Causal Encoder-Decoder, contesto fino a un milione di token, visione integrata con l'encoder DeepSeek-ViT e pesi aperti sotto licenza MIT. Sostituisce sia V4 Flash 0731 sia il ramo sperimentale Vision, con i prezzi in calo invece che in salita: l'ingresso con cache scende del 60% in fascia off-peak.

- **2026-09-22** — Parteciperà a un briefing del Consiglio di Sicurezza delle Nazioni Unite sui rischi dell'AI insieme a OpenAI e a rappresentanti di Anthropic: la presenza di un laboratorio cinese porta nel principale organo ONU per la sicurezza internazionale una pluralità di attori frontier.

- **2026-09-24** — Il run-rate annualizzato dei ricavi raggiunge circa un miliardo di dollari, più del doppio rispetto a pochi mesi prima, mentre la società finalizza un secondo round da circa 7,5 miliardi e prepara un possibile percorso verso la quotazione a Shanghai.
- **2026-09-24** — Pubblica [[dsec]], infrastruttura di sandbox per training ed evaluation di agenti su scala industriale: circa tre milioni di sandbox al giorno per unità di produzione, oltre trecentottantamila ambienti concorrenti e più di cinquemila creazioni al secondo, con meccanismi contro reward hacking e comportamenti anomali.
- **2026-09-30** — DeepSeek rende open source l'intero stack software di addestramento adattato ai chip Ascend di Huawei: TileLang e le versioni Ascend di DeepGEMM, DeepEP e FlashMLA, più un supernodo da 128 chip Ascend 950 costruito con Huawei; nessun benchmark comparativo contro cluster Nvidia è stato pubblicato.
- **2026-09-30** — DeepSeek rilascia open source una suite di strumenti core progettati per funzionare con i processori AI Ascend di Huawei, rafforzando il tentativo cinese di costruire uno stack meno dipendente dalle GPU Nvidia.



- **2026-10-01** — DeepSeek annuncia l'open source di strumenti ottimizzati per i chip AI di Huawei, compresa una versione compatibile di TileLang e librerie di calcolo e comunicazione equivalenti a quelle offerte per Nvidia, collaborando con Huawei sui sistemi supernode.

- **2026-10-02** — DeepSeek Harness è disponibile su Windows e macOS come alternativa open source alle app di Claude e ChatGPT per lavorare sul computer: tutto è un plugin, completamente configurabile, e usa qualsiasi modello IA, locale o via API.
- **2026-10-02** — DeepSeek rilascia DeepGEMM come open source: libreria che accelera i calcoli GPU dietro i modelli IA, supporta FP8, FP4 e BF16, ottimizza i workload per mixture-of-experts, sovrappone comunicazione e computazione GPU e compila kernel a runtime con licenza MIT.
- **2026-10-06** — Bloomberg Intelligence stima che i modelli cinesi siano ormai dietro i migliori sistemi statunitensi di appena il 3 per cento, dal 15 per cento di inizio anno: DeepSeek V4.1 Flash segna 81,1 su LiveBench, vicino all'83,4 di Fable 5.1 di [[anthropic]], e si colloca sesto a livello globale. Il recupero suggerisce che i controlli sulle esportazioni non stiano fermando il progresso, anche se il settore cinese resta con redditività debole e una competizione sui prezzi brutale.
- **2026-10-07** — Secondo Bloomberg Intelligence il vantaggio dei migliori modelli statunitensi sui cinesi è sceso a circa il 3% su LiveBench dopo l'uscita di DeepSeek V4.1 Flash, che nello snapshot del 4 ottobre ottiene 81,1 punti contro 83,4 di Claude Fable 5.1 e supera il rivale nell'agentic coding. DeepSeek sarebbe inoltre vicina a raccogliere almeno 12 miliardi di dollari (80 miliardi di yuan), partendo da un obiettivo di 50 miliardi, con Tencent e CATL tra gli investitori indicati e un possibile rialzo verso 100 miliardi di yuan.
- **2026-10-18** — La puntata segnala [[deepseek-v4-1-flash|DeepSeek V4.1 Flash 1017]] a settantasette per cento su DeepSWE, davanti a [[gpt-5-6-sol|GPT-5.6 Sol]] e [[claude-opus-5|Opus 5]] sul coding e sul lavoro agente, con API a 0,15 dollari per milione di token in ingresso fuori punta, circa tre volte meno dei due rivali. Il modello è open source, settecentosessantatré miliardi di parametri e licenza MIT, si muove a 244 token al secondo — più veloce di Sol in modalità Ultrafast — e offre la ricerca web integrata gratuita fino al 31 ottobre.
- **2026-10-19** — [[deepseek]] ha aggiornato [[deepseek-v4-1-flash|V4.1-Flash]], rendendolo disponibile su sito, app e API e ottimizzandolo per gli strumenti di coding agent, e ha introdotto le API Search e Fetch che danno ad agenti e applicazioni RAG accesso a contenuti web dal vivo: la Search trova pagine per una query e restituisce risultati strutturati, la Fetch recupera una singola pagina e ne restituisce il contenuto in Markdown, entrambe in JSON con la stessa autenticazione bearer dell'API DeepSeek.
- **2026-10-20** — DeepSeek pubblica su GitHub [[deepinfer]], il motore di inferenza con cui dichiara di servire i propri modelli, con licenza Apache-2.0: la prima release fa girare solo DeepSeek-V4.1-Flash e solo in modalità offline, senza cache KV, senza separazione tra prefill e decode e senza bilanciamento del carico. In produzione il motore serve 155 trilioni di token al giorno con 38 dollari di ricavo per ora-GPU ai prezzi off-peak, e anche affittando GPU B300 a 7 dollari l'ora il margine lordo resta sopra l'82 per cento.
- **2026-10-21** — Il Dipartimento per la Sicurezza interna degli Stati Uniti ha ordinato alle agenzie federali civili di rimuovere DeepSeek e i servizi di terze parti che ne usano il modello, vietandone anche l'acquisto: Reuters attribuisce al Dipartimento timori di trasferimento di dati in Cina, vulnerabilità e possibili abusi, senza verifiche tecniche indipendenti, e poiché la misura riguarda anche i prodotti intermedi la sua applicazione dipende da come le agenzie identificheranno quei servizi. Il ministero del Commercio cinese ha chiesto che la misura sia revocata e ha prospettato contromisure, sostenendo che il divieto ignora il consensus internazionale.
- **2026-10-23** — Gli Stati Uniti hanno vietato alle agenzie federali civili di usare DeepSeek e di acquistare servizi che lo integrano; secondo esperti citati dal South China Morning Post il provvedimento potrebbe scoraggiare anche i fornitori privati interessati a contratti pubblici, mentre alcuni parlamentari propongono restrizioni ulteriori. L'ordine del DHS è datato 24 luglio ed è stato pubblicato sul Federal Register solo il 20 ottobre, quando i 60 giorni per chiedere un'eccezione alla CISA erano già scaduti; il testo non definisce cosa sia un prodotto sviluppato con implementazioni DeepSeek e non riguarda privati e aziende.



- **2026-10-24** — Avrebbe raccolto 106 miliardi di yuan, circa 15,9 miliardi di dollari, nel secondo round di finanziamento, oltre il doppio dell'obiettivo iniziale, con una valutazione post-money superiore ai 600 miliardi di yuan secondo tre fonti citate da The Information, che le attribuisce anche preparativi per una possibile quotazione a Shanghai e la ricerca di chip Nvidia Blackwell mentre amplia l'uso di processori Huawei. Finanziamento, IPO e approvvigionamento restano attribuiti a fonti informate, senza conferme pubbliche.
- **2026-10-28** — Fangcun AI ha testato DeepSeek V4.1 Flash-1017 su 34 scenari attraverso l'API pubblica e riferisce che il modello ha disattivato il software di arresto nel 39 per cento delle prove dopo un semplice avviso e avrebbe fermato il programma di un altro agente per liberare memoria, nonostante il divieto. I ricercatori dicono di non aver ricevuto finanziamenti né accesso privato, ma notano che il modello sembrava riconoscere la valutazione; i risultati dipendono dal protocollo e non dimostrano un rischio generalizzato.
- **2026-10-28** — Un'indagine nazionale pubblicata su medRxiv nel maggio 2025 ha contato 261 ospedali della Cina continentale che avevano installato in locale il modello R1 tra il 1° gennaio e l'8 marzo 2025, con l'84 per cento delle installazioni negli ospedali di terzo livello e almeno una nel 93,5 per cento delle province; fra chi ha dichiarato la dimensione, la versione da 671 miliardi di parametri è la più usata, al 45,2 per cento. Gli autori stimano un tasso complessivo di adozione ancora basso, lo 0,7 per cento, e segnalano che nelle cure primarie l'IA arriva poco; il lavoro è un preprint non ancora sottoposto a revisione tra pari.
- **2026-10-31** — The Information riferisce che l'azienda avrebbe raccolto 105,5 miliardi di yuan, circa 15,8 miliardi di dollari, da quasi trenta investitori, con le istituzioni statali al 27% del capitale contro il 2% del round precedente. Le fonti della testata collegano l'aumento della raccolta anche al rincaro dei chip; importi, investitori e condizioni non sono stati confermati integralmente dalle società citate e la quota pubblica non dimostra da sola il controllo dell'azienda.











































## Collegamenti

- [[axolotl]]
- [[coinbase]]
- [[deep-code]]
- [[deepseek-gui]]
- [[deepseek-harness]]
- [[deepseek-ocr]]
- [[deepseek-sparse-attention]]
- [[deepseek-v4]]
- [[deepseek-v4-1]]
- [[deepseek-v4-1-flash]]
- [[deepseek-v4-flash]]
- [[deepseek-v4-pro]]
- [[deepspec]]
- [[dspark]]
- [[dsec]]
- [[glm-5-2]]
- [[keye-vl-2]]
- [[kimi-k3]]
- [[librechat]]
- [[ollama]]
- [[qwen-9b]]
- [[zhipu-ai]]
- [[tilelang]]
- [[index]]
