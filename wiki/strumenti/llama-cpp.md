---
title: "llama.cpp"
category: strumento
tags: [c++, cpp, inference, inferenza, llm, locale, multimodale, open-source, runtime]
related_puntate: [20260509, 20260528, 20260530, 20260608, 20260609, 20260622, 20260729, 20260810, 20260825]
created: 2026-08-12
updated: 2026-10-08
---

# llama.cpp

## Introduzione

Progetto open source di Georgi Gerganov, un singolo file C che esegue modelli IA in locale senza GPU, base di Ollama, LM Studio e GPT4All.

## Funzionalità principali

- llama.cpp, scritto come singolo file C da Georgi Gerganov nel marzo 2023, ha fatto girare un modello IA completo su un MacBook senza GPU né cloud, smontando il mito delle GPU da 10.000 dollari; è la base di Ollama, LM Studio e GPT4All, supera 107.000 stelle GitHub, è il progetto open source IA più veloce a raggiungere 100.000 stelle e nel 2026 Hugging Face ha assunto l'intero team.
- llama.cpp è stato citato come runtime per l'esecuzione locale full speed di LFM 2.5 VL 1.6B di Liquid AI.
- llama.cpp è stato citato come runtime della trascrizione audio realtime locale con LFM 2.5-Audio-1.5B, senza cloud né latenza.

## Azienda / Autore

- [[georgi-gerganov]]
- [[qwen]]

## Modelli supportati / correlati

- [[gemma-4]]
- [[gemma-4-26b-a4b-qat]]
- [[lfm-2-5-audio-1-5b]]
- [[lfm-2-5-vl-1-6b]]
- [[qwen3-tts]]

## Timeline delle notizie

- **2026-05-09** — llama.cpp, scritto come singolo file C da Georgi Gerganov nel marzo 2023, ha fatto girare un modello IA completo su un MacBook senza GPU né cloud, smontando il mito delle GPU da 10.000 dollari; è la base di Ollama, LM Studio e GPT4All, supera 107.000 stelle GitHub, è il progetto open source IA più veloce a raggiungere 100.000 stelle e nel 2026 Hugging Face ha assunto l'intero team. Il rilascio di [[ds4]] da parte di [[antirez]] riapre il dibattito sul rapporto tra runtime generalisti ed engine specializzate: DS4 non linka GGML ma, per ammissione dell'autore, esiste solo grazie al lavoro di llama.cpp su kernel Metal, formato GGUF e precisione numerica, e la tesi è che i progetti generalisti coprono il 95% dei casi d'uso mentre il 5% di modelli con sparsità estrema può giustificare un fork ottimizzato a mano.
- **2026-05-28** — llama.cpp è stato citato come runtime per l'esecuzione locale full speed di LFM 2.5 VL 1.6B di Liquid AI.
- **2026-05-30** — llama.cpp è stato citato come runtime della trascrizione audio realtime locale con LFM 2.5-Audio-1.5B, senza cloud né latenza.
- **2026-06-08** — llama.cpp ha integrato ufficialmente Gemma 4 MTP: la combinazione con la versione QAT permette setup ultraleggero e velocissimo.
- **2026-06-09** — llama.cpp aggiunge il supporto video input: le capacità di comprensione video di Gemma 4 usabili direttamente via chat completions endpoint e con mtmd-cli.
- **2026-06-22** — llama.cpp è il runtime che nelle ultime build supporta MTP (multi token prediction), permettendo a Gemma 4 26b-a4b-it-qat di girare su GPU consumer da sei-otto GB.
- **2026-07-29** — llama.cpp ha fixato un bug di performance MTP: dieci percento più veloce su Qwen 3.6-35B-A3B, incluso nella release b10152 del 27 luglio.
- **2026-08-10** — Qwen3-TTS e' arrivato in llama punto cpp con due GGUF da caricare insieme: a Q4_K_M occupano uno punto due GB piu' duecentocinquantacinque MB, con audio mono ventiquattro kHz e Apache due virgola zero.
- **2026-08-25** — Huihui-Qwen3.8-27B-abliterated-GGUF è multimodale, quasi zero rifiuti e gira in locale anche con llama.cpp.

- **2026-08-28** — Con l'acquisizione di [[hugging-face]] da parte di [[nvidia]], il progetto passa indirettamente sotto il produttore delle GPU: il team GGML, guidato da [[georgi-gerganov]], era entrato in Hugging Face il 20 febbraio 2026 con la promessa che progetti e autonomia tecnica restassero intatti, e llama.cpp resta sotto licenza MIT, che è irrevocabile. Il timore non riguarda quindi il codice già pubblicato ma la direzione futura delle ottimizzazioni, perché il motore gira anche su schede AMD, su Apple Silicon e su CPU senza alcuna GPU Nvidia, e proprio questa indipendenza è la promessa dell'AI locale.
- **2026-09-08** — llama.cpp è il motore indicato come alternativa a [[ollama]]: a parità di hardware macina 1,8 volte i token (161 contro 89 al secondo nel test citato) e va dal 30 al 70 percento più forte su CPU e generazione di codice, con più quantizzazioni disponibili (Q5_K_M, Q6_K e i formati IQ oltre a quelli offerti da Ollama). Nella polemica si contesta a Ollama di aver costruito il proprio fork su llama.cpp senza citarlo né rispettare la licenza MIT per oltre 400 giorni.
- **2026-10-07** — Microsoft annuncia llama.cpp dentro Windows ML: il runtime ufficiale di Windows parla ONNX, mentre buona parte dei modelli aperti che girano sui PC di casa circola in formato GGUF, quindi l'integrazione dovrebbe dare agli sviluppatori una strada diretta per provare i modelli nuovi senza il passaggio da ONNX, con API di alto livello per l'AI generativa; Microsoft non ha indicato né la data di rilascio né i dettagli dell'integrazione.




## Collegamenti

- [[gemma-4]]
- [[gemma-4-26b-a4b-qat]]
- [[georgi-gerganov]]
- [[lfm-2-5-audio-1-5b]]
- [[lfm-2-5-vl-1-6b]]
- [[open-source]]
- [[qwen]]
- [[qwen3-tts]]
- [[whisper-cpp]]
- [[huihui-qwen3-8-27b-abliterated-gguf]]
- [[hugging-face]]
- [[nvidia]]
- [[spark-x2-5-4b]]
- [[index]]

