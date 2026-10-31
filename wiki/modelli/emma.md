---
title: "Emma"
category: modello
tags: [llm, italiano, open-weight, sovranita]
related_puntate: []
created: 2026-09-12
updated: 2026-10-14
---

# Emma

## Introduzione

Famiglia di modelli linguistici sviluppata da [[egomnia]], società quotata su Euronext Growth Milan e guidata dal fondatore Matteo Achilli. Il nome è dedicato alla figlia dello stesso Achilli e il posizionamento dichiarato è un'IA addestrata esclusivamente in italiano, ospitata in Italia e conforme a GDPR e AI Act. Nel 2026 la famiglia comprende quattro modelli, dei quali il più grande accessibile resta Emma-5.

## Capacità e performance

| Modello | Parametri | Dimensione | Note |
| --- | --- | --- | --- |
| Emma-3 | 125,3 M | 0,6 GB | toy model |
| Emma-4 | 317,1 M | 1,48 GB | chatbot leggeri |
| Emma-5 | 550,4 M | 2,46 GB | il modello "di punta" accessibile |
| Emma-6 | ~1,55 B | in addestramento | non ancora disponibile |

- Architettura transformer GPT decoder-only con Grouped-Query Attention, RoPE, RMSNorm e SwiGLU; finestra di contesto di 2.048 token, che la colloca su una scala molto diversa dai modelli di frontiera.
- Sul benchmark interno Vespucci (875 domande in italiano) Emma-5 dichiara il 57,8%; alla domanda su quante "r" contenga la parola "giallo" il modello ha risposto con una frase priva di senso, mentre Gemini ha risposto correttamente.
- I modelli sono definiti dal produttore come sperimentali e non pensati per competere con i modelli internazionali di fascia alta; il disclaimer esclude usi professionali, legali, medici e finanziari.

## Disponibilità

- Pesi scaricabili gratuitamente da [[hugging-face]] con licenza OpenRAIL-M; accesso Premium a un euro all'anno che rimuove i limiti della chat e dà priorità ai modelli maggiori, oltre a chiavi API aziendali su richiesta.
- La chat web gratuita su emma.egomnia.com permette di passare tra Emma-3, Emma-4 ed Emma-5 senza registrazione; l'app per iOS e Android è annunciata ma non disponibile.

## Rilasci e aggiornamenti

- 25 giugno 2026: Egomnia sospende la chat pubblica di Emma-5 dopo "oltre 60.000 chat", dichiarando che il rilascio aveva finalità esplorative e che l'utilizzo emerso non era in linea con gli obiettivi del test; l'azienda annuncia di cercare tester per Emma-6 e mette in vendita EmmaSFT 6.0, dataset di oltre 100.000 coppie domanda-risposta per il fine-tuning di Emma-6, gratuito per università e centri di ricerca non commerciali.
- 3 luglio 2026: dopo lo stop alla chat ufficiale, un progetto indipendente di terze parti (gli sviluppatori Arm4x e italianbldrs) rimette online Emma-5 su maremma.app a partire dai pesi distribuiti con licenza aperta, con parametri come temperatura, top-p e token massimi.

## Azienda di riferimento

- [[egomnia]]

## Timeline delle notizie

- **2026-06-24** — Il caso social di Emma-5: il modello da 550 milioni di parametri finisce al centro dei meme per risposte incoerenti e viene sospeso il giorno dopo, mentre il confronto serio sulla sovranità tecnologica italiana resta su altri progetti.
- **2026-10-12** — Emma-6 arriva in beta la sera del 12 ottobre con accesso controllato via email ai tester registrati, a differenza di Emma-5 aperta a chiunque in giugno: 1,55 miliardi di parametri contro i 550 milioni di Emma-5, contesto da 4.096 token, vocabolario 64.000, corpus di 100 GB (circa 25 miliardi di token) con 90.000 passi di pretraining contro i 200.000 precedenti, file ONNX da 6,26 GB e licenza OpenRAIL. Nei primi giorni le risposte errate diventano meme su X (la risposta su «1 è un numero primo», i galli che depongono uova) e il profilo ufficiale risponde in modo autoironico, ammettendo di essere «moooolto lontani dalla perfezione».




## Collegamenti

- [[egomnia]]
- [[hugging-face]]
- [[apertus]]
- [[open-source]]
- [[index]]
