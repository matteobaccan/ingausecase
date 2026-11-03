# Casi d'uso

Casi d'uso di [Inga](https://github.com/matteobaccan/inga), provati su ogni nuova
versione: ogni caso è una cartella in `cases/`, con i suoi dati, cosa chiedere e come
dare il voto; i risultati vanno in `results/<versione>/`.

| Cartella | Cosa prova |
| --- | --- |
| [`wiki/`](wiki) | la base di conoscenza dei casi (la wiki di AINews) |
| [`cases/articoli/`](cases/articoli) | un articolo su un tema, dalla wiki e dal web, con un tono dato |
| [`cases/contratti/`](cases/contratti) | domande verificate su un contratto collettivo (il CCNL Commercio e Terziario di Conflavoro), con la Divina Commedia come distrattore |
| [`cases/documenti/`](cases/documenti) | domande su una collezione di documenti (pagine della wiki e la Divina Commedia), con risposte e pagine note |
| [`cases/email/`](cases/email) | smistamento di email e ticket, voto esatto |
| [`cases/pdf/`](cases/pdf) | estrazione di dati da PDF, voto esatto |
| [`cases/prova/`](cases/prova) | avvio e prima risposta con un modello piccolo |
| [`cases/rag-recupero/`](cases/rag-recupero) | il recupero delle collezioni di documenti su un test pubblico (SciFact di BEIR): nDCG@10, recall@10 |
| [`cases/rag-rgb/`](cases/rag-rgb) | risposte da documenti rumorosi e rifiuto quando la risposta non c'è, su un test pubblico (RGB) |
| [`cases/gsm8k/`](cases/gsm8k) | aritmetica a parole (GSM8K), Inga e llama.cpp sullo stesso modello |
| [`cases/arc/`](cases/arc) | domande di scienze a scelta multipla (ARC-Challenge), Inga e llama.cpp |
| [`cases/ifeval/`](cases/ifeval) | rispetto di istruzioni verificabili (IFEval), Inga e llama.cpp |
| [`cases/velocita/`](cases/velocita) | velocità (pp512, tg128) e perplexity (wikitext-2) di Inga su quelle di llama.cpp |
| [`cases/colibri-qualita/`](cases/colibri-qualita) | domande di ARC-Challenge e GSM8K a Inga e a Colibri sullo stesso GGUF |
| [`cases/colibri-velocita/`](cases/colibri-velocita) | lettura del prompt e generazione di Inga su quelle di Colibri, dall'API in streaming |
| [`cases/liyab-qualita/`](cases/liyab-qualita) | domande di ARC-Challenge e GSM8K a Inga e a Liyab sullo stesso GGUF |
| [`cases/liyab-velocita/`](cases/liyab-velocita) | lettura del prompt e generazione di Inga su quelle di Liyab (liyab-cli --json) |
| [`cases/colibri-moe/`](cases/colibri-moe) | una mixture of experts più grande della RAM data (Qwen3-30B-A3B, 8 GB) con gli esperti dal disco: Inga e Colibri |
| [`cases/tokensave/`](cases/tokensave) | Inga come host MCP con gli strumenti di tokensave su un codice vero (itsdangerous): risposte, chiamate e token, con e senza strumenti |
| [`cases/memoria/`](cases/memoria) | la memoria dei progetti fra una chat e l'altra, su un test pubblico (LongMemEval) |
| [`tools/`](tools) | lo script comune: scarica Inga, lo avvia, esegue i casi, dà i voti |
| [`results/`](results) | i risultati, una cartella per versione, con `summary.md` |

Tutto gira sui runner di GitHub, un job per caso in parallelo: nessun PC personale e,
per ora, nessuna mesh. I dati sono pubblici o sintetici. I casi `gsm8k`, `arc`, `ifeval`
e `velocita` fanno le stesse domande anche a llama.cpp (versione in
[`llama-cpp.txt`](llama-cpp.txt), compilato sul runner) con lo stesso file del modello; i
casi `colibri-*` a [Colibri](https://github.com/JustVugg/colibri) (commit in
[`colibri.txt`](colibri.txt), compilato sul runner), che legge dal disco gli esperti
delle mixture of experts; i casi `liyab-*` a [Liyab](https://github.com/andrei-borcea/liyab)
(commit in [`liyab.txt`](liyab.txt), compilato sul runner per la CPU), il motore C++ per
GGUF pensato per telefono e Mac, misurato con il suo `liyab-cli --json`.

In `summary.md` ogni caso dice nel titolo da che parte è il meglio: ↑ più alto è meglio
(il voto di un caso, al massimo 100), ↓ più basso è meglio (ad esempio gli estratti del
distrattore), ≈ solo descrittivo. I rapporti "A su B" valgono 100 quando sono pari, le
differenze "A meno B" 0. In neretto i valori migliori: dal lato buono della parità, il
migliore fra due motori o due modi, o il migliore fra questa versione e la precedente. Le
voci da leggere al contrario o solo descrittive sono in `case.json` (`voci_meglio_basso`,
`voci_neutre`; `voci_confronto` per i gruppi di voci da confrontare fra loro).

## Versione, modelli, esecuzione

- [`inga-version.txt`](inga-version.txt): la versione di Inga da provare (Renovate la
  aggiorna con una PR verso questo ramo quando esce una release).
- [`models.json`](models.json): i modelli dei casi, con repository, file, sha256 e
  dimensione su Hugging Face. Il runner controlla lo sha256 di ogni file e si ferma se
  Hugging Face ne dichiara uno diverso.
- [`fonti.json`](fonti.json): i PDF che i casi scaricano a ogni esecuzione (il contratto
  e la Divina Commedia), con URL, sha256 e dimensione del file controllato: il testo non
  va nel repository, e se il file scaricato cambia il caso si ferma con un messaggio
  chiaro.
- [`dati.json`](dati.json): i dati dei test pubblici (SciFact, RGB, LongMemEval, ...) e
  il programma di tokensave che i casi scaricano a ogni esecuzione, con URL fissato a una revisione dove possibile,
  sha256, dimensione e licenza: non vanno nel repository (RGB è solo per uso non
  commerciale).
- [`tools/runner.py`](tools/runner.py): esegue i casi in locale o in CI (vedi
  [`tools/README.md`](tools/README.md)). Temperatura 0 e seed fisso.

## Il workflow

`.github/workflows/cases.yml` sta, identico, sia su `main` sia su questo ramo: GitHub
legge il workflow da `main` per l'esecuzione pianificata e per quella a mano, e dal
ramo base della PR (questo) per le pull request. Va cambiato su tutti e due, come
`fonti.yml`.

- **A mano** (`workflow_dispatch`): `version` (vuoto: l'ultima release) e `case` (casi
  separati da virgole; vuoto: tutti). `gh workflow run cases.yml -R matteobaccan/ingausecase --ref main -f version=0.40.0`.
- **Ogni giorno**: se l'ultima release di Inga non ha ancora `results/<versione>/`, la
  prova.
- **Pull request verso `cases`** (Renovate che cambia `inga-version.txt`, o chi cambia
  casi e strumenti): esegue i casi sulla versione della PR, senza salvare nulla.

I casi girano in parallelo, un job per caso, con permessi di sola lettura; un ultimo
job raccoglie i loro JSON, scrive `summary.md` con il runner di questo ramo (mai il
codice di una PR) e, solo per le esecuzioni pianificate e a mano, salva
`results/<versione>/` su questo ramo. Le PR da fork non hanno segreti né permessi di
scrittura. La cache di GitHub tiene i modelli di ogni job, con la chiave fatta dai loro
sha256 (non quelli oltre i 6 GB, che si scaricano ogni volta), llama.cpp e Colibri
compilati, con la chiave fatta da versione (o commit) e CPU del runner, e i PDF di
`fonti.json`, con la chiave fatta da URL e sha256. Un caso con `disco_gb` in `case.json`
(`colibri-moe`) toglie prima dal runner gli SDK che i casi non usano, se lo spazio
libero non basta.

`.github/workflows/prova.yml` (identico sui due rami, si lancia solo a mano) prova un
ramo o un commit di Inga, compilato in ogni job, con uno o più modelli: un job per ogni
caso e modello, in parallelo, e un riepilogo per modello nella pagina della run; i
risultati restano come artifact (solo JSON e log, mai il binario di Inga).
`gh workflow run prova.yml -R matteobaccan/ingausecase --ref main -f ref=exp/web-steps -f modelli=qwen3-4b,lfm3-1.7b`.

Un secondo workflow, `.github/workflows/fonti.yml` (anche lui identico sui due rami),
si lancia solo a mano: scarica i PDF di `fonti.json`, ne stampa sha256, dimensione e
pagine e, nel log, il testo di una fonte pagina per pagina
(`gh workflow run fonti.yml -R matteobaccan/ingausecase --ref main -f chiave=ccnl`).
Serve a leggere i testi per verificare le domande.

Segreti facoltativi: `INGA_TOKEN` (legge le release di `matteobaccan/inga` finché quel
repository è privato: senza, il download di Inga in CI fallisce) e `HF_TOKEN`.
