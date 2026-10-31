---
title: "Harness²"
category: strumento
tags: [google, agenti, ricerca, open-source, auto-miglioramento]
related_puntate: [20261018, 20261019, 20261020]
created: 2026-10-15
updated: 2026-10-20
---

# Harness²

## Introduzione

Strumento di Google Research che permette agli agenti di migliorare in modo iterativo prompt, strumenti, memoria e orchestrazione senza modificare i pesi del modello.

## Funzionalità principali

- Affina l'harness per ogni attività e porta avanti le lezioni sostenute da evidenze per migliorare le attività successive.
- Funziona su due livelli: sul singolo compito propone una variante "invariante" e una "di dominio", le prova sullo stesso lavoro e compone l'harness migliore (Propose, Probe, Compose); a fine compito conserva le modifiche adottate e le lezioni apprese in una libreria che orienta i compiti successivi.
- Le modifiche cadono su otto componenti, ciascuno un file nell'ambiente di esecuzione: prompt di sistema, guardrail, memoria, guida agli strumenti, sotto-agenti, skill, script e plugin.
- Con un solo passaggio migliora GLM-5 e Gemini 3.5 Flash su WorkBuddy-Bench, JobBench e LAB, con guadagni fino a 11,5 punti sul primo, 4,5 su JobBench e 11,8 su LAB; GLM-5 con l'harness migliorato arriva a 75,7 su WorkBuddy-Bench, sopra il 72,4 di Gemini 3.5 Flash con l'harness di serie.
- Il codice è su GitHub dal 6 ottobre 2026 con licenza Apache-2.0 e il paper su arXiv dal 9 ottobre; il README precisa che il progetto non è ufficialmente supportato da Google e che l'esecutore ha accesso alla rete senza restrizioni.

## Repository

- GitHub: https://github.com/google-research/harness2

## Azienda / Autore

- [[google]]

## Timeline delle notizie

- **2026-10-15** — TLDR AI segnala Harness², strumento di Google Research con cui gli agenti migliorano in modo iterativo prompt, strumenti, memoria e orchestrazione senza toccare i pesi del modello, affinando l'harness per ogni attività e portando avanti le lezioni sostenute da evidenze.
- **2026-10-18** — [[google]] ha rilasciato [[harness2|Harness²]], framework open source per agent ricorsivi in otto componenti — system prompt, guardrail, memoria, tool guidance, subagent, skill, script e plugin — pensato per i task per cui il sistema non era stato progettato.
- **2026-10-18** - Il framework di Google Cloud AI Research, su GitHub dal 6 ottobre con licenza Apache-2.0 e su arXiv dal 9 ottobre, migliora l'harness su due livelli: varianti invariante e di dominio provate sullo stesso compito e una libreria di esperienze per i compiti successivi. Con un solo passaggio guadagna fino a 11,5 punti su WorkBuddy-Bench, 4,5 su JobBench e 11,8 su LAB; il README precisa che non è un prodotto ufficialmente supportato da Google.



- **2026-10-19** — [[google]] ha rilasciato [[harness2|Harness²]], framework open source con licenza Apache che permette agli agenti di migliorare da soli la propria configurazione senza riaddestrare il modello: l'agente propone modifiche a sistema di prompt, tool e skill, le testa sulla stessa task, confronta i risultati e tiene solo ciò che funziona meglio, con ogni task completata che lascia una traccia per l'ottimizzazione successiva. Su benchmark reali come WorkBuddy e Harvey's LAB una sola iterazione basta per guadagnare undici punti.
- **2026-10-20** — Harness² viene integrato in JEV 1.14 senza toccare i pesi, con guadagni dichiarati sui benchmark di visione: riscrive i propri prompt, costruisce i propri tool e distilla la propria esperienza, e il repository dedicato è annunciato in arrivo.










## Collegamenti

- [[agenti-ai]]
- [[google]]
- [[index]]
