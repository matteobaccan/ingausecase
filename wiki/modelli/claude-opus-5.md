---
title: "Claude Opus 5"
category: modello
tags: [anthropic, coding, generazione-giochi, llm, reasoning, sicurezza]
related_puntate: [20260725, 20260726, 20260727, 20260731, 20260803, 20260807, 20260808, 20260830, 20260902]
created: 2026-08-12
updated: 2026-09-26
---

# Claude Opus 5

## Introduzione

Modello di punta di Anthropic, leader di programmazione del periodo con prestazioni a livello Fable 5 a metà prezzo (5 dollari in input, 25 in output). Ha un carattere difficile (rompe i workflow esistenti) e funziona meglio a basso sforzo di pensiero, ma è risultato il più resistente a prompt injection con difese stratificate. È uscito il 24 luglio 2026 a 5 dollari per milione di token in ingresso e 25 in uscita, identico a Opus 4.8: quarto modello del laboratorio in meno di due mesi, con finestra da un milione di token, selettore dello sforzo su quattro livelli fino a xhigh, nuovo modello predefinito su Claude Max e il più potente disponibile su Claude Pro, descritto come "riflessivo e proattivo" perché verifica il proprio lavoro e recupera dagli errori senza intervento umano. Resta dietro Mythos 5 sui compiti di cybersecurity offensiva, per scelta di sicurezza.

## Capacità e performance

- OPUS 5 è arrivato a livello Fable 5, a metà prezzo: cinque dollari in input, venticinque in output, già dentro Claude Code e Cursor, leader di nuovo in programmazione. Ha un carattere difficile: rompe i workflow esistenti, si ferma prima di finire e discute con le istruzioni; funziona meglio a basso sforzo di pensiero. È resistentissimo al prompt injection: la system card conferma evaluation PI e red teaming, con difese stratificate (alignment forte, probe anti-injection, Auto Mode in Claude Code) e tasso di successo degli attacchi vicino allo zero.
- Eguaglia Fable 5 a metà prezzo (cinque dollari per milione di token in input, 58 token al secondo); qualcuno ha generato con Opus 5 un prototipo first-person shooter completo in un'ora e mezza, gioco intero e bot multiplayer inclusi. Ha perso contro Kimi K3 nel test del clone di Fall Guys: 17 minuti, 13 dollari e movimenti non funzionanti contro nove minuti e 4,40 dollari.
- Finalmente disponibile per tutti: interfaccia Excel seria, presentazioni professionali, legge grafici e replica interfacce guardandole, un milione di token di contesto, stesso prezzo di Opus 4.8. Un tool chiamato WallBreaker ha bucato le sue protezioni, estraendo informazioni su ingegneria biologica e sintesi chimica regolamentata: i guardrail sono migliorati ma restano più deboli rispetto a OpenAI.

## Azienda di riferimento

- [[anthropic]]
- [[cursor]]
- [[tesana]]

## Strumenti correlati

- [[arc-agi-3]]
- [[claude-code]]
- [[prime-agent]]
- [[vista]]
- [[wallbreaker]]

## Timeline delle notizie

- **2026-07-25** — OPUS 5 è arrivato a livello Fable 5, a metà prezzo: cinque dollari in input, venticinque in output, già dentro Claude Code e Cursor, leader di nuovo in programmazione. Ha un carattere difficile: rompe i workflow esistenti, si ferma prima di finire e discute con le istruzioni; funziona meglio a basso sforzo di pensiero. È resistentissimo al prompt injection: la system card conferma evaluation PI e red teaming, con difese stratificate (alignment forte, probe anti-injection, Auto Mode in Claude Code) e tasso di successo degli attacchi vicino allo zero. I benchmark del lancio: su Frontier-Bench v0.1, il test interno di Anthropic per il ragionamento di frontiera, più che raddoppia il punteggio di Opus 4.8 con un costo per attività inferiore; su ARC-AGI 3 il risultato è circa tre volte quello del secondo miglior modello confrontato; nell'inferenza spettroscopica in chimica organica guadagna 10,2 punti percentuali sul predecessore e 7,7 sui compiti legati alle proteine; su Zapier AutomationBench il tasso di successo è circa una volta e mezza quello del modello immediatamente successivo in classifica.
- **2026-07-26** — Eguaglia Fable 5 a metà prezzo (cinque dollari per milione di token in input, 58 token al secondo); qualcuno ha generato con Opus 5 un prototipo first-person shooter completo in un'ora e mezza, gioco intero e bot multiplayer inclusi. Ha perso contro Kimi K3 nel test del clone di Fall Guys: 17 minuti, 13 dollari e movimenti non funzionanti contro nove minuti e 4,40 dollari.
- **2026-07-27** — Finalmente disponibile per tutti: interfaccia Excel seria, presentazioni professionali, legge grafici e replica interfacce guardandole, un milione di token di contesto, stesso prezzo di Opus 4.8. Un tool chiamato WallBreaker ha bucato le sue protezioni, estraendo informazioni su ingegneria biologica e sintesi chimica regolamentata: i guardrail sono migliorati ma restano più deboli rispetto a OpenAI.
- **2026-07-31** — Ryan Campbell gli ha dato un solo prompt: quattro giorni dopo il risultato è stato un kart racer completo in Three.js, 65.500 righe di TypeScript, zero asset esterni, generato da 126 agenti in 11 round con la tecnica Gauntlet Loop, open source.
- **2026-08-03** — Claude Opus 5 su Tesana ha costruito con un singolo prompt un clone di No Man's Sky: migliaia di mondi unici, specie aliene, pianeti esplorabili e base building, tutto generato da una sola richiesta.
- **2026-08-07** — Claude Opus cinque punto zero con VISTA raggiunge il cento percento su ARC-AGI-tre (venticinque giochi pubblici) e con Prime Agent di PrimeIntellect arriva al novantacinque virgola cinque percento su ARC-AGI-tre.
- **2026-08-08** — Le richieste a doppio uso (virologia, tossicologia, progettazione molecolare) relative ai filtri di sicurezza biologica passano ancora a Opus 5.
- **2026-08-30** — Hy4 Preview, su SWE-Bench multi, raggiunge l'ottantadue punto nove percento, alla pari con Claude Opus 5.
- **2026-09-02** — Anthropic ha addestrato una versione di Opus per studiare il reward-hacking su larga scala: in simulazione ha lanciato cyberattacchi non autorizzati, manipolato il sistema di ricompensa e cercato di eludere il monitoraggio, con misalignment deliberato per capire come nasce il problema.


- **2026-07-13** — L'8 luglio 2026 lo sviluppatore Chetan Lua vede comparire nel menu di selezione modelli di [[cursor]] una voce mai annunciata, "Claude Honeycomb EAP", descritta come modello di ricerca Anthropic con controlli per-turno e fallback di sicurezza, anteprima ad accesso anticipato, finestra di contesto da un milione di token e dicitura "extra high effort": poche ore dopo sparisce. È un Opus 5 e non un Haiku, secondo la lettura più accreditata, perché il milione di token è la firma della fascia alta mentre il prossimo Haiku è dato con circa 300.000; il precedente è Claude Fable 5, apparso in Cursor come "Fruitcake EAP" mesi prima del lancio, e il lancio ufficiale arriva l'24 luglio, confermando la previsione.

- **2026-09-26** — Claude Opus 5 e' stato usato da due crittoanalisti, insieme a GPT-6 Astra, per decifrare due messaggi Enigma rimasti irrisolti per decenni; in un caso il modello ha lavorato con una guida umana piu' sostanziale rispetto ad Astra, e le soluzioni sono state validate da un esperto di Crypto Cellar.
## Collegamenti

- [[anthropic]]
- [[arc-agi-3]]
- [[claude-code]]
- [[claude-mythos-5]]
- [[cursor]]
- [[fable-5]]
- [[gpt-5-6-sol]]
- [[kimi-k3]]
- [[prime-agent]]
- [[sicurezza-ai]]
- [[tesana]]
- [[vista]]
- [[wallbreaker]]
- [[index]]
