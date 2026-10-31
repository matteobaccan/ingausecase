---
title: "Comfy Router"
category: strumento
tags: [api, comfyui, generativo, routing]
related_puntate: [20260924]
created: 2026-09-25
updated: 2026-09-25
---

# Comfy Router

## Introduzione

API unica di [[comfyui]] per i modelli frontier di immagine, video, 3D e audio, presentata il 24 settembre 2026: stesso nome di modello e stessi argomenti a prescindere dal provider, senza nuovo SDK, nuova chiave o redeploy.

## Funzionalità principali

- Il routing è esplicito: si nomina il provider e viene chiamato quello, quindi se è offline la richiesta fallisce lì invece di essere dirottata altrove; ogni job restituisce il provider che l'ha eseguito.
- È asincrono, con submit che restituisce subito un ID di richiesta e ritenzione di ventiquattro ore su input e output prima della cancellazione.
- Provider al lancio: Comfy, Runware, Wavespeed, [[fal]] e [[higgsfield]].

## Azienda / Autore

- [[comfyui]]

## Timeline delle notizie

- **2026-09-24** — Comfy Router è un'unica API per modelli frontier di immagine, video, 3D e audio: stesso nome modello e stessi argomenti, nessun nuovo SDK o chiave, routing esplicito verso il provider nominato, submit asincrono con ID richiesta e ritenzione di ventiquattro ore. Al lancio copre Comfy, Runware, Wavespeed, Fal e Higgsfield.

## Collegamenti

- [[comfyui]]
- [[fal]]
- [[higgsfield]]
- [[index]]
