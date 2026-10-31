---
title: "GPU-Unlock"
category: strumento
tags: [nvidia, gpu, linux, ai-locale, open-source, kernel]
related_puntate: []
created: 2026-10-26
updated: 2026-10-27
---

# GPU-Unlock

## Introduzione

Modulo del kernel Linux open source con licenza GPL-2.0 che porta le istruzioni FP16 e BF16 delle schede Nvidia GeForce RTX serie 30 alla velocità delle schede professionali equivalenti senza toccare il driver. Il repository Zagitta/gpu-unlock, firmato dall'autore con il nome Zagitta, è nato il 18 ottobre 2026 e al 25 ottobre conta 5.619 stelle, 601 fork e un centinaio fra segnalazioni e pull request aperte.

## Funzionalità principali

- Sulle GeForce serie 30 la GPU avvia le istruzioni FP16 e BF16 con accumulo in FP32 — il passaggio che evita di perdere precisione nelle somme — a metà della velocità delle schede professionali equivalenti; il modulo toglie quel limite e, secondo il repository, raddoppia il ritmo di emissione per i chip GA102, GA103, GA104 e GA106, dalla RTX 3090 Ti alla 3060 da 12 GB.
- Il modulo si carica nell'initramfs prima del driver Nvidia, scrive due selettori di velocità, resetta la scheda e lascia che il driver, rimasto invariato, la prenda in carico: non è un'applicazione UEFI né un driver modificato, quindi non va ripatchato a ogni aggiornamento del driver.
- Nel benchmark GEMM su una RTX 3090 Ti a 450 watt la BF16 passa da 87,5 a 157,4 TFLOPS, la TF32 da 42,6 a 82,6 e la FP16 da 87,5 a 118,4: sono mediane di cinque campioni con accumulo in FP32 riportate dal README.

## Prestazioni sugli LLM locali

- Il guadagno misurato nei quattro report citati dal README sta nel prefill, la fase in cui il modello legge il prompt: dal 14 al 36 per cento, con la generazione dei token e il lavoro in INT8 invariati, perché dipendono dalla banda della memoria e non dal calcolo.
- Chi ha confrontato gli output prima e dopo li ha trovati identici bit per bit; il raddoppio che compare nei titoli riguarda la velocità di emissione delle istruzioni, non quella del modello.

## Installazione e uso

- Serve un PC con Linux e una RTX serie 30: l'installazione richiede privilegi di amministratore, è automatica su Arch, Debian e Ubuntu, Fedora e RHEL e per le altre distribuzioni va configurata a mano, e si chiude con la modifica della riga di comando del kernel (`gpu_unlock.targets=all` oppure gli indirizzi PCI delle sole schede scelte) e un riavvio.
- Il modulo non fa nulla su una scheda già agganciata dal driver, quindi caricarlo a sistema avviato non serve; se la scheda pilota il monitor lo schermo resta nero dal reset fino al caricamento di nvidia-drm, dopo la sospensione in RAM i selettori si azzerano e il modulo li riapplica prima del risveglio, mentre l'ibernazione non è coperta.

## Limiti

- I guadagni dal 25 all'80 per cento sono benchmark sintetici con limiti di potenza diversi da scheda a scheda, e sul lavoro vero il prefill sale dal 10 al 36 per cento.
- Non esiste una prova indipendente di una testata o di un laboratorio: i report sono segnalazioni degli utenti nel repository, ancora da replicare con prompt, modelli e potenza dichiarati.
- Per le RTX 40 e per i portatili ci sono solo pull request sperimentali e resoconti non verificati, e per Windows il README riporta soltanto risultati di un porting via UEFI su alcune schede, non un pacchetto.
- Non è un prodotto Nvidia e interviene sul firmware della scheda prima che parta il driver, quindi chi ha una scheda ancora in garanzia se la gioca da sé.

## Repository

- `github.com/Zagitta/gpu-unlock`, licenza GPL-2.0, creato il 18 ottobre 2026, 5.619 stelle e 601 fork al 25 ottobre 2026.

## Azienda/autore

- Zagitta, autore del repository: non ha una pagina in wiki.

## Timeline delle notizie
- **2026-10-25** — Il modulo diventa virale su GitHub, dove il repository creato il 18 ottobre conta 5.619 stelle e 601 fork: sblocca le istruzioni FP16 e BF16 delle GeForce RTX serie 30 caricandosi nell'initramfs prima del driver, con guadagni dal 14 al 36 per cento sul prefill dei modelli locali e problemi noti che vanno dallo schermo nero durante il reset all'ibernazione non coperta.
- **2026-10-27** — La tecnica di sblocco dei tensor core arriva anche alle RTX 20 e 40 con i fork turing-unlock e gpu-unlock-ada, accanto al modulo per le RTX 30: i tre progetti gratuiti girano su Linux e sfruttano un overflow nel Booter firmato Nvidia per rimettere a piena velocità l'accumulo FP32, con il repository originale a 10.715 stelle e 1.059 fork. Il raddoppio riguarda il picco — su una RTX 4090 da 165,6 a 331,6 TFLOPS in FP16 — mentre su una moltiplicazione di matrici reale un proprietario indipendente riporta +12-34 per cento; il decode dei token non cambia, perché dipende dalla banda di memoria, e per le RTX 50 non esiste sblocco.







## Collegamenti

- [[nvidia]]
- [[ai-locale]]
- [[index]]
