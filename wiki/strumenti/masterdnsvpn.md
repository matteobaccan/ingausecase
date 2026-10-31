---
title: "MasterDnsVPN"
category: strumento
tags: [dns, sicurezza, tunnel, vpn]
related_puntate: [20260610, 20260611]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260610.md, raw/puntate/ainews20260611.md]
---

# MasterDnsVPN

## Introduzione

VPN che nasconde il traffico in query DNS sulla porta 53 con tunnel AES-256-GCM, dodici percorsi resolver.

## Funzionalità principali

- MasterDnsVPN nasconde il traffico dentro query DNS sulla porta cinquantatré (che ogni firewall deve lasciare aperta): tunnel criptato AES-256-GCM che funziona dove le altre VPN sono bloccate, con dodici percorsi resolver simultanei.
- MasterDnsVPN tunnella il traffico attraverso la porta cinquantatré DNS (che ogni firewall deve lasciare aperta): layer ARQ custom per affidabilità TCP-like su UDP DNS, fino a dodici percorsi resolver simultanei, probe automatico dell'MTU massimo; crittografia AES-256-GCM, ChaCha20, AES-128 e AES-192; proxy SOCKS5 su localhost porta milleottanta; binari per Windows, Linux AMD64/ARM64 e macOS ARM64; MIT.

## Timeline delle notizie

- **2026-06-10** — MasterDnsVPN nasconde il traffico dentro query DNS sulla porta cinquantatré (che ogni firewall deve lasciare aperta): tunnel criptato AES-256-GCM che funziona dove le altre VPN sono bloccate, con dodici percorsi resolver simultanei. [Fonte: raw/puntate/ainews20260610.md]
- **2026-06-11** — MasterDnsVPN tunnella il traffico attraverso la porta cinquantatré DNS (che ogni firewall deve lasciare aperta): layer ARQ custom per affidabilità TCP-like su UDP DNS, fino a dodici percorsi resolver simultanei, probe automatico dell'MTU massimo; crittografia AES-256-GCM, ChaCha20, AES-128 e AES-192; proxy SOCKS5 su localhost porta milleottanta; binari per Windows, Linux AMD64/ARM64 e macOS ARM64; MIT. [Fonte: raw/puntate/ainews20260611.md]

## Collegamenti

- [[index]]

