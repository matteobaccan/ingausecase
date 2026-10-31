---
title: "TypeSafe AI"
category: azienda
tags: [agent, decisioni, inferenza, san-francisco, startup, usa]
related_puntate: [20260918, 20261016]
created: 2026-09-16
updated: 2026-10-20
---

# TypeSafe AI

## Introduzione

Startup di San Francisco che sviluppa modelli di intelligenza artificiale pensati per le macchine e non per il dialogo con una persona: il 16 settembre 2026 ha lanciato in accesso anticipato [[jev]], un modello che non genera testo e restituisce soltanto decisioni tipizzate accompagnate da una probabilità di confidenza. TypeSafe lo presenta come il primo "System One Model", per contrasto con i modelli linguistici di grandi dimensioni che lavorano come il Sistema 2 di Kahneman, quello lento e ragionato.

## Modelli

- [[jev]]

## Annunci recenti

- Il 16 settembre 2026 l'azienda annuncia in contemporanea il lancio in early access di Jev e un round seed da 40 milioni di dollari guidato da DCVC, destinato ad allargare operazioni e sviluppo.

## Persone chiave

- Diogo Almeida, amministratore delegato, con un passato in [[openai]] sui metodi di instruction-following che hanno reso ChatGPT capace di seguire le istruzioni.
- Erik Gafni, responsabile tecnico, e Sasha Sheng alle operazioni.

## Timeline delle notizie

- **2026-09-16** — TypeSafe AI esce dalla modalità stealth con un posizionamento dichiarato senza giri di parole, modelli AI nativi per le macchine e componibili, pensati per l'automazione più che per la conversazione. Il mercato di riferimento è quello degli agenti che devono decidere in fretta e parlarsi fra loro, lo stesso strato descritto dai cinque livelli dell'AI di [[openai]], dove il Livello 5 è l'organizzazione autonoma: la scommessa della startup è sul gradino di sotto, quello che tiene insieme la macchina, con la verifica e i guardrail sopra gli LLM indicati come uno dei casi d'uso principali.
- **2026-09-18** — Jev fa scelte discrete in millisecondi invece di generare testo: latenza mediana di duecentocinquantasei millisecondi per classificare mille paper al costo di otto centesimi, e un browser agent basato su Jev che ha cercato voli in sette secondi per meno di un centesimo.
- **2026-09-29** — OpenAI risponde a Jev con la Decisions API due settimane dopo il lancio: TypeSafe arriva dopo con una categoria consolidata (cloni open source su RTX 3090, CLM-8B di Stanford e NVIDIA nove volte più veloce), e i test indipendenti temperano i numeri del lancio (81,9% di media su undici compiti per Jev contro 80% del miglior open); restano i limiti ammessi su numeri e date, il prompt injection documentato da Check Point e il vantaggio della calibrazione RLCD che la Decisions API non dichiara.
- **2026-10-15** — Rilascia Jev 1.14.0, con supporto alle immagini, un nuovo tipo e contesto più lungo; la multimodalità è stata attivata anche su Jev 1.13.0 e il nuovo tipo box restituisce un singolo bounding box, come esplorazione dei System One Models oltre le decisioni semplici.
- **2026-10-16** — [[jev]] 1.14 esce con immagini sperimentali, tipo box e contesto più lungo: le capacità visive lasciano la preview in zona pericolosa, da usare con cautela. L'articolo di Pillitteri del 20 ottobre precisa il meccanismo: le immagini passano solo con l'header TypeSafe-Danger-Zone-Images e una mappa assets, ogni file è un PNG o JPEG da 16 MiB con lati tra 280 e 1.568 pixel, una domanda Box restituisce sempre un riquadro anche quando l'oggetto non c'è e va affiancata a una domanda Noul di controllo, il costo resta 0,042 dollari per milione di token di input e il contesto predefinito è di 64.000 token, estendibile a 262.000 con un secondo header.










## Collegamenti

- [[agenti-ai]]
- [[claude]]
- [[jev]]
- [[openai]]
- [[index]]
