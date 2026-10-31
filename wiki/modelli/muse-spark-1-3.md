---
title: "Muse Spark 1.3"
category: modello
tags: [agent, coding, llm, meta, lavoro-agente]
related_puntate: [20260903, 20260909, 20261016]
created: 2026-09-03
updated: 2026-10-16
---

# Muse Spark 1.3

## Introduzione

Terzo modello della famiglia di Meta per il coding e il lavoro agentico, rilasciato il 2 settembre 2026 e annunciato da Mark Zuckerberg su X come il progresso più grande mai fatto dall'azienda su coding e agenti. Non è un modello da chat generalista come i vecchi Llama ma un motore cucito addosso allo sviluppo software, in diretta concorrenza con [[claude-code]] e [[codex]].

Il numero che racconta il salto non è un punteggio ma un consumo: la 1.3 chiude gli stessi compiti della 1.2 con circa il 25% di token in meno e il 20% di chiamate agli strumenti in meno, e per chi paga a consumo il costo per task finito pesa più del prezzo unitario del token.

## Capacità e performance

| Benchmark | Muse Spark 1.3 | Muse Spark 1.2 | Rivale di riferimento |
| --- | --- | --- | --- |
| Terminal-Bench 2.1 (coding da CLI) | 88,8 | 82,9 | GPT-5.6: 88,8 |
| DeepSWE v1.1 (issue su repo reali) | 75,4 | 59,3 | - |
| MRCR 512K-1M (contesto lungo) | 98,1 | - | - |
| DeepSearchQA (ricerca) | 89,4 | - | GPT-5.6: 93,0 |
| Agentic IF Index | 57,8 | - | GPT-5.6: 60,5 |
| GDPVal-AA v2 | 1754 | - | Opus 5: 1824 |

- Il vantaggio resta concentrato sul codice: su DeepSWE v1.1 il salto è di sedici punti in un mese, su Terminal-Bench 2.1 la 1.3 pareggia GPT-5.6 e sul contesto lungo arriva a 98,5 nel recupero di informazioni tra 256mila e 512mila token.
- I margini degli altri restano: GPT-5.6 conserva il primato su ricerca web (93,0 contro 89,4) e sull'aderenza alle istruzioni agentiche, [[claude-opus-5]] su GDPVal, il benchmark che simula compiti lavorativi complessi.

## Listino

| Modello | Input / milione token | Output / milione token |
| --- | --- | --- |
| Muse Spark 1.3 | 1,25 $ | 4,25 $ |
| GPT-5.6 (OpenAI) | 2,00 $ | 12,00 $ |
| Claude Opus 5 (Anthropic) | 5,00 $ | 25,00 $ |

- La 1.3 non ha un listino proprio: gira allo stesso prezzo della 1.2, con la fascia contributor a 0,10 e 0,20 dollari in cambio del permesso di usare i propri dati per addestrare i modelli futuri. Un token in uscita di [[claude-opus-5]] costa quasi sei volte uno di Muse Spark.

## Disponibilità

- Il modello è in distribuzione dentro [[muse-code]], l'agente da terminale uscito dalla beta a settembre, e tramite la Meta Model API.
- Zuckerberg ha promesso una prossima release **open weights** di Muse Spark, anticipata con l'emoji dell'anguria come ormai d'uso nell'ambiente, senza data: aprire i pesi del modello grande (non della versione ridotta [[muse-glimmer]]) metterebbe in mano agli sviluppatori il motore che alimenta l'API a pagamento.
- In arrivo anche modelli più grandi e una modalità di ragionamento spinto, la max reasoning, che uscirà dopo i test di sicurezza.

## Azienda di riferimento

- [[meta]]

## Strumenti correlati

- [[muse-code]]
- [[muse]]

## Timeline delle notizie

- **2026-09-02** — Zuckerberg annuncia su X Muse Spark 1.3 come il salto più grande dell'azienda sul coding e l'agentico: 75,4 su DeepSWE v1.1 contro 59,3 della 1.2, 88,8 su Terminal-Bench 2.1, 25% di token e 20% di chiamate agli strumenti in meno, stesso listino della famiglia (1,25 e 4,25 dollari) e promessa di pesi aperti per il modello grande. In parallelo Meta porta l'agente personale [[muse]] a tutti gli utenti.
- **2026-09-03** — Meta ha rilasciato Muse Spark 1.3 con un salto importante su coding e lavoro agente, disponibile in Muse Code e via API, in arrivo le versioni open weights.
- **2026-09-09** — Muse Spark 1.3 alimenta [[muse]], l'agente personale di Meta disponibile nell'app dedicata.
- **2026-10-16** — Muse Spark Open da 816 miliardi di parametri totali e 42 attivi, con contesto da un milione di token e multimodalità nativa su testo, immagini, video e audio. [[meta]] lo definisce il modello open-weight più capace mai rilasciato dagli USA, costruito per coding e lavoro agente.




## Collegamenti

- [[meta]]
- [[muse]]
- [[muse-code]]
- [[muse-glimmer]]
- [[muse-spark-1-2]]
- [[claude-opus-5]]
- [[codex]]
- [[open-source]]
- [[index]]
