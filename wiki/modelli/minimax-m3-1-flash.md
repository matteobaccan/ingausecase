---
title: "MiniMax M3.1 Flash"
category: modello
tags: [cina, coding, agenti, contesto-lungo, multimodale, open-weight]
related_puntate: [20261020]
created: 2026-10-19
updated: 2026-10-23
sources: [raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md, raw/puntate/ainews20261020.md, raw/tldr/tldr20261020.md, raw/pillitteri/pillitteri20261023-minimax-m3-1-flash-pesi-hugging-face-licenza.md]
---

# MiniMax M3.1 Flash

## Introduzione

Modello multimodale di [[minimax]] per la programmazione e i compiti da agente, lanciato il 19 ottobre 2026 dopo un'anteprima iniziata a fine settembre. Ha una finestra di contesto da un milione di token e accetta in ingresso testo, immagini e video, rispondendo con testo. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]

## Capacità e performance

- Il livello di ragionamento è regolabile con cinque valori - low, medium, high, xhigh e max - e il pensiero non si può spegnere; max è l'impostazione di partenza. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- MiniMax dichiara Automation-Bench al 62% e ALE al 30% per i compiti da collega digitale, DeepSWE al 74% per la programmazione e BabyVision al 91% per il ragionamento visivo; sono tutti numeri dell'azienda, non misure di terzi. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- Space Bunny, il modello anonimo che circolava da settimane, era una versione precedente di M3.1 Flash: era comparso il 23 settembre su OpenRouter e OpenCode con contesto da un milione di token e, secondo MiniMax, ha guidato le classifiche globali con oltre 200 trilioni di token elaborati. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]

## Prezzi

- Tariffa unica di 0,15 dollari per milione di token in ingresso e 0,60 in uscita, con lettura dalla cache a 0,015 dollari per milione. Non ci sono scaglioni legati alla lunghezza del contesto. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- M3 costa 0,30 e 1,20 dollari fino a 512.000 token di ingresso e raddoppia oltre quella soglia: a parità di token M3.1 Flash costa la metà sotto i 512.000 token e un quarto sopra. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- È disponibile via API a consumo, con l'abbonamento M Plan e dentro MiniMax Code per desktop; l'endpoint compatibile con Anthropic è https://api.minimax.io/anthropic, quello in formato OpenAI https://api.minimax.io/v1, con identificativo MiniMax-M3.1-Flash. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]

## Pesi e limiti

- I pesi sono annunciati per il 23 ottobre 2026 senza licenza, dimensioni o formato; fino a quella data resta una promessa. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- Il "terzo del costo di M3" e la velocità tripla dichiarati da MiniMax non hanno un metodo di calcolo esplicito, e il risparmio reale dipende dai token consumati per compito. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- Le prove indipendenti disponibili riguardano l'anteprima e singole sessioni: in un test con M-Code il modello ha prodotto un JSON valido per le decisioni di un drone con un errore sulla posizione del cavo, mentre un test cinese riporta un'uscita stabile intorno ai 100 token al secondo ma una tendenza a ragionare a lungo anche su domande semplici. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]

## Azienda di riferimento

- [[minimax]]

## Modelli correlati

- [[minimax-m3]]

## Timeline delle notizie

- **2026-09-23** - "Space Bunny Alpha" compare su OpenRouter e su OpenCode, gratuito durante l'anteprima e con contesto da un milione di token; il 24 settembre un ricercatore indipendente nota che i conteggi dei token coincidono con quelli dei modelli MiniMax. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
- **2026-10-19** - MiniMax lancia M3.1 Flash a 0,15 dollari per milione di token in ingresso e 0,60 in uscita, con cache a 0,015, contesto da un milione di token e pesi annunciati per il 23 ottobre; l'azienda conferma che Space Bunny era una versione precedente del modello e dichiara risultati su Automation-Bench, ALE, DeepSWE e BabyVision. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md] TLDR AI aggiunge che l'inferenza online è quasi tre volte più veloce e i costi d'uso calano del 70%, e che i pesi saranno rilasciati in un secondo momento. [Fonte: raw/tldr/tldr20261020.md]
- **2026-10-23** — I pesi arrivano su Hugging Face come promesso il 19 ottobre: repository pubblico senza richiesta di accesso, 72 file per 252,4 GB, 428 miliardi di parametri totali e 23 attivi per token, ingresso multimodale con testo, immagini e video e uscita solo testo. Rispetto a M3, che occupava 854 GB, la dimensione scende a un terzo grazie alla quantizzazione durante l'addestramento, all'attenzione sparsa nei primi tre strati e alla decodifica speculativa DSpark. [Fonte: raw/pillitteri/pillitteri20261023-minimax-m3-1-flash-pesi-hugging-face-licenza.md]

- **2026-10-23** — La licenza MiniMax Community non è open source: l'uso non commerciale è gratuito, quello commerciale richiede la dicitura «Built with MiniMax M3.1-Flash» e una notifica a MiniMax, con autorizzazione scritta oltre i 20 milioni di dollari di ricavi annui. Per farlo girare in locale la ricetta ufficiale chiede otto GPU Hopper oppure quattro Blackwell o quattro AMD MI355X, con vLLM 0.33.0 o successivo e blocchi da 128. [Fonte: raw/pillitteri/pillitteri20261023-minimax-m3-1-flash-pesi-hugging-face-licenza.md]




## Collegamenti

- [[minimax]]
- [[minimax-m3]]
- [[deepseek-v4-1-flash]]
- [[index]]
