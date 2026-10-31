---
title: "Ollama"
category: strumento
tags: [inference, llm, locale, mlx, modello, open-source, runtime]
related_puntate: [20260509, 20260511, 20260530, 20260601, 20260603, 20260613, 20260623, 20260702, 20260805, 20260811, 20260824, 20260825, 20260827, 20260912, 20261016]
created: 2026-08-12
updated: 2026-10-16
sources: [raw/pillitteri/pillitteri20260607-inferenza-locale-pc-normali-ollama-gemma-4-hermes.md, raw/puntate/ainews20260912.md, raw/puntate/ainews20260509.md, raw/puntate/ainews20260511.md, raw/puntate/ainews20260530.md, raw/puntate/ainews20260601.md, raw/puntate/ainews20260603.md, raw/puntate/ainews20260613.md, raw/puntate/ainews20260623.md, raw/puntate/ainews20260702.md, raw/puntate/ainews20260805.md, raw/puntate/ainews20260811.md, raw/puntate/ainews20260824.md, raw/puntate/ainews20260825.md, raw/puntate/ainews20260827.md, raw/pillitteri/pillitteri20260908-microsoft-codice-a-mano-finito-sviluppatori-ollama.md, raw/pillitteri/pillitteri20260615-autonomous-computer-costruire-ai-locale-casa.md, raw/pillitteri/pillitteri20260529-ollama-cosa-e-come-iniziare-guida-2026.md, raw/pillitteri/pillitteri20261004-installare-modello-uncensored-locale-mac-windows.md, raw/pillitteri/pillitteri20260813-meta-muse-glimmer-30b-open-weight-locale.md, raw/puntate/ainews20261016.md]
---

# Ollama

## Introduzione

Strumento open source per eseguire modelli LLM in locale. Ha riportato che DeepSeek-V4-Flash-0731 e' il modello a crescita piu' rapida di sempre per uso token.

## Funzionalità principali

- Ollama è tra i tool costruiti sulla base del codice di llama.cpp di Georgi Gerganov per eseguire modelli LLM localmente, insieme a LM Studio e GPT4All.
- Ollama locale è uno dei backend supportati dal tool no-code open source di Microsoft per analisi dati, insieme a OpenAI e Claude.
- Ollama è stato citato tra i backend compatibili di OpenHuman, l'agente personale privato e open source.

## Azienda / Autore

- [[deepseek]]
- [[georgi-gerganov]]
- [[microsoft]]
- [[openai]]
- [[qwen]]

## Modelli supportati / correlati

- [[chatgpt]]
- [[claude]]
- [[deepseek-v4-flash]]
- [[gemma-4]]
- [[llama]]
- [[muse-glimmer]]
- [[whisper]]

## Timeline delle notizie

- **2026-05-29** — La guida di riferimento fotografa il progetto al 29 maggio 2026: centosettantaduemilacinquecentosettantadue stelle su GitHub dal giugno 2023, sedicimila fork, licenza MIT e un rilascio a settimana, con la community che lo chiama il "Docker dei modelli linguistici" perché scarica, esegue e interroga i modelli in locale senza API esterne né connessione dopo il download; l'API REST locale gira di default su `http://localhost:11434`. [Fonte: raw/pillitteri/pillitteri20260529-ollama-cosa-e-come-iniziare-guida-2026.md]
- **2026-05-09** — Ollama è tra i tool costruiti sulla base del codice di llama.cpp di Georgi Gerganov per eseguire modelli LLM localmente, insieme a LM Studio e GPT4All. [Fonte: raw/puntate/ainews20260509.md]
- **2026-05-11** — Ollama locale è uno dei backend supportati dal tool no-code open source di Microsoft per analisi dati, insieme a OpenAI e Claude. [Fonte: raw/puntate/ainews20260511.md]
- **2026-05-30** — Ollama è stato citato tra i backend compatibili di OpenHuman, l'agente personale privato e open source. [Fonte: raw/puntate/ainews20260530.md]
- **2026-06-01** — Nella nuova ondata di alternative open source ai software a pagamento, Ollama è stato indicato come alternativa alle API di OpenAI, completamente gratuito e funzionale. [Fonte: raw/puntate/ainews20260601.md]
- **2026-06-03** — Ollama insieme a Open WebUI permette di eseguire localmente Qwen, DeepSeek e Llama: niente token, niente rate limit, niente cloud, e un Mac Mini M4 da cinquecentonovantanove dollari si ripaga in meno di due mesi contro i quattrocentocinquantanove dollari mensili. [Fonte: raw/puntate/ainews20260603.md]
- **2026-06-07** — Ollama è lo standard de facto dell'inferenza locale con oltre 173.000 stelle su GitHub e gira su macOS, Linux e Windows; il suo perno è l'API compatibile con OpenAI attiva su http://localhost:11434, che permette a framework come LangChain e CrewAI e agli agenti da terminale di puntarsi all'indirizzo locale cambiando solo l'URL. [Fonte: raw/pillitteri/pillitteri20260607-inferenza-locale-pc-normali-ollama-gemma-4-hermes.md]
- **2026-06-13** — Ollama con Mac Mini M4 e Claude Code sostituisce uno stack di subscription da quattromilanovecento dollari l'anno con hardware da cinquecentonovantanove dollari: tre dollari di elettricità al mese e oltre cinquemiladuecento dollari di risparmio annuale. [Fonte: raw/puntate/ainews20260613.md]
- **2026-06-23** — Ollama è il runtime locale su cui gira Open Notebook, l'alternativa open source a NotebookLM Plus con podcast multi-speaker. [Fonte: raw/puntate/ainews20260623.md]
- **2026-07-02** — Porta Gemma 4 a velocità quasi raddoppiata su Apple Silicon grazie a MLX: il miglioramento deriva dalla predizione multi-token ora attiva per default, con regolazione automatica di quanti token anticipare. [Fonte: raw/puntate/ainews20260702.md]
- **2026-08-05** — Ollama riporta che DeepSeek-V4-Flash-0731 e' il modello a crescita piu' rapida di sempre per uso token, con capacita' scalate in USA ed Europa, oltre cento token al secondo e zero data retention. [Fonte: raw/puntate/ainews20260805.md]
- **2026-08-11** — Ollama supporta Muse Glimmer: disponibile via engine MLX su Apple Silicon, con ottimizzazioni per NVIDIA e AMD in arrivo. [Fonte: raw/puntate/ainews20260811.md]

- **2026-08-13** — Ollama aggiunge Muse Glimmer nella versione 0.32.7, insieme ai build ExecuTorch pre-esportati per NVIDIA CUDA e Apple Silicon. [Fonte: raw/pillitteri/pillitteri20260813-meta-muse-glimmer-30b-open-weight-locale.md]

- **2026-08-24** - FreeToken di UC Berkeley si presenta come piu' veloce di Ollama nell'esecuzione locale di modelli frontier MoE su hardware consumer. [Fonte: raw/puntate/ainews20260824.md]
- **2026-08-25** — Huihui-Qwen3.8-27B-abliterated-GGUF è multimodale, quasi zero rifiuti e gira in locale anche con Ollama. [Fonte: raw/puntate/ainews20260825.md]

- **2026-08-27** — Ollama 0.33 integra Claude Desktop come gateway per modelli locali: un toggle e i modelli locali funzionano. [Fonte: raw/puntate/ainews20260827.md]

- **2026-09-12** — La versione zero punto trentaquattro di Ollama permette di configurare ChatGPT Desktop per usare modelli Ollama in locale: basta aggiornare. [Fonte: raw/puntate/ainews20260912.md]

- **2026-09-08** — Un lungo atto d'accusa raccoglie oltre 1.600 voti su r/LocalLLaMA con il 92 percento di consenso ("Friends Don't Let Friends Use Ollama", uscito il 15 aprile 2026 sul blog Sleeping Robots): Ollama poggia su [[llama-cpp]] ma per oltre 400 giorni non lo ha citato né rispettato la licenza MIT, a parità di hardware macina 1,8 volte i token di llama.cpp (89 contro 161 al secondo nel test citato) e va dal 30 al 70 percento meno forte su CPU e generazione di codice, offre meno quantizzazioni (Q4_K_S, Q4_K_M, Q8_0, F16, F32 contro Q5_K_M, Q6_K e i formati IQ) e ha spacciato per modello completo varianti distillate come le riduzioni di DeepSeek-R1. Tra le alternative indicano llama.cpp, LM Studio, Jan, ramalama e koboldcpp. [Fonte: raw/pillitteri/pillitteri20260908-microsoft-codice-a-mano-finito-sviluppatori-ollama.md]
- **2026-06-15** — È uno dei tre motori di inferenza coperti dalla guida autonomous-computer per costruirsi in casa un computer AI, insieme a [[vllm]] e [[llama-cpp]], ed è quello che compare anche nella prima distribuzione con assistente IA a bordo, [[linux-ai-os]], dove fa girare i modelli della famiglia Llama di Meta in locale. [Fonte: raw/pillitteri/pillitteri20260615-autonomous-computer-costruire-ai-locale-casa.md]
- **2026-10-04** — Una guida mostra l'installazione in locale di un modello uncensored con Ollama, LM Studio, llama.cpp e MLX: il comando `ollama run hf.co/{utente}/{repository}:{quantizzazione}` scarica e avvia un GGUF direttamente da Hugging Face. [Fonte: raw/pillitteri/pillitteri20261004-installare-modello-uncensored-locale-mac-windows.md]
- **2026-10-16** — Citato come riferimento da Magnitude, che dichiara oltre 2 volte la sua velocità sui modelli aperti senza nuovo hardware. [Fonte: raw/puntate/ainews20261016.md]







## Collegamenti

- [[chatgpt]]
- [[claude]]
- [[claude-code]]
- [[deepseek]]
- [[deepseek-v4-flash]]
- [[gemma-4]]
- [[georgi-gerganov]]
- [[llama]]
- [[llama-cpp]]
- [[microsoft]]
- [[muse-glimmer]]
- [[n8n]]
- [[openai]]
- [[openhuman]]
- [[open-notebook]]
- [[open-webui]]
- [[qwen]]
- [[whisper]]
- [[freetoken]]
- [[huihui-qwen3-8-27b-abliterated-gguf]]
- [[anythingllm]]
- [[spark-x2-5-4b]]
- [[index]]

