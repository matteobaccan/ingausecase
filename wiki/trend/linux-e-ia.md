---
title: "Linux e IA nel 2026: le regole di kernel e distribuzioni"
category: trend
tags: [linux, open-source, ia, kernel, governance]
related_puntate: []
created: 2026-09-21
updated: 2026-10-24
sources: [raw/pillitteri/pillitteri20260921-linux-e-ia-2026-cosa-hanno-deciso-kernel-distribuzioni.md, raw/pillitteri/pillitteri20260921-linux-ai-os-1-0-star-distro-ia-locale.md, raw/pillitteri/pillitteri20261012-torvalds-claude-code-kernel-linux.md, raw/pillitteri/pillitteri20261018-torvalds-regole-anti-ai-assisted-by-kernel-linux.md, raw/pillitteri/pillitteri20261024-linux-day-2026-eventi-programma-dirette.md]
---

# Linux e IA nel 2026: le regole di kernel e distribuzioni

## Introduzione

Nel 2026 il mondo Linux ha smesso di chiedersi se ammettere l'intelligenza artificiale e ha cominciato a scrivere le regole: il kernel vuole che a firmare una patch sia sempre una persona e prevede un tag per dichiarare l'aiuto della macchina, Debian ha votato per l'uso responsabile dell'IA generativa, Gentoo la vieta da più di due anni, mentre le segnalazioni di bug prodotte dall'IA sommergono i manutentori. [Fonte: raw/pillitteri/pillitteri20260921-linux-e-ia-2026-cosa-hanno-deciso-kernel-distribuzioni.md]

## Attori coinvolti

- Kernel Linux, con il file coding-assistants.rst e la sezione "Responsible use of AI to find bugs" di security-bugs.rst.
- Debian, che ha votato per l'uso responsabile dell'IA generativa, e Gentoo, che la vieta.
- Le distribuzioni che invece mettono l'IA dentro il desktop, come [[linux-ai-os]].

## Timeline delle notizie

- **2026-09-21** — Dal 23 dicembre 2025 la documentazione del kernel, nel file coding-assistants.rst con un commit di Sasha Levin, vieta all'assistente IA di aggiungere una riga Signed-off-by, perché solo una persona può certificare l'origine di una patch: l'aiuto ricevuto si dichiara con il tag Assisted-by, come stabilito dal consenso raggiunto al Maintainers Summit 2025. Il formato del tag è già cambiato una volta, perché il 1° luglio 2026 un commit di Christian Brauner l'ha ridotto a "Assisted-by: LLM [TOOL...]" senza più il nome del modello, con la motivazione che citarlo sarebbe pubblicità gratuita per aziende proprietarie. [Fonte: raw/pillitteri/pillitteri20260921-linux-e-ia-2026-cosa-hanno-deciso-kernel-distribuzioni.md]
- **2026-09-21** — L'altro fronte è il volume delle segnalazioni: secondo Phoronix, che cita una slide di Greg Kroah-Hartman per Kernel Recipes 2026, le CVE per release sono passate da circa 500 nella serie 6.x a oltre 1.000 con il kernel 7.0 e oltre 1.500 con il 7.2, con la 7.3 che potrebbe sfiorare quota 2.000. Il numero è di seconda mano e lo stesso Phoronix avverte che spesso si tratta di falle a bassa priorità in driver vecchi o marginali. [Fonte: raw/pillitteri/pillitteri20260921-linux-e-ia-2026-cosa-hanno-deciso-kernel-distribuzioni.md]
- **2026-09-21** — Sul piano delle regole, il file security-bugs.rst ha una sezione intitolata "Responsible use of AI to find bugs" aggiunta il 9 maggio 2026 e chiarita il 2 agosto: dice che i bug trovati con l'IA vanno trattati come pubblici, osserva che una parte significativa delle segnalazioni alla lista di sicurezza nasce da lì e elenca i difetti tipici di quei rapporti, cioè la lunghezza eccessiva e gli impatti inventati. [Fonte: raw/pillitteri/pillitteri20260921-linux-e-ia-2026-cosa-hanno-deciso-kernel-distribuzioni.md]
- **2026-09-21** — Il quadro è ricostruito dalle fonti primarie il 21 settembre 2026, cioè documentazione del kernel, voto di Debian, wiki dei progetti, repository e note di sicurezza dei produttori: le cifre che non è stato possibile verificare non sono riportate, e questo spiega perché i numeri sulle CVE restino indicati come di seconda mano. [Fonte: raw/pillitteri/pillitteri20260921-linux-e-ia-2026-cosa-hanno-deciso-kernel-distribuzioni.md]
- **2026-10-12** — Linus Torvalds pubblica nel repository ufficiale del kernel il branch noref-filemap-read-with-llm, con una serie di patch scritte con Claude Code e dichiarate nel commit «sotto la mia direzione», test e revisione compresi: la patch toglie il contatore di riferimenti dal percorso di lettura dei file e lo sposta in una sezione critica RCU, e le misure circolate (da circa 2.950 a 725 cicli per lettura a otto thread, 10 a 33 milioni di letture al secondo) arrivano da un unico portatile e restano preliminari. Non è il primo passo con l'AI: il visualizzatore di AudioNoise con Google Antigravity a gennaio, la posizione del 15 luglio contro i divieti nella lista del kernel e il fix del driver Intel Xe dell'agosto. [Fonte: raw/pillitteri/pillitteri20261012-torvalds-claude-code-kernel-linux.md]
- **2026-10-18** — Il kernel Linux ritira il tag Assisted-by, la riga con cui chi invia una patch dichiarava di aver usato un assistente AI: il consenso è arrivato al Maintainers Summit dell'8 ottobre a Praga (forte ma non unanime), la patch di Sasha Levin è del 9 e Jonathan Corbet l'ha applicata alla documentazione il 14, mentre la modifica deve ancora confluire nel ramo principale di Torvalds. La cifra che ha pesato è che circa il 10% dei 18.533 commit non di merge arrivati in Linux 7.3 fino alla rc7 porta il tag, mentre l'uso reale degli strumenti è più diffuso: la sua assenza non dice nulla su come sia nata una patch. Le informazioni sull'uso dell'AI si sposteranno nella cover letter della serie di patch, e restano invariati il documento sui contenuti generati e l'obbligo del Signed-off-by umano. Il 13 ottobre Torvalds ha definito «idiota» l'idea di regole del tipo «non usare l'AI per X», rispondendo a Laurent Pinchart. [Fonte: raw/pillitteri/pillitteri20261018-torvalds-regole-anti-ai-assisted-by-kernel-linux.md]
- **2026-10-24** — Il Linux Day 2026, ventiseiesima edizione con 48 eventi in Italia il 24 ottobre, dedica metà dei programmi all'AI aperta e locale: a Torino interventi su Linux come sistema operativo per gli agenti e sui modelli aperti, a Napoli uno sul Model Context Protocol, accanto al filone sulla sovranità digitale. Il contesto sono le ultime due settimane, con il kernel che ha ritirato il tag Assisted-by dopo il no di Torvalds alle regole anti-AI e Torvalds che ha dichiarato di usare Claude Code per il kernel. [Fonte: raw/pillitteri/pillitteri20261024-linux-day-2026-eventi-programma-dirette.md]










## Collegamenti

- [[ai-locale]]
- [[linux-ai-os]]
- [[open-source]]
- [[sicurezza-ai]]
- [[linus-torvalds]]
- [[index]]
