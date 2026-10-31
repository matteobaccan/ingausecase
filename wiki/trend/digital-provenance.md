---
title: "Digital Provenance"
category: trend
tags: [autenticità, deepfake, fiducia, provenienza, regolamentazione, sicurezza]
related_puntate: []
created: 2026-09-16
updated: 2026-10-13
sources: [raw/pillitteri/pillitteri20260609-digital-provenance-gartner-trend-2026.md, raw/pillitteri/pillitteri20260609-ingegneria-fiducia-ia-autorevolezza-fonti.md, raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md, raw/pillitteri/pillitteri20260916-iphone-18-pro-reference-image.md, raw/pillitteri/pillitteri20260801-google-earth-ai-immagini-satellitari-false-ritiro.md, raw/pillitteri/pillitteri20260613-google-responsabile-ai-overview-tribunale-monaco.md, raw/tldr/tldr20261006.md, raw/pillitteri/pillitteri20260415-reverse-synthid-watermark-google-ai-spectral-analysis.md, raw/pillitteri/pillitteri20260811-claude-watermark-invisibile-testo-c2pa.md, raw/pillitteri/pillitteri20260815-distribuzione-parole-zipf-watermark.md, raw/pillitteri/pillitteri20261005-openai-textgrain-filigrana-testo-ue.md, raw/pillitteri/pillitteri20261013-chatgpt-claude-gemini-watermark-testi-ai.md]
---

# Digital Provenance

## Introduzione

Capacità di dimostrare l'origine e l'affidabilità di un asset digitale, che si tratti di software, dati, processi o contenuti multimediali: il termine arriva dal mondo dell'arte e degli archivi, dove la provenienza di un'opera è la catena documentata dei suoi passaggi di proprietà. Gartner l'ha inserita tra i dieci trend tecnologici strategici per il 2026, presentati il 20 ottobre 2025, nel cluster che associa al tema del "Sentinel" — la dimensione della protezione e della fiducia — insieme a cybersecurity preventiva, piattaforme di AI security e confidential computing. [Fonte: raw/pillitteri/pillitteri20260609-digital-provenance-gartner-trend-2026.md]

La ragione dell'urgenza è semplice: per decenni si è dato per scontato che un documento digitale fosse affidabile, ma l'AI generativa e gli attacchi alla catena di fornitura hanno mandato in frantumi quella presunzione. L'autenticità oggi non si presume più, va dimostrata. [Fonte: raw/pillitteri/pillitteri20260609-digital-provenance-gartner-trend-2026.md]

## Evoluzione nel tempo

- Gartner prevede che entro il 2029 le organizzazioni che non avranno investito adeguatamente nella provenienza digitale rischino sanzioni potenzialmente nell'ordine dei miliardi di dollari.
- Il numero di file deepfake in circolazione è passato da circa 500.000 nel 2023 a quasi 8 milioni stimati a fine 2025, un aumento di circa il 1.500% in due anni; secondo Deloitte le frodi abilitate dall'AI generativa negli Stati Uniti potrebbero salire a 40 miliardi di dollari entro il 2027 dai 12,3 miliardi del 2023, con i tentativi di frode basati su deepfake cresciuti del 2.137% in tre anni, dallo 0,1% al 6,5% del totale.
- Il Global Risks Report 2025 del World Economic Forum colloca la disinformazione al primo posto tra i rischi globali di breve termine: è la prima volta che un rischio legato all'informazione, e non a guerre, pandemie o crisi climatiche, occupa quella posizione.
- La pressione normativa trasforma la buona pratica in obbligo: dal 2 agosto 2026 l'articolo 50 dell'AI Act europeo impone di marcare i contenuti generati o manipolati dall'AI in un formato leggibile dalle macchine, con sanzioni fino a 15 milioni di euro o al 3% del fatturato globale, mentre il regolamento eIDAS 2.0 (UE 2024/1183) impone a ogni Stato membro di rendere disponibile un portafoglio europeo di identità digitale entro dicembre 2026.

## Attori coinvolti

- Lo standard di riferimento è C2PA (Coalition for Content Provenance and Authenticity), nato nel febbraio 2021 da una coalizione che riunisce Adobe, Arm, BBC, Intel, Microsoft e Truepic; la sua implementazione più diffusa sono le Content Credentials, un manifesto firmato che viaggia dentro il file e registra autore, strumenti usati, eventuale coinvolgimento dell'AI e ogni modifica significativa. C2PA è lo standard, Content Credentials il marchio e l'implementazione commerciale promossa dalla Content Authenticity Initiative di Adobe.
- Agenzie come Associated Press, Reuters e BBC hanno già adottato la firma C2PA nei propri flussi editoriali.
- Sul fronte dei watermark, SynthID di [[google-deepmind]] è citato come esempio di segnale incorporato nel contenuto invece che in un campo separabile; nella stessa direzione va Apple Reference Image, che sull'iPhone 18 Pro sposta la firma dentro il sensore. [Fonte: raw/pillitteri/pillitteri20260916-iphone-18-pro-reference-image.md]

## Notizie rilevanti

- Le quattro categorie di asset coperte: software, tracciato con la SBOM (Software Bill of Materials, la distinta base del software) e la firma degli artefatti di build; dati, di cui si tracciano fonte e trasformazioni; processi, di cui si dimostra che una procedura automatica si è svolta senza manomissioni; contenuti multimediali, certificati come autentici e non generati o manipolati.
- L'infrastruttura di autenticità poggia su tre colonne: acquisizione certificata alla fonte (metadati firmati crittograficamente al momento della creazione), catena di custodia verificabile (impronte crittografiche a ogni passaggio, secondo le procedure dello standard ISO/IEC 27037 sulle prove digitali) e integrazione nei processi esistenti, perché se verificare costa cinque passaggi manuali in più nessuno lo farà.
- Il costo dell'inazione è descritto come lineare: chi non sa dimostrare la provenienza dei propri contenuti AI viola l'articolo 50, chi subisce una frode da deepfake senza processi di verifica risponde delle perdite, un fornitore di software che non documenta le dipendenze via SBOM diventa il punto debole della catena a valle.
- L'asimmetria che resta da risolvere è che la presenza di credenziali valide prova l'autenticità, mentre la loro assenza non prova nulla: solo quando le credenziali diventeranno la norma l'assenza comincerà a essere un segnale di sospetto.

## Timeline delle notizie

- **2026-04-15** — Il repository [[reverse-synthid]] di Alosh Denny mostra che il watermark SynthID di Google è aggirabile con la sola analisi spettrale: SynthID codifica frequenze carrier a fase costante, la coerenza di fase tra immagini diverse supera il 99,5 per cento e questo permette di sottrarre i bin nel dominio di Fourier, rimuovendo il 91 per cento dell'energia del watermark con qualità quasi intatta (PSNR 43,5 dB) e un detector al 90 per cento di accuratezza. Il caso si aggiunge a UnMarker (rimozione del 79 per cento su SynthID) e a Crack in the Bark (AUC del detector Tree-Ring da 0,993 a 0,153): ogni schema di watermarking dura mesi, non anni, prima che qualcuno trovi un attacco efficace. [Fonte: raw/pillitteri/pillitteri20260415-reverse-synthid-watermark-google-ai-spectral-analysis.md]

- **2026-08-11** — Anthropic aderisce al Codice di Condotta sull'articolo 50(2) dell'AI Act e dal 2 agosto 2026 marca ogni modello lanciato da quella data: sul testo una filigrana statistica intessuta nelle parole, sui file svg, png e jpg metadati firmati C2PA che dichiarano l'origine e rilevano manomissioni. La marcatura avviene a livello di modello e vale in tutto il mondo, su API, web, Claude Code e istanze ospitate su AWS, Google Cloud e Microsoft Foundry, senza un opt-out documentato; i metadati C2PA si perdono a un ri-salvataggio, mentre il segnale nel testo sopravvive al copia-incolla. [Fonte: raw/pillitteri/pillitteri20260811-claude-watermark-invisibile-testo-c2pa.md]

- **2026-08-15** — Il watermark statistico vive nella distribuzione delle parole: la legge di Zipf garantisce che in ogni lingua esistano in continuazione scelte quasi equivalenti tra parole frequenti («di», «che», «per») e sinonimi, e il marchio abita quei bivi. La misura sul corpus del blog in 14 lingue mostra la parola più comune al 3,59 per cento in italiano («di») e al 7,36 per cento in inglese («the»), con le prime dieci parole che in olandese coprono il 27,3 per cento del testo; il rilevamento richiede testi lunghi, perché su venti parole la deviazione dal 50 per cento può nascere dal caso. [Fonte: raw/pillitteri/pillitteri20260815-distribuzione-parole-zipf-watermark.md]

- **2026-06-09** — Gartner inserisce la digital provenance tra i dieci trend tecnologici strategici del 2026, con la previsione di sanzioni nell'ordine dei miliardi di dollari entro il 2029 per chi non investe: il tema è definito come capacità di provare origine, proprietà e integrità di dati, software, contenuti e processi, e le tecnologie chiave indicate sono C2PA e Content Credentials, le firme qualificate eIDAS 2.0, i watermark come SynthID e le distinte base del software. In Italia il terreno è preparato dalla firma digitale qualificata e dalla PEC, con l'articolo 50 dell'AI Act in vigore dal 2 agosto 2026 e il primo codice di condotta attuativo pubblicato in bozza il 17 dicembre 2025. [Fonte: raw/pillitteri/pillitteri20260609-digital-provenance-gartner-trend-2026.md]
- **2026-06-09** — L'ingegneria della fiducia nell'era dell'IA, il tema del seminario del Consiglio Nazionale degli Ingegneri del 9 giugno 2026, si legge così: la fiducia sul web non è mai stata naturale ma un artefatto costruito e ricalibrato, per venticinque anni da Google, e oggi la deleghiamo a modelli linguistici che nel nucleo statistico non distinguono un paper su Nature da un video virale. La fiducia viene re-iniettata a valle, da uno strato nascosto del sistema, e il problema vero non è la qualità delle risposte ma la loro opacità. [Fonte: raw/pillitteri/pillitteri20260609-ingegneria-fiducia-ia-autorevolezza-fonti.md]
- **2026-06-13** — Il Tribunale Regionale di Monaco qualifica l'AI Overview come contenuto editoriale di Google, non intermediazione: rafforza il principio che chi pubblica una sintesi generata risponde delle sue affermazioni, con riflessi sul diritto di rettifica e sul principio di esattezza del GDPR. [Fonte: raw/pillitteri/pillitteri20260613-google-responsabile-ai-overview-tribunale-monaco.md]



- **2026-07-31** — Il watermark SynthID di Google Earth non sopravvive a uno screenshot ricampionato: il segnale statistico nei pixel degrada e gli strumenti di verifica non riconoscono più l'immagine come generata. [Fonte: raw/pillitteri/pillitteri20260801-google-earth-ai-immagini-satellitari-false-ritiro.md]

- **2026-08-28** — Il plugin [[watermarks-remover]] per [[claude-code]] arriva a 18.981 stelle GitHub mostrando il lato opposto della provenienza: elimina i manifest C2PA firmati, gli EXIF e gli XMP, le properties dei documenti Office e le tracce SynthID, oltre ai caratteri Unicode invisibili usati come firma. Il C2PA non è cifrato ma firmato, quindi il plugin non rompe la firma, rimuove il manifest: per un verificatore il file risulta privo di provenienza dichiarata e non manomesso, ed è la distinzione che conta nel dibattito legale sul tema. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **2026-08-28** — Il layer statistico resta il punto scoperto: sul watermark che condiziona la scelta dei token non esiste un fix deterministico, il costo dichiarato è la perdita di qualità del testo riscritto e quasi ogni frase porta un po' del marchio. La conclusione della fonte è che il watermark AI non è un problema binario risolvibile con un flag ma una serie di segnali stratificati, da affrontare livello per livello. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **2026-10-06** — [[openai]] annuncia che aggiungerà filigrane invisibili al testo nei risultati idonei di ChatGPT e Codex nell'Unione europea per rispettare gli obblighi di trasparenza dell'AI Act: il metodo textGrain altera in modo sottile la scelta delle parole perché il testo generato sia rilevabile, ma editing, traduzione e passaggi brevi possono indebolire il rilevamento. [Fonte: raw/tldr/tldr20261006.md] La news di Pillitteri aggiunge i dettagli del rapporto tecnico: la selezione è modellata come un problema di trasporto ottimale con costi da variabili casuali di Gumbel e regolarizzazione Kullback-Leibler, con un budget di entropia che limita la varietà sacrificata; con l'1 per cento di falsi positivi il rilevatore individua la filigrana in circa l'80 per cento dei brani da 200 token e nel 95 per cento di quelli da 400, ma la detection scende al 66 per cento con il 10 per cento delle parole sostituite e crolla al 17 per cento con il 25 per cento. Il metodo [[textgrain]] resta in opt-in per le API, per ChatGPT e Codex riguarda solo l'UE e il rilevatore è riservato a ricercatori e organizzazioni approvate. [Fonte: raw/pillitteri/pillitteri20261005-openai-textgrain-filigrana-testo-ue.md]
- **2026-10-13** — A ottobre 2026 tre chatbot marcano i testi generati: Claude lo fa in tutto il mondo sui modelli supportati, Gemini nell'app dal 2024 e ChatGPT lo porterà nelle prossime settimane solo nell'Unione europea, mentre Copilot, Mistral e Meta AI non documentano alcuna filigrana. La spinta è l'articolo 50 dell'AI Act in vigore dal 2 agosto 2026, che chiede di marcare i contenuti sintetici in un formato leggibile dalle macchine: circa 190 organizzazioni hanno firmato il Codice di condotta che accompagna l'obbligo, ma ogni fornitore lo applica a modo suo. [Fonte: raw/pillitteri/pillitteri20261013-chatgpt-claude-gemini-watermark-testi-ai.md]







## Collegamenti

- [[apple]]
- [[attacco-supply-chain-npm]]
- [[cybersicurezza]]
- [[deepfake]]
- [[google-deepmind]]
- [[regolamentazione]]
- [[sicurezza-ai]]
- [[synthid-bio]]
- [[index]]
