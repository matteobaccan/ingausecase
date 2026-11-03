# Risultati di Inga 0.43.0

Eseguito con `inga 0.43.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.42.0).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 6:37 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | 142.9 | **143.2** | -0.3 | 19:39 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 82.5 | 82.5 | 0.0 | 18:49 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 2:53 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 10:28 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 29:51 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 82.5 | 82.5 | 0.0 | 3:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | 80.0 | **83.3** | -3.3 | 13:37 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | 82.2 | 82.2 | 0.0 | 24:37 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-cli | 181.7 | - | - | 6:50 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-confronto | 157.1 | - | - | 11:58 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-moe | 207.8 | - | - | 54:58 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| liyab-qualita | 82.5 | - | - | 19:46 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-velocita | 168.8 | - | - | 3:20 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | 20.0 | 0.0 | 52:54 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 92.5 | 92.5 | 0.0 | 12:58 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:02 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-recupero | 70.6 | **70.8** | -0.2 | 4:34 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | 85.0 | 85.0 | 0.0 | 72:57 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 55.0 | 55.0 | 0.0 | 64:54 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | 106.8 | **108.4** | -1.7 | 28:55 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | 91.7 | 91.7 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | 0.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 96.7 | 95.0 | +1.7 |
| tempo di llama.cpp su quello di Inga | ↑ | **119.3** | **135.1** | -15.8 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **128.8** | **128.1** | +0.7 |
| generazione (128 token), Inga su Colibri | ↑ | **157.1** | **158.3** | -1.3 |
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
| tempo di Colibri su quello di Inga | ↑ | **128.3** | **127.1** | +1.2 |
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
| urgenza | ↑ | 75.0 | 75.0 | 0.0 |
| reparto | ↑ | 90.0 | 90.0 | 0.0 |
| entrambi giusti | ↑ | 67.5 | 67.5 | 0.0 |

### gsm8k — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 80.0 | **83.3** | -3.3 |
| llama.cpp | ↑ | **83.3** | 83.3 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | 0.0 | -3.3 |
| risposte con lo stesso testo | ≈ | 56.7 | 40.0 | +16.7 |
| tempo di llama.cpp su quello di Inga | ↑ | 97.7 | 94.3 | +3.4 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.2 | 82.2 | 0.0 |
| llama.cpp | ↑ | **85.6** | 85.6 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | -3.3 | 0.0 |
| risposte con lo stesso testo | ≈ | 10.0 | 10.0 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | 86.2 | 87.1 | -0.9 |
| richieste con tutte le istruzioni, Inga | ↑ | 76.7 | 76.7 | 0.0 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | **80.0** | 80.0 | 0.0 |

### liyab-cli — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **252.6** | - | - |
| generazione (128 token), Inga su Liyab senza bozze | ↑ | **110.7** | - | - |
| generazione (128 token), Inga su Liyab con le sue bozze | ↑ | **111.2** | - | - |
| generazione, Inga (tok/s) | ↑ | 1004.0 | - | - |
| generazione, Liyab senza bozze (tok/s) | ↑ | 906.5 | - | - |
| generazione, Liyab con le sue bozze (tok/s) | ↑ | 903.1 | - | - |
| picco di memoria residente, Inga (MiB) | ↓ | 285490.0 | - | - |
| picco di memoria residente, Liyab (MiB) | ↓ | 250650.0 | - | - |
| picco di memoria, Inga su Liyab | ↓ | 113.9 | - | - |

### liyab-confronto — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: prompt, Inga API su Liyab | ↑ | **155.9** | - | - |
| qwen3-0.6b: generazione, Inga API su Liyab | ↑ | **215.9** | - | - |
| qwen3-0.6b: prompt, Inga bench su Liyab | ↑ | **154.1** | - | - |
| qwen3-0.6b: generazione, Inga bench su Liyab | ↑ | **373.7** | - | - |
| qwen3-0.6b: generazione, Inga API su Inga bench | ↑ | 57.8 | - | - |
| qwen3-0.6b: picco di RAM, Inga API (MiB) | ↑ | 104900.0 | - | - |
| qwen3-0.6b: picco di RAM, Inga bench (MiB) | ↑ | 129973.3 | - | - |
| qwen3-0.6b: picco di RAM, Liyab (MiB) | ↑ | 69923.3 | - | - |
| qwen3-4b: prompt, Inga API su Liyab | ↑ | **155.3** | - | - |
| qwen3-4b: generazione, Inga API su Liyab | ↑ | **101.5** | - | - |
| qwen3-4b: prompt, Inga bench su Liyab | ↑ | **156.1** | - | - |
| qwen3-4b: generazione, Inga bench su Liyab | ↑ | **126.1** | - | - |
| qwen3-4b: generazione, Inga API su Inga bench | ↑ | 80.4 | - | - |
| qwen3-4b: picco di RAM, Inga API (MiB) | ↑ | 273700.0 | - | - |
| qwen3-4b: picco di RAM, Inga bench (MiB) | ↑ | 285486.7 | - | - |
| qwen3-4b: picco di RAM, Liyab (MiB) | ↑ | 250633.3 | - | - |

### liyab-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **161.1** | - | - |
| generazione (128 token), Inga su Liyab | ↑ | **254.4** | - | - |
| lettura del prompt, Inga (tok/s) | ↑ | 2405.5 | - | - |
| lettura del prompt, Liyab (tok/s) | ↑ | 1493.0 | - | - |
| generazione, Inga (tok/s) | ↑ | 725.4 | - | - |
| generazione, Liyab (tok/s) | ↑ | 285.1 | - | - |
| picco di RAM, Inga (MiB) | ↑ | 1360890.0 | - | - |
| picco di RAM, Liyab (MiB) | ↑ | 774520.0 | - | - |
| risposte giuste, Inga | ↑ | 100.0 | - | - |
| risposte giuste, Liyab | ↑ | 10.0 | - | - |
| risposte con lo stesso testo | ≈ | 0.0 | - | - |

### liyab-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.5 | - | - |
| Liyab | ↑ | 80.0 | - | - |
| Inga meno Liyab | ↑ | **2.5** | - | - |
| risposte con lo stesso testo | ≈ | 62.5 | - | - |
| tempo di Liyab su quello di Inga | ↑ | **110.1** | - | - |
| picco di memoria residente, Inga (MiB) | ↑ | 364360.0 | - | - |
| picco di memoria residente, Liyab (MiB) | ↑ | 248580.0 | - | - |
| ARC, Inga | ↑ | 90.0 | - | - |
| ARC, Liyab | ↑ | 90.0 | - | - |
| GSM8K, Inga | ↑ | 75.0 | - | - |
| GSM8K, Liyab | ↑ | 70.0 | - | - |

### liyab-velocita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **247.5** | - | - |
| generazione (128 token), Inga su Liyab | ↑ | 90.0 | - | - |
| lettura del prompt, Inga (tok/s) | ↑ | 6336.1 | - | - |
| lettura del prompt, Liyab (tok/s) | ↑ | 2559.7 | - | - |
| generazione, Inga (tok/s) | ↑ | 916.1 | - | - |
| generazione, Liyab (tok/s) | ↑ | 1017.5 | - | - |
| picco di memoria residente, Inga (MiB) | ↑ | 302400.0 | - | - |
| picco di memoria residente, Liyab (MiB) | ↑ | 250820.0 | - | - |

### memoria — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| giuste, diario | ↑ | 30.0 | 30.0 | 0.0 |
| giuste, tutta la chat | ↑ | 70.0 | 70.0 | 0.0 |
| testo atteso contenuto, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| testo atteso contenuto, diario | ↑ | 30.0 | 30.0 | 0.0 |
| testo atteso contenuto, tutta la chat | ↑ | 60.0 | 60.0 | 0.0 |
| abstention, diario | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, diario | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, diario | ↑ | 50.0 | 50.0 | 0.0 |
| single-session-user, diario | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, diario | ↑ | 0.0 | 0.0 | 0.0 |
| abstention, oggi | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| single-session-user, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| sessioni scritte nel diario | ↑ | 87.5 | 87.5 | 0.0 |

### pdf — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| campo numero | ↑ | 100.0 | 100.0 | 0.0 |
| campo data | ↑ | 100.0 | 100.0 | 0.0 |
| campo fornitore | ↑ | 85.0 | 85.0 | 0.0 |
| campo partita_iva | ↑ | 85.0 | 85.0 | 0.0 |
| campo imponibile | ↑ | 100.0 | 100.0 | 0.0 |
| campo iva | ↑ | 100.0 | 100.0 | 0.0 |
| campo totale | ↑ | 100.0 | 100.0 | 0.0 |
| campo righe | ↑ | 70.0 | 70.0 | 0.0 |
| righe singole | ↑ | 88.0 | 88.0 | 0.0 |

### prova — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta non vuota | ↑ | 100.0 | 100.0 | 0.0 |

### rag-recupero — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| nDCG@10 | ↑ | 70.6 | **70.8** | -0.2 |
| recall@10 | ↑ | 91.7 | 91.7 | 0.0 |
| recall@5 | ↑ | 82.4 | 82.4 | 0.0 |
| MRR@10 | ↑ | 63.6 | **63.8** | -0.2 |

### rag-rgb — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta con rumore | ↑ | 100.0 | 100.0 | 0.0 |
| rifiuto senza la risposta | ↑ | 70.0 | 70.0 | 0.0 |
| passaggio giusto fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| risposte date con rumore | ↑ | 100.0 | 100.0 | 0.0 |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 55.0 | 55.0 | 0.0 |
| giuste senza strumenti | ↑ | 10.0 | **15.0** | -5.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 100.0 | 95.0 | +5.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **72.6** | **72.7** | -0.1 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | 136.8 | 119.2 | +17.6 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | **122.3** | **125.6** | -3.3 |
| generazione (tg128), Inga su llama.cpp | ↑ | 91.2 | 91.2 | 0.0 |
| perplexity, Inga su llama.cpp | ↓ | **99.9** | **99.9** | 0.0 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
