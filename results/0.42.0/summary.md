# Risultati di Inga 0.42.0

Eseguito con `inga 0.42.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.41.0).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 4:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | 143.2 | **174.0** | -30.8 | 19:28 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 82.5 | 82.5 | 0.0 | 18:42 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 2:54 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 29:22 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 31:02 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 82.5 | **83.8** | -1.3 | 3:21 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | 83.3 | 83.3 | 0.0 | 20:15 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | 82.2 | 82.2 | 0.0 | 30:41 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | - | - | 53:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 92.5 | **93.1** | -0.6 | 13:29 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:09 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-recupero | 70.8 | - | - | 8:57 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | **85.0** | 82.5 | +2.5 | 72:21 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 55.0 | 55.0 | 0.0 | 82:55 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | **108.4** | 108.2 | +0.2 | 28:47 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | 91.7 | 91.7 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | 0.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 95.0 | 95.0 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | **135.1** | **136.4** | -1.3 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **128.1** | **162.4** | -34.4 |
| generazione (128 token), Inga su Colibri | ↑ | **158.3** | **185.6** | -27.2 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Colibri | ↑ | 100.0 | 100.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 70.0 | 70.0 | 0.0 |

### colibri-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **82.5** | 82.5 | 0.0 |
| Colibri | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Colibri | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 42.5 | 42.5 | 0.0 |
| tempo di Colibri su quello di Inga | ↑ | **127.1** | **128.9** | -1.7 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Colibri | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | **75.0** | 75.0 | 0.0 |
| GSM8K, Colibri | ↑ | 70.0 | 70.0 | 0.0 |

### contratti — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta | ↑ | 93.3 | 93.3 | 0.0 |
| articolo giusto | ↑ | 60.0 | 60.0 | 0.0 |
| citazione fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| estratti dal distrattore | ↓ | 27.7 | 27.7 | 0.0 |

### documenti — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta | ↑ | 100.0 | 100.0 | 0.0 |
| pagina giusta | ↑ | 100.0 | 100.0 | 0.0 |
| pagina giusta fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| estratti dal distrattore | ↓ | 1.7 | 1.7 | 0.0 |

### email — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| urgenza | ↑ | 75.0 | **80.0** | -5.0 |
| reparto | ↑ | **90.0** | 87.5 | +2.5 |
| entrambi giusti | ↑ | 67.5 | 67.5 | 0.0 |

### gsm8k — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 83.3 | 83.3 | 0.0 |
| llama.cpp | ↑ | 83.3 | 83.3 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | 0.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 40.0 | 40.0 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | 94.3 | 94.0 | +0.3 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.2 | 82.2 | 0.0 |
| llama.cpp | ↑ | **85.6** | 85.6 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | -3.3 | 0.0 |
| risposte con lo stesso testo | ≈ | 10.0 | 10.0 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | 87.1 | 87.7 | -0.6 |
| richieste con tutte le istruzioni, Inga | ↑ | 76.7 | 76.7 | 0.0 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | **80.0** | 80.0 | 0.0 |

### memoria — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste, oggi | ↑ | 20.0 | - | - |
| giuste, diario | ↑ | 30.0 | - | - |
| giuste, tutta la chat | ↑ | 70.0 | - | - |
| testo atteso contenuto, oggi | ↑ | 20.0 | - | - |
| testo atteso contenuto, diario | ↑ | 30.0 | - | - |
| testo atteso contenuto, tutta la chat | ↑ | 60.0 | - | - |
| abstention, diario | ↑ | 100.0 | - | - |
| knowledge-update, diario | ↑ | 0.0 | - | - |
| multi-session, diario | ↑ | 50.0 | - | - |
| single-session-user, diario | ↑ | 0.0 | - | - |
| temporal-reasoning, diario | ↑ | 0.0 | - | - |
| abstention, oggi | ↑ | 100.0 | - | - |
| knowledge-update, oggi | ↑ | 0.0 | - | - |
| multi-session, oggi | ↑ | 0.0 | - | - |
| single-session-user, oggi | ↑ | 0.0 | - | - |
| temporal-reasoning, oggi | ↑ | 0.0 | - | - |
| sessioni scritte nel diario | ↑ | 87.5 | - | - |

### pdf — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| campo numero | ↑ | 100.0 | 100.0 | 0.0 |
| campo data | ↑ | 100.0 | 100.0 | 0.0 |
| campo fornitore | ↑ | **85.0** | 80.0 | +5.0 |
| campo partita_iva | ↑ | **85.0** | 80.0 | +5.0 |
| campo imponibile | ↑ | 100.0 | 100.0 | 0.0 |
| campo iva | ↑ | 100.0 | 100.0 | 0.0 |
| campo totale | ↑ | 100.0 | 100.0 | 0.0 |
| campo righe | ↑ | 70.0 | **85.0** | -15.0 |
| righe singole | ↑ | 88.0 | **94.0** | -6.0 |

### prova — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta non vuota | ↑ | 100.0 | 100.0 | 0.0 |

### rag-recupero — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| nDCG@10 | ↑ | 70.8 | - | - |
| recall@10 | ↑ | 91.7 | - | - |
| recall@5 | ↑ | 82.4 | - | - |
| MRR@10 | ↑ | 63.8 | - | - |

### rag-rgb — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta con rumore | ↑ | 100.0 | 100.0 | 0.0 |
| rifiuto senza la risposta | ↑ | **70.0** | 65.0 | +5.0 |
| passaggio giusto fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| risposte date con rumore | ↑ | 100.0 | 100.0 | 0.0 |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 55.0 | 55.0 | 0.0 |
| giuste senza strumenti | ↑ | 15.0 | 15.0 | 0.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 95.0 | 95.0 | 0.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **72.7** | **72.7** | 0.0 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | 119.2 | 119.2 | 0.0 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | **125.6** | **125.2** | +0.4 |
| generazione (tg128), Inga su llama.cpp | ↑ | 91.2 | 91.2 | 0.0 |
| perplexity, Inga su llama.cpp | ↓ | **99.9** | **99.9** | 0.0 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
