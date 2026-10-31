# Casi d'uso

Casi d'uso di [Inga](https://github.com/matteobaccan/inga), provati su ogni nuova
versione: ogni caso è una cartella in `cases/`, con i suoi dati, cosa chiedere e come
dare il voto; i risultati vanno in `results/<versione>/`.

| Cartella | Cosa prova |
| --- | --- |
| [`wiki/`](wiki) | la base di conoscenza dei casi (la wiki di AINews) |
| [`cases/articoli/`](cases/articoli) | un articolo su un tema, dalla wiki e dal web, con un tono dato |
| `cases/contratti/` | domande e controlli su un contratto collettivo (CCNL del commercio) |
| `cases/documenti/` | domande su documenti, con risposte e pagine note |
| `cases/email/` | smistamento di email e ticket, voto esatto |
| `cases/pdf/` | estrazione di dati da PDF, voto esatto |
| `tools/` | lo script comune: scarica Inga, lo avvia, esegue i casi, dà i voti |

Tutto gira sui runner di GitHub, un solo PC alla volta: nessun PC personale e, per
ora, nessuna mesh. I dati sono pubblici o sintetici.
