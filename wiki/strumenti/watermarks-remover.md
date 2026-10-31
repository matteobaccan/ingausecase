---
title: "Watermarks Remover"
category: strumento
tags: [claude-code, plugin, watermark, c2pa, open-source, provenienza]
related_puntate: []
created: 2026-09-21
updated: 2026-10-12
sources: [raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md, raw/pillitteri/pillitteri20260812-watermark-remover-claude-github-test.md, raw/pillitteri/pillitteri20261011-chatgpt-watermark-remover-textgrain.md]
---

# Watermarks Remover

## Introduzione

Plugin ufficiale del marketplace di [[claude-code]] che ripulisce testi e file dai marchi di provenienza inseriti dai modelli di intelligenza artificiale, pubblicato da Guillaume Meyer con licenza MIT. Il repository guillaumemeyer/watermarks-remover ha raggiunto 18.981 stelle GitHub nella giornata del 27 agosto 2026, con l'ultimo commit datato 28 agosto: la velocità della crescita dice quanto la caccia ai watermark AI sia passata da nicchia a tema mainstream nell'estate 2026, sull'onda delle polemiche sui rilevatori commerciali che segnalano come AI anche testi scritti a mano. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]

## Funzionalità principali

- **Layer A, deterministico**: rimuove i caratteri Unicode invisibili usati come firma, come lo zero-width space, i bidirectional marks, i tag characters del blocco E0000 e spazi esotici al posto dello spazio normale. È l'unico livello riproducibile al cento per cento e non degrada il senso della frase. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **Layer B, best-effort**: affronta i watermark statistici, quelli che condizionano la scelta dei token durante la generazione. Non esiste un fix deterministico, quindi il plugin propone hook di riscrittura configurabili che parafrasano il testo con un secondo modello; il README dichiara apertamente che il testo riscritto perde qualità e che quasi ogni frase porta un po' del watermark. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **Layer C, sui file**: rimuove i manifest C2PA firmati, gli EXIF e gli XMP dalle immagini, le properties dai documenti Office e le tracce SynthID; copre PNG, JPEG, WebP, AVIF, HEIC, BMP, GIF e TIFF, i documenti PDF, DOCX, XLSX, PPTX, EPUB, ODT e SVG, testo HTML e Markdown, più i formati audio e video MP4, MOV, M4A, M4V, WAV, MP3 e FLAC. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- Il C2PA non è cifrato ma firmato: il plugin non rompe la firma, semplicemente elimina il manifest, quindi per un verificatore il file risulta privo di provenienza dichiarata e non manomesso. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- Sotto il plugin restano script Python richiamabili direttamente, come service/scripts/clean_file.py, clean_text.py e inspect_image.py, così il motore è utilizzabile anche fuori da Claude Code, per esempio in una pipeline CI. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]

## Azienda / Autore

- Guillaume Meyer

## Timeline delle notizie

- **2026-08-12** — Test sistematico dei watermark remover per Claude su GitHub: claude-watermark-cleaner (144 stelle, nessuna licenza) ha buoni guardrail su codice, URL e integrità numerica ma lascia passare i variation selector, il vettore steganografico più diffuso, mentre watermarks-remover (18.981 stelle, MIT) chiude quel buco ma distrugge emoji e sequenze di variazione ideografica del giapponese e riscrive senza controlli di integrità. Sui pixel nessuno «toglie» il watermark, si rigenera l'immagine con una diffusione lossy, e battere il verificatore non rende il file forensicamente neutro perché la rigenerazione lascia una firma che un classificatore ResNet-50 riconosce con AUROC fino a 0,9999. [Fonte: raw/pillitteri/pillitteri20260812-watermark-remover-claude-github-test.md]

- **2026-08-28** — Il plugin si installa dal marketplace di [[claude-code]] con due comandi, `/plugin marketplace add guillaumemeyer/watermarks-remover` e `/plugin install watermarks-remover@watermarks-remover`, e da lì il modello invoca le operazioni come agent-skill senza che l'utente debba ricordare la sintassi degli script sottostanti. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **2026-08-28** — Il README pone una linea etica esplicita, il progetto è per contenuti che si possiedono o si è autorizzati a trattare, perché uno strumento del genere è dual-use per definizione; le zone grigie indicate sono l'accademia, dove rimuovere il watermark per aggirare i rilevatori viola i codici etici, le pubblicazioni scientifiche con obbligo di dichiarare l'uso di AI e le piattaforme che hanno iniziato a bloccare autori con troppo testo AI non dichiarato. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **2026-08-28** — Il confronto sul fronte commerciale è con rephrasy.ai, SaaS a pagamento che punta solo sul layer statistico del rewriting in cloud: scatola chiusa contro codice aperto, ma nessuna delle due strade elimina il fatto che riscrivere per cancellare un watermark statistico costa qualità. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **2026-08-28** — Il formato "agent-skill installabile via marketplace" viene letto come il nuovo modo naturale di distribuire capacità nell'ecosistema Claude Code, oltre la stagione dei repository sciolti da clonare a mano. [Fonte: raw/pillitteri/pillitteri20260828-watermarks-remover-plugin-claude-code-19mila-stelle.md]
- **2026-10-11** — I ChatGPT watermark remover ripuliscono i caratteri Unicode invisibili (spazi a larghezza zero, U+202F, joiner, BOM, trattini morbidi) ma non toccano [[textgrain]], che vive nella scelta delle parole: GPTCleanup elenca quello che cancella e mette la riscrittura a pagamento, AI Watermark Remover promette testo «pulito e non rilevabile» lavorando sullo strato sbagliato, AICheckr sostituisce token senza poter misurare il risultato perché il rilevatore di OpenAI è chiuso. [Fonte: raw/pillitteri/pillitteri20261011-chatgpt-watermark-remover-textgrain.md]




## Collegamenti

- [[agent-skills]]
- [[ai-humanize-text]]
- [[claude-code]]
- [[digital-provenance]]
- [[humanizer]]
- [[index]]
