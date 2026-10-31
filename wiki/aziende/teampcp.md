---
title: "TeamPCP"
category: azienda
tags: [teampcp, malware, sicurezza, supply-chain]
related_puntate: [20260521]
created: 2026-08-12
updated: 2026-08-12
---

# TeamPCP

## Introduzione

Attore minaccioso che avvelena ecosystem di pacchetti (npm/PyPI) con malware auto-propagante, vendendo i dati rubati sul dark web.

## Strumenti

- [[nx-console]]
- [[trivy]]

## Timeline delle notizie

- **2026-05-21** — TeamPCP vende sul dark web i dati rubati nella compromissione di GitHub (3800 repository interni) e non è un caso isolato: l'operazione ha avvelenato Trivy a marzo, Checkmarx ad aprile e TanStack a maggio, colpendo anche Cisco, Bitwarden e Aqua Security; il malware si autopropaga infettando un package, rubando i token di publish e saltando al successivo attraverso npm e PyPI automaticamente.

## Collegamenti

- [[aqua-security]]
- [[bitwarden]]
- [[checkmarx]]
- [[cisco]]
- [[github]]
- [[nx-console]]
- [[tanstack]]
- [[trivy]]
- [[index]]

