---
title: "TextGrain"
category: strumento
tags: [watermark, provenienza, openai, ai-act]
related_puntate: []
created: 2026-10-06
updated: 2026-10-12
sources: [raw/tldr/tldr20261006.md, raw/pillitteri/pillitteri20261005-openai-textgrain-filigrana-testo-ue.md, raw/pillitteri/pillitteri20261011-chatgpt-watermark-remover-textgrain.md, raw/pillitteri/pillitteri20261011-filigrana-chatgpt-compiti-tesi-textgrain.md, raw/pillitteri/pillitteri20261011-filigrana-chatgpt-lingue-italiano.md, raw/pillitteri/pillitteri20261011-textgrain-api-openai-come-attivare.md]
---

# TextGrain

## Introduzione

Sistema di filigrana per il testo annunciato da [[openai]] il 5 ottobre 2026: inserisce un segnale statistico invisibile nelle parole scelte dal modello, attivabile in opt-in dalle API in tutto il mondo e destinato nelle settimane successive ai testi di ChatGPT e Codex nell'Unione europea per rispettare l'obbligo di marcatura dell'AI Act. [Fonte: raw/pillitteri/pillitteri20261005-openai-textgrain-filigrana-testo-ue.md]

## Funzionalità principali

- La selezione dei token è modellata come un problema di trasporto ottimale, con costi derivati da variabili casuali di Gumbel e una regolarizzazione Kullback-Leibler; un budget di entropia limita quanta varietà il modello può sacrificare per inserire il segnale. [Fonte: raw/pillitteri/pillitteri20261005-openai-textgrain-filigrana-testo-ue.md]
- Con un tasso di falsi positivi dell'1 per cento, il rilevatore individua la filigrana in circa l'80 per cento dei brani da 200 token e nel 95 per cento di quelli da 400; con il 10 per cento delle parole sostituite la detection scende al 66 per cento e con il 25 per cento crolla al 17 per cento. [Fonte: raw/pillitteri/pillitteri20261005-openai-textgrain-filigrana-testo-ue.md]
- L'accesso al rilevatore è riservato a ricercatori e organizzazioni approvate. [Fonte: raw/pillitteri/pillitteri20261005-openai-textgrain-filigrana-testo-ue.md]

## Timeline delle notizie

- **2026-10-06** — OpenAI annuncia textGrain, filigrana invisibile per il testo: opt-in dalle API a livello mondiale e, nelle settimane successive, attiva sui testi di ChatGPT e Codex nell'UE per l'AI Act. [Fonte: raw/tldr/tldr20261006.md]
- **2026-10-11** — OpenAI esclude l'integrità accademica dal programma di accesso al rilevatore: controllare saggi e tesi resta fuori dall'ambito, come gli usi commerciali, e attivare la filigrana dalle impostazioni dell'API non dà accesso al rilevatore. I dati per lingua stanno solo nell'help center: l'italiano passa dal 54 al 64 per cento con l'aumento d'intensità, con lo spagnolo al 69,0 e il rumeno al 42,2 per cento e falsi positivi fissati all'1 per cento. Fra i partner del rilevatore restano John Thickstun della Cornell, Martin Vechev dell'ETH di Zurigo e direttore scientifico di INSAIT e i ricercatori del Kempelen Institute di Bratislava. [Fonte: raw/pillitteri/pillitteri20261011-filigrana-chatgpt-compiti-tesi-textgrain.md] [Fonte: raw/pillitteri/pillitteri20261011-filigrana-chatgpt-lingue-italiano.md] [Fonte: raw/pillitteri/pillitteri20261011-chatgpt-watermark-remover-textgrain.md] Sempre dall'11: l'attivazione nelle API è un interruttore lato piattaforma (Organization settings, Data controls, Text provenance, con override per singolo progetto), senza parametro per la richiesta né campo di risposta, e l'endpoint content_provenance_checks copre solo immagini e audio mentre per il testo serve l'approvazione. Il codice si marca meno della prosa perché ha meno scelte plausibili per il token successivo, e OpenAI pubblica benchmark avanti e indietro con scarti dentro il rumore (49,57 contro 49,76 punti nell'Artificial Analysis Intelligence Index), con il Digital Omnibus che fissa al 2 dicembre 2026 la marcatura dell'art. 50 per i sistemi già sul mercato. [Fonte: raw/pillitteri/pillitteri20261011-textgrain-api-openai-come-attivare.md]




## Collegamenti

- [[openai]]
- [[digital-provenance]]
- [[claude]]
- [[index]]
