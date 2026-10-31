---
name: tono-veterano
description: Analisi e riscrittura di articoli tecnici con il tono di uno sviluppatore veterano, pragmatico, aneddotico e ironico, ricco di riferimenti pop, tecnologici e sportivi.
---

# Tono da sviluppatore veterano

Questa skill guida l'analisi (`check`) e la riscrittura (`align`) di articoli tecnici con un tono da programmatore di lungo corso: diretto, pragmatico, aneddotico e leggermente ironico, che unisce la credibilità tecnica alla capacità di raccontare e di parlare alla community degli sviluppatori.

## Modalità

1. **`check`**: non modifica il testo. Valuta i tratti di stile (struttura, tono, riferimenti, aneddoti, terminologia) e produce un report con suggerimenti puntuali e un voto di aderenza da 1 a 10.
2. **`align`**: riscrive l'articolo con lo stile, il tono e la struttura descritti qui. Paragrafi brevi e ritmati, aneddoti o metafore pop e calcistiche dove servono, massime in blocchi ```text, niente formalità accademica. Mostra le modifiche con un diff.

## Regole

### Struttura e formattazione
- Nessun frontmatter: l'articolo inizia dal titolo H1.
- Titoli in sentence case: maiuscola solo la prima parola (nomi propri e termini tecnici restano come sono: JavaScript, GitHub).
- Paragrafi da 1 a 3 righe, eccezionalmente 4.
- Le massime e i pensieri centrali vanno in blocchi ```text, non in citazioni `>`. Per esempio:
  ```text
  Talk is cheap. Show me the code
  ```
- Elenchi puntati spesso: manifesti, pro e contro, prove.
- Chiusura con `## Conclusione` o `## Conclusioni`: un bilancio pragmatico e un consiglio costruttivo.
- Niente emoji, salvo necessità tecniche.

### Temi
- **La gavetta**: programmare richiede tempo ed esperienza sul campo; i miti della riconversione facile o delle scorciatoie sul debito tecnico si smontano con realismo.
- **Il purismo macho**: ironia su chi usa solo l'editor più spartano per darsi un tono, sulle guerre di religione tra sistemi operativi, su chi rifiuta l'AI per orgoglio.
- **L'AI alleata, con giudizio**: ottima per il boilerplate e i test, ma non deve sostituire il problem solving di chi programma.
- **Ieri e oggi**: il software di una volta, centralizzato e con il posto fisso, contro il presente frammentato di servizi web, startup e strumenti che dettano i ritmi.

### Metafore e riferimenti
- Diventare programmatore senza gavetta come diventare chirurgo a metà carriera; chi fa tutto da solo come un meccanico che aggiusta il carburatore col martello; lo sviluppatore fuori contesto come "un giocatore di bowling in una partita di briscola"; le cartelle delle dipendenze come un accumulatore seriale (200 MB per un Hello World).
- Fantascienza e cultura pop: Star Trek (i Borg e l'assimilazione), Jurassic Park (chi tiene tutto a mente), The Matrix (vedere il codice).
- Cultura italiana: Luciano De Crescenzo, Antoine de Saint-Exupéry, Checco Zalone e il posto fisso, il Milanese Imbruttito.
- Detti della tecnologia: "640K ought to be enough for anybody", "Talk is cheap. Show me the code", Tony Hoare e il null pointer.

### Lessico
- Incipit colloquiali: "Chi passa molte ore online non può non aver visto..."
- Per smontare un mito: "Proviamo a portare un po' di realtà...", "Sia chiaro...", "Sfatiamo un'idea...", "Non nascondiamoci dietro a un dito...".
- Iperboli: "Ormai non conto più le notti passate a...", "come dice chi ha pestato la tastiera più di me...".
- Parole chiave: pestare la tastiera, gavetta, vibe coding, chiacchiere da bar, guerre di religione, accumulatore seriale, problem solving, posto fisso, Grande Capo.

### Termini tecnici
- In inglese, senza tradurli: Full Stack Developer, frontend, backend, devops, CLI, IDE, boilerplate, pull request, merge conflict, feature, framework.
- Maiuscole per ruoli e tendenze: Full Stack Developer, Grande Capo, Foundation Models.
- Strumenti e linguaggi citati con naturalezza (React, Node, Python, Go, Git, AWS), senza spiegazioni accademiche.
- Niente articolo davanti a marchi e linguaggi: "sviluppare su Windows", "usare JavaScript".

## Output

- **`check`**: analisi di aderenza (ritmo dei paragrafi, tono, aneddoti e metafore, terminologia); interventi consigliati; voto da 1 a 10 e una proposta di aneddoto o battuta.
- **`align`**: elenco delle modifiche; diff delle parti riscritte; altri spunti di aneddoti sul tema.

## Esempio

Testo di partenza:

> L'adozione di un approccio metodologico rigoroso nello sviluppo software richiede una pianificazione dettagliata delle specifiche. Spesso i programmatori tendono a iniziare la scrittura del codice senza aver prima definito i requisiti formali del sistema, confidando unicamente sulla propria memoria di lavoro. Questo modus operandi genera problemi di integrazione nelle fasi successive del ciclo di vita del progetto.

Riscrittura:

> Scrivere software è un atto che, in apparenza, chiunque può compiere. Ci si siede, si accende il computer e si inizia a digitare.
>
> Non servono nemmeno specifiche dettagliate: a cosa servono quando hai tutto in testa? A volte basta un'idea e la voglia di arrivare a un risultato. E qualcosa, inevitabilmente, accade.
>
> Questo approccio ha però un errore di base: la mente umana, per quanto meravigliosa, ha un limite alle informazioni che riesce a tenere. L'illusione di gestire tutto a memoria prima o poi si scontra con la realtà, e porta il progetto dritto verso il collasso.
