---
title: "Artificial Analysis Intelligence Index"
category: strumento
tags: [benchmark, open-weight, valutazione]
related_puntate: [20261002]
created: 2026-09-12
updated: 2026-10-03
---

# Artificial Analysis Intelligence Index

## Introduzione

Punteggio unico che aggrega decine di benchmark (ragionamento, codice, matematica, compiti agentici) in un solo numero di intelligenza per modello, così da confrontare oltre 170 sistemi sulla stessa scala. È diventato il termometro più citato della gara tra i laboratori.

## Classifica di settembre 2026

| Modello | Punteggio | Tipo |
| --- | --- | --- |
| [[fable-5-1]] (Anthropic) | 65,7 | chiuso |
| [[claude-opus-5]] (Anthropic) | 63,0 | chiuso |
| [[muse-spark-1-3]] (Meta) | 62,1 | chiuso |
| [[gpt-6-astra]] (OpenAI) | 61,2 | chiuso |
| [[kimi-k3]] (Moonshot) | 59,7 | aperto |
| [[glm-5-3-cybersecurity-fp8]] (Z.AI) | 59,5 | aperto |
| [[qwen-3-8-max]] Preview (Alibaba) | 58,1 | aperto |
| [[deepseek-v4-pro]] (DeepSeek) | 53,2 | aperto |

## Il gap che si dimezza

- A settembre 2026 tra il miglior modello chiuso e il miglior aperto ballano **6 punti**; dodici mesi prima erano 13, mentre i migliori pesi aperti galleggiavano nella parte bassa dei 30. Nel giro di un anno quattro modelli aperti hanno superato quota 50.
- SemiAnalysis ha misurato il tempo di recupero più che il punteggio: circa 18 mesi per colmare un divario iniziale di quasi 36 punti nell'era dello scaling puro, otto mesi e mezzo per 12 punti nell'era del ragionamento, attorno ai **cinque mesi** nell'era degli agenti. A ogni generazione i modelli aperti impiegano circa la metà del tempo per raggiungere il primo modello chiuso di quell'era; il ritardo per compito oggi va dai cinque ai ventidue mesi.

## Chi guida i pesi aperti

- La fascia alta è quasi tutta cinese: Moonshot con Kimi K3 punta su sessioni lunghe e lavoro agentico, Z.AI insegue il codice (GLM-5.3 ha macinato 2.436 vulnerabilità su CyberGym e la generazione precedente segna 77,8 su SWE-bench Verified, la cifra più alta del campo aperto), Alibaba resta la base più adottata con la famiglia Qwen e l'anteprima dell'architettura Qwen4, DeepSeek vince sul prezzo per token con progetti come K2 Horizon che aprono dataset e codice.
- Fuori dalla Cina il quadro è più magro: [[muse-spark-1-3]] è chiuso e sta in vetta, la linea aperta di [[meta]] arranca e restano i modelli piccoli, dove [[gemma]] di [[google]] e Phi di [[microsoft]] tengono su hardware leggero.

## Caveat

L'indice misura una media di benchmark, non l'esperienza su un compito specifico: su un lavoro agentico complesso o su ragionamento lungo il migliore chiuso resta avanti e il ritardo può ancora contarsi in mesi. La vetta assoluta non è stata agganciata, ma la fascia sotto — dove si gioca la maggior parte del lavoro vero — è ormai contendibile da chiunque scarichi un file.

## Timeline delle notizie

- **2026-09-06** — L'indice di settembre misura 65,7 per [[fable-5-1]] e 59,7 per Kimi K3, il miglior modello a pesi aperti, settimo assoluto: il divario in vetta scende a 6 punti, dai 13 di dodici mesi prima.

## Collegamenti

- [[open-source]]
- [[deepseek-v4-pro]]
- [[kimi-k3]]
- [[index]]
