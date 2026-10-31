---
title: "SkillOpt"
category: strumento
tags: [agent, microsoft, ottimizzazione, research, skill, training]
related_puntate: [20260526, 20260529, 20260618, 20260927]
created: 2026-08-12
updated: 2026-09-27
---

# SkillOpt

## Introduzione

Ottimizzatore che tratta la skill in linguaggio naturale come parametro trainabile esterno invece di fare fine-tuning dei pesi, con learning rate, schedule, mini-batch, epoch e momentum nello spazio testuale.

## Funzionalità principali

- SkillOpt è un ottimizzatore per skill di agenti: invece di fare fine-tuning dei pesi, tratta la skill in linguaggio naturale come parametro trainabile esterno, applicando learning rate, schedule, mini-batch, epoch e momentum nello spazio testuale, con edit controllati e aggiornamenti stabili; testato su 6 benchmark e 7 modelli, best o tied-best in 52 configurazioni su 52.
- SkillOpt di Microsoft addestra le skill degli agenti come reti neurali: il file markdown diventa il parametro addestrabile con learning rate, validation gate, batch size ed epoch, stessa disciplina dell'addestramento dei pesi; il modello resta frozen e la skill si evolve.
- SkillOpt di Microsoft ottimizza i documenti skill degli agenti come se fossero reti neurali: epoca, batch e learning rate applicati alla documentazione, con miglioramenti di ventitré punto cinque punti su GPT cinque punto cinque e senza toccare i pesi del modello.

## Azienda / Autore

- [[microsoft]]

## Modelli supportati / correlati

- [[gpt-5-5-pro]]

## Timeline delle notizie

- **2026-05-26** — SkillOpt è un ottimizzatore per skill di agenti: invece di fare fine-tuning dei pesi, tratta la skill in linguaggio naturale come parametro trainabile esterno, applicando learning rate, schedule, mini-batch, epoch e momentum nello spazio testuale, con edit controllati e aggiornamenti stabili; testato su 6 benchmark e 7 modelli, best o tied-best in 52 configurazioni su 52.
- **2026-05-29** — SkillOpt di Microsoft addestra le skill degli agenti come reti neurali: il file markdown diventa il parametro addestrabile con learning rate, validation gate, batch size ed epoch, stessa disciplina dell'addestramento dei pesi; il modello resta frozen e la skill si evolve.
- **2026-06-18** — SkillOpt di Microsoft ottimizza i documenti skill degli agenti come se fossero reti neurali: epoca, batch e learning rate applicati alla documentazione, con miglioramenti di ventitré punto cinque punti su GPT cinque punto cinque e senza toccare i pesi del modello.
- **2026-09-27** — Il modello base esegue il task, un optimizer valuta l'output e riscrive le istruzioni da solo: separa i percorsi di successo dai fallimenti, scarta ogni modifica che non supera il benchmark definito e batte prompt scritti a mano e altri optimizer. Le competenze così sviluppate si trasferiscono tra modelli diversi senza lock-in.

## Collegamenti

- [[gpt-5-5-pro]]
- [[microsoft]]
- [[index]]

