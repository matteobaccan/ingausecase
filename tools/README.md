# Strumenti

`runner.py` esegue i casi di `cases/` su una versione di Inga:

1. legge la versione da `inga-version.txt` (o da `--version`);
2. scarica l'archivio `inga-linux-x86_64-<versione>.tar.gz` della release, lo controlla
   con `SHA256SUMS` e lo estrae;
3. scarica i modelli di `models.json` e ne controlla lo sha256, sia sul file sia
   contro quello che Hugging Face dichiara oggi (`lfs.oid`): se il file è cambiato si
   ferma con un messaggio chiaro;
4. per ogni caso avvia `inga serve` con il modello del caso su una porta libera
   (temperatura 0, seed fisso, senza rete, senza web UI, memoria, MCP e ricerca web),
   aspetta `/health` ed esegue `run.py` del caso; un caso con `modello_embedding` ha
   anche quel modello, servito accanto (`--models-max 2`) e scelto come modello di
   embedding del server, e l'archivio locale di Inga, dove stanno le collezioni di
   documenti (la memoria resta inutilizzata: nessuna richiesta la chiede);
5. scrive `results/<versione>/<caso>.json` e `results/<versione>/summary.md`, con il
   confronto con la versione precedente più recente presente in `results/`.

Esce con un codice diverso da zero solo se un caso va in errore, non se un voto scende.

```
python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/runner.py                 # tutti i casi, versione di inga-version.txt
.venv/bin/python tools/runner.py --case pdf      # un caso solo (ripetibile)
.venv/bin/python tools/runner.py --version 0.40.0 --cache /tmp/iuc
.venv/bin/python tools/runner.py --list
.venv/bin/python tools/runner.py --matrix qwen3-4b,lfm3-1.7b  # la matrice dei job di GitHub Actions
.venv/bin/python tools/runner.py --summary-only --version 0.40.0   # riscrive solo summary.md
```

Variabili d'ambiente lette (nessuna è obbligatoria):

| Variabile | Uso |
| --- | --- |
| `INGA_TOKEN`, poi `GH_TOKEN`, poi `GITHUB_TOKEN` | lettura delle release di `matteobaccan/inga` finché il repository è privato |
| `HF_TOKEN` | download da Hugging Face, se presente |
| `IUC_CACHE` | cartella dei download (Inga, modelli, fonti) e dei file di lavoro (`~/.cache/ingausecase`); il runner la passa ai casi |

## Come è fatto un caso

Una cartella `cases/<nome>/` con:

- `case.json`: `modello` (una chiave di `models.json`), `ctx`, `timeout_minuti`,
  `descrizione`, ed eventualmente `modello_embedding` (una chiave di `models.json`, per
  le collezioni di documenti) e `argomenti_serve` (altre opzioni di `inga serve`);
- `run.py`: parla con il server tramite `inga_api.py` (l'URL è in `INGA_URL`) e scrive
  il risultato con `inga_api.write_result`: `stato` (`ok` o `saltato`), `voto` da 0 a
  1, `voci` (i voti parziali, da 0 a 1), `motivo` (per un caso saltato) e `dettagli`;
- `README.md`: cosa prova e come si dà il voto.

I file generati (PDF, testi scaricati) vanno nella cartella di lavoro (`IUC_WORK_DIR`)
e non nel repository. Ogni richiesta usa temperatura 0 e seed 42.

`inga_api.py` ha anche `get`, `post` e `put` per le altre API di Inga (un 404 diventa
`NonDisponibile`: il caso si dà come saltato su una versione che non ha quella API),
`search_documents` (la ricerca diretta nelle collezioni) e `add_document`, che aggiunge un file (un PDF o un testo) a una
collezione di documenti di Inga (`POST /api/inga/documents`).

## Le fonti scaricate

`fonti.py` scarica i PDF di [`fonti.json`](../fonti.json) in `<cache>/fonti` (in CI la
cache di GitHub tiene quella cartella, con la chiave fatta da URL e sha256 di ogni
fonte) e li controlla: se lo sha256 del file non è quello di `fonti.json` solleva
`Cambiato`, e il caso si ferma in errore con il motivo. Estrae il testo con pypdf, una
pagina alla volta, e lo tiene accanto al PDF. `in_collezione` aggiunge una fonte a una
collezione di Inga (il PDF letto da Inga; se Inga lo rifiuta, il testo di pypdf).

```
.venv/bin/python tools/fonti.py scarica                      # sha256, dimensione, pagine
.venv/bin/python tools/fonti.py testo ccnl                   # il testo, pagina per pagina
.venv/bin/python tools/fonti.py testo divina-commedia --pagine 1-5
```

Il workflow `fonti.yml` fa le stesse due cose su un runner di GitHub (alcuni siti delle
fonti non si raggiungono da tutte le reti).

## I dati dei test pubblici

`dati.py` scarica i file di [`dati.json`](../dati.json) in `<cache>/dati` e ne controlla
lo sha256: se il file è cambiato, `dati.Cambiato` e il caso si ferma con un messaggio
chiaro. Un caso lo usa con `dati.file("<chiave>")`.

`inga serve` di ogni caso ha la sua cartella dei dati dell'utente (`XDG_DATA_HOME` e
`APPDATA` nella cartella di lavoro del caso), dove sta la memoria dei progetti: un caso
non vede quella di un altro, né quella di chi esegue il runner.

## llama.cpp accanto a Inga

I casi con `"llama_cpp": true` in `case.json` (`gsm8k`, `arc`, `ifeval`, `velocita`)
confrontano Inga con llama.cpp sullo stesso file del modello. I workflow compilano
llama.cpp alla versione di [`llama-cpp.txt`](../llama-cpp.txt) per la CPU del runner
(`.github/actions/llama-cpp`) e mettono la cartella dei programmi in `IUC_LLAMA`; senza,
quei casi si danno come saltati. `llama.py` avvia `llama-server`; `confronto.py` fa le
stesse domande ai due server e scrive i voti di tutti e due. Il runner passa ai casi
anche `IUC_INGA` (l'eseguibile di Inga), `IUC_MODEL_PATH` (il file del modello) e
`IUC_CTX`.
