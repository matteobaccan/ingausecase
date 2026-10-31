---
title: "AI nello sviluppo software"
category: trend
tags: [agent, claude, coding, debito-tecnico, sicurezza, verifica]
related_puntate: [20260913, 20260917, 20260918, 20260924, 20260925, 20261009, 20261014]
created: 2026-09-12
updated: 2026-10-31
sources: [raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md, raw/pillitteri/pillitteri20260813-deepseek-harness-open-source-claude-code.md, raw/puntate/ainews20260913.md, raw/puntate/ainews20260917.md, raw/puntate/ainews20260918.md, raw/pillitteri/pillitteri20260825-google-labs-play-with-putty-vibe-coding-multiplayer.md, raw/pillitteri/pillitteri20260910-emergent-ingegneri-umani-vibe-coding.md, raw/puntate/ainews20260924.md, raw/puntate/ainews20260925.md, raw/pillitteri/pillitteri20260525-aidd-vs-vibe-coding-spec-driven-development-2026.md, raw/pillitteri/pillitteri20260527-vibe-coding-impalcatura-architettura-app-2026.md, raw/controrumore/controrumore20260929-diario-ai-quando-lai-ci-convince.md, raw/pillitteri/pillitteri20260814-codegraph-token-agenti-coding.md, raw/pillitteri/pillitteri20260614-lovable-500-milioni-vibe-coding.md, raw/pillitteri/pillitteri20260809-gitlab-orbit-grafo-contesto-agenti-ai.md, raw/pillitteri/pillitteri20261002-ux-ui-differenza.md, raw/myclaw/myclaw20261005-airbnb-keeps-agents-outside.md, raw/controrumore/controrumore20261008-diario-ai-lai-entra-nella-zona-grigia.md, raw/puntate/ainews20261009.md, raw/pillitteri/pillitteri20261009-strata-riscrive-cronologia-github-firme-claude.md, raw/controrumore/controrumore20261010-diario-ai-lai-decide-ma-chi-ne-risponde.md, raw/pillitteri/pillitteri20260204-superpowers-claude-code-guida-completa.md, raw/pillitteri/pillitteri20260512-compressori-esternalizzatori-sviluppatori.md, raw/pillitteri/pillitteri20261010-black-ops-zombies-skate-3-halo-browser-gratis.md, raw/controrumore/controrumore20261013-diario-ai-lai-sa-dove-abiti-e-chi.md, raw/puntate/ainews20261014.md, raw/tldr/tldr20261013.md, raw/pillitteri/pillitteri20260312-alexey-grigorev-claude-code-backup-lezione.md, raw/pillitteri/pillitteri20261015-app-desktop-agenti-ai-parallelo-confronto.md, raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md, raw/pillitteri/pillitteri20261018-giochi-decompilati-ricompilati-pc-allrecomps.md, raw/controrumore/controrumore20261019-diario-ai-regole-investimenti-e-nuovi.md, raw/tldr/tldr20261019.md, raw/pillitteri/pillitteri20261019-gta-4-android-port-tweet-virale-legale.md, raw/pillitteri/pillitteri20261031-cisco-token-ai-illimitati-27enne-codice-legacy.md]
---

# AI nello sviluppo software

## Introduzione

Quanto del codice che finisce in produzione porta la firma di un modello, e quanto di quel lavoro è davvero delegabile senza pagare un conto mesi dopo. Il quadro del 2026 è coerente su un punto: l'AI accelera le fasi verificabili in fretta e va tenuta sotto controllo umano su architettura, integrazione in produzione e sicurezza. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

Il dato che riassume il divario: [[anthropic]] dichiara che l'80% del codice unito alla sua codebase porta la firma di Claude, gli sviluppatori dicono di usare l'AI in circa il 60% del lavoro, e gli stessi ammettono di poterle delegare per intero solo dallo zero al 20% dei compiti. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

## I numeri del 2026

- [[claude-code]] sfiora le 144.000 stelle su GitHub con oltre 23.000 fork, a poco più di un anno dalla nascita (febbraio 2025); il volume di chiamate API per il coding è cresciuto di quasi 70 volte in un anno. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]
- Rakuten ha fatto completare a Claude un compito di implementazione su una codebase da 12,5 milioni di righe in sette ore, con il 99,9% di accuratezza numerica; TELUS ha creato oltre 13.000 soluzioni interne e dichiara più di 500.000 ore risparmiate; Zapier è all'89% di adozione con oltre 800 agenti; Samsung ha tagliato alcuni passaggi del design dei chip da un mese a due giorni. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]
- La stessa Anthropic scrive che usare bene l'AI richiede supervisione, verifica e giudizio umano: gli ingegneri passano dallo scrivere codice al coordinare agenti, spostando la propria testa su architettura e scelte di sistema. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

## Dove l'AI aiuta e dove no

| Fase del ciclo | Delegabile all'AI | Controllo umano |
| --- | --- | --- |
| Prototipazione, boilerplate | Sì, con revisione veloce | Basso |
| Esplorare codice sconosciuto | Sì, ottimo per orientarsi | Basso |
| Architettura e design di sistema | Come sparring partner | Alto |
| Review e merge in produzione | Solo primo passaggio | Alto |
| Sicurezza e gestione dei segreti | Assistita, mai autonoma | Critico |

[Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

Il rapporto DORA 2025 di Google Cloud lo riassume: l'AI è un amplificatore, non una cura. Un team con testing solido e piattaforme interne di qualità diventa più veloce; un team con strumenti frammentati e infrastruttura fragile accelera soltanto la produzione di problemi. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

## Il conto nascosto: la tassa di verifica

- DORA rileva che il 90% dei professionisti tech usa l'AI e oltre l'80% è convinto che aumenti la produttività, ma circa il 30% dichiara poca o nessuna fiducia nel codice generato; a più AI corrisponde più throughput e insieme più instabilità nel rilascio, perché il tempo risparmiato scrivendo si trasferisce quasi intero a chi deve controllare. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]
- Lo studio randomizzato controllato di [[metr]] su 16 sviluppatori esperti di grandi progetti open source (repo da oltre 22.000 stelle, più di un milione di righe, 246 compiti, febbraio-giugno 2025, Cursor Pro con Claude 3.5 e 3.7) ha misurato il contrario di quello che i partecipanti credevano: **19% di tempo in più** con l'AI, contro una previsione di andare il 24% più veloci e una stima a posteriori di essere stati il 20% più produttivi. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

## Debito tecnico

- L'analisi di GitClear su 623 milioni di modifiche dal 2023 al 2026 fotografa un codice che invecchia male: duplicazione di blocchi cresciuta dell'81%, copia-incolla al 15,7% delle righe modificate nella prima metà del 2026 e codice spostato o rifattorizzato crollato al 3,8%, con il churn a due settimane aumentato del 15%. Un modello, dentro una singola sessione, tende a incollare invece di astrarre, perché incollare risolve il compito di adesso. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]
- Il codice clonato porta tra il 15 e il 50% di difetti in più secondo la ricerca citata, e ogni copia è un punto in più dove il bug va corretto due volte. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

## Sicurezza

- Lo studio di Stanford di Perry e colleghi (CCS 2023) ha messo 47 persone davanti a cinque compiti di programmazione in Python, JavaScript e C: chi aveva un assistente AI ha scritto codice meno sicuro, con più vulnerabilità su iniezione SQL e cifratura delle stringhe, e si sentiva **più** sicuro di aver scritto codice protetto. Chi invece si fidava di meno dell'AI e riformulava i prompt produceva meno falle. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]
- La fase security resta quella dove delegare senza rete fa più male, e i rischi nuovi introdotti dagli agenti stessi si sommano a quelli classici. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

## Come lavora chi ha costruito il modello

Il modo in cui Anthropic mette in sicurezza il proprio ciclo di sviluppo AI-nativo è la prova migliore che il controllo umano serve: [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]

- Il codice viene classificato per rischio: le codebase sensibili hanno approvazione umana obbligatoria, il codice a basso rischio può passare in automatico, ma un campione pesato sul rischio finisce comunque sotto occhi umani, con ogni azione dell'agente registrata per l'audit.
- Un agente di risposta agli incidenti non può fare il deploy della correzione da solo: servono un secondo agente e un revisore umano; le review le fanno più agenti specializzati con compiti stretti, con scanner deterministici SAST che commentano direttamente sulle pull request.
- Gli agenti nuovi lavorano in modalità ombra, proponendo commenti che un umano deve approvare finché non si guadagnano il credito; il loro traffico gira su macchine virtuali con l'uscita verso internet ristretta a una lista chiusa, per limitare i danni di un agente compromesso da un prompt malevolo.
- Le regole di codice sicuro sono scritte nei file di configurazione perché l'AI le segua di default, e periodicamente qualcuno prova a inserire modifiche malevole per testare i revisori.

## Timeline delle notizie

- **2026-02-04** — Il caso di Superpowers mostra il limite dell'approccio code-first: senza design pattern dichiarati all'agente tra il 50 e il 60 per cento dei casi produce codice errato o incompleto, funzionalità saltate e nessun test. Il framework risponde imponendo la scrittura dei test prima del codice e cancellando quello scritto in violazione della regola, e il suo autore dichiara coperture dell'85-95 per cento. [Fonte: raw/pillitteri/pillitteri20260204-superpowers-claude-code-guida-completa.md]

- **2026-03-12** — L'incidente di DataTalks.Club serve da caso studio per chi lavora con agenti: la sera del 26 febbraio 2025 un agente ha eseguito `terraform destroy` sull'infrastruttura di produzione cancellando 2,5 anni di dati, 1.943.200 righe della tabella `courses_answer` di oltre 100.000 studenti; il post-mortem di Alexey Grigorev sposta la responsabilità sull'errore umano, cioè sui backup mai fatti, non sull'AI. [Fonte: raw/pillitteri/pillitteri20260312-alexey-grigorev-claude-code-backup-lezione.md]

- **2026-05-12** — Un modello proposto dall'ingegnere giapponese torao divide gli sviluppatori in compressori, che tengono il modello mentale del sistema nella memoria di lavoro e sono più forti sui bug logici, ed esternalizzatori, che lo spostano in diagrammi, ADR e test e sono più forti sui bug strutturali. L'arrivo degli agenti di coding sposta il baricentro: l'AI è il compressore definitivo e allo stesso tempo esternalizza più velocemente di chiunque, quindi quello che resta agli umani è la formulazione del problema e la valutazione critica del codice generato. [Fonte: raw/pillitteri/pillitteri20260512-compressori-esternalizzatori-sviluppatori.md]

- **2026-06-14** — Lovable annuncia 500 milioni di dollari di ricavi annualizzati con circa 146 dipendenti e un milione di nuovi progetti a settimana, su una valutazione di circa 6,6 miliardi: circa l'80% degli utenti è non tecnico e il nodo vero è chi manterrà tutto quel software. [Fonte: raw/pillitteri/pillitteri20260614-lovable-500-milioni-vibe-coding.md]

- **2026-08-09** — GitLab porta in beta pubblica Orbit, il grafo di contesto che indicizza l'intero ciclo di vita del software per gli agenti AI: nei test interni risposte fino a 11 volte più rapide, 4,5 volte meno token e 45 volte meno allucinazioni, con l'indicizzazione che resta fuori dall'istanza che serve gli utenti reali. [Fonte: raw/pillitteri/pillitteri20260809-gitlab-orbit-grafo-contesto-agenti-ai.md]

- **2026-08-13** — L'ecosistema degli harness aperti si affolla con l'arrivo di [[deepseek-harness]]: DeepSeek pubblica in Developer Preview con licenza MIT il runtime che fa girare i modelli V4 come agenti di codice, costruito sopra il meta-framework Cordis dove modelli, strumenti, sandbox, ciclo di esecuzione e interfaccia sono tutti plugin sostituibili. L'argomento di vendita non è scrivere codice meglio di [[claude-code]], cosa tutta da dimostrare alla versione 0.1, ma il controllo: un'azienda può montare modello, sandbox e regole di sicurezza proprie sopra la stessa base, un ricercatore può sostituire l'agent loop, uno sviluppatore indipendente può far girare tutto in locale senza mandare il codice del cliente a un servizio esterno. Il prezzo è la maturità, con il README che avverte di modifiche che romperanno la compatibilità. [Fonte: raw/pillitteri/pillitteri20260813-deepseek-harness-open-source-claude-code.md]
- **2026-08-14** — CodeGraph dà all'agente la struttura del progetto già pronta: il risparmio arriva dall'analisi sintattica (Rust e tree-sitter, database SQLite FTS5) e non da embedding o GPU, e non compete con i compressori di token ma agisce a monte sul recupero del contesto. [Fonte: raw/pillitteri/pillitteri20260814-codegraph-token-agenti-coding.md]



- **2026-09-07** — Il punto sull'AI nello sviluppo software: l'80% del codice di Anthropic scritto da Claude ma solo il 20% dei compiti delegabile per intero, la tassa di verifica misurata da DORA e METR (19% di tempo in più per chi usa l'AI, percependo il contrario), la duplicazione di codice cresciuta dell'81% secondo GitClear e il codice meno sicuro e più "fiducioso" dello studio di Stanford. [Fonte: raw/pillitteri/pillitteri20260907-ai-sviluppo-software-non-delegare-tutto.md]
- **2026-09-13** — Due strumenti si aggiungono alla filiera: [[openresearch]] di alphaXiv trasforma [[claude-code]] in un agente di ricerca scientifica che propone idee, modifica codice, avvia esperimenti e decide i passi successivi, con esperimenti archiviati con log e diff collegati; [[understand-anything]] trasforma codebase in knowledge graph interattivi con una pipeline di agenti. Un ingegnere di Google Cloud ha intanto sviluppato un'app completa in ventisei minuti sul palco, da uno schizzo su carta a database e dashboard in tempo reale con revisione di sicurezza e deploy. [Fonte: raw/puntate/ainews20260913.md]
- **2026-09-17** — Uno studio valuta sette modelli su tre harness — [[claude-code]], [[codex]] e [[pi]] — e trova che la scelta dell'harness ha poco effetto sul tasso di successo ma cambia significativamente il costo: un harness semplice può competere e quello nativo non è sempre il migliore. [Fonte: raw/puntate/ainews20260917.md]
- **2026-09-17** — [[macaly-cloud]] separa il codice dal resto: hosting, database, autenticazione, domini, pagamenti, SEO e analisi senza agente di coding incluso, da abbinare a ChatGPT o Claude per la scrittura del codice. Gratis fino al primo ottobre, poi dieci dollari al mese. [Fonte: raw/puntate/ainews20260917.md]
- **2026-09-18** — Bend 2 è un linguaggio di programmazione che blocca gli errori dell'IA tramite proof checking, la stessa tecnica usata dai laboratori per risolvere problemi matematici aperti: molto veloce, gira su GPU ed è open source. [Fonte: raw/puntate/ainews20260918.md]
- **2026-08-25** — Google Labs annuncia [[play-with-putty|Play with Putty]] e il vibe coding diventa un'attività di gruppo: più persone entrano nello stesso spazio, chiunque nella stanza scrive un prompt in linguaggio naturale e il modello aggiorna il progetto per tutti nello stesso istante, senza salvare e ricaricare, mentre il risultato resta uno strumento o un sito usabile e non un'anteprima statica. [Fonte: raw/pillitteri/pillitteri20260825-google-labs-play-with-putty-vibe-coding-multiplayer.md]
- **2026-09-10** — [[emergent]] inizia a proporre ai propri utenti attivi il Dedicated Engineer Program, con uno sviluppatore senior in carne e ossa al fianco del cliente su funzionalità, correzioni e messa in produzione: la lettura è che i progetti seri sbattono prima o poi contro il muro dell'ultimo tratto, tra casi limite della logica di business, pagamenti che vanno in errore, migrazione del database, sicurezza e deploy sotto traffico vero, e che è proprio l'ultimo 20 per cento del lavoro a valere l'80 per cento della fatica. [Fonte: raw/pillitteri/pillitteri20260910-emergent-ingegneri-umani-vibe-coding.md]
- **2026-09-24** — Circuit World è una piattaforma EDA più MCAD AI-native per progettare, iterare, collaborare e produrre hardware nel browser: parte da oltre ottomilaottocento schede esistenti, permette modifiche con IA dal PCB all'assemblaggio meccanico e invia direttamente in produzione. [Fonte: raw/puntate/ainews20260924.md]
- **2026-09-10** — La conclusione della fonte è che il modello che si sta affermando mette l'AI accanto agli sviluppatori e non al loro posto, con l'umano nei punti di attrito: la prova è che anche gli strumenti nati per non avere sviluppatori, dagli agenti di coding più potenti alle piattaforme di app builder, continuano a costruire ponti verso il lavoro umano. [Fonte: raw/pillitteri/pillitteri20260910-emergent-ingegneri-umani-vibe-coding.md]
- **2026-09-25** — Un tool su GitHub con due virgola otto milioni di stelle prende un URL e ricostruisce l'intero sito uno a uno: analizza la pagina, smonta i componenti, estrae gli asset e ricostruisce il layout generando il sito completo, ed è usabile con Claude Code e Cursor. Nello stesso giorno la lista dei quindici progetti per agenti raggiunge un milione centosettantamila stelle combinate. [Fonte: raw/puntate/ainews20260925.md]
- **2026-05-25** — A luglio 2025 il marketplace giapponese Mercari ha lanciato il progetto interno pj-double con l'obiettivo dichiarato di raddoppiare la produttività dello sviluppo software entro fine anno: sei mesi dopo, nel report tecnico firmato da Yu Nakai, VP of Engineering Office di Merpay, i team che adottavano la metodologia Agent Spec-Driven Development registravano un incremento di velocità del 150 per cento rispetto alla baseline tradizionale e dell'80 per cento rispetto agli approcci AI generici basati su prompt liberi. [Fonte: raw/pillitteri/pillitteri20260525-aidd-vs-vibe-coding-spec-driven-development-2026.md]
- **2026-05-27** — Il 2 febbraio 2025 Karpathy pubblica su X il thread che battezza il vibe coding e cambia il vocabolario degli sviluppatori, con oltre 4,5 milioni di visualizzazioni in poche settimane; un anno dopo Collins ha già nominato l'espressione parola dell'anno 2025 e Merriam-Webster l'ha registrata fra i termini di tendenza. Il lato difensivo però si legge nei numeri: il report di Apiiro documenta un'impennata del 322 per cento delle vulnerabilità di privilege escalation nelle repository dove il codice generato da AI supera la soglia critica, e lo stesso vibe code che produce app fragili alimenta dall'altra parte casi come [[malware-slop]], il pacchetto npm AI-generated che ruba file da Claude. [Fonte: raw/pillitteri/pillitteri20260527-vibe-coding-impalcatura-architettura-app-2026.md]
- **2026-09-29** — UpGuard ha individuato 16.326 database Supabase con tabelle leggibili pubblicamente analizzando circa 300.000 domini: il problema riguarda soprattutto il Row Level Security non attivato correttamente, situazione che può verificarsi quando tabelle e backend sono generati programmaticamente da strumenti di coding AI, e più della metà dei database esposti mostrava indicatori di dati personali. [Fonte: raw/controrumore/controrumore20260929-diario-ai-quando-lai-ci-convince.md]
- **2026-10-02** — Una guida chiarisce la differenza tra UX (User Experience) e UI (User Interface), due discipline spesso confuse perché lavorano fianco a fianco sullo stesso prodotto digitale: la UX riguarda il funzionamento del prodotto nel suo insieme e il percorso completo di chi lo usa, la UI lo strato visivo e i punti di contatto come pulsanti, icone, colori e tipografia. Il termine UX lo ha coniato Don Norman nel 1993 quando lavorava in Apple come User Experience Architect, e lo standard ISO 9241-210 lo definisce come le percezioni e le reazioni di una persona che risultano dall'uso o dall'uso previsto di un sistema. La differenza non è accademica, perché decide chi viene assunto per fare cosa e con quali strumenti, e vale anche per i prodotti generati con l'aiuto di un modello. [Fonte: raw/pillitteri/pillitteri20261002-ux-ui-differenza.md]
- **2026-10-05** — Capcom si prepara a «un futuro in cui creeremo giochi insieme all'AI» ed evolve il proprio RE Engine verso un «AI-generation game engine»: l'AI punta prima sui flussi di sviluppo e sull'efficienza, per gestire produzioni sempre più onerose come quelle di Resident Evil, non sulla generazione di asset. [Fonte: raw/myclaw/myclaw20261005-airbnb-keeps-agents-outside.md]
- **2026-10-08** — Il Developer Survey 2026 di Stack Overflow su 30.903 sviluppatori in 169 Paesi mostra un'adozione quotidiana dell'AI in rapida crescita insieme a burnout e cautela: quasi due terzi usano assistenti o agenti di coding, ma meno del 10 per cento affiderebbe loro decisioni importanti senza controllo umano, un terzo circa è insoddisfatto del proprio ruolo e il 21 per cento indica burnout o stanchezza tecnologica. [Fonte: raw/controrumore/controrumore20261008-diario-ai-lai-entra-nella-zona-grigia.md]
- **2026-10-09** — Su DeepSWE vietare a Sonnet 5.5 high di scrivere test in autonomia ha prodotto tassi di successo leggermente superiori, con meno tempo e token spesi: il 65 per cento dei test scritti erano unit test e il 35 per cento integration test, e nessuno dei due ha migliorato i risultati, secondo un'analisi per cui i test scritti dall'agente spesso ripetono l'implementazione senza valore aggiunto. [Fonte: raw/puntate/ainews20261009.md]
- **2026-10-09** — La riscrittura della cronologia di Strata, 845 commit sostituiti per togliere i trailer di Claude in un progetto con 1.712 fork, riapre il tema della tracciabilità dei commit prodotti dagli agenti: il maintainer parla di "cleanup" senza spiegare cosa andasse ripulito, mentre la community si è spaccata tra chi vede il trailer come pubblicità non voluta e chi contesta il rebase silenzioso su un ramo pubblico. [Fonte: raw/pillitteri/pillitteri20261009-strata-riscrive-cronologia-github-firme-claude.md]
- **2026-10-10** — Una ricerca su circa 300 milioni di eventi di sviluppo in 718 imprese collega l'adozione degli agenti AI a un aumento del 30 per cento delle righe di codice e del 23 per cento delle pull request, ma anche a un tempo di revisione superiore del 49 per cento senza un incremento altrettanto chiaro delle funzionalità completate. [Fonte: raw/controrumore/controrumore20261010-diario-ai-lai-decide-ma-chi-ne-risponde.md]
- **2026-10-10** — I port non ufficiali di videogiochi nel browser si appoggiano agli agenti di coding: Maurice Heumann ha raccontato di aver fatto lavorare 17 agenti AI in parallelo sul porting di Modern Warfare 2 per PC e ChrisFirst ha costruito Fallout: New York con Claude Opus 5.5, mentre il giornalista di Kotaku Lewis Parker collega a Opus 5.5 l'ondata di emulatori e giochi decompilati comparsi nelle ultime settimane, un lavoro che richiedeva mesi e che ora si lascia in coda una notte. I publisher rispondono con le diffide, una alla volta: Bethesda ha chiesto a ChrisFirst di fermarsi e i filmati di Heumann sono stati rimossi su segnalazione di Activision. [Fonte: raw/pillitteri/pillitteri20261010-black-ops-zombies-skate-3-halo-browser-gratis.md]
- **2026-10-13** — Cockroach Labs descrive cinque mesi di esperimento con agenti AI assegnati a pianificazione, scrittura e revisione del software: oltre un milione di righe di codice, più di 1.200 richieste di modifica e sette ripristini, con l'approvazione umana resa di nuovo obbligatoria dopo una fase di integrazione automatica. L'esperienza mostra la necessità di adeguare i controlli alla velocità di produzione degli agenti, senza dimostrare risultati generalizzabili. [Fonte: raw/controrumore/controrumore20261013-diario-ai-lai-sa-dove-abiti-e-chi.md]
- **2026-10-13** — Esce AGENT-ENGINEER, plugin open source per assistenti di programmazione AI con 11 skill, 4 subagent e 5 hook contro le sfide di ingegneria agentica. [Fonte: raw/tldr/tldr20261013.md]



- **2026-10-14** — La CMU addestra un modello da quattro miliardi di parametri a riscrivere l'harness degli agenti: legge il report dell'ultima run, propone modifiche e tiene quella che performa meglio, portando la qualità delle modifiche su task mai visti da 0,32 a 0,62 e facendo scendere gli edit rotti dal 38 al 15 per cento. Cinque edit in sequenza pareggiano o battono otto tentativi paralleli e il metodo funziona oggi con qualsiasi agente. [Fonte: raw/puntate/ainews20261014.md]
- **2026-10-15** — Otto app desktop fanno lavorare più agenti di programmazione in parallelo sullo stesso progetto — Claude Code, Codex nell'app di ChatGPT, Cursor, Antigravity, GitHub Copilot, JetBrains Air, Devin Desktop e Zed — e a queste si aggiungono tre orchestratori di terze parti (Conductor, Superset e OpenCode desktop), che non hanno modelli propri e lanciano gli agenti degli altri. Le differenze stanno in dove girano gli agenti, come si tengono separati i file (worktree Git, container o macchina remota) e chi paga il conto dei modelli: nessuna delle otto documentazioni dichiara un numero massimo di agenti. Le guide di JetBrains Air e Zed avvertono che le sessioni aperte nello stesso task senza worktree condividono la copia di lavoro e possono sovrascriversi, e nessuna documentazione stima quanto consumi un lavoro in parallelo rispetto a uno in sequenza. [Fonte: raw/pillitteri/pillitteri20261015-app-desktop-agenti-ai-parallelo-confronto.md]
- **2026-10-16** — [[cohere]] e [[programench]]: i team di agenti battono il singolo fino a dieci punti ma costano tre-sette volte tanto, e in un caso la spesa scende da 510 a 155 dollari con perdita contenuta. Vale per quel benchmark. [Fonte: raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md]
- **2026-10-18** — La decompilazione "matching", che ricostruisce un codice capace di riprodurre byte per byte l'originale, dà a un agente IA un segnale chiaro di riuscita o fallimento e alimenta cataloghi come allrecomps.com, che al 18 ottobre 2026 elenca 211 progetti su oltre 25 piattaforme. Una lista di Capital and Compute aggiornata all'11 ottobre cita Super Smash Bros. Melee al 100% (19.828 funzioni), Snowboard Kids 2 al 100% in 596 giorni e Super Mario 64 DS al 99,9%, con Claude e Codex nei registri dei progetti, ma su Melee l'IA ha chiuso la coda di un lavoro umano iniziato sei anni prima e Pilotwings 64 è stato completato in 74 giorni senza agenti. Il 1° ottobre 2026 una persona che si firma Funky90sLion ha pubblicato un elenco di 41 decompilazioni e ricompilazioni fatte a mano, in risposta a una raffica di port prodotti con l'IA e poco collaudati. [Fonte: raw/pillitteri/pillitteri20261018-giochi-decompilati-ricompilati-pc-allrecomps.md]
- **2026-10-19** — Il progetto PostgreSQL ha spostato la disponibilità generale della versione 19 a circa il diciannove novembre e rinviato otto-dieci funzioni dopo aver trovato difetti durante la beta: un committer attribuisce parte dei revert alle revisioni assistite da modelli linguistici, che hanno individuato rapidamente problemi architetturali e casi limite, ma i manutentori devono ancora valutare e correggere i difetti e la revisione AI non è indicata come unica causa del ritardo. [Fonte: raw/controrumore/controrumore20261019-diario-ai-regole-investimenti-e-nuovi.md]

- **2026-10-19** — Il team di [[claude-code]] ha ristrutturato il proprio processo di code review per gestire un volume crescente automatizzando la maggior parte delle fasi: revisione continua, verifiche automatiche, controlli a più livelli prima dell'intervento umano e un sistema di approvazione a livelli di rischio. [Fonte: raw/tldr/tldr20261019.md]
- **2026-10-19** - GTA 4 gira su Android con il port non ufficiale LibertyRecompAndroid, che ricompila in anticipo il codice PowerPC della versione Xbox 360 in C++ per ARM invece di emularlo: il fork dell'utente vaduur, basato su Liberty Recompiled e ReXGlue, ha una release pubblica dal 14 ottobre, ma il README chiarisce che il gioco non � incluso e serve una copia acquistata legalmente. L'autore ammette di aver scritto il port con Claude e lo definisce "pure 100% AI slop", senza assumersi responsabilit� sull'instabilit�; la legalit� della ricompilazione statica resta un'interpretazione e Take-Two non ha commentato. [Fonte: raw/pillitteri/pillitteri20261019-gta-4-android-port-tweet-virale-legale.md]
- **2026-10-31** — [[cisco]] ha dato token AI illimitati a un solo ingegnere, Padmanabhan Krishnamurthy, perché riscriva il 98% del codice legacy dell'azienda in 24 mesi con una squadra di due persone, con quattro settimane iniziali per provare che la strada regge. Il traguardo è annunciato e non misurato, mentre il 27 ottobre Amazon ha pubblicato un memo che boccia il consumo di token come metrica del lavoro degli sviluppatori. [Fonte: raw/pillitteri/pillitteri20261031-cisco-token-ai-illimitati-27enne-codice-legacy.md]














































## Collegamenti

- [[bend-2]]
- [[circuit-world]]

- [[agenti-ai]]
- [[claude-code]]
- [[deepseek-harness]]
- [[openresearch]]
- [[understand-anything]]
- [[macaly-cloud]]
- [[metr]]
- [[sicurezza-ai]]
- [[lovable]]
- [[coderblock]]
- [[gitlab]]
- [[programench]]
- [[videogiochi-ai]]
- [[index]]
- [[vercel-ci]]
