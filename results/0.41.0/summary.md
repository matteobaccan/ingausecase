# Risultati di Inga 0.41.0

Eseguito con `inga 0.41.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.40.0).

| Caso | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| contratti | - | - | - | 0:26 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | saltato |
| documenti | 100.0 | 100.0 | 0.0 | 24:35 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 85.0 | 83.8 | +1.2 | 3:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 94.4 | 93.1 | +1.2 | 13:30 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:14 | Qwen3-0.6B-Q8_0.gguf | ok |

## Voci di ogni caso

### documenti

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| risposta giusta | 100.0 | 100.0 | 0.0 |
| pagina giusta | 100.0 | 100.0 | 0.0 |

### email

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| urgenza | 80.0 | 80.0 | 0.0 |
| reparto | 90.0 | 87.5 | +2.5 |
| entrambi giusti | 72.5 | 67.5 | +5.0 |

### pdf

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| campo numero | 100.0 | 100.0 | 0.0 |
| campo data | 100.0 | 100.0 | 0.0 |
| campo fornitore | 85.0 | 80.0 | +5.0 |
| campo partita_iva | 85.0 | 80.0 | +5.0 |
| campo imponibile | 100.0 | 100.0 | 0.0 |
| campo iva | 100.0 | 100.0 | 0.0 |
| campo totale | 100.0 | 100.0 | 0.0 |
| campo righe | 85.0 | 85.0 | 0.0 |
| righe singole | 94.0 | 94.0 | 0.0 |

### prova

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| risposta non vuota | 100.0 | 100.0 | 0.0 |

## Casi saltati o in errore

- contratti: l'URL ufficiale del testo del CCNL non è impostato in cases/contratti/fonte.json

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
