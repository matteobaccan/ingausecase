---
title: "Crittografia e IA"
category: trend
tags: [crittografia, sicurezza, ai-safety, matematica]
created: 2026-10-09
updated: 2026-10-18
---

# Crittografia e IA

## Introduzione

Il filone che collega i progressi della matematica fatti con l'intelligenza artificiale alla tenuta della crittografia a chiave pubblica. Il 7 ottobre 2026 Justin Drake, ricercatore della Ethereum Foundation, ha chiesto di pianificare la \u201cbunker mode\u201d, cioè lo spostamento dei fondi verso indirizzi che non hanno mai firmato una transazione, perché l'IA potrebbe rompere ECDSA (la firma digitale di Bitcoin ed Ethereum) prima dei computer quantistici, nel caso peggiore \u201cin months not years\u201d.

## Timeline delle notizie

- **2026-10-09** — Drake motiva la bunker mode con il rilascio da parte di [[openai]] del repository `openai/math`, una raccolta di risultati matematici prodotti da un modello interno non ancora pubblicato: sui Bitcoin e su Ethereum l'indirizzo è l'hash della chiave pubblica, quindi la chiave resta nascosta finché il portafoglio non firma la prima transazione, e un indirizzo mai usato per firmare resterebbe fuori portata se ECDSA cadesse. Drake invita exchange e custodi (Binance, Bitbank, Robinhood, Bitfinex, Tether) a rafforzare la custodia a freddo.
- **2026-10-09** — Vitalik Buterin frena: non raccomanda a nessuno di correre a spostare i fondi, ma considera sensata la raccomandazione degli indirizzi nuovi e ritiene che l'area di rischio inedita siano ML-DSA, la crittografia omomorfica e i reticoli, con una buona probabilità che la loro sicurezza subisca colpi seri dai prossimi due anni di matematica fatta dall'IA. Nessuna fonte riporta un attacco pratico alle firme di Bitcoin o Ethereum e lo stesso Drake presenta la sua come una raccomandazione personale.
- **2026-10-17** — Il circuito quantistico di Claude Mythos 5 per la somma di punti su curva ellittica usa il 12% di qubit in più (935 contro 838) e 17 volte meno porte del progetto più piccolo pubblicato (4,0 milioni di Toffoli contro 70 milioni), e i parametri della curva del test (y² = x³ + 7 sul primo 2²⁵⁶ − 2³² − 977) coincidono con quelli di secp256k1, la curva delle firme di Bitcoin ed Ethereum, anche se né Anthropic né il paper la nominano. Il circuito riduce il costo di un passo, non cambia l'hardware, e i computer quantistici costruiti finora contano da centinaia a poche migliaia di qubit.

- **2026-10-17** — Chiude il mistero dei seed delle curve NIST: secondo [[anthropic]] i numeri consegnati dall'NSA per P-192, P-224, P-256, P-384 e P-521 non derivano dall'hash di una frase ma da lrand48 avviato dall'orologio del computer, con timestamp ricostruiti tra il 18 maggio 1997 e il 3 aprile 1998, e lo stesso schema vale per cinque seed dello standard ANSI X9.62 e per i punti base di sei curve del 1997 presi dal generatore di FreeLIP di Arjen Lenstra. Restano inspiegati il seed di B-163 e i punti base di P-224, P-256, P-384 e P-521, e la conclusione «nessuna backdoor» è un'inferenza e non una dimostrazione.




## Collegamenti

- [[openai]]
- [[sicurezza-ai]]
- [[matematica-ai]]
- [[index]]
