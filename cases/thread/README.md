# thread

Quanto della differenza di velocità in generazione fra Inga, llama.cpp e Liyab viene dal
numero di thread. In [velocita](https://github.com/matteobaccan/ingausecase/blob/cases/cases/velocita/README.md)
e [liyab-velocita](https://github.com/matteobaccan/ingausecase/blob/cases/cases/liyab-velocita/README.md)
Inga parte senza `-t` e in generazione usa un thread per core fisico (2 su un runner a 4
vCPU con SMT), mentre llama.cpp e Liyab ne ricevono 4.

Qui tutti e tre generano 128 token con 2 e con 4 thread, 3 ripetizioni, sulla stessa
macchina (Qwen3-4B Q4_K_M):

- Inga: `inga bench -p 0 -n 128 -r 3 -t T`, e una volta senza `-t`;
- llama.cpp: `llama-bench -p 0 -n 128 -r 3 -t T`;
- Liyab: `liyab-cli --threads T --json`, un prompt breve, la media di 3 prove.

Voci: Inga su llama.cpp e Inga su Liyab a parità di thread, quanto guadagna ognuno da 2 a
4 thread, e Inga senza `-t` su llama.cpp con 4. Voto: Inga su llama.cpp con 4 thread. Il
JSON tiene l'uscita di `lscpu`.
