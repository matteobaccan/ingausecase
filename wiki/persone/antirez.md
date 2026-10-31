---
title: "antirez"
category: persona
tags: [developer, europa, open-source]
related_puntate: [20260629]
created: 2026-08-12
updated: 2026-10-15
---

# antirez

## Introduzione

Salvatore Sanfilippo, creatore di Redis e sviluppatore di punta nel mondo open source, attivo su test di modelli LLM su hardware Apple.

## Carriera e contributi

- Ha fatto girare GLM 5.2 su M5 Max con 128 GB usando SSD streaming, con parametri quantizzati a circa 2,6 bit.
- Ha pubblicato il 6 maggio 2026 DS4 (DwarfStar4), motore di inferenza specializzato per DeepSeek V4 Flash con licenza MIT: scelta controcorrente rispetto ai runtime generalisti, ottimizzata a mano per l'architettura sparsa del modello e portata su Metal, CUDA e ROCm.
- Nel README di DS4 dichiara l'assistenza di GPT-5.5, GPT-5.6 e Claude Fable nello sviluppo, pur restando lui a guidare design e collaudo.

## Affiliazioni

- [[zhipu-ai]]

## Timeline delle notizie

- **2026-04-28** — Salvatore Sanfilippo porta in Redis, con la pull request #15162, il tipo Array e il comando ARGREP: una struttura nativa che unifica memoria breve, cache e knowledge graph testuale in un solo backbone in RAM, segnalata come il tassello mancante per le architetture di memoria degli agenti.

- **2026-09-10** — Pubblica sette punti contro la tesi del saldo negativo di [[terence-tao]] per la matematica: una dimostrazione resta un oggetto studiabile e non un oracolo, per Fermat e Poincaré nacquero tecniche nuove, la comunità mantiene tutti gli strumenti di ieri più le nuove prove e un'IA ha già fatto cadere una congettura di Erdős del 1946. Il primo post supera le 76.000 visualizzazioni in ventiquattro ore.
- **2026-08-26** — Commenta il lancio del Mac Studio M5 Ultra ribaltando la prospettiva del marketing: il valore della macchina non è la somma delle specifiche, ma quante sessioni parallele regge con GLM 5.3, e il discrimine è il batching, perché un singolo utente lascia buona parte della macchina inattiva. Su Apple Silicon MLX non regge il confronto con [[vllm]] sul batching, ed è il buco che [[ds4]] prova a colmare preassegnando sessioni residenti indipendenti e valutando insieme i passi di decodifica pronti. Sul tetto a 512 GB senza opzione da 1 TB è netto: montare più memoria per far entrare un modello di classe [[kimi-k3]] sarebbe inutile, perché il rapporto tra calcolo e banda non regge quei carichi.
- **2026-09-01** — Mostra [[deepseek-v4-flash]] con la visione in locale su un Mac M5 Max e annuncia il supporto Metal, CUDA e ROCm di [[ds4]] in uscita nel giro di ore.
- **2026-05-09** — Pubblica su GitHub DS4, il motore di inferenza in C e Metal dedicato a un solo modello su una sola classe di macchine: il 7 maggio esce con backend Metal-only per Apple Silicon, quantizzazione asimmetrica a 2 bit sugli esperti instradati, cache KV su disco e server compatibile OpenAI e Anthropic, e l'11 maggio arriva il refactoring con backend CUDA per il DGX Spark e il single-direction activation steering. Nel README dichiara lo sviluppo "con forte assistenza di GPT-5.5" e chiude con "se non accetti codice sviluppato con assistenza AI, questo software non fa per te".
- **2026-06-29** — Ha fatto girare GLM 5.2 su M5 Max con 128 GB usando SSD streaming, con parametri quantizzati a circa 2,6 bit.

- **2026-09-11** — Il rilascio di [[deepseek-v4-1-flash]] mette [[ds4]] in prima fila per l'inferenza locale: il motore è la porta d'ingresso per chi vuole provare il modello senza data center, la issue numero 1023 segnala i pesi disponibili e il porting è in lavorazione.
- **2026-09-13** — Nel confronto tra i motori a streaming da disco [[ds4]] viene sorpassato in stelle da [[colibri]] (22.318 contro 28.756): quando su Hacker News molti accostano i due lavori, l'autore di Colibrì gli riconosce il debito con un secco "Antirez is the number one!". La voce di [[ai-locale]] registra anche il consiglio d'acquisto: chi ha un Mac di fascia alta con 96 GB o più trova in ds4 il motore nato per Metal.
- **2026-10-15** — Sanfilippo pubblica c64-hw-sim, simulatore a livello di piedino della scheda madre del Commodore 64 (revisione PAL ASSY 250407) costruito dalla netlist di una replica KiCad, con 216 componenti e 249 reti: i core a ciclo esatto di CPU 6510, VIC-II, CIA e SID vengono dagli emulatori di chip di Andre Weissflog, mentre il lavoro nuovo sta nei modelli a livello di piedino di RAM, ROM, PLA e logica di contorno e nelle regole elettriche che li legano alla scheda, con soglie e costanti dichiarate come stime. Un piedino si può mettere a massa, a +5 volt o lasciare flottante, un chip si può estrarre dallo zoccolo e lo script tests/faults.sh lancia 31 guasti comuni di cui il simulatore non conosce i sintomi attesi, perché li deriva dal circuito; la simulazione gira però al 31 per cento della velocità reale di un C64 su Apple M3 Max e al 48 per cento su M5 Max, quindi non serve a giocare. Il repository ha un solo commit, del 14 ottobre 2026, e GitHub non vi rileva una licenza; nel PLAN.md l'obiettivo dichiarato è rendere tutto pilotabile dal protocollo socket già usato per gli agenti LLM, così che un agente possa lavorare su un «C64 rotto in ingresso, diagnosi in uscita».




## Collegamenti

- [[ai-locale]]
- [[deepseek-v4-flash]]
- [[ds4]]
- [[glm-5-2]]
- [[matematica-ai]]
- [[terence-tao]]
- [[zhipu-ai]]
- [[index]]

