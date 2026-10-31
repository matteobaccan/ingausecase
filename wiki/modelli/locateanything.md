---
title: "LocateAnything"
category: modello
tags: [grounding, nvidia, open-weight, vision]
related_puntate: [20260603, 20260617]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260603.md, raw/puntate/ainews20260617.md]
---

# LocateAnything

## Introduzione

Modello NVIDIA di grounding visivo che predice l'intera bounding box in un unico passaggio invece che in sequenza.

## Capacità e performance

- LocateAnything 3B di NVIDIA, primo in trending su HuggingFace, fa da occhi a Qwen 3.6 35B permettendogli di compilare moduli cartacei: nove minuti e dieci secondi, circa 224.500 token in input, ventiquattromila e trecento in output, ventuno turni.
- NVIDIA ha eliminato con LocateAnything il collo di bottiglia della generazione sequenziale delle coordinate dei bounding box: predice l'intera scatola in un unico passaggio, con dodici punto sette box al secondo su singola H100, dieci volte più veloce di Qwen3-VL e maggiore accuratezza.

## Azienda di riferimento

- [[hugging-face]]
- [[nvidia]]

## Timeline delle notizie

- **2026-06-03** — LocateAnything 3B di NVIDIA, primo in trending su HuggingFace, fa da occhi a Qwen 3.6 35B permettendogli di compilare moduli cartacei: nove minuti e dieci secondi, circa 224.500 token in input, ventiquattromila e trecento in output, ventuno turni. [Fonte: raw/puntate/ainews20260603.md]
- **2026-06-17** — NVIDIA ha eliminato con LocateAnything il collo di bottiglia della generazione sequenziale delle coordinate dei bounding box: predice l'intera scatola in un unico passaggio, con dodici punto sette box al secondo su singola H100, dieci volte più veloce di Qwen3-VL e maggiore accuratezza. [Fonte: raw/puntate/ainews20260617.md]

## Collegamenti

- [[hugging-face]]
- [[nvidia]]
- [[qwen-3-6-35b]]
- [[qwen3-vl]]
- [[index]]

