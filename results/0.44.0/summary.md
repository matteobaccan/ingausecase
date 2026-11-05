# Risultati di Inga 0.44.0

Eseguito con `inga 0.44.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.43.0).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 2:28 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| canale-http | **78.9** | 68.6 | +10.3 | 42:22 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | **155.5** | 142.9 | +12.5 | 18:26 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 80.0 | **82.5** | -2.5 | 11:05 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 2:51 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 16:52 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 29:34 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 81.2 | **82.5** | -1.2 | 2:12 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | **83.3** | 80.0 | +3.3 | 20:24 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | 82.2 | 82.2 | 0.0 | 29:11 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-cli | 142.5 | **181.7** | -39.2 | 7:25 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-confronto | **294.3** | 157.1 | +137.1 | 10:15 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-moe | **246.9** | 207.8 | +39.1 | 48:34 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| liyab-qualita | 82.5 | 82.5 | 0.0 | 19:15 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-velocita | **136.6** | 130.5 | +6.1 | 4:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | 20.0 | 0.0 | 50:49 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 92.5 | 92.5 | 0.0 | 12:31 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:02 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-recupero | **70.8** | 70.6 | +0.2 | 8:39 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | 82.5 | **85.0** | -2.5 | 40:45 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| thread | 132.3 | - | - | 7:08 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 55.0 | 55.0 | 0.0 | 45:01 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | **129.3** | 106.8 | +22.5 | 20:00 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | 91.7 | 91.7 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | 0.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 95.0 | 96.7 | -1.7 |
| tempo di llama.cpp su quello di Inga | ↑ | **139.2** | **119.3** | +19.9 |

### canale-http — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **183.0** | - | - |
| qwen3-0.6b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **289.8** | - | - |
| qwen3-0.6b: generazione a d=2048, split-KV su spento | ↑ | **100.6** | - | - |
| qwen3-0.6b: generazione a d=4096, split-KV su spento | ↑ | 99.6 | - | - |
| qwen3-0.6b: generazione bench, tok/s | ↑ | **4768.8** | 3723.1 | +1045.7 |
| qwen3-0.6b: prompt bench, tok/s | ↑ | **15203.8** | 14591.2 | +612.6 |
| qwen3-0.6b: generazione bench_d, tok/s | ↑ | **3814.4** | 2399.4 | +1414.9 |
| qwen3-0.6b: generazione bench_d su bench | ↑ | 80.0 | 64.4 | +15.5 |
| qwen3-0.6b: prompt bench_d, tok/s | ↑ | **13369.5** | 12705.0 | +664.5 |
| qwen3-0.6b: generazione bench_t, tok/s | ↑ | **4943.2** | 3841.4 | +1101.8 |
| qwen3-0.6b: generazione bench_t su bench | ↑ | **103.7** | **103.2** | +0.5 |
| qwen3-0.6b: prompt bench_t, tok/s | ↑ | **14541.5** | 14117.5 | +424.1 |
| qwen3-0.6b: generazione run, tok/s | ↑ | **3470.0** | 2226.7 | +1243.3 |
| qwen3-0.6b: generazione run su bench | ↑ | 72.8 | 59.8 | +13.0 |
| qwen3-0.6b: prompt run, tok/s | ↑ | **15066.7** | 14716.7 | +350.0 |
| qwen3-0.6b: generazione run_corto, tok/s | ↑ | **4376.7** | 3360.0 | +1016.7 |
| qwen3-0.6b: generazione run_corto su bench | ↑ | 91.8 | 90.2 | +1.5 |
| qwen3-0.6b: prompt run_corto, tok/s | ↑ | **16330.0** | 15630.0 | +700.0 |
| qwen3-0.6b: generazione api, tok/s | ↑ | **3355.4** | 2147.3 | +1208.1 |
| qwen3-0.6b: generazione api su bench | ↑ | 70.4 | 57.7 | +12.7 |
| qwen3-0.6b: generazione api, il motore, tok/s | ↑ | **3382.2** | 2164.4 | +1217.8 |
| qwen3-0.6b: generazione api, il motore su bench | ↑ | 70.9 | 58.1 | +12.8 |
| qwen3-0.6b: prompt api, tok/s | ↑ | **15195.5** | 14809.8 | +385.6 |
| qwen3-0.6b: generazione stream, tok/s | ↑ | **3368.1** | 2122.9 | +1245.3 |
| qwen3-0.6b: generazione stream su bench | ↑ | 70.6 | 57.0 | +13.6 |
| qwen3-0.6b: generazione stream, il motore, tok/s | ↑ | **3394.5** | 2139.5 | +1255.0 |
| qwen3-0.6b: generazione stream, il motore su bench | ↑ | 71.2 | 57.5 | +13.7 |
| qwen3-0.6b: prompt stream, tok/s | ↑ | **15205.7** | 14763.4 | +442.3 |
| qwen3-0.6b: generazione stream_meno, tok/s | ↑ | **3378.9** | 2185.0 | +1193.9 |
| qwen3-0.6b: generazione stream_meno su bench | ↑ | 70.9 | 58.7 | +12.2 |
| qwen3-0.6b: generazione stream_meno, il motore, tok/s | ↑ | **3404.6** | 2202.0 | +1202.6 |
| qwen3-0.6b: generazione stream_meno, il motore su bench | ↑ | 71.4 | 59.1 | +12.2 |
| qwen3-0.6b: prompt stream_meno, tok/s | ↑ | **15128.6** | 14815.4 | +313.3 |
| qwen3-4b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **126.6** | - | - |
| qwen3-4b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **180.7** | - | - |
| qwen3-4b: generazione a d=2048, split-KV su spento | ↑ | **100.2** | - | - |
| qwen3-4b: generazione bench, tok/s | ↑ | **1140.6** | 961.6 | +179.1 |
| qwen3-4b: prompt bench, tok/s | ↑ | **3272.6** | 3246.7 | +25.9 |
| qwen3-4b: generazione bench_d, tok/s | ↑ | **1038.4** | 806.0 | +232.4 |
| qwen3-4b: generazione bench_d su bench | ↑ | 91.0 | 83.8 | +7.2 |
| qwen3-4b: prompt bench_d, tok/s | ↑ | **3053.9** | 3010.6 | +43.3 |
| qwen3-4b: generazione bench_t, tok/s | ↑ | **1159.3** | 968.8 | +190.5 |
| qwen3-4b: generazione bench_t su bench | ↑ | **101.6** | **100.8** | +0.9 |
| qwen3-4b: prompt bench_t, tok/s | ↑ | 3171.3 | **3178.7** | -7.4 |
| qwen3-4b: generazione run, tok/s | ↑ | **990.0** | 776.7 | +213.3 |
| qwen3-4b: generazione run su bench | ↑ | 86.8 | 80.8 | +6.0 |
| qwen3-4b: prompt run, tok/s | ↑ | **3243.3** | 3213.3 | +30.0 |
| qwen3-4b: generazione run_corto, tok/s | ↑ | **1080.0** | 920.0 | +160.0 |
| qwen3-4b: generazione run_corto su bench | ↑ | 94.7 | 95.7 | -1.0 |
| qwen3-4b: prompt run_corto, tok/s | ↑ | **3073.3** | 3066.7 | +6.7 |
| qwen3-4b: generazione api, tok/s | ↑ | **978.8** | 790.3 | +188.5 |
| qwen3-4b: generazione api su bench | ↑ | 85.8 | 82.2 | +3.6 |
| qwen3-4b: generazione api, il motore, tok/s | ↑ | **986.5** | 796.6 | +190.0 |
| qwen3-4b: generazione api, il motore su bench | ↑ | 86.5 | 82.8 | +3.6 |
| qwen3-4b: prompt api, tok/s | ↑ | **3251.8** | 3220.1 | +31.7 |
| qwen3-4b: generazione stream, tok/s | ↑ | **994.3** | 770.5 | +223.8 |
| qwen3-4b: generazione stream su bench | ↑ | 87.2 | 80.1 | +7.0 |
| qwen3-4b: generazione stream, il motore, tok/s | ↑ | **1002.1** | 776.6 | +225.5 |
| qwen3-4b: generazione stream, il motore su bench | ↑ | 87.9 | 80.8 | +7.1 |
| qwen3-4b: prompt stream, tok/s | ↑ | **3237.6** | 3223.7 | +13.9 |
| qwen3-4b: generazione stream_meno, tok/s | ↑ | **1013.9** | 798.9 | +215.0 |
| qwen3-4b: generazione stream_meno su bench | ↑ | 88.9 | 83.1 | +5.8 |
| qwen3-4b: generazione stream_meno, il motore, tok/s | ↑ | **1021.9** | 805.2 | +216.7 |
| qwen3-4b: generazione stream_meno, il motore su bench | ↑ | 89.6 | 83.7 | +5.9 |
| qwen3-4b: prompt stream_meno, tok/s | ↑ | **3241.0** | 3227.2 | +13.9 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **144.4** | **128.8** | +15.6 |
| generazione (128 token), Inga su Colibri | ↑ | **166.5** | **157.1** | +9.5 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Colibri | ↑ | 100.0 | 100.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 70.0 | 70.0 | 0.0 |

### colibri-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 80.0 | **82.5** | -2.5 |
| Colibri | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Colibri | ↑ | 0.0 | **2.5** | -2.5 |
| risposte con lo stesso testo | ≈ | 45.0 | 42.5 | +2.5 |
| tempo di Colibri su quello di Inga | ↑ | **134.7** | **128.3** | +6.4 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Colibri | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | 70.0 | **75.0** | -5.0 |
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
| urgenza | ↑ | 72.5 | **75.0** | -2.5 |
| reparto | ↑ | 90.0 | 90.0 | 0.0 |
| entrambi giusti | ↑ | 65.0 | **67.5** | -2.5 |

### gsm8k — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **83.3** | 80.0 | +3.3 |
| llama.cpp | ↑ | 83.3 | 83.3 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | -3.3 | +3.3 |
| risposte con lo stesso testo | ≈ | 40.0 | 56.7 | -16.7 |
| tempo di llama.cpp su quello di Inga | ↑ | 95.9 | 97.7 | -1.8 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.2 | 82.2 | 0.0 |
| llama.cpp | ↑ | **85.6** | 85.6 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | -3.3 | 0.0 |
| risposte con lo stesso testo | ≈ | 10.0 | 10.0 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | 91.9 | 86.2 | +5.8 |
| richieste con tutte le istruzioni, Inga | ↑ | 76.7 | 76.7 | 0.0 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | **80.0** | 80.0 | 0.0 |

### liyab-cli — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **155.6** | **252.6** | -97.1 |
| generazione (128 token), Inga su Liyab senza bozze | ↑ | **129.5** | **110.7** | +18.7 |
| generazione (128 token), Inga su Liyab con le sue bozze | ↑ | **130.1** | **111.2** | +18.9 |
| generazione, Inga (tok/s) | ↑ | **1147.4** | 1004.0 | +143.4 |
| generazione, Liyab senza bozze (tok/s) | ↑ | 886.3 | **906.5** | -20.3 |
| generazione, Liyab con le sue bozze (tok/s) | ↑ | 882.0 | **903.1** | -21.0 |
| picco di memoria residente, Inga (MiB) | ↓ | 285530.0 | **285490.0** | +40.0 |
| picco di memoria residente, Liyab (MiB) | ↓ | 250660.0 | **250650.0** | +10.0 |
| picco di memoria, Inga su Liyab | ↓ | 113.9 | 113.9 | 0.0 |

### liyab-confronto — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: prompt, Inga API su Liyab | ↑ | **415.1** | **155.9** | +259.3 |
| qwen3-0.6b: generazione, Inga API su Liyab | ↑ | **280.2** | **215.9** | +64.3 |
| qwen3-0.6b: prompt, Inga bench su Liyab | ↑ | **415.4** | **154.1** | +261.3 |
| qwen3-0.6b: generazione, Inga bench su Liyab | ↑ | **342.4** | **373.7** | -31.3 |
| qwen3-0.6b: generazione, Inga API su Inga bench | ↑ | 81.8 | 57.8 | +24.1 |
| qwen3-0.6b: picco di RAM, Inga API (MiB) | ↑ | 104900.0 | 104900.0 | 0.0 |
| qwen3-0.6b: picco di RAM, Inga bench (MiB) | ↑ | 128836.7 | **129973.3** | -1136.7 |
| qwen3-0.6b: picco di RAM, Liyab (MiB) | ↑ | **69933.3** | 69923.3 | +10.0 |
| qwen3-4b: prompt, Inga API su Liyab | ↑ | **369.3** | **155.3** | +214.0 |
| qwen3-4b: generazione, Inga API su Liyab | ↑ | **112.4** | **101.5** | +10.9 |
| qwen3-4b: prompt, Inga bench su Liyab | ↑ | **370.0** | **156.1** | +214.0 |
| qwen3-4b: generazione, Inga bench su Liyab | ↑ | **121.6** | **126.1** | -4.5 |
| qwen3-4b: generazione, Inga API su Inga bench | ↑ | 92.4 | 80.4 | +11.9 |
| qwen3-4b: picco di RAM, Inga API (MiB) | ↑ | 273700.0 | 273700.0 | 0.0 |
| qwen3-4b: picco di RAM, Inga bench (MiB) | ↑ | **285566.7** | 285486.7 | +80.0 |
| qwen3-4b: picco di RAM, Liyab (MiB) | ↑ | 250633.3 | 250633.3 | 0.0 |

### liyab-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **194.3** | **161.1** | +33.2 |
| generazione (128 token), Inga su Liyab | ↑ | **299.5** | **254.4** | +45.1 |
| lettura del prompt, Inga (tok/s) | ↑ | **2922.4** | 2405.5 | +516.9 |
| lettura del prompt, Liyab (tok/s) | ↑ | **1503.9** | 1493.0 | +10.9 |
| generazione, Inga (tok/s) | ↑ | **879.3** | 725.4 | +153.9 |
| generazione, Liyab (tok/s) | ↑ | **293.6** | 285.1 | +8.4 |
| picco di RAM, Inga (MiB) | ↑ | **1366620.0** | 1360890.0 | +5730.0 |
| picco di RAM, Liyab (MiB) | ↑ | 774470.0 | **774520.0** | -50.0 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Liyab | ↑ | 10.0 | 10.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 0.0 | 0.0 | 0.0 |

### liyab-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.5 | 82.5 | 0.0 |
| Liyab | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Liyab | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 62.5 | 55.0 | +7.5 |
| tempo di Liyab su quello di Inga | ↑ | **117.8** | **113.0** | +4.9 |
| picco di memoria residente, Inga (MiB) | ↑ | **366330.0** | 363490.0 | +2840.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 248570.0 | **248590.0** | -20.0 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Liyab | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | 75.0 | 75.0 | 0.0 |
| GSM8K, Liyab | ↑ | 70.0 | 70.0 | 0.0 |

### liyab-velocita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **157.0** | **156.5** | +0.6 |
| generazione (128 token), Inga su Liyab | ↑ | **116.2** | **104.6** | +11.7 |
| lettura del prompt, Inga (tok/s) | ↑ | **3254.9** | 3251.6 | +3.3 |
| lettura del prompt, Liyab (tok/s) | ↑ | 2072.6 | **2077.9** | -5.3 |
| generazione, Inga (tok/s) | ↑ | **1012.2** | 911.6 | +100.6 |
| generazione, Liyab (tok/s) | ↑ | 870.7 | **871.6** | -0.9 |
| picco di memoria residente, Inga (MiB) | ↑ | **302610.0** | 302370.0 | +240.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | **250830.0** | 250820.0 | +10.0 |

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
| nDCG@10 | ↑ | **70.8** | 70.6 | +0.2 |
| recall@10 | ↑ | 91.7 | 91.7 | 0.0 |
| recall@5 | ↑ | 82.4 | 82.4 | 0.0 |
| MRR@10 | ↑ | **63.8** | 63.6 | +0.2 |

### rag-rgb — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta con rumore | ↑ | 100.0 | 100.0 | 0.0 |
| rifiuto senza la risposta | ↑ | 65.0 | **70.0** | -5.0 |
| passaggio giusto fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| risposte date con rumore | ↑ | 100.0 | 100.0 | 0.0 |

### thread — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| generazione con 2 thread, Inga su llama.cpp | ↑ | **106.9** | - | - |
| generazione con 2 thread, Inga su Liyab | ↑ | **180.2** | - | - |
| generazione con 4 thread, Inga su llama.cpp | ↑ | **132.3** | - | - |
| generazione con 4 thread, Inga su Liyab | ↑ | **145.6** | - | - |
| Inga con 4 thread su Inga con 2 | ↑ | **140.8** | - | - |
| llama.cpp con 4 thread su llama.cpp con 2 | ↑ | **113.8** | - | - |
| Inga senza -t su llama.cpp con 4 thread | ↑ | 93.9 | - | - |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 55.0 | 55.0 | 0.0 |
| giuste senza strumenti | ↑ | 10.0 | 10.0 | 0.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 100.0 | 100.0 | 0.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **72.6** | **72.6** | 0.0 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | 136.8 | 136.8 | 0.0 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | **159.4** | **122.3** | +37.1 |
| generazione (tg128), Inga su llama.cpp | ↑ | 99.1 | 91.2 | +7.9 |
| perplexity, Inga su llama.cpp | ↓ | **99.8** | **99.9** | -0.1 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
