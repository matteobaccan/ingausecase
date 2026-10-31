# Risultati

Una cartella per versione di Inga (`results/<versione>/`), scritta dal runner:

- `<caso>.json`: il risultato di un caso: `stato` (`ok`, `saltato` o `errore`),
  `voto` da 0 a 1, `voci` (i voti parziali), `motivo`, `dettagli`, il modello con il
  suo sha256, il seed e il tempo;
- `summary.md`: la tabella dei casi con il voto, il voto della versione precedente
  presente qui, la differenza, il tempo e il modello, poi le voci di ogni caso.

Le cartelle si confrontano per numero di versione; un voto più basso non fa fallire
l'esecuzione, un caso in errore sì.
