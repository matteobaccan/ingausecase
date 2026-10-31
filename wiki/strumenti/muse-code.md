---
title: "Muse Code"
category: strumento
tags: [agent, beta, coding, generazione-app, meta]
related_puntate: [20260806, 20260807]
created: 2026-08-12
updated: 2026-10-13
---

# Muse Code

## Introduzione

Alternativa a Claude Code lanciata da Meta, basata sul modello Muse Spark 1.2, con skill predefinite e sub-agenti e prezzi sotto DeepSeek V4 Flash in cambio del training sul codice.

## Funzionalità principali

- Muse Code ora e' in beta insieme a Muse Spark uno virgola due: team di agenti che pianificano, scrivono e affinano il codice, con deploy su repository multipli.
- Muse Code di Meta e' un'alternativa a Claude Code basata su Spark uno virgola due, con skill predefinite e sub-agenti e prezzi sotto DeepSeek V4 Flash se accetti che il codice addestri il modello.
- Ogni chiamata al modello, ogni esecuzione di strumento, ogni approvazione e ogni modifica vengono scritte su un registro locale in sola aggiunta prima di essere eseguite: Meta lo chiama replay-exact, e una sessione che va in crash riparte dall'ultimo passo registrato senza rileggere il repository e senza ricostruire un contesto già acquisito.
- I sub-agenti in background lavorano in worktree Git separati, quindi la copia di lavoro e il suo git status restano intatti mentre più agenti modificano file diversi in parallelo; persistono per tutta la sessione e accumulano contesto sul progetto, con un costo in token che sale sulle sessioni lunghe.
- Tre skill preinstallate: /plan produce un piano di modifica da approvare prima di toccare i file, /grill mette sotto stress il lavoro appena fatto cercando casi limite e ipotesi non verificate, /goal fissa l'obiettivo della sessione tenendolo come riferimento per i passi successivi.
- Due tier di listino per lo stesso modello: standard a 1,25 dollari per milione di token in input e 4,25 in output, contributor a 0,10 in input e 0,20 in output perché Meta si riserva di addestrare i propri modelli sui prompt inviati; il contesto è di 1.048.576 token.
- Uscito dalla beta il 2 settembre 2026 insieme a [[muse-spark-1-3]]: la versione stabile aggiunge la messaggistica tra sessioni, un motore di workflow multi-agente e un'anteprima dell'SDK per gli sviluppatori.

## Azienda / Autore

- [[meta]]

## Modelli supportati / correlati

- [[muse-spark-1-2]]
- [[muse-spark-1-3]]

## Timeline delle notizie

- **2026-08-06** — Muse Code ora e' in beta insieme a Muse Spark uno virgola due: team di agenti che pianificano, scrivono e affinano il codice, con deploy su repository multipli.
- **2026-08-07** — Muse Code di Meta e' un'alternativa a Claude Code basata su Spark uno virgola due, con skill predefinite e sub-agenti e prezzi sotto DeepSeek V4 Flash se accetti che il codice addestri il modello.
- **2026-08-07** — La ricostruzione completa del lancio del 5 agosto: Muse Spark 1.2 e Muse Code sono co-addestrati, e questo spiega perché il vantaggio si vede sui compiti da terminale (82,9% su Terminal-Bench 2.1 contro l'86,7% di Claude Opus 5 in Claude Code) e sparisce su DeepSWE, dove il modello scende terzo con 59,3% dietro Opus 5 e GPT-5.6 Terra. Il tier contributor costa 0,10 dollari per milione di token in input invece di 1,25 perché Meta si riserva di addestrare sui prompt inviati: su un repository proprietario è una clausola contrattuale, non un'opzione di fatturazione. Muse Spark 1.2 non ha pesi scaricabili, al contrario della linea Llama; due giorni dopo l'annuncio xAI rilascia Grok Build 1.0, chiudendo la beta del suo agente da terminale.
- **2026-09-02** — Muse Code esce dalla beta insieme a [[muse-spark-1-3]]: stabile con messaggistica tra sessioni, workflow multi-agente e anteprima dell'SDK. Il mercato degli agenti da terminale si è intanto affollato al punto che [[deepseek-harness]], il progetto che ingloba Claude Code e Codex, ha superato le 200.000 stelle su GitHub.
- **2026-10-13** — Muse Code è fra i canali di accesso iniziale a Muse Wonder e Wonder Full, i nuovi modelli annunciati da Meta, insieme ad alcuni canali API. Muse Wonder Full, la variante a più calcolo, non ha API pubblica ed è riservata ai piani Power e Maximum di Muse Code, da 50 e 200 dollari al mese, mentre il modello base arriva anche dalla Meta Model API e da OpenRouter.




## Collegamenti

- [[claude-code]]
- [[codex]]
- [[meta]]
- [[muse-spark-1-2]]
- [[muse-spark-1-3]]
- [[deepseek-harness]]
- [[muse-wonder]]
- [[index]]

