---
title: "Security Audit Skill (Cloudflare)"
category: strumento
tags: [cloudflare, sicurezza, audit, agenti, skill, open-source]
related_puntate: []
created: 2026-10-25
updated: 2026-10-25
sources: [raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
---

# Security Audit Skill (Cloudflare)

## Introduzione

Pacchetto di istruzioni open source con licenza MIT che trasforma un coding agent in un auditor di sicurezza: l'agente legge il codice del progetto, cerca le vulnerabilità con sotto-agenti separati, fa smentire ogni sospetto da un verificatore indipendente e consegna un report con i problemi confermati. Il repository cloudflare/security-audit-skill è stato creato il 18 giugno 2026, lo stesso giorno del post Build your own vulnerability harness firmato da Grant Bourzikas, e al 24 ottobre conta 43.428 stelle, 2.712 fork e 85 fra issue e pull request aperte. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]

## Come funziona

- L'audit completo segue sei fasi: ricognizione con agenti di ricerca in parallelo, caccia con un cacciatore isolato per ogni gruppo di unità, validazione di ogni candidato da parte di un agente nuovo, scrittura di findings.json con tre verdetti, verifica indipendente dei record e produzione di REPORT.md, FINDINGS-DETAIL.md e NEEDS-VALIDATION.md. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
- L'agente genitore resta l'unico a scrivere i file condivisi e ogni sotto-agente riceve la propria cartella di lavoro, senza accesso al codice del progetto né ai file degli altri; un registro di copertura, riletto da un critico dopo ogni ondata, serve a non lasciare unità scoperte. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
- La caccia copre nove classi di attacco generali, dalle injection alla logica di business alle catene di vulnerabilità, più dieci file specialistici da attivare quando il progetto lo richiede, per esempio memoria e binari nativi, prompt injection degli agenti LLM, filiera delle dipendenze e cloud/IAM. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
- Il principio che regge il metodo è che chi trova un problema non è mai chi lo conferma, e un candidato senza un danno concreto — chi lo sfrutta, su quale risorsa, con quale risultato osservabile — non diventa un finding; la separazione dei ruoli costa più chiamate all'agente ed è la scelta con cui la skill prova a ridurre i falsi allarmi. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]

## Requisiti e installazione

- L'installazione passa dalla Skills CLI di skills.sh con `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit`, e con `--global` la skill diventa disponibile in tutti i progetti invece che in uno solo. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
- Servono un agente con un modello capace di usare strumenti e lanciare sotto-agenti in parallelo, Node.js per i due validatori senza dipendenze e, per eseguire build, test o fuzzer del progetto, una sandbox imposta dal sistema operativo: senza quella la skill non esegue il codice del bersaglio e lascia il sospetto in stato needs_validation. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
- I profili quick, standard e deep cambiano l'ampiezza della ricerca e la ridondanza dei controlli, mai la soglia di prova, e il budget è un tetto alle invocazioni di agenti che la skill controlla prima di partire: se non basta non lancia nulla e chiede più budget, un perimetro più stretto o un altro profilo. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]

## Limiti

- I 20.799 candidati, i 7.245 risultati utilizzabili e il calo dei rigetti in validazione dal 40 all'11 per cento li ha misurati Cloudflare sul proprio harness interno e sui propri repository, non sulla skill pubblica, e nessun terzo li ha replicati. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
- Il post non dichiara un tasso di falsi negativi, perché senza un insieme di bug reali già etichettati qualsiasi stima sarebbe speculativa: un report senza problemi confermati non dimostra che il codice sia sicuro, e una singola esecuzione trova circa la metà di ciò che trovano più esecuzioni. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]
- La skill legge i sorgenti ed esegue test locali in sandbox, ma non vede la configurazione del server, le regole del firewall o i permessi nel cloud, e descrive le correzioni senza applicarle. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]

## Timeline delle notizie

- **2026-10-24** — Cloudflare ha trasformato in skill pubblica il seme del suo harness interno di ricerca delle vulnerabilità: un file di circa 450 righe usato su un singolo repository è diventato in sei settimane uno scanner di flotta su 128 repository, con 20.799 candidati grezzi, circa 12.057 superati la validazione e 7.245 lavorabili dopo deduplica. L'harness completo non è pubblico. [Fonte: raw/pillitteri/pillitteri20261024-security-audit-skill-cloudflare-come-usarla.md]

## Collegamenti

- [[cloudflare]]
- [[bug-hunting-ai]]
- [[claude-code]]
- [[codex-cli]]
- [[cybersicurezza]]
- [[index]]
