---
title: "Pangram"
category: strumento
tags: [rilevamento, formazione, token, mistura-di-esperti]
related_puntate: []
created: 2026-09-28
updated: 2026-09-06
---

# Pangram

## Introduzione

Rilevatore di testo generato dall'AI che, nello studio degli economisti Jabarian e Imas dell'Università di Chicago, è rimasto vicino al 100 per cento di efficacia anche su testo passato attraverso un humanizer, mentre i detector generici sono crollati da oltre il 90 per cento a meno del 50 per cento.

## Funzionalità principali

- L'architettura è una mistura di esperti pensata per classificare token singoli, invece di misurare la prevedibilità statistica dell'intero testo: è la differenza tecnica che spiega la tenuta contro la parafrasi automatica.

## Timeline delle notizie

- **2026-08-27** — Pangram pubblica l'analisi sui nove segnali che tradiscono un testo generato, ognuno espresso come moltiplicatore sulla media umana: il Markdown fuori contesto (12 volte), le frasi fatte da chatbot (12 volte), l'em-dash (10 volte, con i modelli OpenAI a 45 occorrenze ogni 10.000 parole contro 2 umane e Gemini 3 Pro sotto la media), gli elenchi puntati (9 volte), le triadi (4 volte), il costrutto "non solo X ma anche Y" (3 volte), i caratteri Unicode insoliti (3 volte), le intestazioni collaborative (2 volte) e le emoji funzionali (2 volte). Il motore è alla versione Pangram 4 dal 29 luglio 2026, dichiara lo 0,0041 per cento di falsi positivi — circa un errore ogni 24.000 documenti — identifica i contenuti di 26 modelli sopra il 99 per cento e copre oltre venti lingue compreso l'italiano, con accuratezza minore sotto le cinquanta parole, sul codice sorgente e sui documenti tabellari; Epoch AI l'ha testato su 495 testi umani nell'estate 2026 senza registrare un falso positivo. Dal 21 luglio 2026 alimenta il rilevatore integrato in Substack e il piano gratuito permette di analizzare 2.000 parole al giorno e tre immagini senza carta di pagamento.
- **2026-08-30** — Il divulgatore Ruben Hassid ribalta Pangram con una sola battuta di tastiera: lo stesso testo che il rilevatore bocciava al 100 per cento come AI passa al 100 per cento umano dopo aver sostituito un unico trattino lungo con i due punti, e la stessa fragilità si riproduce in italiano togliendo la copula in un'enumerazione («Il primo motivo è simbolico, il secondo è politico» contro «Il primo simbolico, il secondo politico»). Un rilevatore statistico non capisce chi ha scritto il testo, stima da che parte pende il campione, e su un brano vicino al minimo delle 100 parole basta spostare un segnale di peso alto come l'em-dash.

- **2026-09-06** — Semafor passa Pangram sui 310 editoriali ospiti di Wall Street Journal, New York Times e Washington Post usciti in un mese e ne trova 10 classificati come scritti dalla macchina e 40 come misti: il Washington Post da solo ne conta 17, nonostante il modulo chieda una dichiarazione di non uso dell'AI, mentre un preprint arXiv su 186.000 articoli di 1.500 giornali stima il 9,1 per cento di contenuto AI o misto, concentrato sulle testate piccole (9,3 per cento) e non su quelle sopra le 100.000 copie (1,7 per cento). Una ricerca di Stanford citata nell'inchiesta ricorda che i rilevatori tendono a marchiare come artificiale la prosa di chi non ha l'inglese come lingua madre, e James Taranto definisce lo strumento una «macchina diffamatoria» dopo aver ottenuto punteggi diversi sugli stessi testi.



- **2026-09-28** — Pangram è l'unico prodotto citato dallo studio dell'Università di Chicago che regga il confronto con gli humanizer, in un panorama in cui gli atenei statunitensi stanno smettendo di usare i punteggi AI come prova nei procedimenti disciplinari.

## Riferimenti

- https://pasqualepillitteri.it/news/19023/detector-ai-humanizer-guerra-testo

## Collegamenti

- [[turnitin]]
- [[formazione-ai]]
- [[ai-slop]]
- [[chatgpt-work]]
- [[index]]
