---
title: "Living Weights"
category: modello
tags: [memoria, open-weight, pesi, modello]
related_puntate: [20261010]
created: 2026-10-11
updated: 2026-10-11
---

# Living Weights

## Introduzione

Modello di [[tensorfold]] che aggiorna i propri pesi durante l'uso invece di appoggiarsi a una memoria esterna.

## Capacità e performance

- Il modello impara mentre lo si usa e non usa una cache KV esterna: si scarica il modello, lo si sposta su un'altra macchina e ricorda ancora quanto gli è stato insegnato.
- La prima release supporta NVIDIA Nemotron Lightning.

## Disponibilità

- Prima release pubblica con supporto a Nemotron Lightning.

## Azienda di riferimento

- [[tensorfold]]

## Timeline delle notizie

- **2026-10-10** — Primo rilascio di Living Weights, il modello di TensorFold che aggiorna i pesi durante l'uso e li porta con sé da una macchina all'altra.

## Collegamenti

- [[tensorfold]]
- [[nvidia]]
- [[index]]
