---
title: "Sakana AI"
category: azienda
tags: [sakana-ai, agent, coding, giappone, llm, research, ricerca, robotica, startup]
related_puntate: [20260623, 20260627, 20260704, 20260714, 20260722, 20260725, 20260727, 20260804, 20260915]
created: 2026-08-12
updated: 2026-10-13
---

# Sakana AI

## Introduzione

Laboratorio AI giapponese noto per l'ottimizzazione e la fusione di modelli (serie Fugu). Nel periodo ha aggiornato Fugu-Cyber a prestazioni da frontier sui benchmark di sicurezza e ha rilasciato Fugu-Ultra 1.1 con interfaccia compatibile con Claude Code.

## Modelli

- [[claude-mythos-5]]
- [[kimi-k2-6]]
- [[fable-5]]
- [[fugu-ultra]]
- [[namazu]]
- [[sakana-fugu]]

## Strumenti

- [[claude-code]]
- [[coffeebench]]

## Timeline delle notizie

- **2026-06-23** — Sakana AI ha rilasciato Sakana Fugu, un modello che orchestra altri modelli: Fugu Ultra raggiunge prestazioni simili a Claude Fable 5 e Mythos su benchmark complessi; dietro una sola API distribuisce task tra modelli specializzati, verifica risultati e restituisce una risposta unica.
- **2026-06-22** — Il laboratorio di Tokyo, fondato da Llion Jones (uno dei padri dell'architettura Transformer) e David Ha, lancia Sakana Fugu: un sistema multi-agente venduto come singolo modello, con due varianti (Fugu, veloce, e Fugu Ultra, per i problemi difficili) dietro una sola API compatibile con OpenAI. Sakana rivendica per Fugu Ultra prestazioni pari a Claude Fable 5 e Mythos di Anthropic senza averli nel proprio repertorio, e quindi senza il rischio degli export control americani.
- **2026-06-23** — Lancia Fugu orchestratore su pool Claude/GPT/Gemini con 73,7 SWE-Bench Pro.
- **2026-06-27** — Insieme a KPMG ha lanciato CoffeeBench, benchmark per valutare la gestione economica a lungo termine di agenti LLM, presentato all'ICML 2026 Workshop Failure Modes in Agentic AI.
- **2026-07-04** — Paper accettato a ICML 2026: Learning Multi-Agent Coordination via Sheaf-ADMM, framework per problem-solving collettivo. Multi-Agent Sudoku 93% di successo, Image Classification 86% su shift di dominio, Maze Pathfinding con canale comunicativo a 5 dimensioni, 8 volte più piccolo del baseline.
- **2026-07-14** — Sakana AI e IT University hanno pubblicato su Nature Communications uno studio su moduli fisici intelligenti: ogni modulo riconosce la propria forma e si ripara da solo, senza controllo centrale.
- **2026-07-22** — Ha aggiornato Fugu-Cyber: raggiunge prestazioni da frontier su benchmark reali, risultando confrontabile con GPT-5.5-Cyber e Mythos Preview.
- **2026-07-25** — Fugu-Ultra v1.1 è stato aggiornato con i modelli frontier più recenti: fino a 7,9 punti in più rispetto alla v1.0, allo stesso prezzo.
- **2026-07-27** — Ha rilasciato Fugu-Ultra 1.1 con interfaccia compatibile con Claude Code: invece di un singolo modello, orchestra un pool di modelli allo stato dell'arte direttamente dal terminale.
- **2026-08-04** — Sakana AI ha aperto l'API Namazu per il loro modello di linguaggio giapponese aggiornato.
- **2026-08-13** — Sakana Chat, la chat gratuita su chat.sakana.ai, impara a eseguire codice: il modello scrive ed esegue Python in una sandbox isolata e mostra il risultato (calcoli, grafici, pagine HTML, documenti Word, presentazioni e piccoli giochi) in un pannello a destra, alimentato da allegati PDF e file Office; Sakana Fugu debutta nella chat, gratuito ma con registrazione via email, e Sakana Namazu passa alla nuova generazione costruita sulla base aperta Kimi K2.6 di Moonshot AI. Il servizio resta chiuso a UE, SEE, Regno Unito e Svizzera per ragioni di GDPR.
- **2026-09-11** — Sakana AI rilancia l'orchestrazione con due modelli in un colpo: Fugu Ultra v2.0 e il low cost Fugu Max. Ultra v2 segna 48,3 su Chartography (contro 29,5 di Claude Fable 5 e 27,3 di Opus 5) e 74,3 su DeepSWE, e rivendica il primo posto su cinque prove su otto senza avere nel pool né GPT-6 Astra né i Claude Fable; Max porta nel pool la famiglia open weight Nemotron di [[nvidia]] e costa 2 dollari per milione di token in ingresso e 6 in uscita. Il servizio non è disponibile in UE e SEE e i pesi non vengono rilasciati.

- **2026-09-15** — Sakana AI presenta PC-ALM, alternativa alla retropropagazione basata su apprendimento locale: addestra reti neurali da mille strati usando solo dinamiche locali, senza backprop, e generalizza il predictive coding usando un Lagrangiano aumentato al posto dell'energia, permettendo di propagare segnali a profondità apparentemente arbitrarie.
- **2026-10-13** — Con ricercatori di Berkeley, Sakana AI presenta MASS, un metodo che usa il lavoro collettivo di più agenti come materiale di apprendimento per migliorare lo stesso modello, valutando i contributi e selezionando i migliori per l'addestramento successivo. Gli esperimenti mostrano progressi in alcuni benchmark di ricerca ma risultati meno uniformi fuori dai compiti esaminati, e il nodo resta capire se un modello possa valutare in modo affidabile il proprio miglioramento senza controlli esterni.




## Collegamenti

- [[claude-code]]
- [[claude-mythos-5]]
- [[coffeebench]]
- [[fable-5]]
- [[fugu-ultra]]
- [[kimi-k2-6]]
- [[kpmg]]
- [[nvidia]]
- [[namazu]]
- [[sakana-fugu]]
- [[index]]

