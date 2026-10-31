---
title: "GPT-SoVITS"
category: strumento
tags: [open-source, tts, voce, voice-cloning, locale]
related_puntate: []
created: 2026-09-12
updated: 2026-09-12
---

# GPT-SoVITS

## Introduzione

Sistema di sintesi vocale e clonazione della voce open source pubblicato dallo sviluppatore noto come RVC-Boss a gennaio 2024, con oltre 59.000 stelle su GitHub e licenza MIT. Combina due modelli neurali distinti: la parte GPT (autoregressiva) si occupa della prosodia, cioè ritmo, intonazione e pause, mentre la parte SoVITS (SoftVC VITS) ricostruisce il timbro della voce clonata.

## Funzionalità principali

- Due modalità: zero-shot TTS, che genera parlato da un campione di circa 5 secondi senza addestramento, e few-shot TTS, che con circa un minuto di audio pulito esegue un fine-tuning di pochi minuti e ottiene somiglianza e gestione delle emozioni nettamente superiori.
- Sintesi cross-lingua: una voce registrata in una lingua può leggere testi in inglese, giapponese, coreano o cantonese; il cinese è la lingua più curata, mentre l'italiano non è tra le lingue native ottimizzate ma la clonazione del timbro funziona a prescindere dalla lingua del testo.
- Versioni: v1 e v2 restano leggere e veloci, la v3 ha migliorato la somiglianza introducendo un artefatto metallico dovuto a un ricampionamento non intero, la v4 lo corregge e produce audio nativo a 48 kHz, mentre v2Pro e v2ProPlus sono indicate come le varianti consigliate nel 2026 per il miglior equilibrio tra qualità e requisiti hardware.

## Installazione e uso

- Windows: pacchetto integrato con Python, dipendenze e modelli già dentro, avviato con go-webui.bat su http://localhost:9874. Linux e macOS: ambiente Conda e script di installazione con parametri --device (CU126, CU128 o CPU) e --source (HF, HF-Mirror o ModelScope). Docker completo e "lite" via Docker Compose per l'isolamento.
- Flusso few-shot: preparare almeno un minuto di audio pulito (separazione vocale, slicing automatico e riduzione del rumore sono integrati nel WebUI), trascrivere con il modulo ASR e correggere gli errori a mano, addestrare separatamente SoVITS per il timbro e GPT per la prosodia, quindi generare la voce indicando pesi, audio di riferimento e testo.
- Requisiti pratici: per la sola inferenza bastano 6 GB di VRAM con una RTX 2060 o superiore, per il fine-tuning sono consigliati 12 GB con una RTX 3060; Apple Silicon è supportato con prestazioni inferiori, la sola CPU è possibile ma lenta e conviene tenere liberi 15-20 GB di disco. La modalità fp16 nel WebUI riduce l'uso di VRAM con un impatto quasi impercettibile sulla qualità.

## Casi d'uso

- Doppiaggio e localizzazione di un personaggio con lo stesso timbro in più lingue, audiolibri e podcast (come con [[audiblez]]), assistenti vocali personalizzati e accessibilità, per ridare la propria voce a chi la sta perdendo partendo da vecchie registrazioni.

## Limiti e avvertenze

- Clonare la voce di una persona senza consenso esplicito è illecito e può integrare violazioni del GDPR, del diritto all'immagine e, in caso di frode, reati penali: lo strumento va usato solo su voci proprie o autorizzate.
- La qualità dipende dal dataset più che dalla sua quantità: un minuto di audio nitido batte dieci minuti sporchi, e sui testi molto tecnici la pronuncia può inciampare.

## Repository

- RVC-Boss/GPT-SoVITS su GitHub, oltre 59.000 stelle, licenza MIT.

## Azienda/autore

- RVC-Boss, sviluppatore indipendente

## Modelli supportati

- Kokoro e altri TTS non sono coinvolti: GPT-SoVITS usa i propri modelli SoVITS e GPT addestrati dall'utente a partire dai pre-addestrati del progetto.

## Timeline delle notizie

- **2026-07-02** — Guida al tool: 59.000 stelle, licenza MIT, modalità zero-shot e few-shot, sintesi cross-lingua, requisiti hardware per inferenza e fine-tuning e il confronto di filosofia con i servizi gestiti come [[mai-voice-2]].

## Collegamenti

- [[voce-ai]]
- [[audiblez]]
- [[omnivoice]]
- [[fish-audio]]
- [[mai-voice-2]]
- [[open-source]]
- [[index]]
