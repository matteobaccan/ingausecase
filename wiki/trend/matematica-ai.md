---
title: "Matematica AI"
category: trend
tags: [dimostrazioni, matematica, openai, ricerca, verifica-formale]
related_puntate: [20260521, 20260905, 20261016]
created: 2026-09-12
updated: 2026-10-29
---

# Matematica AI

## Introduzione

Il filone dell'AI che produce matematica: dimostrazioni verificate al computer, problemi aperti attaccati con sciami di agenti e il dibattito su cosa resta alla disciplina quando il risultato arriva da una macchina. La domanda non è più se un modello sappia dimostrare, ma quanto valga una dimostrazione che nessuno ha letto.

## Evoluzione nel tempo

- **Maggio 2026** — Il primo risultato pubblico su un problema aperto: la congettura di [[paul-erdoes]] sulla distanza unitaria planare, aperta da ottant'anni, cade sotto un modello di [[openai]] che trova il controesempio collegando la geometria combinatoria alla teoria dei numeri algebrica, con verifica di matematici esterni tra cui [[timothy-gowers]] e un esponente esplicito (n alla 1,014).
- **Agosto 2026** — La verifica formale diventa il metro: i dieci risultati di [[ten-proofs]] certificati in [[lean]] spostano il dibattito da "quanto è bravo il modello" a "quanto è controllabile la prova".
- **Agosto 2026** — Il primo miglioramento di un limite, non la soluzione di un problema: [[anthropic]] porta dal 41,6% al 67,2% la frazione di zeri della funzione zeta garantita sulla retta critica, combinando due lavori già pubblicati che nessuno aveva messo insieme.
- **Settembre 2026** — Il salto di scala: quasi 10.000 agenti in parallelo su un problema del millennio, e in risposta il dibattito sull'economia della ricerca, con Terence Tao che parla di "net negative" e [[antirez]] che ribatte punto per punto.

## Attori coinvolti

- [[anthropic]]
- [[andreas-thom]]
- [[antirez]]
- [[frontiermath]]
- [[gpt-6-astra]]
- [[lean]]
- [[openai]]
- [[paul-erdoes]]
- [[ten-proofs]]
- [[terence-tao]]

## Notizie rilevanti

- **La distanza tra l'annuncio e il problema del millennio**: il risultato del 8 settembre 2026 riguarda Navier-Stokes tridimensionali con una forzante liscia, non la versione classica senza forze esterne che vale il premio Clay. La prova mostra l'esistenza di una singolarità in tempo finito in quel caso specifico, ed è formalizzata in [[lean]].
- **Il metodo conta quanto il risultato**: quasi 10.000 agenti coordinati da un modello più capace di [[gpt-6-astra]] e non ancora rilasciato, circa 5 milioni di messaggi in 88 ore più 17 ore di formalizzazione, con un costo di calcolo stimato in diversi milioni di dollari da Sébastien Bubeck.
- **L'acqua potabile e l'oceano**: Tao sostiene che i problemi aperti formulabili siano infiniti ma solo pochi insegnino qualcosa, e che riconoscere quali valgano la pena richieda la conoscenza del "paesaggio di difficoltà" di un settore. Con l'AI quel paesaggio si appiattisce senza il compenso abituale, perché non esiste un confine visibile tra i problemi che una macchina risolve e quelli su cui si blocca.
- **La forza bruta intellettuale**: il valore del risultato di Claude su Riemann non sta nell'aver toccato un problema del millennio, che nessuno rivendica, ma nell'aver setacciato in modo esaustivo lo spazio delle idee già pubblicate, un lavoro dove pazienza e parallelizzazione contano più del lampo di genio. Anthropic però dichiara che la dimostrazione non ha ancora peer review, non è riproducibile dall'inizio alla fine perché il modello di ricerca usato non è stato reso pubblico, e le tecniche impiegate non dovrebbero portare a dimostrare l'ipotesi completa.
- **L'incentivo a tacere**: se basta la voce che qualcuno stia lavorando a un problema per far partire una campagna da milioni di dollari di calcolo, la mossa razionale per un ricercatore diventa non dire a cosa sta lavorando. Per Tao sarebbe un ribaltamento di secoli di scienza aperta.
- **Compilare non è capire**: la verifica in [[lean]] garantisce che il teorema segua dagli assiomi, non che qualcuno abbia compreso perché. È l'obiezione sollevata nel dibattito sotto il thread di [[antirez]], riassunta nella formula "la prova in Lean è l'equivalente di un compila".
- **La dichiarazione dei Fields**: venticinque medaglie Fields firmano l'11 settembre 2026 un documento che non chiede di fermare l'AI ma di cambiarne la metrica, perché il rischio non è il singolo teorema sbagliato ma un processo di conoscenza che si sposta dal capire al totalizzare. Restano comunque riconosciuti gli usi in cui l'AI è già una collega utile, dalla verifica formale in [[lean]] al miglioramento di limiti noti come quello di Claude sull'ipotesi di Riemann.
- **La trasparenza sull'uso dei dati diventa un caso**: dopo il risultato sul gruppo non-sofico, [[andreas-thom]] accusa [[openai]] di non essere stata onesta sulla sorte delle sue conversazioni con ChatGPT, che toccavano da mesi le tecniche del lavoro su cui poggia la prova. Il nodo non è un furto dimostrato ma la verificabilità: la de-identificazione toglie un nome, non il contenuto intellettuale di un'idea matematica, e un opt-out non auditabile resta una promessa che vale solo per il futuro.

## Timeline delle notizie

- **2026-05-21** — Un modello di [[openai]] smentisce la congettura di [[paul-erdoes]] del 1946 sulle distanze unitarie: il 20 maggio l'azienda annuncia un controesempio che porta il lower bound a n alla 1,014, polinomiale e indipendente da n, contro il tetto n alla 4/3 fermo dal 1984 (Spencer-Szemerédi-Trotter), e Will Sawin lo rende esplicito con δ ≥ 0,014. La strada non è geometrica: la costruzione usa campi numerici algebrici e torri di campi di classe con il criterio di Golod-Shafarevich. La prova copre 125 pagine in due paper, il secondo dei quali è un companion di 19 pagine firmato da nove matematici (Noga Alon, [[thomas-bloom]], [[timothy-gowers]], Daniel Litt, Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang e Melanie Matchett Wood) che l'hanno resa leggibile e verificata passaggio per passaggio; la formalizzazione in [[lean]] o Coq non è ancora arrivata. Il dettaglio che pesa è il tipo di modello: un reasoning generalista interno, lo stesso genere di architettura che alimenta ChatGPT e Codex, non un sistema specializzato come AlphaProof di Google DeepMind.
- **2026-08-01** — Tre dei dieci risultati di [[ten-proofs]] chiudono altrettanti problemi del catalogo di [[paul-erdoes]], verificati in [[lean]].
- **2026-08-10** — [[anthropic]] pubblica il risultato di una versione di ricerca di Claude non rilasciata: non risolve l'ipotesi di Riemann, aperta dal 1859, ma migliora un limite inferiore collegato portando dal 41,6% al 67,2% la frazione di zeri della funzione zeta che si riesce a dimostrare stiano sulla retta critica. Il metodo è multi-agente: circa 650 idee fallite in una prima sessione, poi circa 60 sotto-agenti coordinati in [[claude-code]] con 31 milioni di token di output, 2.400 comandi di shell e 54 articoli arXiv scaricati, da cui esce la combinazione di due lavori già pubblicati. La dimostrazione è formalizzata in [[lean]] nel repository `zeta-23-lean` e validata da due matematici interni e da Brian Conrey e Dan Goldston, ma non ha ancora peer review né è riproducibile, perché il modello di ricerca interno non è stato identificato.
- **2026-09-09** — [[openai]] annuncia che un modello non rilasciato ha dimostrato l'esistenza di una singolarità nelle equazioni di Navier-Stokes 3D con forzante liscia, con quasi 10.000 agenti in parallelo in 88 ore e una formalizzazione in [[lean]]; il premio Clay da un milione di dollari resta lontano, perché richiede pubblicazione peer-reviewed e due anni di validazione.
- **2026-09-10** — [[antirez]] pubblica sette punti contro la tesi del saldo negativo di [[terence-tao]], che risponde distinguendo lo stock di teoremi dimostrati dal flusso di capacità della disciplina di produrne di nuovi.
- **2026-09-10** — [[andreas-thom]], teorico dei gruppi alla TU Dresda, accusa [[openai]] di una risposta fuorviante sulle sue conversazioni private con ChatGPT: il passo tecnico centrale della prova sul gruppo non-sofico poggiava su un lavoro che aveva pubblicato nel 2019 con Gábor Kun, e per mesi prima dell'annuncio aveva discusso con il modello proprio quelle tecniche. La risposta di Mark Sellke, riporta, è stata una riga sola — «Regarding your conversations with ChatGPT: that did not happen» — senza distinguere le due domande che aveva posto né mostrare prove, mentre settimane dopo nel caso Navier-Stokes l'azienda ha ammesso di non poter escludere l'uso di dati de-identificati. Thom aveva disattivato l'addestramento sui propri dati il 29 giugno, ma osserva che il controllo non è verificabile dall'esterno e non copre le conversazioni precedenti. La prova sul gruppo non-sofico resta tecnicamente autonoma e verificata in [[lean]]: quella di Thom è un'accusa pubblica di mancanza di trasparenza, non un furto dimostrato.
- **2026-09-11** — Venticinque vincitori della medaglia Fields firmano una dichiarazione congiunta, pubblicata su mathandai.org e sul blog di [[terence-tao]], che parla di un disallineamento grave tra gli obiettivi dell'industria dell'AI e quelli della matematica: tra le firme [[terence-tao]], Peter Scholze, Maryna Viazovska, Pierre Deligne, Martin Hairer, Cédric Villani, Manjul Bhargava e il vincitore 2026 Yu Deng. I firmatari non chiedono di fermare l'AI ma di smettere di trattarla come una gara a chi risolve di più, perché quella metrica premia la quantità di problemi chiusi e ignora la comprensione che resta; le preoccupazioni concrete sono l'attribuzione e il plagio (spesso non è chiaro su quali lavori umani il modello si sia appoggiato), la verifica (una dimostrazione prodotta in fretta e in grande quantità resta difficile da controllare riga per riga) e il senso del mestiere, perché una dimostrazione serve a capire *perché* un teorema è vero, non solo a stabilire che è vero. La dichiarazione arriva in coda ai casi Erdős, Navier-Stokes e all'accusa di [[andreas-thom]] a [[openai]], ed è aperta a nuove firme.

- **2026-09-23** — Vals AI pubblica [[c-hd]], algoritmo shortest-path ideato da dieci agenti [[claude-opus-5-5]] diretti da un ricercatore e accompagnato da una prova [[lean]] della correttezza e del bound di runtime, ottenuta in circa quindici ore: ricerca algoritmica multi-agente e verifica formale nello stesso lavoro, con l'umano nella direzione.

- **2026-09-28** — Fisici di [[anthropic]] hanno usato [[claude]] per calcolare un'ampiezza a nove loop in N=4 super-Yang-Mills, un problema considerato non calcolabile con risorse limitate: con il metodo bootstrap e l'approccio form-factor i risultati sono comparabili ai tentativi umani ma con maggiore efficienza e meno supervisione, e il lavoro suggerisce che ulteriori avanzamenti dipendano più dalle pratiche di calcolo e di software che dalla potenza di calcolo.
- **2026-10-01** — Un modello Claude dimostra la congettura della percolazione morente, problema aperto da oltre sessant'anni sulla continuità della transizione di fase nelle dimensioni da 3 a 10: la prova si appoggia alla congettura formulata nel 2024 da Gady Kozma e Shahaf Nitzan e viene formalizzata in Lean e pubblicata sul repository anthropics/formal-math.



- **2026-10-02** — Un sistema AI per Stratego viene pubblicato su Nature dopo aver battuto un quattro volte campione mondiale con 15 vittorie, una sconfitta e quattro pareggi: gli autori stimano un costo di addestramento di poche migliaia di dollari e dichiarano risultati superumani anche applicando reinforcement learning e ricerca ad altri giochi.
- **2026-10-05** — Stephen Wolfram sostiene che l'AI possa automatizzare una parte crescente della ricerca matematica, collegando idee e proponendo passaggi, ma che la scelta delle domande decisive resti umana; un passaggio critico è l'autoformalizzazione, perché tradurre male un problema in simboli porta a dimostrare qualcosa di diverso da ciò che si voleva capire.
- **2026-10-05** — Meta ha collaborato con i matematici per risolvere problemi aperti di ricerca matematica usando i suoi modelli Muse Spark.
- **2026-10-06** — OpenAI pubblica su GitHub con licenza Apache-2.0 il pacchetto openai/math: 722 manoscritti in 372 famiglie di risultati, una libreria in Lean e dieci riassunti del ragionamento del modello, con circa 4.000 problemi posti e ogni risultato accettato costato in media l'equivalente di tre ore di ragionamento di ChatGPT Pro. Tra i risultati figurano una zona libera da zeri per la funzione zeta di Riemann (parte reale maggiore di 7/8, con certificato Lean) e la congettura di Hodge razionale per le varietà abeliane a moltiplicazione complessa, non formalizzata; i matematici chiedono le prove e OpenAI avverte che alcuni risultati non formalizzati potrebbero contenere errori.



- **2026-10-07** — OpenAI pubblica un ampio insieme di risultati matematici prodotti da un modello frontier interno, con le dimostrazioni formalizzate in Lean raccolte in un repository GitHub e protocolli per revisione e citazioni. Il pacchetto include dieci sintesi del ragionamento del modello, stime del calcolo speso in termini di utilizzo Pro su ChatGPT e statistiche sul numero di problemi tentati.
- **2026-10-08** — L'Association for Human Mathematics pubblica una dichiarazione, ripresa da Terence Tao come guest post sul suo blog, in cui definisce il rilascio di oltre 700 file di OpenAI una «dimostrazione di potere» e non di erudizione e invita i matematici a interrompere il lavoro con l'azienda; l'AGMAI, il comitato indipendente di nove matematici ospitato dall'Institute for Advanced Study, commenta lo stesso rilascio in toni diversi, definendo costruttive le discussioni e precisando che non si tratta di un'approvazione del processo seguito.
- **2026-10-10** — [[openai]] ritira tre manoscritti matematici prodotti con il contributo dei propri modelli dopo la scoperta di un errore di segno in una dimostrazione, che avrebbe compromesso i risultati costruiti sullo stesso ragionamento: il caso mostra come passaggi apparentemente coerenti propaghino errori e quanto conti la corrispondenza tra prove formalizzate, argomentazioni testuali e versioni pubblicate, anche usando strumenti come Lean.
- **2026-10-12** — Le slide Math 2.0 (Caltech 2026) sostengono che l'AI abbia aperto una nuova era della matematica sperimentale.
- **2026-10-16** — [[anthropic]] mette 5 milioni fra funding, compute e Claude per la comunità matematica, con la Simons Foundation a gestire workshop e conferenze.
- **2026-10-17** — [[anthropic]] porta Claude Mythos 5 a progettare otto circuiti quantistici da descrizioni in linguaggio naturale, con il costo TQ (porte Toffoli per picco di qubit) ridotto da 4,1 a 39 volte rispetto ai riferimenti e senza alcuna esecuzione su hardware reale: il caso della somma di punti su curva ellittica, risolto con un'architettura nuova basata su divsteps dopo 53 ore di ricerca e verificato in [[lean]], lega il risultato alla teoria dei numeri.
- **2026-10-18** — La congettura di Grad del 1967 sulla fusione cade su tre famiglie di soluzioni esplicite: due le ha trovate il fisico Matt Landreman con GPT-6 Astra Pro, con equazioni confermate a mano, e la terza è dei matematici Gómez-Serrano, Liehr e Taylor, certificata in Lean 4 con GPT-5.6 Sol, Claude Fable 5 e Claude Opus 5 come supporto e GPT-6 Astra e Claude Fable 5.1 nella verifica finale. Il 5 ottobre un gruppo con tre ricercatori di Google DeepMind e lo stesso Landreman ha rimosso la simmetria da stellarator usando Gemini 4 in Google Antigravity.
- **2026-10-26** — Il matematico Steven Strogatz esamina su The Atlantic le conseguenze per la disciplina dopo le dichiarazioni di [[openai]] secondo cui i suoi modelli avrebbero affrontato quasi 400 problemi aperti: il resoconto richiama l'esperimento su Navier-Stokes con migliaia di agenti, risultati attribuiti all'azienda e valutabili solo verificando le dimostrazioni, e discute possibili benefici per la matematica applicata accanto ai timori per formazione, ricerca individuale e opportunità dei giovani studiosi.
- **2026-10-27** — [[openai]] annuncia tre risultati prodotti dai suoi modelli in analisi armonica, teoria della complessità e teoria quantistica dei campi, tra cui una prova verificata in Lean che l'ipotesi del tempo esponenziale è falsa; gruppi esterni, compresi Russell Impagliazzo e Ramamohan Paturi che formularono l'ipotesi, controlleranno e spiegheranno i risultati. Il paper si intitola «The Exponential Time Hypothesis is False», descrive un algoritmo deterministico che conta le soluzioni di una formula k-CNF in circa 2^(n/(log n)^(1/2+o(1))) con spazio polinomiale e sostiene di smentire anche SETH, Gap-ETH e NSETH senza dimostrare limiti superpolinomiali per NP; testo e prova Lean sono nel repository openai/math con licenza Apache-2.0 e la verifica è affidata a un gruppo guidato da Russell Impagliazzo, Ramamohan Paturi e Ryan Williams, con la pubblicazione dei dati grezzi e una conferenza finanziata. Per local smoothing e Kakeya la formalizzazione Lean c'è ma nessun gruppo di verifica annunciato, mentre su Yang-Mills e QCD il materiale non è pubblico e il gruppo guidato da David Gross ha deciso di trattenere gli artefatti e scrivere da sé la spiegazione.
- **2026-10-28** — [[axiom-math]] pubblica la prima prova completa verificata al computer della classificazione dei gruppi semplici finiti, la dimostrazione più lunga mai scritta da esseri umani con circa 15.000 pagine in più di 500 articoli: ingegneri e matematici del laboratorio hanno diretto sciami di decine di agenti AI per 24 giorni, producendo circa 43,1 milioni di righe di codice in [[lean]].
- **2026-10-28** — [[anthropic]] riferisce che un modello di ricerca interno ha trovato senza input umano un algoritmo deterministico che conta le assegnazioni soddisfacenti delle formule 3-SAT in tempo 2^O(n log log n/√log n), il che renderebbe il 3-SAT subesponenziale e confuterebbe l'Ipotesi del tempo esponenziale; il repository pubblica il paper e una formalizzazione in Lean 4 scritta da modelli AI che compila in circa otto minuti. L'azienda avverte che nessuna macchina verifica la corrispondenza fra enunciato Lean e paper e che il risultato non dice nulla sulla risoluzione pratica del SAT.
- **2026-10-29** — [[openai]] e [[anthropic]] sostengono di aver prodotto dimostrazioni che metterebbero in discussione l'Exponential Time Hypothesis, un'ipotesi centrale della teoria della complessità: OpenAI ha presentato soluzioni a problemi aperti e Anthropic ha poi diffuso una propria prova, riaccendendo il dibattito su verifica e attribuzione del lavoro. Ricercatori universitari chiedono esame pubblico e norme per distinguere contributo umano e automatico, e la comunità non ha dato per confutata l'ipotesi: le conseguenze teoriche dipendono dalla validità delle prove e dal vaglio indipendente.














































## Collegamenti

- [[andreas-thom]]
- [[antirez]]
- [[c-hd]]
- [[frontiermath]]
- [[gpt-6-astra]]
- [[lean]]
- [[openai]]
- [[paul-erdoes]]
- [[terence-tao]]
- [[index]]
