---
title: "Agent Compute Engine"
category: strumento
tags: [google, cloud, agenti, sicurezza, microvm, spiffe, infrastruttura]
related_puntate: []
created: 2026-10-23
updated: 2026-10-25
---

# Agent Compute Engine

## Introduzione

Servizio di calcolo di Google Cloud, presentato il 22 ottobre 2026 ad AGNTCon + MCPCon a San Jose, che assegna a ogni agente AI una microVM dedicata: il kernel e l'accesso root sono suoi, il confine è hardware e l'avvio ha la rapidità di un container.

La scelta risponde a un problema pratico: un container condivide il kernel con i vicini, quindi un agente che esegue codice scritto da sé o suggerito da una pagina ostile ha una superficie d'attacco più larga, mentre una macchina virtuale tradizionale isola meglio ma impiega secondi o minuti ad avviarsi. Google lo usa già per Gemini come agente per il lavoro e per l'agente di programmazione Antigravity, e aprirà la preview «nei prossimi mesi».

## Funzionalità principali

- Ogni sessione gira in una microVM single-tenant e memory-safe, su un server senza stato e immutabile con il filesystem di base in sola lettura; Titan verifica l'integrità di hardware e firmware e Titanium (l'IPU) si occupa di rete, storage e cifratura al posto della CPU.
- Dentro la microVM non ci sono chiavi API, token OAuth né chiavi di account di servizio, in memoria o su disco, e il sandbox non raggiunge il metadata server dell'istanza: l'agente riceve solo un certificato SPIFFE pubblico ed effimero e un token di identità a breve scadenza.
- Le credenziali reali restano fuori: la richiesta esce da virtio-vsock, passa per un proxy e arriva ad Agent Gateway, che verifica l'identità della sessione, applica le regole sul traffico in uscita e sostituisce il token con la credenziale vera. La microVM non ha una scheda di rete virtuale e non vede la VPC del cliente.
- Quando l'agente aspetta, l'host lo porta da attivo a inattivo con un checkpoint e la microVM smette di consumare risorse: Google riassume il modello con «you don't pay for idle VMs». Il risparmio di memoria viene da DAX e copy-on-write, con le pagine statiche condivise per server e snapshot clonabili per valutazioni e addestramento per rinforzo.
- Accanto al servizio arriva Agent Substrate, runtime open source per Kubernetes che gira su GKE e su qualsiasi altro cluster, lavora in modalità zero-trust e usa microVM oppure gVisor: Google dichiara fino a 10 volte la densità del calcolo tradizionale e un test con 200.000 agenti, 500 attivazioni al secondo e sospensione e ripresa sotto i 500 millisecondi.

## Limiti e avvertenze

- I numeri del «10x» e dei 200.000 agenti riguardano Agent Substrate su GKE, non Agent Compute Engine, per il quale Google usa formule qualitative.
- I benchmark li ha misurati Google senza descrivere hardware, carico di lavoro né metodo, e mancano prezzi, quote, limiti di CPU e memoria, API, SDK e una data: la preview è «nei prossimi mesi» e sulla disponibilità in Italia il post tace.
- Il servizio gira solo per gli agenti di Google e si aprirà ai clienti in un secondo momento, mentre la governance degli agenti locali come Claude Code sui dispositivi aziendali è in preview «a breve».

## Timeline delle notizie

- **2026-10-22** — Google presenta Agent Compute Engine ad AGNTCon + MCPCon: una microVM per agente senza segreti all'interno, credenziali sostituite al volo da Agent Gateway, e con Agent Substrate come runtime open source per Kubernetes.
- **2026-10-25** — Il resoconto di OpenAI del 23 ottobre cita la microVM per agente di Google come la risposta che molti fornitori di sandbox presentano come soluzione, e la usa come controprova: gli agenti separati da un hypervisor hanno comunicato lo stesso, perché condividevano la macchina fisica, e chi condivide un processore condivide anche un orologio.




## Collegamenti

- [[google]]
- [[agenti-ai]]
- [[antigravity]]
- [[index]]
