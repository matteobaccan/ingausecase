---
title: "Claude Fable 5.1"
category: modello
tags: [agent, anthropic, claude, coding, llm, reasoning, safety]
related_puntate: [20260902, 20260903, 20260905, 20260911, 20260915, 20260923, 20261004]
created: 2026-09-02
updated: 2026-10-16
---

# Claude Fable 5.1

## Introduzione

Versione aggiornata del modello frontier di Anthropic Claude Fable, rilasciata come "Fable 5.1" su Claude Code e Platform. Stesso prezzo di Fable 5, con cache read piÃ¹ economiche e migliore esecuzione nei task lunghi.

## CapacitÃ  e performance

- Fable 5.1 va piÃ¹ avanti nei task lunghi prima di fermarsi, spiega meglio quando Ã¨ bloccato e ha una scrittura piÃ¹ naturale. Cache read settantacinque percento piÃ¹ economiche di Fable 5.
- La **writing density** è la tendenza del modello a comprimere più concetti in periodi lunghi con pochi a capo: il testo resta corretto, ma diventa più faticoso da leggere e nel 2026 è anche uno dei segnali che i rilevatori di testo AI leggono come scrittura automatica. Il rimedio ufficiale è un'istruzione contro la *mannered prose*, la prosa manierata che sostituisce la frase diretta con metafora e ornamento ("girare una manopola" invece di "variare un parametro"): quando esiste una parola letterale va usata, e la versione lunga con definizione ed esempi serve quando "Please remove all mannered prose" non basta. Anthropic indica il messaggio utente come posto preferibile, riservando il system prompt ai casi in cui lo stile deve restare stabile su conversazioni lunghe o chiamate ripetute.
- Rispetto a Fable 5 il modello usa meno grassetto, titoli, elenchi e virgolette, tende a raccontare il passo successivo invece di eseguirlo sui compiti lunghi e a riscrivere interi file per modifiche piccole; al livello di effort low chiama meno spesso gli strumenti di ricerca e risponde più a memoria, un rischio su nomi di modelli e strumenti che cambiano ogni pochi mesi.
- Il leak di Fable 5.1 ha diffuso duecentosettantamila caratteri: rispetto a Opus 5 ha cutoff giugno 2026, blocchi fable_safeguards_routing e thinking_behavior rimossi, sezioni refusal_handling e user_wellbeing estese, nuovo sistema memory_filesystem con scrittura in background, e quarantasei tool schema contro i trenta di luglio.

- Il costo scende di circa un quarto sui carichi tipici, effetto delle cache read più economiche a listino invariato, e sull'indice Artificial Analysis di settembre 2026 resta il primo assoluto, a sei punti dal miglior modello aperto; sui livelli di sforzo bassi e medi Anthropic dichiara risultati simili o migliori della generazione precedente a una frazione della spesa, e durante i test il fondo di investimento Millennium lo ha lasciato indagare su un crash raro dei propri sistemi interni che nessun ingegnere aveva saputo spiegare per anni, con il modello che ne ha trovato la causa.

Uscito il 1 settembre 2026 insieme al gemello [[claude-mythos-5]] — stesso modello, salvaguardie diverse: Fable è ad accesso generale, Mythos gira solo dentro programmi di accesso verificato con protezioni tarate per cybersecurity e scienze della vita — sul benchmark Terminal-Bench 4.0, dedicato al lavoro da terminale, Anthropic dichiara il 55,8% e stima costi inferiori di circa il 25% rispetto a Fable 5, con le letture da cache tagliate del 75%.

## Azienda di riferimento

- [[anthropic]]

## Strumenti correlati

- [[claude-code]]
- [[claude-platform]]

## Timeline delle notizie

- **2026-09-02** â€” Anthropic rilascia Fable 5.1 su Claude Code e Platform, stesso prezzo di Fable 5, cache read settantacinque percento piÃ¹ economiche, va piÃ¹ nei task lunghi e spiega meglio quando Ã¨ bloccato, scrittura piÃ¹ naturale.

- **2026-09-02** — Fable 5.1 ha progettato una casa, l'ha renderizzata e prodotto un walkthrough cinematico tutto via codice, zero editor video. Richiesto di creare cento file HTML senza design ripetitivi, quasi nessun file rotto e frontend impeccabile (tunnel iperspaziale, synth suonabile with visualizer, orologio di lusso, lampade lava, aurora boreale sul lago Inari, galassia a spirale, ecc.).
- **2026-09-05** — Su ARC-AGI-4, il nuovo benchmark che succede a ARC-AGI-3, Fable restano fermo intorno al quattro percento, lontano dalla capacità di un agente umano su questi giochi.
- **2026-09-03** — Anthropic ha aggiornato la documentazione ufficiale di Prompt Engineering con una sezione su Writing density, ammettendo che Fable cinque virgola uno a volte scrive troppo denso (frasi troppo lunghe, mannered prose) e rilasciando un prompt ufficiale per rimuoverlo: "Please remove all mannered prose".
- **2026-09-11** — Fable 5.1 alla base di StoryComet: quindici libri animati per bambini in cinque lingue con voiceover tradotti, copertine e interfaccia completa costruiti in tre giorni; genitori tracciano progressi, bambini fanno quiz, raccolgono pin e souvenir 3D, cambiano lingua in tempo reale; primi tre libri gratuiti.

- **2026-09-03** — La guida ufficiale al prompting di Fable 5.1 documenta la scrittura densa e il rimedio: un'istruzione anti mannered prose da incollare nel prompt, con la versione completa (definizione più esempi) e quella breve, preferibilmente nel messaggio utente e nel system prompt solo per gli stili da tenere per tutta una sessione. La guida registra anche una quindicina di differenze rispetto a Fable 5, tra cui le regole anti formattazione dei prompt datati che ora fanno più male che bene.

- **2026-09-06** — Con 65,7 guida l'[[artificial-analysis-intelligence-index]] di settembre, davanti a [[claude-opus-5]] (63,0), [[muse-spark-1-3]] (62,1) e [[gpt-6-astra]] (61,2): i primi quattro posti restano dei modelli chiusi, ma il divario dal miglior modello a pesi aperti scende a 6 punti.

- **2026-09-09** — Gira da giorni un leak su un nuovo pretrain di Anthropic: l'account X @kimmonismus parla il 5 settembre di un ciclo di addestramento chiuso, «un salto in avanti notevole», in arrivo «prestissimo», e l'8 settembre sposta la finestra a fine settembre o inizio ottobre. Il modello è chiamato Fable 5.2 «o come finirà per chiamarsi», con l'ipotesi di un «6» lasciata aperta; di concreto non c'è però alcun artefatto verificabile — nessun identificatore EAP, nessuna voce in un catalogo, nessun endpoint anomalo — e la prima finestra indicata (entro il 9 settembre) è già passata a vuoto. L'8 settembre Polymarket prezza il 49% per un rilascio entro il 31 ottobre e l'86% entro fine anno, Manifold circa il 13% prima di ottobre e il 52% prima di novembre.
- **2026-09-14** — Claude Fable 5.1 avrebbe decifrato il **Cyphral Distich**, un crittogramma di 64 numeri in coda al Logopandecteision di Thomas Urquhart (1653) irrisolto da oltre 370 anni e ventottesimo nella lista dei 50 cifrari storici irrisolti di Klaus Schmeh: secondo il test pubblicato da Vals AI il 31 agosto 2026 il modello ci avrebbe messo 44 minuti e 176.000 token, ricostruendo la regola (per l'i-esima cifra si va all'i-esima sezione *Proquiritation* e si prende la prima lettera della parola indicata) e ottenendo il distico «O GOD UPHOLD KING CHARLS THE SECOND...». Il 1 settembre i ricercatori di Reticuli hanno però pubblicato una confutazione: nelle copie del libro del 1653 non esisterebbe alcun distico numerico finale, dieci posizioni sarebbero impossibili per costruzione e i cifrari attribuiti a Urquhart proverrebbero da una biografia del 1899 (John Willcock) e non dalle trascrizioni digitali. Il caso resta aperto in attesa della scansione della pagina originale.

- **2026-09-23** — Resta il riferimento di prestazioni per la nuova generazione Anthropic: [[claude-opus-5-5]] è dichiarato al suo livello sulla maggior parte dei compiti e costa il quaranta per cento in meno di Opus 5.
- **2026-10-02** — Circola un leak su un presunto Claude Fable 5.5 già in rollout segreto e superiore a Opus 5.5 e GPT-6 Astra: la pagina di documentazione citata come prova (platform.claude.com/docs/en/models/fable-5-5/overview) è vuota, nessun post allega un benchmark o un prompt riproducibile, e il confronto ufficiale dei modelli non lascia spazio a un quinto nome nella famiglia 5.x. Anthropic non lo ha annunciato.
- **2026-10-04** — Nella guida di Anthropic ai team di agenti in Claude Code Fable 5.1 ricopre il ruolo di avversario per i controlli di sicurezza.
- **2026-10-13** — Nel catalogo modelli di Azure, regione East US 2, compare la riga `claude-fable-5-5` con stato GenerallyAvailable e data di ritiro fissata al 5 dicembre 2027, rilevata da un post e da un file di LiteLLM: nessun documento di Anthropic o Microsoft lo conferma e le descrizioni sembrano copiate da Fable 5.1, quindi si tratta di una voce di catalogo, non di un lancio.
- **2026-10-16** — Il benchmark di [[chipagents]] e Nvidia per il chip design premia un sistema su Fable 5.1 con il 16,6% di prove risolte lungo l'intero processo di progettazione.













## Collegamenti

- [[claude-opus-5-5]]
- [[anthropic]]
- [[claude-mythos-5]]
- [[storycomet]]
- [[index]]