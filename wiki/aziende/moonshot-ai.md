---
title: "Moonshot AI"
category: azienda
tags: [moonshot-ai, agent, cina, kimi, llm, open-weight, ricerca]
related_puntate: [20260619, 20260718, 20260721, 20260722, 20260723, 20260728, 20260812, 20260825]
created: 2026-08-12
updated: 2026-10-25
sources: [raw/puntate/ainews20260619.md, raw/puntate/ainews20260718.md, raw/puntate/ainews20260721.md, raw/puntate/ainews20260722.md, raw/puntate/ainews20260723.md, raw/puntate/ainews20260728.md, raw/puntate/ainews20260812.md, raw/puntate/ainews20260825.md, raw/pillitteri/pillitteri20260729-kimi-k3-distillazione-fable-accusa-usa.md, raw/pillitteri/pillitteri20260609-kimi-for-work-agente-ai-desktop-swarm-300-agenti.md, raw/pillitteri/pillitteri20261009-ecosia-lascia-mistral-modelli-cinesi.md, raw/pillitteri/pillitteri20261013-anthropic-difese-distillazione-claude-zhipu-kimi.md, raw/pillitteri/pillitteri20261023-kimi-k3-1-pro-arriva-pesi-aperti-4-novembre.md, raw/pillitteri/pillitteri20261024-moonshot-ai-50-miliardi-ipo-hong-kong.md]
---

# Moonshot AI

## Introduzione

Startup cinese creatrice del modello Kimi K3 da 2,8 trilioni di parametri, uno dei principali open-weight del periodo. Ha rilasciato il modello con licenza MIT modificata e i progetti tecnici correlati (PerceptionBench, AgentENV, FlashKDA). È stata accusata da fonti del Dipartimento di Stato USA di aver distillato Anthropic Fable per sviluppare K3.

## Modelli

- [[fable-5]]
- [[kimi-k3]]
- [[kimi-k3-1]]
- [[kimi-linear]]

## Strumenti

- [[attention-residuals]]
- [[kimi-code-cli]]
- [[kimi-work]]

## Persone chiave

- [[zhilin-yang]]

## Timeline delle notizie

- **2026-06-09** — Moonshot AI presenta Kimi for Work, applicazione desktop locale che porta lo swarm di agenti fuori dai framework e dalla riga di comando: fino a 300 sotto-agenti in parallelo, browser integrato via WebBridge e memoria persistente, pronta da installare su macOS e Windows senza scrivere orchestrazione. [Fonte: raw/pillitteri/pillitteri20260609-kimi-for-work-agente-ai-desktop-swarm-300-agenti.md]

- **2026-06-19** — Moonshot AI è l'autrice di Kimi Work, agente desktop locale che esegue fino a trecento agenti in parallelo con Goal Mode da ventiquattro ore. [Fonte: raw/puntate/ainews20260619.md]
- **2026-07-18** — Moonshot AI ha rilasciato Kimi K3, modello da 2,8 trilioni di parametri che compete con GPT-5.6 Sol e Fable 5: supera Claude Opus 4.8 su diversi benchmark di programmazione e ragionamento, costa circa la metà di Opus 4.8 sull'API e sarà open source il 27 luglio. [Fonte: raw/puntate/ainews20260718.md]
- **2026-07-21** — Moonshot rilascia Kimi Code CLI open source MIT e ora sponsorizza claude-code-router: gli setup esistenti restano intatti, Kimi K3 si connette con un click, con preset integrati, failover automatico e caching a 0,30 dollari per milione di token. [Fonte: raw/puntate/ainews20260721.md]
- **2026-07-22** — Il 27 luglio rilascia Kimi K3 con pesi completi: 2,8 trilioni di parametri, un milione di token di contesto, licenza MIT modificata. [Fonte: raw/puntate/ainews20260722.md]
- **2026-07-23** — Ha rilasciato Kimi Code CLI, un agente da terminale basato su Kimi K3 con supporto a input video e sub-agenti dedicati, open source. Fonti del Dipartimento di Stato USA affermano che Moonshot AI avrebbe distillato Anthropic Fable per sviluppare K3, con una piattaforma interna sofisticata per distillazione su larga scala e accesso a server GB300 in Thailandia; gli USA condannano la distillazione industriale segreta della tecnologia proprietaria. Il 22 luglio 2026 il direttore dell'OSTP Michael Kratsios ha ripetuto l'accusa pubblicamente su X senza allegare prove: né la Casa Bianca né Anthropic hanno pubblicato registri di query o analisi forensi, e la finestra di quindici giorni fra la piena disponibilità di Fable 5 e il lancio di K3 è giudicata troppo stretta da diversi ricercatori indipendenti. [Fonte: raw/puntate/ainews20260723.md] [Fonte: raw/pillitteri/pillitteri20260729-kimi-k3-distillazione-fable-accusa-usa.md]
- **2026-07-28** — Kimi K3 è arrivato come modello open source: 2,8 trilioni di parametri e un milione di token di contesto, già disponibile su LM Studio e Hugging Face; lo stesso team ha rilasciato tre progetti tecnici su GitHub: PerceptionBench per la percezione visiva, AgentENV per gli ambienti di agent distribuiti e FlashKDA per ottimizzare l'attenzione delta. [Fonte: raw/puntate/ainews20260728.md]
- **2026-08-12** — Moonshot AI ha rilasciato Attention Residuals, il piu' grande upgrade ai transformer dal 2015: ogni layer usa softmax attention sulla profondita', guarda indietro, valuta ogni layer precedente e preleva selettivamente solo i dati necessari, con prestazioni equivalenti a modelli addestrati con il venticinque percento in piu' di compute. [Fonte: raw/puntate/ainews20260812.md]
- **2026-08-25** — Kimi Linear è l'architettura di attenzione lineare di Moonshot AI che fa girare gli LLM sei volte più veloce e usa il settantacinque percento in meno di memoria GPU rispetto alla full attention: per la prima volta un'architettura lineare batte la full attention su ogni benchmark, con quarantotto miliardi di parametri totali e tre attivi. [Fonte: raw/puntate/ainews20260825.md]
- **2026-10-09** — Ecosia sceglie Kimi di Moonshot AI tra i modelli open-weight con cui sostituire Mistral, serviti dalla piattaforma tedesca Melious su infrastruttura europea. [Fonte: raw/pillitteri/pillitteri20261009-ecosia-lascia-mistral-modelli-cinesi.md]
- **2026-10-13** — La stessa ricerca riferisce che richieste rivolte ai modelli Kimi sarebbero state inoltrate di nascosto a Claude, e riporta una richiesta di un utente che Anthropic ritiene affiliato all'Esercito Popolare di Liberazione cinese interessato ad analizzare la videosorveglianza di una persona specifica. [Fonte: raw/pillitteri/pillitteri20261013-anthropic-difese-distillazione-claude-zhipu-kimi.md]
- **2026-10-23** — Ha presentato Kimi K3.1 Pro, post-training di K3 da 2,8 trilioni di parametri (104 miliardi attivi) con contesto da un milione di token e pesi aperti promessi entro il 4 novembre, a 2 dollari per milione di token in ingresso e 10 in uscita, due terzi del prezzo di K3, con il 65% di allucinazioni in meno dichiarato sul lavoro finanziario. [Fonte: raw/pillitteri/pillitteri20261023-kimi-k3-1-pro-arriva-pesi-aperti-4-novembre.md]
- **2026-10-24** — Secondo Bloomberg del 6 ottobre Moonshot AI avrebbe chiuso l'ultimo round privato a circa 50 miliardi di dollari, contro i 35 di luglio e meno di 4 un anno prima, e preparerebbe la quotazione a Hong Kong per il primo trimestre 2027 con una raccolta fino a 5 miliardi guidata da Bank of America, con CICC, Deutsche Bank e Goldman Sachs come sponsor. Il dossier sarebbe già depositato in forma riservata e i ricavi annui ricorrenti valgono circa 1 miliardo, con l'obiettivo di 2 miliardi entro dicembre; cifre e tempi restano indiscrezioni e l'azienda non commenta. [Fonte: raw/pillitteri/pillitteri20261024-moonshot-ai-50-miliardi-ipo-hong-kong.md]













## Collegamenti

- [[anthropic]]
- [[attention-residuals]]
- [[fable-5]]
- [[kimi-code-cli]]
- [[kimi-k3]]
- [[kimi-k3-1]]
- [[kimi-work]]
- [[kimi-linear]]
- [[zhilin-yang]]
- [[index]]

