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
   aspetta `/health` ed esegue `run.py` del caso;
5. scrive `results/<versione>/<caso>.json` e `results/<versione>/summary.md`, con il
   confronto con la versione precedente più recente presente in `results/`.

Esce con un codice diverso da zero solo se un caso va in errore, non se un voto scende.

```
python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/runner.py                 # tutti i casi, versione di inga-version.txt
.venv/bin/python tools/runner.py --case pdf      # un caso solo (ripetibile)
.venv/bin/python tools/runner.py --version 0.40.0 --cache /tmp/iuc
.venv/bin/python tools/runner.py --list
.venv/bin/python tools/runner.py --summary-only --version 0.40.0   # riscrive solo summary.md
```

Variabili d'ambiente lette (nessuna è obbligatoria):

| Variabile | Uso |
| --- | --- |
| `INGA_TOKEN`, poi `GH_TOKEN`, poi `GITHUB_TOKEN` | lettura delle release di `matteobaccan/inga` finché il repository è privato |
| `HF_TOKEN` | download da Hugging Face, se presente |
| `IUC_CACHE` | cartella dei download e dei file di lavoro (`~/.cache/ingausecase`) |

## Come è fatto un caso

Una cartella `cases/<nome>/` con:

- `case.json`: `modello` (una chiave di `models.json`), `ctx`, `timeout_minuti`,
  `descrizione`, ed eventualmente `argomenti_serve` (altre opzioni di `inga serve`);
- `run.py`: parla con il server tramite `inga_api.py` (l'URL è in `INGA_URL`) e scrive
  il risultato con `inga_api.write_result`: `stato` (`ok` o `saltato`), `voto` da 0 a
  1, `voci` (i voti parziali, da 0 a 1), `motivo` (per un caso saltato) e `dettagli`;
- `README.md`: cosa prova e come si dà il voto.

I file generati (PDF, testi scaricati) vanno nella cartella di lavoro (`IUC_WORK_DIR`)
e non nel repository. Ogni richiesta usa temperatura 0 e seed 42.
