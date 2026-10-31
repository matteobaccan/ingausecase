---
title: "Laya-MLX"
category: strumento
tags: [apple-silicon, latenza, locale, mlx, open-source, porting]
created: 2026-09-23
updated: 2026-09-23
---

# Laya-MLX

## Introduzione

Porting su MLX — la libreria di calcolo di Apple per la memoria unificata dei chip M-series — di [[laya]], il clone open source più discusso di [[jev]]: pubblicato il 19 settembre 2026 dallo sviluppatore che si firma 雨夹雪 (handle @mizorewww) come repository mizorewww/laya-mlx, risponde a una domanda in 7-14 millisecondi senza mandare un byte a un server esterno.

## Funzionalità principali

- Non genera testo: prende uno stato — una frase, un'email, un ticket di supporto — e una domanda tipizzata, poi restituisce la risposta con probabilità calibrate in un unico passaggio in avanti attraverso la rete, senza catena di pensiero né JSON da validare a posteriori.
- Le domande accettate sono di tre tipi: choice (scegliere fra opzioni date, con una probabilità per ciascuna), score (un valore su una scala ordinata) e noul (la probabilità che un'affermazione sia vera o falsa).
- L'architettura è un encoder bidirezionale che ricorda ModernBERT, con lo stesso schema di attenzione globale e locale e il meccanismo RoPE per la codifica posizionale, non un modello generativo in stile GPT; la tokenizzazione usa il tokenizer Rust di Hugging Face.

## Installazione e uso

- Serve un Mac con chip Apple Silicon e macOS 14 o successivo, Python 3.11 o superiore e MLX in versione 0.32.2 o compatibile; l'installazione è via pip e il modello si scarica al primo utilizzo da Hugging Face. Non esiste una versione per Windows o Linux, perché il progetto dipende dall'architettura hardware Apple: esistono però porting paralleli, come la versione per Node.js via ONNX Runtime.
- Il modello si carica con `laya.load("aac6fef/laya-mlx")` e si interroga con `agent.predict(testo, dizionario_di_domande)`; il pacchetto riscrive il motore di inferenza in MLX ed elimina la dipendenza da PyTorch, Transformers e da qualunque chiamata di rete, con licenza Apache-2.0.

## Performance

- Su un M3 Max la latenza mediana è 13,42 millisecondi per il checkpoint da 421 milioni di parametri e 7,39 per quello multilingue da 322 milioni, con P95 a 13,92 e 7,79; il throughput è di 146,8 e 395,0 domande al secondo su cinquanta domande.
- La memoria di picco resta sotto il gigabyte (943,6 MiB e 687,6 MiB) con zero crescita della memoria attiva su cento chiamate ripetute, dato che conta quando il modello gira in background per ore, e la validazione è su 63 domande di test in FP32 e FP16.
- Nella demo di lancio il modello gioca a Snake con ogni mossa decisa da una chiamata: 60 decisioni al secondo nel tweet, 75,4 mosse al secondo nel README con la compilazione MLX attiva. Snake ha stato piccolo e spazio d'azione limitato, quindi dimostra che la latenza dichiarata è reale per un loop di controllo in tempo reale, non che il modello regga su compiti complessi.
- Il confronto con [[jev]] è la ragione del port: i 70-500 millisecondi dichiarati da [[typesafe-ai]] per una richiesta hostata diventano 7-14 millisecondi in locale, da 5 a oltre 60 volte meno a seconda del checkpoint e del carico di rete tolto di mezzo.

## Repository

- Il repository mizorewww/laya-mlx ha superato le 5.190 stelle in tre giorni; nello stesso arco di tempo il repository originale di Laya (convaiinnovations/laya, licenza Apache-2.0) è passato da poche centinaia a oltre 15.400 stelle con più di 1.270 fork.

## Azienda / autore

- Lo sviluppatore che si firma 雨夹雪 (@mizorewww), che oltre al port MLX ha pubblicato una variante Core ML per il Neural Engine dei Mac, con consumi dichiarati fino al 64 per cento in meno a parità di velocità, e che ha generato un piccolo indotto di porting e tool, dal port per Node.js via ONNX Runtime al confronto diretto laya-vs-jev.

## Timeline delle notizie

- **2026-09-19** — Esce laya-mlx, port di [[laya]] su MLX per Mac con chip Apple Silicon: risposte in 7-14 millisecondi, meno di un gigabyte di memoria, nessun byte inviato a un server esterno e benchmark misurati su M3 Max con 13,42 e 7,39 millisecondi di latenza mediana. Il repository supera le 5.190 stelle in tre giorni.

## Collegamenti

- [[laya]]
- [[jev]]
- [[typesafe-ai]]
- [[ai-locale]]
- [[index]]
