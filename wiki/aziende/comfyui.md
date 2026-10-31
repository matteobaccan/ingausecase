---
title: "Comfy"
category: azienda
tags: [comfyui, generativo, generazione, image-gen, immagini, node-based, nodi, open-source, stabile-diffusion, video, video-ai, workflow]
related_puntate: [20260516, 20260522, 20260525, 20260601, 20260602, 20260603, 20260609, 20260611, 20260613, 20260616, 20260620, 20260624, 20260630, 20260728, 20260729, 20260811, 20260813, 20260825, 20260826, 20260828, 20260830, 20260924, 20260930, 20261001, 20261003]
created: 2026-08-12
updated: 2026-10-01
---

# Comfy

## Introduzione

Editor di pipeline visive per la generazione di immagini e video, standard di fatto della community open source. Nel periodo ha pubblicato tutorial per utility pass da footage con segmentazione SAM3 e profondità, ed è stato usato per flussi anime 2D completi in un'ora.

## Modelli

- [[birefnet]]
- [[florence-2]]
- [[flux-2-klein-4b]]
- [[gemma-4]]
- [[ideogram-4]]
- [[krea-2]]
- [[ltx-2-3]]
- [[sam2]]
- [[seedance]]
- [[stable-audio-3-0]]
- [[tripo-3-1]]
- [[triposplat]]
- [[void]]
- [[wan-animate-2]]
- [[wan-video]]

## Strumenti

- [[comfy-desktop]]
- [[comfy-mcp]]
- [[comfy-router]]
- [[comfytv]]
- [[librechat]]
- [[nexus-bta]]
- [[rebels-prompt-enhancer]]
- [[text-to-cad]]

## Timeline delle notizie

- **2026-05-16** — ComfyUI ha integrato nativamente tre nuovi modelli open source: Gemma 4 di Google DeepMind (LLM multimodale con testo, immagine, audio e video input più reasoning step-by-step integrato), VOID di Netflix (rimozione oggetti video che cancella ombre, riflessi e interazioni fisiche) e BiRefNet (segmentazione background e oggetti ad alta risoluzione).
- **2026-05-22** — ComfyUI supporta già Stable Audio 3.0 (modelli open-weight per musica con dati licenziati) ed è citato come richiesto anche per Flux 2 Klein 4B, che invece gira senza ComfyUI.
- **2026-05-25** — ComfyUI è stato citato come ambiente di esecuzione di LTX 2.3, con output in 7 minuti su RTX 4070 Ti Super.
- **2026-06-01** — ComfyUI è la piattaforma su cui gira il nuovo nodo Rebels Prompt Enhancer per l'espansione automatica dei prompt, compatibile anche con la generazione video.
- **2026-06-02** — ComfyUI ha integrato undici nuovi modelli a maggio tra immagine, 3D, audio, video e multimodale: Krea 2 per immagini style-first, VOID di Netflix per rimozione oggetti, Tripo 3.1 più TripoSplat per asset 3D end-to-end.
- **2026-06-03** — ComfyUI è la piattaforma su cui gira Nexus BTA, lo studio locale per immagini, video, workflow ed esperimenti 3D.
- **2026-06-09** — ComfyUI ha lanciato Comfy Desktop, l'app desktop ricostruita con istanze multiple e snapshot automatici.
- **2026-06-11** — ComfyUI è la piattaforma a cui ComfyTV aggiunge l'infinite canvas e l'integrazione subgraph.
- **2026-06-13** — ComfyUI Desktop permette di generare immagini, video e modelli 3D con oltre venti modelli diversi, completamente gratuito e open source.
- **2026-06-16** — Un workflow ComfyUI automatizza il face swap con Florence 2, SAM2 e WAN Video in un'unica pipeline: coerenza temporale su ogni frame, face replacement e de-aging completamente dentro ComfyUI.
- **2026-06-20** — Un workflow per ComfyUI permette di creare storyboard animati in stile Seedance su GPU da sei gigabyte VRAM: usa LTX due punto tre e Ideogram quattro per mantenere la coerenza visiva tra le scene.
- **2026-06-24** — ComfyUI supporta già Krea 2 con quantizzazione fp8, mxfp8, nvfp4 e int8, per generare immagini 4K in cinquanta secondi.
- **2026-06-30** — Ha lanciato Comfy MCP in beta pubblica, il primo MCP costruito per pipeline produttive, che connette Claude, Codex, Cursor e Hermes all'ecosistema ComfyUI.
- **2026-07-28** — Ha pubblicato un tutorial per generare utility pass direttamente dal footage: rimozione background tramite prompt, segmentazione SAM3, mappe di profondità stabili e pass normali per relighting, senza rotoscoping manuale.
- **2026-07-29** — Un creator ha costruito un'intera sequenza motion 2D ispirata agli anime dentro ComfyUI, da storyboard a render finale in un'ora, tutto in un unico workflow pipeline.
- **2026-08-11** — ComfyUI integra Wan Animate Due nativo: il driving video entra diretto nel transformer e il motion extractor viene eliminato, con migliore motion, identita' forte e camera text-driven; Wan Animate Due Lite ha latenza real-time.
- **2026-08-13** — ComfyUI supporta nativamente LTX 2.5, con Diffusion Fidelity Rendering, decoder video al posto della decodifica VAE e multi-shot nativi.
- **2026-08-25** — Custom nodes per ComfyUI generano video MiniMax-H3 lunghi fino a centoventi secondi con audio sincronizzato da un singolo prompt.

- **2026-08-26** — Wan 3.0 è ora disponibile su Comfy: trenta secondi di scena in un solo take, da 480p per la velocità fino a 1080p per la qualità produzione.
- **2026-08-28** — Comfy diventa il primo distributore commerciale delle licenze per i modelli generativi di MiniMax: quasi venti milioni di download open weight tramite Comfy, ora ottenibile licenza commerciale completa (audio, musica, video) con piano Professional ed Enterprise.
- **2026-08-30** — Kijai ha aggiunto il supporto per Minimax H3 FastVideo a ComfyUI, estendendo l'ecosistema di generazione video del progetto.
- **2026-09-24** — Lancia Comfy Router, un'unica API per i modelli frontier di immagine, video, 3D e audio: stesso nome modello e stessi argomenti a prescindere dal provider, routing esplicito verso quello nominato, submit asincrono con ID di richiesta e ritenzione di ventiquattro ore su input e output. Provider al lancio Comfy, Runware, Wavespeed, [[fal]] e [[higgsfield]].
- **2026-09-30** — Il team ufficiale apre il repository workflow_templates con tutti i template ufficiali: oltre mille stelle in pochi giorni, metadati modello, versioni dei nodi e thumbnail, sub-graph nativi riutilizzabili e un sito statico in undici lingue.
- **2026-10-01** — ComfyUI lancia Comfy API: punta l'API a un file JSON del workflow e gestisce tutto, risolvendo custom node, modelli, LoRA e dipendenze Python, blocca tutto in una build versionata e distribuisce un rilascio immutabile come endpoint autoscaling su RTX PRO 6000, H100, H200 o B200.
- **2026-10-01** — ComfyUI supera le 135.757 stelle su GitHub al 1° ottobre 2026 ed è compatibile nativamente con i chip Apple Silicon grazie al supporto Metal di PyTorch: è un'interfaccia open source per generare immagini in locale, in cui ogni passaggio della generazione (caricamento del modello, campionamento, upscaling) è un nodo collegabile in un grafo visibile e modificabile, con un'interfaccia semplificata a nodo singolo per i primi test. Su Apple Silicon la RAM è unificata, quindi la memoria disponibile per il modello è quella che resta dopo macOS e le altre app; con meno di 16 GB totali serve il flag --cpu-vae all'avvio.











## Collegamenti

- [[birefnet]]
- [[comfy-desktop]]
- [[comfy-mcp]]
- [[comfy-router]]
- [[comfytv]]
- [[florence-2]]
- [[flux-2-klein-4b]]
- [[gemma-4]]
- [[ideogram-4]]
- [[krea-2]]
- [[librechat]]
- [[ltx-2-3]]
- [[ltx-2-5]]
- [[magnific]]
- [[nexus-bta]]
- [[pruna-ai]]
- [[rebels-prompt-enhancer]]
- [[sam2]]
- [[seedance]]
- [[stable-audio-3-0]]
- [[text-to-cad]]
- [[tripo-3-1]]
- [[triposplat]]
- [[void]]
- [[minimax-h3]]
- [[wan-animate-2]]
- [[wan-video]]
- [[comfy-api]]
- [[index]]
