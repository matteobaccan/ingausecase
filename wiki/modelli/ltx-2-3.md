---
title: "LTX-2.3"
category: modello
tags: [audio, comfyui, compressione, generativo, generazione, generazione-video, lightricks, open-weight, tts, video, video-ai, voice-cloning]
related_puntate: [20260511, 20260512, 20260515, 20260525, 20260620, 20260626, 20260627, 20260630, 20260723, 20260729, 20260825]
created: 2026-08-12
updated: 2026-08-25
---

# LTX-2.3

## Introduzione

Modello di generazione video di Lightricks, esteso nel periodo con la variante IC-LoRA per il re-render da nuove angolazioni e accelerato dal decoder PrunaVAED.

## Capacità e performance

- LTX-2.3, modello per video generation, è stato compresso da 46 GB a 15 GB: 88% di riduzione sui layer Transformer con qualità quasi identica all'originale, e gira su GPU standard.
- LTX 2.3 ora fa audio standalone: zero-shot voice cloning emotivo, 8 step distillati con Gemma 3 12B, direzioni sceniche tramite tag, gira a 1,5 volte real-time su RTX 4090, supporta 13 lingue, 48kHz stereo, 16 GB VRAM e genera anche suoni ambientali abbinati.
- Da LTX-2.3 hanno estratto solo il bit audio, lo hanno fine-tuning per TTS e hanno raggiunto un controllo emotivo di altissimo livello nel generatore Scenema Audio.

## Azienda di riferimento

- [[comfyui]]
- [[fal]]
- [[lightricks]]
- [[pruna-ai]]

## Strumenti correlati

- [[3dreal]]
- [[ic-lora]]
- [[scenema-audio]]
- [[sol-video-inference-engine]]

## Timeline delle notizie

- **2026-05-11** — LTX-2.3, modello per video generation, è stato compresso da 46 GB a 15 GB: 88% di riduzione sui layer Transformer con qualità quasi identica all'originale, e gira su GPU standard.
- **2026-05-12** — LTX 2.3 ora fa audio standalone: zero-shot voice cloning emotivo, 8 step distillati con Gemma 3 12B, direzioni sceniche tramite tag, gira a 1,5 volte real-time su RTX 4090, supporta 13 lingue, 48kHz stereo, 16 GB VRAM e genera anche suoni ambientali abbinati.
- **2026-05-15** — Da LTX-2.3 hanno estratto solo il bit audio, lo hanno fine-tuning per TTS e hanno raggiunto un controllo emotivo di altissimo livello nel generatore Scenema Audio.
- **2026-05-25** — LTX 2.3 su ComfyUI modifica immagini Flux 2 con Klein, processate tramite workflow RuneXX: due LoRA per qualità e sync audio, output in 7 minuti su RTX 4070 Ti Super.
- **2026-06-20** — LTX due punto tre è uno dei modelli del workflow ComfyUI per storyboard animati in stile Seedance su GPU da sei gigabyte VRAM.
- **2026-06-26** — LTX-due punto tre ventidue miliardi è uno dei modelli su cui Sol Video Inference Engine risulta oltre due volte più veloce.
- **2026-06-27** — LTX 2.3 è il modello su cui fal ha costruito 3DREAL, IC-LoRA per trasformare render 3D, CG o di gioco in video fotorealistici mantenendo composizione e camera move.
- **2026-06-30** — Primo overall tra i modelli open weights su Video Arena: Elo di 1.138, salto di 115 punti rispetto a LTX-2 19B (attualmente quinto con 1.023).
- **2026-07-23** — LTX-2.3 IC-LoRA re-render di video esistenti da una nuova angolazione: stessa scena, stessa azione, camera diversa; scegli l'angolo e il modello lo costruisce.
- **2026-07-29** — PrunaVAED è un decoder drop-in più veloce per LTX-2.3: da 1,7 a 2,1 volte più veloce con il 50% in meno di VRAM di picco, open source.
- **2026-08-25** — LTX-2.3 Uncensored, variante senza filtri di sicurezza del modello di generazione video di Lightricks, è stata rilasciata e resa disponibile per l'uso locale.

## Collegamenti

- [[3dreal]]
- [[comfyui]]
- [[fal]]
- [[flux-2]]
- [[ic-lora]]
- [[infinitetalk]]
- [[lightricks]]
- [[pruna-ai]]
- [[scenema-audio]]
- [[seedance-2-5]]
- [[sol-video-inference-engine]]
- [[index]]

