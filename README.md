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
| [`cases/memoria/`](cases/memoria) | la memoria dei progetti fra una chat e l'altra, su un test pubblico (LongMemEval) |
| [`tools/`](tools) | lo script comune: scarica Inga, lo avvia, esegue i casi, dà i voti |
| [`results/`](results) | i risultati, una cartella per versione, con `summary.md` |

Tutto gira sui runner di GitHub, un solo PC alla volta: nessun PC personale e, per
ora, nessuna mesh. I dati sono pubblici o sintetici.

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
- [`dati.json`](dati.json): i dati dei test pubblici (SciFact, RGB, LongMemEval) che i
  casi scaricano a ogni esecuzione, con URL fissato a una revisione dove possibile,
  sha256, dimensione e licenza: non vanno nel repository (RGB è solo per uso non
  commerciale).
- [`tools/runner.py`](tools/runner.py): esegue i casi in locale o in CI (vedi
  [`tools/README.md`](tools/README.md)). Temperatura 0 e seed fisso.

## Il workflow

`.github/workflows/cases.yml` sta, identico, sia su `main` sia su questo ramo: GitHub
legge il workflow da `main` per l'esecuzione pianificata e per quella a mano, e dal
ramo base della PR (questo) per le pull request. Va cambiato su tutti e due, come
`fonti.yml`.

- **A mano** (`workflow_dispatch`): `version` (vuoto: l'ultima release) e `case` (vuoto:
  tutti). `gh workflow run cases.yml -R matteobaccan/ingausecase --ref main -f version=0.40.0`.
- **Ogni giorno**: se l'ultima release di Inga non ha ancora `results/<versione>/`, la
  prova.
- **Pull request verso `cases`** (Renovate che cambia `inga-version.txt`, o chi cambia
  casi e strumenti): esegue i casi sulla versione della PR, senza salvare nulla.

I casi girano in un job con permessi di sola lettura; solo per le esecuzioni
pianificate e a mano un secondo job, che non esegue codice del repository, salva
`results/<versione>/` su questo ramo. Le PR da fork non hanno segreti né permessi di
scrittura. La cache di GitHub tiene i modelli, con la chiave fatta dai loro sha256, e
i PDF di `fonti.json`, con la chiave fatta da URL e sha256.

Un secondo workflow, `.github/workflows/fonti.yml` (anche lui identico sui due rami),
si lancia solo a mano: scarica i PDF di `fonti.json`, ne stampa sha256, dimensione e
pagine e, nel log, il testo di una fonte pagina per pagina
(`gh workflow run fonti.yml -R matteobaccan/ingausecase --ref main -f chiave=ccnl`).
Serve a leggere i testi per verificare le domande.

Segreti facoltativi: `INGA_TOKEN` (legge le release di `matteobaccan/inga` finché quel
repository è privato: senza, il download di Inga in CI fallisce) e `HF_TOKEN`.
