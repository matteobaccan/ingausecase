# Risultati di Inga 0.40.0

Eseguito con `inga 0.40.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (nessuna).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| contratti | - | - | - | 0:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | saltato |
| documenti | 100.0 | - | - | 14:09 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 83.8 | - | - | 2:29 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 93.1 | - | - | 11:42 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | - | - | 0:04 | Qwen3-0.6B-Q8_0.gguf | ok |

## Voci di ogni caso

### documenti — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta | ↑ | 100.0 | - | - |
| pagina giusta | ↑ | 100.0 | - | - |

### email — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| urgenza | ↑ | 80.0 | - | - |
| reparto | ↑ | 87.5 | - | - |
| entrambi giusti | ↑ | 67.5 | - | - |

### pdf — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| campo numero | ↑ | 100.0 | - | - |
| campo data | ↑ | 100.0 | - | - |
| campo fornitore | ↑ | 80.0 | - | - |
| campo partita_iva | ↑ | 80.0 | - | - |
| campo imponibile | ↑ | 100.0 | - | - |
| campo iva | ↑ | 100.0 | - | - |
| campo totale | ↑ | 100.0 | - | - |
| campo righe | ↑ | 85.0 | - | - |
| righe singole | ↑ | 94.0 | - | - |

### prova — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta non vuota | ↑ | 100.0 | - | - |

## Casi saltati o in errore

- contratti: l'URL ufficiale del testo del CCNL non è impostato in cases/contratti/fonte.json

Macchina: x86_64, 4 CPU, Linux-6.18.44-fc-v185-x86_64-with-glibc2.39.
