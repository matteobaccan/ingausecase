# liyab-cli

Inga e [Liyab](https://github.com/andrei-borcea/liyab) **senza server HTTP**, ognuno con il suo comando di misura, sullo stesso GGUF e sulla stessa macchina: `inga bench -p 512 -n 128 -r 3 --json` per Inga, `liyab-cli --json` per Liyab (circa 512 token di prompt, 128 generati, 3 prove dopo una non misurata), una volta con le impostazioni di Liyab (le sue "bozze dal testo") e una con `--no-lookup`. Il picco di memoria residente di ogni processo da `/usr/bin/time -v`, lo stesso modo per i due; il runner non avvia `inga serve`.

Voto: la media dei rapporti di velocità Inga su Liyab senza bozze. Il prompt di `inga bench` è di token casuali e la sua generazione parte da un contesto vuoto, quella di Liyab dopo il prompt: con un modello da 4B la differenza è piccola, ma c'è.
