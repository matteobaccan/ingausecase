---
title: "Kimi K3"
category: modello
tags: [agent, cina, coding, frontier, llm, moonshot, multimodale, open-weight, reasoning, vibe-coding]
related_puntate: [20260603, 20260715, 20260717, 20260718, 20260719, 20260720, 20260721, 20260722, 20260723, 20260725, 20260726, 20260728, 20260729, 20260730, 20260802, 20260803, 20260807, 20260923]
created: 2026-08-12
updated: 2026-10-20
---

# Kimi K3

## Introduzione

Modello LLM open-weight di Moonshot AI da 2,8 trilioni di parametri con un milione di token di contesto, basato sull'architettura KDA (Kimi Delta Attention). Modello di punta del periodo: ha battuto Claude Opus 5 in task di coding-gioco, trovato zero-day in Redis e dimostrato di girare in locale su hardware consumer con compressione a un bit.

## Capacità e performance

- Kimi K3 è citato tra i competitor di DeepSeek V4.1 nel mercato dei modelli.
- Kimi K3 dovrebbe arrivare a breve: K2.6 era già forte su agenti e visione nativa, K3 arriva con architettura nuova, supporto per sciami di agenti paralleli e workflow a lungo termine, sfidando GLM-5.2 e GPT-5.6.
- Kimi K3 ha 2,8 trilioni di parametri e un milione di token di contesto, nativo multimodale: oggi è primo nella Frontend Code Arena con 1679 punti superando Claude Fable 5, con il settantasei per cento di vittorie dirette e sei domini su sette vinti; pesi aperti dal ventisette luglio, prezzi a tre dollari per milione di input e quindici per milione di output, cinque volte K2.7.

## Azienda di riferimento

- [[moonshot-ai]]
- [[thinking-machines]]
- [[unity]]

## Strumenti correlati

- [[airllm]]
- [[blender-mcp]]
- [[claude-code]]
- [[claude-code-router]]
- [[colibri]]
- [[ds4]]
- [[hermes-agent]]
- [[kimi-code-cli]]
- [[vllm]]

## Timeline delle notizie

- **2026-06-03** — Kimi K3 è citato tra i competitor di DeepSeek V4.1 nel mercato dei modelli.
- **2026-07-12** — Con lo streaming degli esperti da disco la stessa strada di [[colibri]] arriva ai modelli da trilioni di parametri: Kimi K3 è stato eseguito su una singola CPU con 8,24 GB di RAM, leggendo gli esperti dal NVMe a ogni token.
- **2026-07-15** — Kimi K3 dovrebbe arrivare a breve: K2.6 era già forte su agenti e visione nativa, K3 arriva con architettura nuova, supporto per sciami di agenti paralleli e workflow a lungo termine, sfidando GLM-5.2 e GPT-5.6.
- **2026-07-17** — Kimi K3 ha 2,8 trilioni di parametri e un milione di token di contesto, nativo multimodale: oggi è primo nella Frontend Code Arena con 1679 punti superando Claude Fable 5, con il settantasei per cento di vittorie dirette e sei domini su sette vinti; pesi aperti dal ventisette luglio, prezzi a tre dollari per milione di input e quindici per milione di output, cinque volte K2.7.
- **2026-07-18** — Kimi K3 ha 2,8 trilioni di parametri e supera Claude Opus 4.8 su diversi benchmark di programmazione e ragionamento: costa circa la metà di Opus 4.8 sull'API e verrà rilasciato open source il 27 luglio.
- **2026-07-19** — Kimi K3 ha ricostruito una dashboard 3D interattiva da un solo prompt e un'immagine di riferimento, con texture e illuminazione identiche all'originale, a prezzi Sonnet; nel test del team di Cline ha risolto un bug reale in dodici minuti contro i tre virgola cinque di Fable ma costa 2,3 volte meno (0,92 dollari contro 2,13); un YouTuber che spendeva mille dollari al giorno in token ha completato lo stesso lavoro per sessantatré dollari con centoventidue task autonomi e audit di sicurezza con venticinque agenti, definendolo classe frontier.
- **2026-07-20** — Kimi K3 ha fatto parlare di sé: un utente ha vibe-codato un clone completo di FIFA in tre ore con texture, kit, squadre e loghi tutti generati; un altro ha rifatto Limbo con tremila righe di codice a dodici centesimi, dieci volte più economico di Fable 5.
- **2026-07-21** — Kimi K3 ha rifatto in tre ore un visualizzatore 3D per posti negli stadi che Fable 5 aveva fatto in un'ora: ha eseguito test end-to-end, validato desktop, tablet e mobile e prodotto componenti React modulari, risultando tre volte più economico; qualcuno ha cablato la subscription Kimi in Codex via OAuth, facendo comparire K3 nel selettore modelli accanto a Sol 5.6; pesi aperti il ventisette luglio.
- **2026-07-22** — Moonshot lo rilascia il 27 luglio con pesi completi: 2,8 trilioni di parametri, un milione di token di contesto, licenza MIT modificata.
- **2026-07-23** — Kimi ha introdotto Attention Residuals nel modello K3: ogni layer decide quanto attingere dai layer precedenti in modo input-dependent, niente più somma fissa; 2,8 trilioni di parametri e decodifica 6,3 volte più veloce su contesti da un milione di token, pesi in arrivo il 27 luglio.
- **2026-07-25** — Rilasciato con Delta Attention: una matrice fissa sostituisce l'intera cache KV, ogni token legge prima di scrivere, passando da quadratico a lineare (75% lineare, 25% softmax); ha trovato vulnerabilità zero-day in Redis e costruito exploit RCE funzionanti che abusano RESTORE su più release: sette aggiornamenti di sicurezza rilasciati, nessuna segnalazione di exploitation in the wild.
- **2026-07-26** — Ha battuto Claude Opus 5 nella costruzione di un clone di Fall Guys: nove minuti e 4,40 dollari, con fisica funzionante, contro 17 minuti e 13 dollari di Claude Opus 5; qualcuno lo ha collegato a Blender via MCP, costruendo e modificando scene descrivendole a voce.
- **2026-07-28** — È arrivato come modello open source con 2,8 trilioni di parametri e un milione di token di contesto, già disponibile su LM Studio e Hugging Face.
- **2026-07-28** — Il technical report di 47 pagine pubblicato il 27 luglio insieme ai pesi su Hugging Face corregge la stima della community: i parametri attivi sono 104 miliardi su 2,8 trilioni totali (rapporto del 3,7%, non del 2%), non i circa 50 ipotizzati dai forum. La scheda tecnica elenca 93 livelli di cui uno denso, 69 livelli di Kimi Delta Attention più 24 di Gated MLA, 896 esperti instradati con 16 attivi per token più due condivisi, encoder visivo MoonViT-V2 da 401 milioni di parametri, vocabolario da 160.000 token e contesto da 1.048.576; la quantizzazione MXFP4 sui pesi e MXFP8 sulle attivazioni non è applicata dopo ma entra nel training dal fine-tuning supervisionato, quindi i pesi occupano circa 1,4 terabyte contro i 5,6 dell'FP16. Insieme al modello escono sotto licenza MIT tre pezzi dello stack interno: FlashKDA, i kernel di attenzione (da 1,72 a 2,22 volte più veloci di flash-linear-attention in prefill su H20, 806 stelle), MoonEP per il parallelismo tra esperti (716) e AgentENV, la piattaforma di sandbox agentica sviluppata con KVCache.ai (1.295).
- **2026-07-28** — Il report ammette il distacco dai modelli chiusi, cosa rara in un lancio: le prestazioni complessive restano dietro a Claude Fable 5 e GPT-5.6 Sol, con il primo posto rivendicato tra tutti gli altri sistemi valutati. Kimi K3 vince dove conta la resistenza sulla distanza e l'uso di strumenti esterni (SWE-Marathon 42,0 contro 35,0 di Fable 5, BrowseComp 91,2, MCPMark-Verified 94,5) e perde dove serve capire a fondo una base di codice esistente (FrontierSWE 81,2 contro 86,6, DeepSWE 67,5 contro 70,0). Nei casi di studio il modello progetta in una sessione autonoma di 48 ore un prototipo di chip di inferenza entro 4 millimetri quadrati di area e 100 MHz, con 1,46 milioni di celle standard e il codice RTL pubblicato nel repository nano-kpu.
- **2026-07-28** — La licenza non è MIT né Apache ma un testo su misura sul modello di quella di K2: uso interno libero senza condizioni, accordo separato con Moonshot per chi rivende inferenza o fine-tuning superando i 20 milioni di dollari di ricavi in dodici mesi, e obbligo di mostrare la scritta «Kimi K3» nell'interfaccia per i prodotti sopra i 100 milioni di utenti attivi mensili o i 20 milioni di dollari di ricavi mensili. Per l'API il modello ragiona sempre, con un campo `reasoning_content` e uno sforzo regolabile con `reasoning_effort` su low, high e max (predefinito), e nelle conversazioni a più turni il messaggio dell'assistente va rimandato indietro intero; i motori di inferenza supportati sono vLLM, SGLang e TokenSpeed.
- **2026-07-29** — Un ingegnere di Baseten ha analizzato il codice del modello: 22.580 GPT-2 del 2019 come riferimento, architettura KDA (Kimi Delta Attention), attenzione residuale cross-layer e NoPE ovunque.
- **2026-07-29** — Il 22 luglio 2026 Michael Kratsios, direttore dell'Office of Science and Technology Policy della Casa Bianca, scrive su X che il governo statunitense ha informazioni secondo cui Moonshot AI avrebbe distillato Claude Fable di Anthropic per sviluppare Kimi K3, la prima volta che un funzionario di quel livello indica pubblicamente un laboratorio cinese e un modello americano specifici. A una settimana di distanza né la Casa Bianca né Anthropic pubblicano un registro di query, un manifesto dei dati di addestramento o un'analisi forense a sostegno, e diversi ricercatori indipendenti contestano la tesi: fra la piena disponibilità di Fable 5 (1 luglio) e il lancio di K3 (16 luglio) restano quindici giorni, troppo pochi per raccogliere, filtrare e addestrare un modello da 2,8 trilioni di parametri. L'accusa ha però un precedente documentato, perché a febbraio 2026 Anthropic aveva ricostruito oltre 3,4 milioni di scambi di Moonshot con Claude attraverso account fraudolenti.



- **2026-07-30** — Gira ora su Mac: caricato da 1,6 TB in formato nativo MXFP4 su M5 Max con 128 GB di RAM (per velocità utilizzabili servono due Mac Studio con 512 GB ciascuno); compresso del 62% mantenendo il 79% di accuratezza, da 1,56 TB a 594 GB con quantizzazione dinamica a un bit; testato su 28 task identici con Claude Code, Hermes e Kimi Code, con costo token fino a 30 volte diverso a seconda dell'harness; vLLM ha raggiunto 464 token al secondo in batch uno con 4x4 GB300. Uno studio legale americano che spendeva quasi 30.000 dollari al mese su Claude API lo sta testando in locale: server da 8 AMD MI355X (circa 2,3 TB di memoria) per circa 18.000 dollari al mese, un risparmio del 20-30% con dati che non escono mai.
- **2026-08-02** — In un test comparativo con DeepSeek V4 Flash e GLM 5.2 è primo con 9,5 su dieci al costo di sette centesimi; con la tecnica layer-by-layer (AirLLM) gira sotto 4 GB di VRAM senza quantizzazione.
- **2026-08-03** — Kimi K3 collegato a Blender MCP trasforma descrizioni in linguaggio naturale in scene tridimensionali complete: terreno, edifici, illuminazione, animazioni e script Python, tutto editabile.
- **2026-08-07** — Kimi K3 ha generato giochi completi con un solo prompt nello strumento CLI di Unity, ed e' ora disponibile in GitHub Copilot come ultimo modello open-weight di Moonshot per coding agentico, hostato da Fireworks.

- **2026-08-26** — Anche nella sua forma compressa non entra nei 512 GB di memoria unificata del Mac Studio M5 Ultra, e comunque i 104 miliardi di parametri attivi per token (su 2,8 trilioni totali) affosserebbero la velocità di generazione: è il contro-esempio usato per spiegare perché quella macchina è tarata su modelli come GLM 5.3 e non sui giganti da classifica.
- **2026-09-06** — Sull'[[artificial-analysis-intelligence-index]] di settembre è il miglior modello a pesi aperti con 59,7, settimo assoluto e a 6 punti dal primo ([[fable-5-1]] a 65,7), davanti a GLM-5.3 (59,5), Qwen3.8 Max Preview (58,1) e [[deepseek-v4-pro]] (53,2).
- **2026-09-13** — Nel confronto sui motori a streaming da disco resta l'esempio massimo della sparsità MoE sfruttabile: i suoi 2,8 trilioni di parametri sono tra i modelli che [[colibri]] ora fa girare leggendo gli esperti dal disco di un portatile.
- **2026-09-23** — Un progetto lo fa girare su una singola CPU con otto gigabyte di RAM: tutti i due punto settantotto trilioni di parametri, senza framework e senza GPU.
- **2026-10-20** — Secondo il report di SOCRadar è tra i modelli raggiunti via OpenRouter dagli affiliati di INC Ransom e The Gentlemen, che disponevano così di due fornitori con regole diverse e ricorrevano alla stessa riformulazione della richiesta quando un modello rifiutava.




## Collegamenti

- [[airllm]]
- [[blender-mcp]]
- [[claude-code]]
- [[claude-code-router]]
- [[claude-opus-5]]
- [[deepseek-v4-1]]
- [[deepseek-v4-flash]]
- [[deepseek-v4-ga]]
- [[fable-5]]
- [[gemini-3-5-pro]]
- [[glm-5-5]]
- [[gpt-5-6-sol]]
- [[hermes-agent]]
- [[kimi-code-cli]]
- [[kimi-k2-5]]
- [[kimi-k3-1]]
- [[monolith-1-0]]
- [[moonshot-ai]]
- [[qwen-3-8]]
- [[sicurezza-ai]]
- [[thinking-machines]]
- [[unity]]
- [[vllm]]
- [[queen]]
- [[index]]

