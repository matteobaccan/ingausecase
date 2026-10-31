# Prova

Il caso più piccolo: avvia `inga serve` con Qwen3-0.6B (Q8_0), fa una domanda in chat
in streaming e controlla che la risposta non sia vuota. Serve a capire subito se una
versione si avvia e risponde, prima dei casi lunghi.

Come si dà il voto: 100 se la risposta non è vuota, 0 altrimenti. Nei dettagli del
risultato ci sono anche il tempo al primo token, il tempo della risposta e se la
risposta nomina Roma (solo informativo, non entra nel voto).
