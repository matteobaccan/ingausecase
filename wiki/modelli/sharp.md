---
title: "SHARP"
category: modello
tags: [3d, apple, gaussian-splatting, open-source, ricerca]
related_puntate: []
created: 2026-09-16
updated: 2026-09-16
---

# SHARP

## Introduzione

Modello di sintesi di viste pubblicato in open source da [[apple]] a dicembre 2025: trasforma una singola fotografia in una scena tridimensionale. Il codice sta nel repository `apple/ml-sharp` su GitHub, che al giugno 2026 aveva raccolto circa 8.483 stelle, con il paper su arXiv.

## Capacità e performance

- Mentre il 3D Gaussian Splatting tradizionale ha bisogno di decine o centinaia di scatti dello stesso soggetto, SHARP stima profondità e geometria e predice la posizione di milioni di gaussiane in un solo passaggio della rete, in meno di un secondo su una GPU comune.
- È pensato per la singola immagine e non coincide con la pipeline aerea multi-vista che Apple usa per il Flyover di Apple Maps, ma dimostra che la competenza interna dell'azienda sui campi di radianza è matura.

## Installazione e uso

- Il repository si clona da GitHub, si installano le dipendenze e si genera una scena in formato PLY da una foto:

```bash
git clone https://github.com/apple/ml-sharp.git
cd ml-sharp
pip install -r requirements.txt
python demo.py --image street.jpg --out scene.ply
```

## Azienda di riferimento

- [[apple]]

## Timeline delle notizie

- **2026-06-09** — Il modello viene citato come prova dell'investimento di Apple sul 3D Gaussian Splatting, nello stesso giorno in cui l'azienda annuncia il passaggio del Flyover di Apple Maps a quella tecnica di rendering: SHARP è pubblico dalla fine del 2025, con paper su arXiv e circa 8.483 stelle su GitHub.

## Collegamenti

- [[3d-gaussian-splatting]]
- [[apple]]
- [[index]]
