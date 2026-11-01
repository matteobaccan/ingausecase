# Risultati di Inga 0.41.0

Eseguito con `inga 0.41.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.40.0).

| Caso | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| contratti | 76.7 | - | - | 29:04 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 17:21 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 83.8 | 83.8 | 0.0 | 2:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 93.1 | 93.1 | 0.0 | 10:45 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:15 | Qwen3-0.6B-Q8_0.gguf | ok |

## Voci di ogni caso

### contratti

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| risposta giusta | 93.3 | - | - |
| articolo giusto | 60.0 | - | - |
| citazione fra gli estratti | 100.0 | - | - |
| estratti dal distrattore | 27.7 | - | - |

### documenti

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| risposta giusta | 100.0 | 100.0 | 0.0 |
| pagina giusta | 100.0 | 100.0 | 0.0 |
| pagina giusta fra gli estratti | 100.0 | - | - |
| estratti dal distrattore | 1.7 | - | - |

### email

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| urgenza | 80.0 | 80.0 | 0.0 |
| reparto | 87.5 | 87.5 | 0.0 |
| entrambi giusti | 67.5 | 67.5 | 0.0 |

### pdf

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| campo numero | 100.0 | 100.0 | 0.0 |
| campo data | 100.0 | 100.0 | 0.0 |
| campo fornitore | 80.0 | 80.0 | 0.0 |
| campo partita_iva | 80.0 | 80.0 | 0.0 |
| campo imponibile | 100.0 | 100.0 | 0.0 |
| campo iva | 100.0 | 100.0 | 0.0 |
| campo totale | 100.0 | 100.0 | 0.0 |
| campo righe | 85.0 | 85.0 | 0.0 |
| righe singole | 94.0 | 94.0 | 0.0 |

### prova

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| risposta non vuota | 100.0 | 100.0 | 0.0 |

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
