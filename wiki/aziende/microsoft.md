---
title: "Microsoft"
category: azienda
tags: [microsoft, 3d, agent, azure, big-tech, cloud, coding, documenti, hardware, imaging, llm, multimodale, open-source, sicurezza, usa]
related_puntate: [20260508, 20260510, 20260511, 20260519, 20260526, 20260527, 20260528, 20260529, 20260530, 20260531, 20260602, 20260603, 20260604, 20260616, 20260618, 20260624, 20260625, 20260627, 20260630, 20260709, 20260718, 20260723, 20260728, 20260730, 20260802, 20260805, 20260808, 20260826, 20260907, 20260908, 20260910, 20260926, 20260927, 20260930, 20261002, 20261008, 20261009, 20261010, 20261013, 20261016, 20261019]
created: 2026-08-12
updated: 2026-10-31
---

# Microsoft

## Introduzione

Big tech statunitense, partner strategico di OpenAI ed espansosi in Asia con modelli propri open source. Nel periodo ha pubblicato Mage-Flow (image generation), Mage-VL 4B (video in streaming), la famiglia computer-use Fara 1.5, VibeVoice-ASR-BitNet, TRELLIS 2 per il 3D e Skill Recorder per l'automazione dei task.

## Modelli

- [[claude]]
- [[fara-1-5]]
- [[mage-vl-4b]]
- [[mai-code-1-flash]]
- [[mai-image-2-5]]
- [[mai-realtime]]
- [[mai-thinking-1]]
- [[mai-transcribe-1-5]]
- [[mai-voice-2]]
- [[o-voxel]]
- [[vibevoice-asr]]
- [[vibevoice-asr-streaming-7b]]

## Strumenti

- [[agent-governance-toolkit]]
- [[agent-plugins]]
- [[argusagent]]
- [[autogen]]
- [[bitnet-cpp]]
- [[claude-ads]]
- [[claude-code]]
- [[data-formulator]]
- [[github-copilot]]
- [[markitdown]]
- [[frognano]]
- [[ollama]]
- [[openclaw]]
- [[orchard]]
- [[project-solara]]
- [[rampart]]
- [[semantic-kernel]]
- [[skillopt]]
- [[surface-laptop-ultra]]
- [[tgrep]]
- [[webwright]]

## Timeline delle notizie

- **2026-05-08** — Microsoft ha rilasciato un corso gratuito di dodici lezioni su agenti AI, con codice reale ed esercizi, in cui CrewAI permette di costruire il primo crew multi-agente in meno di tre ore; CrewAI è usato dal 60% delle Fortune 500.
- **2026-05-10** — Microsoft ha pubblicato AI-Agents-for-Beginners, dodici lezioni gratuite su agenti IA, e mantiene qlib, la piattaforma completa di investimento quantitativo, tra gli undici repository che distillano cervelli brillanti in IA installabile.
- **2026-05-11** — Microsoft ha rilasciato un tool no-code open source per analisi dati: drag and drop, scrivi cosa vuoi e l'IA costruisce grafici, trasforma dati e scrive SQL, funzionando su screenshot, CSV e database live con OpenAI, Claude o Ollama locale.
- **2026-05-19** — Microsoft ha rilasciato un modello da 4 miliardi di parametri che trasforma qualsiasi immagine in asset 3D completo in tre secondi: usa il formato geometrico O-Voxel e converte tutto in mesh con texture in meno di 100 millisecondi su CUDA, con output GLB e materiali PBR completi per Blender, Unity e Unreal, completamente open source.
- **2026-05-26** — Microsoft ha rilasciato Webwright (aggiornamento di Playwright per agenti) e ha bloccato l'uso di Claude Code agli ingegneri interni: il motivo è che il costo dell'AI ha superato il costo dell'assunzione umana, un ribaltamento delle premesse sull'adozione AI.
- **2026-05-27** — Microsoft ha reso open-source Agent Governance Toolkit, che intercetta ogni tool call prima che parta con policy engine YAML (allow, deny o richiesta di approvazione umana), identity zero-trust via SPIFFE, DID e mTLS, sandbox di esecuzione a quattro livelli e audit log Merkle tamper-evident; copre tutti e dieci i rischi OWASP Agentic Top Ten ed è compatibile con LangChain, CrewAI, AutoGen, OpenAI Agents SDK e Semantic Kernel in Python, TypeScript, Go, Rust e .NET.
- **2026-05-28** — Microsoft ha rilasciato RAMPART, framework pytest per testare agenti AI: attacchi adversarial, failure mode benigni, categorie di harm e assertion-based evaluation, 100% pytest-native, si integra nella suite esistente per chi shippa agenti in produzione.
- **2026-05-29** — Microsoft ha rilasciato SkillOpt, framework per addestrare le skill degli agenti come reti neurali, e un corso completo su AI gratuito e open source su GitHub (neural network, computer vision, NLP, transformer, BERT, LLM, generative AI, reinforcement learning, multi-agent, etica).
- **2026-05-30** — Microsoft ha rilasciato un modello che da una singola immagine genera un 3D completo di texture in tre secondi, con export pronto per Blender, Unity e Unreal; open source e gratuito.
- **2026-05-30** — Uno screenshot trapelato il 30 maggio ha mostrato la futura super app di Microsoft: un'unica applicazione che raccoglie la chat di Copilot, GitHub Copilot, il gestore di attività Cowork e il nuovo strato agentico Autopilot, con un agente proattivo battezzato [[scout]]. Il progetto è guidato da [[jacob-andreou]], a capo di Copilot, con lancio indicato entro fine estate 2026; Microsoft ha rifiutato di commentare il leak.
- **2026-05-31** — Microsoft ha pubblicato MarkItDown (100000 stelle, file a Markdown pulito) e sta preparando nuovi modelli per l'annuncio del 2 giugno: MAI Voice 2 (multilingua, 15 nuove lingue, spettro emotivo più ampio), MAI Transcribe 1.5 (speech-to-text) e MAI Image 2.5 (già in preview su LM Arena, con upload file e image editing).
- **2026-06-02** — Microsoft Ads è tra le piattaforme coperte dai centonovanta controlli di audit della skill gratuita Claude Ads.
- **2026-06-02** — Microsoft presenta al Build 2026 Intelligent Terminal, fork open source di Windows Terminal con un agente AI nell'agent pane: intercetta i comandi che falliscono e propone la correzione, avvia task in background, ripristina le sessioni e parla con le CLI degli agenti via Agent Client Protocol; Microsoft lo tiene fuori dal ramo principale, che continua a sviluppare in parallelo, e depreca Terminal Chat nel canale Canary.



- **2026-06-03** — Microsoft ha rilasciato MAI-Thinking-1, modello reasoning ottimizzato per i chip MAIA 200, e MAI-Transcribe-1.5, trascrizione vocale molto veloce.
- **2026-06-03** — Satya Nadella presenta al Build di San Francisco MAI-Code-1-Flash, primo modello di coding costruito interamente in casa senza dati di OpenAI, e lo mette gratis nel selettore di GitHub Copilot su VS Code: è la mossa con cui Redmond passa dal consumare un modello di frontiera al partecipare alla frontiera e riduce la dipendenza da OpenAI.



- **2026-06-04** — Microsoft ha annunciato MAI-Thinking-1, il suo primo modello di reasoning interno, e l'app ufficiale di OpenClaw con controllo di Windows in container.
- **2026-06-16** — Microsoft ha rilasciato MAI-Code-1-Flash, il suo modello di programmazione proprietario, gratuito su tutti i livelli di GitHub Copilot, e ha pubblicato un modello da quattro miliardi di parametri per esplorare codebase che riduce i costi token dal dieci al cinquanta percento.
- **2026-06-18** — Microsoft presenta SkillOpt, che ottimizza i documenti skill degli agenti come se fossero reti neurali: epoca, batch e learning rate applicati alla documentazione, con miglioramenti su GPT cinque punto cinque di ventitré punto cinque punti senza toccare i pesi del modello.
- **2026-06-19** — Il framework open source Presidio, sviluppato da Microsoft dal 2018, torna al centro dell'attenzione come scudo per le PII verso gli LLM: individua e anonimizza nomi, email, telefoni e carte di credito prima che il modello li veda.



- **2026-06-24** — Microsoft MarkItDown converte PDF, Word, PPT, Excel, immagini, audio e HTML in Markdown pulito: supporta centosessanta lingue ed è ideale per preprocessing RAG e knowledge base.
- **2026-06-25** — Microsoft è tra gli otto provider dell'API unificata di generazione immagini lanciata da OpenRouter.
- **2026-06-27** — Ha rilasciato bitnet.cpp come open source, framework di inferenza a un bit per eseguire modelli da 100 miliardi di parametri su CPU senza GPU.
- **2026-06-30** — Claude è ora disponibile in Microsoft Foundry, ospitato su Azure: i clienti Azure ottengono Claude Opus 4.8 e Claude Haiku 4.5, con autenticazione Azure, fatturazione e pensionamento degli impegni inclusi.
- **2026-07-07** — Il 2 luglio 2026 Microsoft annuncia la Frontier Company, unità da 2,5 miliardi di dollari che manda 6.000 esperti di ingegneria dentro le aziende clienti per costruire e mantenere i sistemi di IA, guidata da Rodrigo Kede Lima; tra i primi clienti London Stock Exchange Group, Unilever, Land O'Lakes e Novo Nordisk.



- **2026-07-09** — Microsoft lancia MarkItDown, tool Python che converte quasi ogni file in Markdown pulito: PDF, Word, PowerPoint, Excel e immagini, centomila stelle su GitHub, tool ufficiale open source con uso commerciale libero.
- **2026-07-18** — Microsoft ha presentato Surface Laptop Ultra, primo PC Windows con chip ARM di NVIDIA: include RTX Spark e fino a centoventotto gigabyte di memoria unificata, progettato per eseguire agenti IA in locale, uscita prevista nel secondo semestre dell'anno.
- **2026-07-23** — Da Microsoft Asia è arrivato Mage-Flow, modello da quattro miliardi di parametri per image generation ed editing: quattro step in meno di un secondo a 1024x1024, supporta fino a 4K ed è open source.
- **2026-07-27** — Microsoft AI presenta MAI-Cyber-1-Flash, primo modello interno per la sicurezza informatica, dentro MDASH, l'impalcatura multi-agente che cerca e corregge vulnerabilità: rivendica il 95,95% su CyberGym e porta MDASH fra i sei contributi tecnici della Open Secure AI Alliance.



- **2026-07-28** — Ha rilasciato Mage-VL 4B, un modello visivo streaming che descrive eventi live mentre accadono: puoi chiedergli quando arriva il treno o quando viene segnato un goal.
- **2026-07-30** — Ha rilasciato VibeVoice-ASR-BitNet, la versione a 1,58 bit del modello di trascrizione multilingue che funziona in tempo reale su CPU e supera Whisper nei benchmark. TRELLIS 2 crea asset 3D production-ready da immagine in tre secondi: modello da quattro miliardi di parametri con PBR completo, gestione di capelli, tessuti, vetro e geometrie non-manifold, export .glb pronto per Unity, Unreal e Blender.
- **2026-08-02** — TestingCatalog individua MAI Realtime nel MAI Playground, in early access e senza annuncio ufficiale: è il primo modello vocale nativo in tempo reale costruito internamente da Microsoft, full-duplex, con 17 lingue tra cui l'italiano, le voci Victoria e Grant e due modalità di gestione del turno di parola (Switchboard con l'endpointer MAI-Ears e una modalità deterministica con endpointer semantico basato su Whisper); nessun benchmark pubblicato, nessun prezzo e nessuna data di apertura.
- **2026-08-02** — Ha rilasciato Skill Recorder: registri lo schermo mentre fai un task e il sistema converte tutto in documentazione e automazione, trasformando le azioni in API e comandi stabili; compatibile con Microsoft Scout e Microsoft 365 Copilot Cowork.
- **2026-08-05** — Microsoft ha rilasciato Orchard, infrastruttura open source per training, reinforcement learning e testing di agenti, con tre direzioni: Orchard-SWE, Orchard-GUI e Orchard-Claw.
- **2026-08-08** — Microsoft partecipa alla standardizzazione di Agent Plugins e ha rilasciato un creatore automatico di Skills per IA: registri una volta la tua azione e diventa skill per l'agente, rilevando click, cambio app, finestre e web, con narrazione vocale opzionale e CLI GitHub Copilot per generare skill.

- **2026-08-13** — Microsoft avvia la fusione delle due app Copilot, consumer e business, nella prospettiva di una super app, con icona ridisegnata, una sola icona sulla barra delle applicazioni e l'indirizzo della versione commerciale che passa da m365.cloud.microsoft a copilot.cloud.microsoft; contestualmente chiude cinque funzioni consumer entro il 18 agosto — chat di gruppo, podcast AI, Copilot Labs, Deep Research e la mascotte Mico — con Researcher al posto di Deep Research per i paganti, e il dirigente Jacob Andreou motiva la scelta dicendo che ogni funzione deve giustificare la propria esistenza con l'uso effettivo.

- **2026-08-26** — Microsoft ha rilasciato un framework di inferenza a un bit: esegue modelli massicci da cento miliardi di parametri direttamente su CPU senza GPU, con ottantadue percento di energia in meno, sei volte più veloce e cento percento open source.
- **2026-09-04** — Avvia il rollout limitato di [[gpt-6-astra]] su Azure e Foundry il 3 settembre, prima che il modello arrivi agli abbonati ChatGPT paganti.
- **2026-09-07** — Microsoft ha rilasciato VibeVoice-ASR-Streaming-7B, modello streaming che trascrive e distingue in tempo reale chi ha detto cosa con dieci lingue e hot-word personalizzate, e MarkItDown ha raggiunto 100.000 stelle come tool Python che converte PDF, Word, PowerPoint, Excel e immagini in Markdown per workflow RAG.
- **2026-09-08** — Ha rilasciato tgrep: ricerca in code base con client-server, 7-50x più veloce di ripgrep e ugrep, Rust MIT, rispetta gitignore, già integrato in GitHub Copilot CLI.
- **2026-09-05** — La clausola sull'AGI che regolava il rapporto con [[openai]] non esiste più: la partnership del luglio 2019 legava i diritti di Microsoft sulla proprietà intellettuale e l'esclusiva sulle API Azure "per le tecnologie pre-AGI", e nel dicembre 2024 la soglia era stata spostata su una definizione finanziaria (100 miliardi di dollari di profitti per i primi investitori), con un panel indipendente a verificare l'eventuale annuncio dall'ottobre 2025. Il 27 aprile 2026 i due accordi sono stati riscritti: la licenza di Microsoft è diventata non esclusiva, Redmond ha smesso di versare una quota dei ricavi e i pagamenti di OpenAI proseguono fino al 2030 a prescindere dai progressi tecnologici. È il motivo per cui cinque mesi dopo [[greg-brockman]] può dire "era dell'AGI" senza che scatti nulla.
- **2026-09-10** — Microsoft ha costruito FrogNano, un agente di coding da quattro miliardi di parametri addestrato su circa millecinquecento ambienti software: zero distillazione, solo reinforcement learning su task sintetici calibrati sulla frontiera di apprendibilità del checkpoint corrente. Ha anche presentato ArgusAgent, sistema multi-agente con ciclo piano/esecuzione/verifica/revisione/continuazione (Manager, Planner, Engineer, Reviewer): su ventisette campagne e 1.548 ore ha richiesto intervento umano ogni 310 ore circa, con duty cycle dal 95 al 99 percento.

- **2026-09-11** — La Confederazione Svizzera avvia un test su 3.000 postazioni per sostituire Microsoft 365 con [[opendesk]], la suite open source tedesca: circa 9 milioni di franchi per la prima fase, migrazione da chiudere entro fine 2027 e le due suite in parallelo per mesi. Le ragioni dichiarate sono la protezione dei dati dalle leggi americane sul cloud, l'accesso continuo ai propri dati e il costo crescente delle licenze; sul mercato elvetico l'azienda ha annunciato investimenti per 325 milioni di franchi in infrastrutture cloud e AI. Il precedente dello Schleswig-Holstein dichiara oltre 15 milioni di euro di risparmio annuo sulle licenze.

- **2026-09-08** — David Fowler, Distinguished Engineer di Microsoft con diciotto anni in azienda e la firma su SignalR e .NET Aspire, scrive che "digitare codice è assolutamente finito": non sostiene che gli ingegneri diventino inutili, ma che il tempo scivola dal battere riga per riga al disegno del sistema, ai requisiti e alla revisione. L'argomento sta in piedi perché l'agente di [[github-copilot]] non completa più la singola riga ma prepara l'ambiente, mette mano al repository, lancia i test e apre una pull request pronta per la revisione, e secondo Windows Latest Redmond sviluppa già pezzi di Windows 11 in questo modo.

- **2026-06-02** — Al Build di San Francisco presenta **[[project-solara]]**, piattaforma chip-to-cloud per dispositivi agentici: nessun app store, nessun browser al centro, nessun desktop tradizionale. I due oggetti di riferimento sono un badge da collo e uno schermo da scrivania, entrambi su MDEP, il sistema basato su AOSP adattato all'hardware aziendale, con autenticazione Entra ID, gestione via Intune e chip Arm di Qualcomm e MediaTek; il pilota parte con AccuWeather, Best Buy, CVS Health, Levi's, Target e centinaia di dipendenti interni. Nello stesso evento arrivano i modelli MAI Voice 2 e MAI Image 2.5 e l'agente proattivo Scout della super app Copilot.

- **2026-09-17** — Fissa per il 7 ottobre 2026 a San Francisco il primo grande evento dedicato a Windows e Surface da maggio 2024, con Satya Nadella, [[jensen-huang]] e Pavan Davuluri sul palco: sul tavolo Windows, la piattaforma [[rtx-spark]] e i due dispositivi che la montano, il [[surface-laptop-ultra]] e il Surface RTX Spark Dev Box, con prezzi, configurazioni e date ancora da annunciare. Nessun debutto di Windows 12, che arriverà solo quando l'ecosistema RTX Spark sarà maturo.
- **2026-09-22** — Analisi su IA, furto di lavoro e storia: Microsoft al centro del dibattito su automazione e occupazione.

- **2026-09-22** — La Digital Crimes Unit ottiene dal tribunale federale del Distretto Est della Virginia il sequestro di 50 siti web e la disattivazione di oltre 150 domini di EvilTokens, piattaforma di phishing-as-a-service attiva da febbraio 2026 e tracciata internamente come Storm-2992, che aveva compromesso più di 12.000 caselle Microsoft 365 in oltre 10.000 organizzazioni nel mondo. È il quarantesimo sequestro giudiziario della DCU in quasi due decenni di attività e il primo diretto in modo specifico contro un servizio criminale costruito attorno all'intelligenza artificiale, non semplicemente assistito da essa: all'operazione hanno collaborato Health-ISAC, Cloudflare, Coinbase, [[openai]], Railway, SpyCloud, la Shadowserver Foundation e TRM Labs. L'11 settembre la Metropolitan Police britannica ha arrestato due uomini di 32 e 38 anni per la gestione dell'infrastruttura tecnica del servizio, poi rilasciati su cauzione.

- **2026-09-25** — Il 25 settembre Microsoft ha presentato Copilot ricostruito attorno a tre schede: Home, che riunisce chat e Cowork e permette di creare e modificare documenti Word, Excel e PowerPoint senza uscire da Copilot; Code, che costruisce app, tracker e dashboard descrivendoli in linguaggio naturale, con il codice in sandbox nel tenant aziendale; e Autopilot, l'agente con nome, ruolo e obiettivo che lavora anche quando nessuno lo usa. Home e Code partono nelle prossime settimane per le aziende del programma Frontier, Autopilot in anteprima privata entro fine mese.
- **2026-09-25** — Il prezzo del nuovo Copilot divide il lavoro in due categorie: una licenza mensile per utente (USL) per chat, Word, Excel, PowerPoint, Outlook e Teams, e la fatturazione a consumo (UBB) per Cowork, Code, Autopilot e i modelli di frontiera come Astra e Claude Fable, con FinOps for AI in Agent 365 per le soglie di spesa. I posti a pagamento di Microsoft 365 Copilot erano 30 milioni a luglio 2026, circa il 7% degli oltre 450 milioni di posti commerciali.
- **2026-09-26** — Microsoft ha riprogettato Copilot attorno a Home, Code e Autopilot: Home unifica conversazione e lavoro sui documenti Microsoft 365, Code permette di creare app, dashboard e automazioni in linguaggio naturale, Autopilot e' un agente cloud persistente con identita', memoria, computer e workspace propri, con permessi, audit e gestione dei costi.
- **2026-09-27** — Rilascia Data-Formulator, strumento per analisi dati via agente che collega CSV, Postgres, BigQuery o URL live e costruisce grafici mescolando drag-and-drop e linguaggio naturale, con l'agente che scrive SQL e trasformazioni sotto; si esegue in locale con la propria chiave API.
- **2026-09-27** — SkillOpt, il sistema che fa evolvere automaticamente le competenze degli agenti, separa i percorsi di successo dai fallimenti e scarta ogni modifica che non supera il benchmark definito, battendo prompt scritti a mano; le competenze sviluppate si trasferiscono tra modelli diversi senza lock-in.
- **2026-09-26** — Microsoft porta Copilot a sistema operativo per il lavoro: Autopilot gestisce attività lunghe in autonomia, Code costruisce app dentro il tenant aziendale, Home unisce chat e collaborazione, Office è completamente integrato e Today è un'esperienza proattiva che mostra le informazioni più importanti di Microsoft 365 senza doverle chiedere.
- **2026-09-29** — Contractor incaricati di valutare Copilot possono leggere prompt, immagini caricate e versioni modificate generate dal sistema, secondo documenti interni ottenuti da 404 Media.
- **2026-09-30** — Microsoft riduce l'ambizione di competere nel mercato degli assistenti personali generalisti e rifocalizza Copilot su produttività, lavoro e clienti aziendali: l'integrazione profonda con Microsoft 365 e i flussi delle organizzazioni diventa il vantaggio competitivo, al posto dell'esperienza conversazionale autonoma.
- **2026-09-30** — Microsoft Research presenta Quine, sistema sperimentale che collega un world model multimodale della biologia con letteratura scientifica, strumenti computazionali, wet lab e ricercatori; con il Broad Institute ha prioritizzato composti capaci di modificare stati tumorali, poi validati in laboratorio.



- **2026-10-01** — Presenta MAI-Transcribe-2-Streaming, il suo primo modello di trascrizione in streaming: parlato in testo mentre la persona parla, 60 lingue con rilevamento automatico, 2,5% di errore su AA-WER Streaming e 0,54 dollari per ora di audio in preview senza SLA.

- **2026-10-02** — Microsoft rilascia tre nuovi modelli: MAI-Transcribe 2-Streaming, MAI-Voice 2.1 e MAI-Voice 2.1-Flash, per trascrizione streaming accurata e voce naturale con meno attesa tra i turni, pensati per costruire voice agent fluidi.
- **2026-10-02** — Per circa trenta minuti il 1° ottobre 2026 l'account X ufficiale di Microsoft, oltre 13 milioni di follower, passa nelle mani di un gruppo di truffatori crypto: il profilo cambia immagine con quella di Clippy, l'assistente a forma di graffetta ritirato da Office nel 2001, segue e riposta un account impostore che prometteva il suo ritorno in cambio di like e promuoveva un token $Clippy descritto falsamente come legato a $MSFT. Microsoft riprende il controllo in circa trenta minuti e dichiara di non aver mai autorizzato il token e di valutare azioni legali, ma la dichiarazione di scuse e avviso legale viene rimossa dallo stesso account senza spiegazione poco dopo.
- **2026-10-06** — Il benchmark ThinkingBox di Microsoft indica che circa due terzi dei tentativi falliti degli agenti terminano senza che gli strumenti restituiscano un errore esplicito: un agente può eseguire chiamate formalmente valide e concludere senza allarmi, ma aggiornare il record sbagliato, saltare un passaggio o dichiarare successo prima che l'obiettivo sia raggiunto. La valutazione controlla lo stato finale del database invece dei soli log, indicando la necessità di riconciliazioni, invarianti e verifiche indipendenti dell'esito.
- **2026-10-07** — Una pagina pubblica di Microsoft descrive GPT-6.1 Sol come basato sugli stessi pesi di GPT-6 Sol ma con «two inference passes instead of three», per un profilo di servizio più efficiente, e precisa che i dettagli di architettura non vengono forniti nelle pubblicazioni rivolte ai clienti. La riga è letta come il primo indizio ufficiale dei looped transformers, ma Microsoft non usa mai il termine e né Microsoft né OpenAI hanno commentato.
- **2026-10-07** — Al keynote Windows Microsoft mostra la nuova Windows Search con «migliaia» di azioni rapide dalla barra delle applicazioni in arrivo da questo autunno, Copilot con accesso ai file del PC e modelli locali dietro un interruttore che chiede l'approvazione prima di ogni invio all'esterno, Microsoft Execution Containers in disponibilità generale, Agent 365 collegato a Windows e la configurazione di OpenClaw e altri agenti in pochi clic: Microsoft dichiara che oltre il 40 per cento dei portatili costruiti per le aziende è un Copilot+ PC e che questi eseguono in locale oltre 2.000 miliardi di inferenze al mese.



- **2026-10-08** — Microsoft rilascia MAI-Code-1.1-Flash in versione locale dentro GitHub Copilot: il modello gira direttamente sul dispositivo senza costi di inferenza per le chiamate locali, è più veloce e costa un quarto delle versioni precedenti, e dovrebbe permettere sviluppo agentico di qualità senza passare per il cloud.
- **2026-10-08** — Microsoft avvia l'iniziativa interna Windows K2 per ridurre il consumo di RAM di Windows 11 e renderlo più reattivo, con priorità ai PC da 8 GB: allocatore di memoria più efficiente, WinUI 3 ottimizzato, Chromium e WebView2 alleggeriti e precaricamento delle app rivisto, mentre l'aggiornamento 26H2 incorpora parte dei miglioramenti (test preliminari parlano di 1,5-3 GB in meno a riposo e avvii di Edge e Outlook circa il 40 per cento più rapidi); è il prerequisito per le funzioni Copilot+ sui PC con poca memoria.



- **2026-10-09** — Microsoft rilascia mxc, repository open source per l'esecuzione sandboxed di codice su Windows, con sandboxing a livello di sistema operativo realizzato insieme a Unsloth e meno di cento millisecondi di overhead.
- **2026-10-10** — Microsoft presenta Decision-1, modello pensato per decisioni rapide che sembra battere sia gli LLM generalisti sia gli altri decision model su latenza e precisione, già in test interno. Il modello si chiama Microsoft-Decision-1, poggia su Qwen3.5-9B di Alibaba post-addestrato da Microsoft, si apre dal catalogo di Microsoft Foundry, accetta solo testo e costa 0,042 dollari per milione di token in ingresso con l'output gratuito, le stesse cifre di Jev di TypeSafe; l'azienda dichiara il punteggio più alto su un confronto di 36 benchmark e 2,5 volte la velocità del secondo classificato sulla latenza mediana, senza che nessuna delle cifre sia stata riprodotta da terzi.
- **2026-10-10** — Satya Nadella pubblica su X il saggio "Models as Insider Risks in the Super Intelligence Era", in cui sostiene che i modelli di frontiera, chiusi o open weight, vanno trattati come rischi interni all'azienda e tenuti sotto controlli che stanno fuori dal modello.
- **2026-10-12** — Microsoft presenta nuovi Surface con chip Nvidia RTX Spark per eseguire le applicazioni AI in locale e una versione di Windows 11 con meccanismi di isolamento per gli agenti software: Surface Laptop Ultra parte da 2.600 dollari e la workstation RTX Spark Dev Box costa 6.000.
- **2026-10-13** — Il presidente Brad Smith chiede standard internazionali di sicurezza per l'AI paragonabili a quelli previsti per altri prodotti destinati ai consumatori, con notifiche obbligatorie alle vittime di violazioni commesse da agenti AI, valutazioni indipendenti dei modelli pericolosi e meccanismi di arresto di emergenza, indicando il Regno Unito come possibile guida di regole comuni. Le proposte non costituiscono ancora obblighi adottati dai governi.

- **2026-10-13** — Microsoft presenta Azure Maia 300, nuova generazione di acceleratori per l'inferenza AI, e annuncia un'espansione multi-gigawatt dei sistemi Maia dal 2027: secondo i test citati dall'azienda il chip genera circa il 40 per cento di token in più per megawatt rispetto ad alcune configurazioni concorrenti, con prestazioni che dipendono dai carichi scelti e impiego soprattutto interno per Azure. La famiglia Maia diventa il sistema primario di inferenza per tutti i prodotti e servizi Microsoft a partire dall'anno prossimo, con deployment multi-gigawatt, mentre Maia 200 è già attivo negli Stati Uniti, in Europa e in Australia e offre fino a 1,7 volte più token per watt in Teams e Copilot. Si tratta della terza generazione degli acceleratori progettati internamente da Microsoft, pensata anche a ridurre la dipendenza dalle GPU Nvidia.
- **2026-10-14** — Il Patch Tuesday di ottobre corregge 1.411 vulnerabilità, il totale più alto mai rilasciato in un solo mese secondo BleepingComputer, con 70 critiche delle quali 57 con esecuzione di codice da remoto e tre zero-day di cui uno solo sfruttato negli attacchi, la CVE-2026-96951 nella Windows Shell che aggira il Mark of the Web (CVSS 8,8), inserita dalla CISA nel catalogo KEV con scadenza al 16 ottobre. L'azienda e diversi analisti legano la curva crescente dei numeri — dai 206 di giugno ai 622 di luglio — alla scoperta di bug con l'intelligenza artificiale, e il responsabile di Windows ha avvertito i clienti di aspettarsi volumi più alti di aggiornamenti.
- **2026-10-16** — [[mustafa-suleyman]] annuncia modelli base MAI pre-addestrati nella classe dei 3 terabyte di parametri, costruiti interamente in-house, con post-training in arrivo.
- **2026-10-17** — Microsoft AI ha completato il pre-addestramento di [[mai-base-2|MAI-Base-2]], mixture-of-experts con 2,8 trilioni di parametri totali e 80 miliardi attivi, addestrato per 38 giorni con 16.000 GPU Nvidia GB200; il post-training è ancora in corso e l'annuncio non equivale a un prodotto commerciale.
- **2026-10-17** — I corsi AI di Microsoft sono gratuiti su Microsoft Learn e si paga solo l'esame: AI-901, AB-730 e AB-731 costano 99 dollari e l'AI-103 165; l'esame AI-900 è stato ritirato il 30 giugno 2026 e sostituito dall'AI-901, con il 55-60% delle domande su Microsoft Foundry e Python tra i prerequisiti. Corsi ed esami principali sono in 12 o 13 lingue, italiano compreso, mentre AI Skills Navigator è solo in inglese.
- **2026-10-19** — [[microsoft]] ha rilasciato [[trellis-2|TRELLIS 2]], modello da quattro miliardi di parametri che trasforma un'immagine piatta in un asset 3D completo: genera geometria aperta, non-manifold e strutture interne chiuse senza conversioni intermedie, con materiali PBR completi (roughness, metallic, transparency). Su H100 una risoluzione 512³ richiede circa tre secondi, 1024³ diciassette secondi e 1536³ sessanta secondi, con almeno ventiquattro gigabyte di VRAM; codice e pesi sono rilasciati con licenza MIT.

- **2026-10-19** — Reuters riferisce che [[microsoft]] avrebbe interrotto l'accordo per un data center che [[nscale]] sviluppa nell'Essex, secondo il Telegraph, senza commentare con l'agenzia: il progetto ha accumulato ritardi e l'alimentazione elettrica del sito potrebbe non arrivare prima degli anni Trenta. Nscale sostiene che il rapporto con Microsoft resti solido, che il problema riguardi l'area londinese e che stia cercando alternative energetiche.
- **2026-10-20** — Brandon Stirrup, Senior Business Strategy Manager della divisione Xbox, scrive su X che Xbox usa l'AI "come tutte le aziende nel 2026" e che nel settore dei videogiochi i vertici hanno paura di dirlo; meno di 24 ore dopo l'account risulta rimosso e Microsoft non ha pubblicato né una conferma né una smentita.
- **2026-10-21** — Presenta [[guardian-agents]] e il progetto Perception per osservare e limitare gli agenti AI negli ambienti aziendali, con permessi legati al compito, restrizioni su dati e sistemi e approvazione umana per le decisioni rischiose; Defender dovrebbe rilevare fino a 60 tipi di agenti introdotti dai dipendenti. Sono funzionalità e obiettivi dichiarati dall'azienda, non una valutazione indipendente della loro efficacia o del tasso di falsi allarmi. La EVP della sicurezza Hayete Gallot avverte che un agente autonomo può diventare una minaccia interna anche senza essere compromesso, perché accede a sistemi sensibili, agisce in modo imprevedibile e coordina le proprie azioni con altri agenti: Microsoft li chiama "agentic insiders" e chiede un monitoraggio continuo di permessi e comportamenti.
- **2026-10-23** — Un gruppo di agenti guidato dai ricercatori Xinzhi Zhang e Zhao Song ha contribuito alla dimostrazione della congettura Kannan-Lovász-Simonovits, aperta dal 1995: gli agenti hanno esplorato oltre cento piste e i ricercatori hanno selezionato e verificato la prova, mentre una seconda équipe pubblicava un risultato indipendente lo stesso giorno.

- **2026-10-23** — Per i data center promette più trasparenza su consumi e impatti e maggiori benefici per le comunità ospitanti.
- **2026-10-24** — Uno studio su Science ha valutato MAI-DxO, il sistema che coordina agenti per interrogare un paziente simulato, richiedere esami e formulare diagnosi: nei casi complessi del New England Journal of Medicine ha ottenuto l'83% di accuratezza contro il 36% di medici generalisti e internisti individuali con materiali di riferimento. Il confronto non includeva specialisti dei casi difficili e riguardava simulazioni, non visite reali; l'azienda avvierà valutazioni ospedaliere con Beth Israel Deaconess e i punteggi di laboratorio non dimostrano sicurezza o efficacia clinica.

- **2026-10-24** — Con Hugging Face ha pubblicato un sistema open source che valuta gli agenti software controllando lo stato finale del database invece della sola risposta testuale: secondo gli autori il fine-tuning di Qwen3.8-27B su 187 attività ha alzato di 9,08 punti percentuali il successo medio su 507 compiti, con almeno sette attività che il sistema non ha risolto. Il risultato sul benchmark non dimostra prestazioni equivalenti in produzione.
- **2026-10-24** — Il governo svedese lo indica fra gli strumenti approvati da usare al posto di ChatGPT e Claude dal 26 ottobre, dopo una stretta sulla sicurezza seguita a una revisione interna; la documentazione aggiornata al 23 ottobre ricorda che i modelli Claude di Anthropic possono essere attivi in Microsoft 365 Copilot come subfornitore, ma sono spenti di default nell'Unione europea e restano esclusi dall'EU Data Boundary.
- **2026-10-27** — Ha proposto uscite volontarie a 60.000 dipendenti in Canada, India, Regno Unito e Stati Uniti, circa il 27 per cento della forza lavoro globale: la platea potenziale non equivale a 60.000 licenziamenti, perché l'azienda non ha comunicato quante persone aderiranno né un obiettivo di risparmio. La misura segue precedenti buyout e arriva mentre crescono gli investimenti in infrastrutture AI, senza che Microsoft abbia indicato se i ruoli saranno sostituiti da automazione. La platea è quella dei dipendenti di Stati Uniti, Canada, India e Regno Unito fino al livello di vice president, con alcune squadre di data center, vendite e marketing escluse; le adesioni vanno comunicate entro l'inizio di dicembre e le uscite avvengono a fine anno, con l'azienda che si aspetta meno adesioni delle offerte. A fine giugno l'organico contava 223.000 persone, 5.000 in meno di fine 2025, dopo circa 15.000 licenziamenti nel 2025, un buyout ad aprile su 8.750 idonei e 4.800 tagli a luglio; il memo interno non nomina l'intelligenza artificiale e il nesso con i 175 miliardi di spesa in infrastrutture AI previsti per il 2026 è una lettura della stampa.
- **2026-10-30** — Nel trimestre chiuso a settembre ha contabilizzato 10 miliardi di dollari di ricavi derivanti dagli accordi commerciali con [[openai]], quasi l'11 per cento dei ricavi complessivi del periodo secondo il filing alla SEC, con i crediti verso OpenAI saliti a 7,2 miliardi a fine settembre dai 6 di giugno. Il documento non separa la quota legata alla condivisione dei ricavi da quella dei servizi Azure, quindi l'importo non è attribuibile a una sola componente.
- **2026-10-31** — Il 30 ottobre 2026 ha pubblicato su Hugging Face [[mage-vl-cowork]], modello visione-linguaggio da 4 miliardi di parametri con licenza Apache-2.0 che usa un computer alternando clic e comandi nel terminale e dichiara il 66,0% su OSWorld-Verified. Il punteggio l'ha misurato il team Microsoft in due passate e nessun provider di inferenza ospita il modello, quindi con un altro scaffold può scendere.









































































## Collegamenti

- [[agent-governance-toolkit]]
- [[agent-plugins]]
- [[anthropic]]
- [[argusagent]]
- [[autogen]]
- [[bitnet-cpp]]
- [[claude]]
- [[claude-ads]]
- [[claude-code]]
- [[fara-1-5]]
- [[github-copilot]]
- [[mage-vl-4b]]
- [[mai-code-1-flash]]
- [[mai-image-2-5]]
- [[mai-realtime]]
- [[mai-thinking-1]]
- [[mai-transcribe-1-5]]
- [[mai-voice-2]]
- [[markitdown]]
- [[ollama]]
- [[openai]]
- [[openclaw]]
- [[openrouter]]
- [[orchard]]
- [[o-voxel]]
- [[project-solara]]
- [[rampart]]
- [[semantic-kernel]]
- [[skillopt]]
- [[surface-laptop-ultra]]
- [[tgrep]]
- [[vibevoice-asr]]
- [[vibevoice-asr-streaming-7b]]
- [[webwright]]
- [[gpt-6-astra]]
- [[microsoft-learn]]
- [[index]]
- [[forward-deployed-engineering]]
