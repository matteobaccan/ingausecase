---
title: "Gemma 4"
category: modello
tags: [agent, edge, google, llm, mtp, multimodale, on-device, open-source, open-weight, quantizzazione, webgpu]
related_puntate: [20260516, 20260517, 20260530, 20260602, 20260604, 20260607, 20260608, 20260609, 20260612, 20260613, 20260619, 20260621, 20260627, 20260702, 20260708, 20260709, 20260711, 20260715, 20260718, 20260719, 20260724, 20260726, 20260729, 20260805, 20260808, 20260812, 20260924, 20260929]
created: 2026-08-12
updated: 2026-10-11
---

# Gemma 4

## Introduzione

Famiglia di modelli open-weight di Google, tra i più scaricati al mondo con oltre 300 milioni di download. Nel periodo ha aggiunto varianti QAT di Unsloth per GPU da 8 GB e versioni post-addestrate con punteggi di confidenza.

## Capacità e performance

- Gemma 4 di Google DeepMind è integrato nativamente in ComfyUI: LLM multimodale con testo, immagine, audio e video input più reasoning step-by-step integrato.
- Gemma 4 ha rifiutato di lanciare 64 agenti in parallelo per un developer, mentre Qwen 3.6 ha iniziato a costruire subito, in esecuzione per otto ore senza permission richieste né API call.
- Google ha rilasciato Gemma 4 nell'app AI Edge Gallery: agente locale al 100% che converte immagini in schemi JSON, trascrive audio e usa skill agente per interagire con app, tutto offline nella tua tasca.

## Azienda di riferimento

- [[comfyui]]
- [[google]]
- [[meta]]
- [[nvidia]]
- [[reactor]]
- [[unsloth]]

## Strumenti correlati

- [[ai-edge-eloquent]]
- [[antigravity]]
- [[ai-edge-gallery]]
- [[google-ai-edge]]
- [[hermes-agent]]
- [[lang-extract]]
- [[llama-cpp]]
- [[ollama]]
- [[surface-laptop-ultra]]
- [[video-remix]]
- [[vllm]]
- [[voicebox]]

## Timeline delle notizie

- **2026-04-03** — Google DeepMind ha lanciato Gemma 4 il 2 aprile 2026 con quattro varianti (E2B ed E4B edge, 26B MoE con 3,8 miliardi di parametri attivi, 31B dense), licenza Apache 2.0 senza restrizioni, multimodalità nativa (testo, immagini, video, audio), function calling nativo, oltre 140 lingue e contesto fino a 256.000 token. Sul coding il Codeforces ELO è passato da 110 della Gemma 3 a 2150 e sull'MMLU Pro la 31B segna 85,2 per cento. NVIDIA ha ottimizzato la famiglia per le GPU RTX serie 40 e 50.
- **2026-04-12** — Google AI Edge Gallery fa girare in locale sul telefono Gemma 4 E2B (meno di 1,5 GB di RAM) ed E4B, con finestra di 128.000 token, oltre 140 lingue e pesi a 2 e 4 bit; benchmark dichiarati: su Pixel 7 Pro con FunctionGemma 1.916 token al secondo in prefill e 142 in decode.



- **2026-05-16** — Gemma 4 di Google DeepMind è integrato nativamente in ComfyUI: LLM multimodale con testo, immagine, audio e video input più reasoning step-by-step integrato.
- **2026-05-17** — Gemma 4 ha rifiutato di lanciare 64 agenti in parallelo per un developer, mentre Qwen 3.6 ha iniziato a costruire subito, in esecuzione per otto ore senza permission richieste né API call.
- **2026-05-30** — Google ha rilasciato Gemma 4 nell'app AI Edge Gallery: agente locale al 100% che converte immagini in schemi JSON, trascrive audio e usa skill agente per interagire con app, tutto offline nella tua tasca.
- **2026-06-02** — Gemma 4 è tra i modelli collegabili a MCP con LLM locali secondo la guida di Unsloth, per workflow automatizzati privati.
- **2026-06-04** — Gemma 4 12B ha dodici miliardi di parametri, prestazioni vicine al 26B, tutto in sedici GB di VRAM con architettura unificata senza encoder separati. Nei test di Atomic Chat su RTX 4090 il 26B-A4B ha vinto su ogni scena (animazione HTML5 con fisica), girando uno punto sette volte più veloce con solo quattro B attivi; Unsloth lo esegue localmente con otto GB di RAM via Dynamic GGUF, con immagini, audio e duecentocinquantasei K di contesto.
- **2026-06-07** — Gemma 4 12B QAT ha dodici miliardi di parametri e gira su schede da otto gigabyte di VRAM: trenta token al secondo con sessantaquattromila di contesto contro i quindici della versione standard; è più piccolo ma più veloce perché addestrato per essere quantizzato.
- **2026-06-07** — Guida allo stack locale con Gemma 4: la famiglia è stata rilasciata da Google DeepMind il 2 aprile 2026 con licenza Apache 2.0 e copre quattro taglie, E2B ed E4B edge (ingombro effettivo di 2 e 4 miliardi di parametri grazie alle Per-Layer Embeddings, contesto a 128.000 token), 12B encoder-free multimodale che gira su un laptop da 16 GB, 26B Mixture of Experts con 3,8 miliardi di parametri attivi e contesto a 256.000 token e 31B dense. Il function calling nativo, addestrato con token speciali dedicati, regge catene di cinque chiamate a strumenti consecutive ed è il motivo per cui la 26B è la scelta tipica per un agente locale.
- **2026-06-08** — Gemma 4 MTP è stato integrato ufficialmente in llama.cpp: la combinazione QAT più MTP permette setup ultraleggero e velocissimo, pronto per la community.
- **2026-06-09** — Gemma 4 12B alimenta AI Edge Eloquent on-device; llama.cpp aggiunge il supporto video input per usare le sue capacità di comprensione video via chat completions endpoint e mtmd-cli.
- **2026-06-12** — Gemma 4 QAT ha ventisei miliardi di parametri in quattro formati, con meno memoria richiesta e deploy locale anche su mobile (reso ufficiale da Google DeepMind). La versione MTP raddoppia la velocità: centosessantadue token al secondo sulla 12B e centouno sulla 31B senza perdita di accuratezza, con GGUF disponibili su Unsloth.
- **2026-06-13** — Gemma 4 standard è consigliata da Google stessa per la precisione fattuale rispetto a DiffusionGemma; la 26B A4B QAT MTP gira con Hermes Agent Desktop App su una macchina da novecento dollari con otto GB di VRAM (venti token al secondo in decode, duecento in prefill, tool call senza allucinazioni).
- **2026-06-19** — Xenova ha usato Claude per creare kernel WebGPU personalizzati e far girare Gemma 4 direttamente nel browser a duecentocinquantacinque token al secondo, tutto locale; Gemma 4 12B raggiunge oltre mille token al secondo in prefill su otto GB di VRAM con centoventi K di contesto su RTX quattromilasessanta e ventotto GB di RAM, ogni layer sulla GPU: visione, input audio e ragionamento su una scheda da otto giga.
- **2026-06-21** — Gemma 4 su WebGPU, ottimizzato dall'agente Fable 5, raggiunge duecentocinquantacinque token al secondo: partenza da nove punto sette, arrivo a duecentocinquantacinque, ventisei volte più veloce, tutto nel browser.
- **2026-06-27** — Oltre 100 agenti hanno collaborato per una settimana e accelerato Gemma 4 su vLLM di 5 volte, sviluppando autonomamente norme di comunicazione, pooling di quote, divisione del lavoro computazionale e debug kernel cross-agent. Usata anche come base di post-training per Ornith 1.0.
- **2026-07-02** — Su Ollama con MLX la velocità è quasi raddoppiata su Apple Silicon grazie alla predizione multi-token per default. Un developer ha usato Claude Fable 5 per scrivere kernel ottimizzati che portano Gemma 4 a 255 token al secondo su WebGPU con M4, con demo in browser.
- **2026-07-03** — Gemma 4 gira dentro il browser a 255 token al secondo su un Mac con chip M4, con i kernel WebGPU scritti da Fable 5 di Anthropic e la demo pubblica sullo Space webml-community/Gemma-4-WebGPU: il download iniziale dei pesi è di circa 2,9 GB, poi ogni token viene generato sulla GPU locale senza server e senza chiave API. Omar Sanseviero di Google DeepMind ha confermato di aver visto la demo girare a quella velocità.



- **2026-07-08** — Technical report ufficiale rilasciato: modelli da E2B a 31B, con variante encoder-free 12B, addestramento quantization-aware e drafter multi-token prediction.
- **2026-07-09** — Gemma 4 ora funziona on-device su React Native: esecuzione completamente offline nelle app cross-platform con accelerazione hardware locale, Vulkan su Android e MLX su Apple Silicon, con capacità di visione e tool-use su dispositivo.
- **2026-07-11** — Gemma 4 è una famiglia di modelli multimodali avanzati che girano direttamente su dispositivi locali senza connessione: già usati per sistemi sanitari offline e supporto alle lingue indigene.
- **2026-07-15** — Gemma 4 riceve aggiornamenti: modello unified da dodici miliardi con supporto MTP e checkpoint QAT, deploy da edge a workstation sotto Apache 2.0, usato per tutor IA offline, bardi medievali e giochi d'avventura real-world.
- **2026-07-18** — Google ha aggiornato Gemma 4 con miglioramenti significativi a tool-calling, accuratezza chat e velocità; Unsloth ha già pubblicato le versioni quantizzate GGUF, MLX e NVFP4 aggiornate.
- **2026-07-19** — Google ha aggiornato Gemma 4 con Flash Attention 4 e template ottimizzati per tool calling: +25,8 per cento su TB2 e +62,7 per cento su Tau2, con cache KV a quattro bit gira a trentatré token al secondo su singola RTX 4090 con centonovantamila token di contesto; Gemma 4 ha completato ts-bench con punteggio cento, mentre le versioni da ventisei e dodici miliardi migliorano ma non completano.
- **2026-07-24** — Ha superato i 300 milioni di download e il team ringrazia la community open source; Unsloth ha rilasciato Gemma 4 26B A4B QAT per schede con 8 GB di VRAM, con 180.000 token di contesto su RTX 4060 con cache KV a 8 bit.
- **2026-07-26** — Ha superato 900.000 download questa settimana: da Gemma 1 a MedGemma fino a Gemma 4, il supporto open source continua.
- **2026-07-29** — Il team Cactus ha post-addestrato Gemma 4 per restituire un punteggio di confidenza: prompt elaborato in locale se la confidenza è alta, con routing al modello cloud solo nel 15-55% dei casi.
- **2026-08-05** — Un utente ha fatto girare Gemma 4 su iPhone con circa cinquecento mega di RAM usando approccio calibration-aware quantization: assistente offline che gestisce azioni calendario con circa cinquecentosedici mega di RAM attiva.
- **2026-08-08** — A un hackathon recente, Gemma 4 ha alimentato un copilot per meeting live a mille token al secondo: conversazioni parlate che diventano prototipi funzionanti prima della fine della riunione.
- **2026-09-24** — L'SDK di [[antigravity]] lo fa girare completamente offline sulla GPU locale, costruito su LiteRT di [[google-ai-edge]]: zero costi API, privacy totale e nessuna connessione internet richiesta.
- **2026-08-12** — Nell'head-to-head contro Muse Glimmer 30B, Gemma 4 31B e' stato superato nella generazione di giochi arcade; nella virtualizzazione Metal su M1 Ultra, Gemma 4 12B segna sette virgola venti per prompt e quattordici virgola cinquantaquattro per generazione, mentre TinyLlama fa undici virgola otto e sedici virgola trentasei.

- **2026-09-25** — La guida all'uso di Gemma 4 con LM Studio mostra come far girare il modello in locale per interrogare contratti, preventivi e bilanci aziendali senza inviare i file a server terzi: la licenza Apache 2.0 ammette l'uso commerciale e LM Studio è gratuita anche in azienda, con l'inferenza che avviene interamente sul computer.
- **2026-09-29** — Google e Kaggle lanciano la Gemma 4 Developer Agent Competition: obiettivo costruire agenti autonomi che girano offline su hardware consumer con le stesse capacità dei modelli cloud, oltre 110.000 dollari in premi e scadenza il 2 novembre 2026.
- **2026-10-09** — In Google AI Edge Foresight l'utente sceglie il modello Gemma 4 da far girare sul Mac: E4B è il predefinito (veloce, leggero, a basso consumo), 12B offre più capacità ma richiede più spazio e memoria.




## Collegamenti

- [[ai-edge-eloquent]]
- [[ai-edge-gallery]]
- [[antigravity]]
- [[bonsai-27b]]
- [[comfyui]]
- [[diffusiongemma]]
- [[fable-5]]
- [[gemma-4-12b]]
- [[google]]
- [[google-ai-edge]]
- [[hermes-agent]]
- [[lang-extract]]
- [[llama-cpp]]
- [[maple-preview]]
- [[meta]]
- [[muse-glimmer]]
- [[nvidia]]
- [[ollama]]
- [[ornith-1-0]]
- [[qwen-3-6]]
- [[reactor]]
- [[surface-laptop-ultra]]
- [[unsloth]]
- [[video-remix]]
- [[vllm]]
- [[voicebox]]
- [[xenova]]
- [[index]]

