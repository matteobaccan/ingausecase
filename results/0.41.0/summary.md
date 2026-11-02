# Risultati di Inga 0.41.0

Eseguito con `inga 0.41.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.40.0).

| Caso | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | - | - | 4:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | 174.0 | - | - | 25:20 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 82.5 | - | - | 18:39 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 2:51 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | - | - | 29:04 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 17:21 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 83.8 | 83.8 | 0.0 | 2:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | 83.3 | - | - | 19:53 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | 82.2 | - | - | 31:22 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | - | - | - | 0:04 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | saltato |
| pdf | 93.1 | 93.1 | 0.0 | 10:45 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:15 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-recupero | - | - | - | 0:06 | Qwen3-0.6B-Q8_0.gguf | saltato |
| rag-rgb | 82.5 | - | - | 35:38 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 55.0 | - | - | 77:15 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | 108.2 | - | - | 28:54 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| Inga | 91.7 | - | - |
| llama.cpp | 91.7 | - | - |
| Inga meno llama.cpp | 0.0 | - | - |
| risposte con lo stesso testo | 95.0 | - | - |
| tempo di llama.cpp su quello di Inga | 136.4 | - | - |

### colibri-moe

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | 162.4 | - | - |
| generazione (128 token), Inga su Colibri | 185.6 | - | - |
| risposte giuste, Inga | 100.0 | - | - |
| risposte giuste, Colibri | 100.0 | - | - |
| risposte con lo stesso testo | 70.0 | - | - |

### colibri-qualita

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| Inga | 82.5 | - | - |
| Colibri | 80.0 | - | - |
| Inga meno Colibri | 2.5 | - | - |
| risposte con lo stesso testo | 42.5 | - | - |
| tempo di Colibri su quello di Inga | 128.9 | - | - |
| ARC, Inga | 90.0 | - | - |
| ARC, Colibri | 90.0 | - | - |
| GSM8K, Inga | 75.0 | - | - |
| GSM8K, Colibri | 70.0 | - | - |

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

### gsm8k

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| Inga | 83.3 | - | - |
| llama.cpp | 83.3 | - | - |
| Inga meno llama.cpp | 0.0 | - | - |
| risposte con lo stesso testo | 40.0 | - | - |
| tempo di llama.cpp su quello di Inga | 94.0 | - | - |

### ifeval

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| Inga | 82.2 | - | - |
| llama.cpp | 85.6 | - | - |
| Inga meno llama.cpp | -3.3 | - | - |
| risposte con lo stesso testo | 10.0 | - | - |
| tempo di llama.cpp su quello di Inga | 87.7 | - | - |
| richieste con tutte le istruzioni, Inga | 76.7 | - | - |
| richieste con tutte le istruzioni, llama.cpp | 80.0 | - | - |

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

### rag-rgb

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| risposta giusta con rumore | 100.0 | - | - |
| rifiuto senza la risposta | 65.0 | - | - |
| passaggio giusto fra gli estratti | 100.0 | - | - |
| risposte date con rumore | 100.0 | - | - |

### tokensave

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| giuste con tokensave | 55.0 | - | - |
| giuste senza strumenti | 15.0 | - | - |
| giuste con il codice nel prompt | 90.0 | - | - |
| domande con almeno una chiamata a tokensave | 95.0 | - | - |
| token del prompt per domanda, con tokensave su codice nel prompt | 72.7 | - | - |
| token generati per domanda, con tokensave su senza strumenti | 119.2 | - | - |

### velocita

| Voce | Valore | Valore precedente | Differenza |
| --- | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | 125.2 | - | - |
| generazione (tg128), Inga su llama.cpp | 91.2 | - | - |
| perplexity, Inga su llama.cpp | 99.9 | - | - |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''
- memoria: questa versione non ha i progetti: GET /api/inga/projects: HTTP 404 (questa versione di Inga non lo ha)
- rag-recupero: GET /api/inga/documents/search?q=prova&collection=scifact&k=1: HTTP 404 (questa versione di Inga non lo ha)

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
