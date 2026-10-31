---
title: "Claude Sonnet 5.5"
category: modello
tags: [anthropic, contesto-lungo, llm, long-context]
related_puntate: [20260805, 20260810, 20260929, 20261004, 20261009, 20261017]
created: 2026-08-12
updated: 2026-10-22
---

# Claude Sonnet 5.5

## Introduzione

Modello Sonnet di Anthropic rilasciato il 28 settembre 2026, secondo della famiglia Claude 5.5 dopo Opus 5.5: oltre il trenta percento più veloce e fino al trenta percento più economico per attività rispetto a Sonnet 5 a parità di listino, con contesto da un milione di token e prestazioni di coding agentico vicine a Opus 5.5.

## Capacità e performance

- Coding agentico e uso del computer: 70,6 per cento su Terminal-Bench 4.0, dove supera il 66,4 di Opus 5.5, 1844 su GDPval-AA v2.1 e 80,1 per cento su OSWorld 2.1, restano pochi punti sotto il fratello maggiore su ogni altra misura.
- Primo modello della linea Sonnet a lanciare con le salvaguardie informatiche di Opus 5.5: classificatori dedicati, fallback automatico verso Sonnet 5 sulle richieste ad alto rischio, protezioni contro l'estrazione del ragionamento e un meccanismo che lega il ragionamento generato all'account che lo ha prodotto.

## Azienda di riferimento

- [[anthropic]]

## Timeline delle notizie

- **2026-08-05** — Secondo le indiscrezioni Claude Sonnet cinque punto cinque potrebbe arrivare il mese prossimo: fase finale prima del rilascio, risposte piu' rapide, latenza ridotta, finestra context di uno virgola cinque milioni di token, capacita' vicine a Fable 5 a prezzo da Sonnet.
- **2026-08-10** — Secondo le indiscrezioni Claude Sonnet cinque punto cinque (codename Fennec) arriva il mese prossimo: due milioni di token di contesto, ragionamento long-context piu' forte, pianificazione multi-step, inferenza piu' veloce, tool use potenziato (browser, terminali, strumenti esterni) e prestazioni quasi a livello Fable 5 ma a prezzo Sonnet.

- **2026-09-27** — Un account pseudonimo su X (@lyraxana) sostiene che Anthropic abbia fatto girare tra i partner un secondo checkpoint di Sonnet 5.5, "migliore del primo", con rilascio previsto la settimana successiva; un secondo account non verificato aggiunge che il modello sarebbe in grey testing dentro [[claude-code]] e ipotizza il lancio il 30 settembre. Le quattro specifiche citate a sostegno (contesto da un milione di token, output da 128.000, 2 e 10 dollari per milione di token) sono quelle gia' pubbliche di [[claude-sonnet-5]], quindi non provano un modello nuovo, e Anthropic non ha mai nominato un "Sonnet 5.5".
- **2026-09-28** — Anthropic rilascia Claude Sonnet 5.5 (ID API claude-sonnet-5-5) al prezzo invariato di 2 dollari per milione di token in ingresso e 10 in uscita, con cache read a 0,20 e cache write a 2,50: genera output oltre il trenta percento più veloce e riduce fino al trenta percento il costo per attività non per uno sconto, ma perché usa meno chiamate agli strumenti e meno token per lo stesso risultato.
- **2026-09-28** — Su Terminal-Bench 4.0, il benchmark del coding agentico, il modello segna 70,6 per cento contro il 10,3 di Sonnet 5 e il 66,4 di Opus 5.5; su GDPval-AA v2.1 arriva a 1844 (Sonnet 5: 1449, Opus 5.5: 1846), su OSWorld 2.1 a 80,1 per cento e su Chartography a 61,6 per cento, restando pochi punti sotto Opus 5.5 su ogni misura tranne il coding agentico.
- **2026-09-28** — È il primo Sonnet con le salvaguardie informatiche di Opus 5.5 (classificatori dedicati e fallback automatico verso Sonnet 5 sulle richieste ad alto rischio), più due misure nuove per la linea: protezioni contro l'estrazione del ragionamento e un meccanismo che lega il ragionamento all'account che lo ha prodotto.
- **2026-09-28** — Disponibile su Claude Platform, Amazon Bedrock, Google Cloud Vertex AI e Microsoft Foundry con opzione di zero data retention, contesto da un milione di token, output massimo di 128.000 token per chiamata (300.000 in batch) e cutoff dei dati di addestramento a gennaio 2026; i clienti citati misurano il risparmio in chiamate e token (Box 2,4 volte più veloce con il 12 per cento di token in meno, Slack il 14 per cento di token in uscita in meno, Lovable un terzo in meno di chiamate agli strumenti, Zendesk ticket processati il 20 per cento più velocemente, Base44 iterazioni per progetto scese da 7,7 a 3,6). Il ciclo si è chiuso in ventiquattro ore, dal leak del 27 settembre al lancio confermato del 28, con le API di Anthropic che arrivano anche su un Nokia 6300 del 2007 tramite un client Java non ufficiale.
- **2026-09-29** — Anthropic rilascia Claude Sonnet 5.5, oltre il trenta percento più veloce di Sonnet 5 e fino al trenta percento più economico per attività: l'upgrade è netto per chi lo ha testato e la famiglia Claude 5.5 conta ora due modelli. A listino invariato consuma meno token, da cui il risparmio, ed è più forte su coding, compiti a lungo orizzonte e comprensione delle immagini.
- **2026-10-03** — Claude Sonnet 5.5 arriva nel selettore dei modelli di [[antigravity]] insieme a Opus 5.5, secondo le prime segnalazioni del 3 ottobre 2026 e con accesso riservato agli abbonati Google AI Pro e Ultra a pagamento; Anthropic lo presenta come il modello che tiene insieme velocità e intelligenza e conviene sui compiti circoscritti e ripetitivi come correzione di bug, modifiche mirate e documenti. Il 2 novembre 2026 Antigravity rimuove Claude Sonnet 4.6 e GPT-OSS-120B.
- **2026-10-04** — Nella guida di Anthropic ai team di agenti in Claude Code gli sviluppatori sono Sonnet 5.5, su branch separati.
- **2026-10-09** — Su DeepSWE vietare a Sonnet 5.5 high di scrivere test in autonomia ha prodotto tassi di successo leggermente superiori e meno tempo e token spesi: il 65 per cento dei test erano unit test e il 35 per cento integration test, e nessuno dei due ha migliorato i risultati.

- **2026-10-09** — [[anthropic]] dimezza il prezzo delle letture dalla cache di Sonnet 5.5, che ora costa circa il 20 per cento in meno sulla maggior parte del lavoro agentico.
- **2026-10-09** — Sonnet 5.5, uscito il 28 settembre, costa 2 dollari per milione di token in ingresso e 10 in uscita, le stesse cifre di GPT-6.1 Sol, e Anthropic ha dimezzato il prezzo di lettura della cache: con i listini allineati il confronto si sposta su cache e token consumati per compito.
- **2026-10-17** — Nel framework robotico [[nvidia-aspire|ASPIRE]] 1.0 di NVIDIA, Sonnet 5.5 è indicato come il modello con il miglior rapporto costo-capacità, a dodici dollari per task.
- **2026-10-22** — In un audit indipendente di Terminal-Bench 4, dopo la correzione di alcune prove e il blocco del reward hacking, il modello passa dal 62,8 all'89,2 per cento di tentativi riusciti: il dato vale per l'insieme ristretto di esercizi rielaborati da Preference Model, non come misura generale del coding.



















## Collegamenti

- [[anthropic]]
- [[index]]

