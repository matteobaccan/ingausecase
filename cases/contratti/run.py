"""Caso contratti: domande con risposta nota sul CCNL del commercio.

Il testo del contratto si scarica a ogni esecuzione dall'URL di fonte.json (mai nel
repository), se ne estrae il testo con pypdf e lo si divide per articoli. Per ogni
domanda verificata (domande.json, "verificata": true) gli articoli più vicini alla
domanda, scelti per parole in comune (BM25), vanno a Inga come documenti
(inga_documents), ciascuno con il suo numero; la risposta deve contenere il dato
atteso e citare l'articolo giusto.

Il caso si salta, con il motivo, se l'URL non è impostato, se il testo non si scarica
o se nessuna domanda è ancora verificata sul testo.
"""

import json
import math
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402

ARTICOLI_PER_DOMANDA = 4

SISTEMA = (
    "Rispondi alle domande sul contratto collettivo nazionale del commercio usando solo "
    "gli articoli dati. Rispondi in italiano con una frase breve che contenga il dato "
    "chiesto, e indica in 'articolo' il numero dell'articolo da cui viene la risposta."
)


def salta(motivo):
    print(f"caso saltato: {motivo}")
    inga_api.write_result({"stato": "saltato", "motivo": motivo})
    sys.exit(0)


def compatto(s):
    return re.sub(r"[\s.,'’\-]", "", str(s).casefold())


def parole(s):
    return re.findall(r"[a-zà-ù0-9]{3,}", s.casefold())


def articoli(testo):
    """{numero: testo} dagli inizi di riga 'Art. N' / 'Articolo N'."""
    parti = re.split(r"(?m)^\s*(?:Art\.|Articolo)\s*(\d+)\b", testo)
    out = {}
    for i in range(1, len(parti) - 1, 2):
        n = parti[i]
        out[n] = (out.get(n, "") + f"Art. {n}" + parti[i + 1]).strip()
    return out


def bm25(domanda, docs, k1=1.5, b=0.75):
    tok = {k: parole(v) for k, v in docs.items()}
    media = sum(len(t) for t in tok.values()) / max(1, len(tok))
    df = {}
    for t in tok.values():
        for w in set(t):
            df[w] = df.get(w, 0) + 1
    n = len(tok)
    punti = {}
    for k, t in tok.items():
        s = 0.0
        for w in set(parole(domanda)):
            if w not in df:
                continue
            f = t.count(w)
            idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
            s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * len(t) / media))
        punti[k] = s
    return sorted(punti, key=lambda k: -punti[k])


def main():
    cdir = inga_api.case_dir()
    with open(os.path.join(cdir, "fonte.json"), encoding="utf-8") as f:
        fonte = json.load(f)
    with open(os.path.join(cdir, "domande.json"), encoding="utf-8") as f:
        domande = [q for q in json.load(f) if q.get("verificata")]
    if not fonte.get("url"):
        salta("l'URL ufficiale del testo del CCNL non è impostato in cases/contratti/fonte.json")
    pdf = os.path.join(inga_api.work_dir(), "ccnl.pdf")
    try:
        req = urllib.request.Request(fonte["url"], headers={"User-Agent": "ingausecase-runner"})
        with urllib.request.urlopen(req, timeout=120) as r, open(pdf, "wb") as out:
            out.write(r.read())
    except OSError as e:
        salta(f"il testo del CCNL non si scarica da {fonte['url']}: {e}")
    if not domande:
        salta("nessuna domanda di cases/contratti/domande.json è ancora verificata sul testo")

    from pypdf import PdfReader
    testo = "\n".join(p.extract_text() or "" for p in PdfReader(pdf).pages)
    arts = articoli(testo)
    if len(arts) < 50:
        salta(f"dal PDF si leggono solo {len(arts)} articoli: il file non sembra il testo del CCNL")
    ok_r = ok_a = 0
    righe = []
    for q in domande:
        scelti = bm25(q["domanda"], arts)[:ARTICOLI_PER_DOMANDA]
        docs = [{"name": f"Art. {n}", "text": arts[n]} for n in scelti]
        schema = {"type": "object",
                  "properties": {"risposta": {"type": "string", "maxLength": 400},
                                 "articolo": {"type": "string", "enum": scelti}},
                  "required": ["risposta", "articolo"]}
        try:
            dato, raw, sec = inga_api.chat(
                [{"role": "system", "content": SISTEMA}, {"role": "user", "content": q["domanda"]}],
                schema=schema, max_tokens=300, extra={"inga_documents": docs})
        except (ValueError, RuntimeError) as e:
            print(f"{q['id']}: risposta non valida: {e}")
            dato, sec = {}, 0.0
        r_ok = any(compatto(r) in compatto(dato.get("risposta", "")) for r in q["risposte"])
        a_ok = str(dato.get("articolo")) == str(q["articolo"])
        ok_r += r_ok
        ok_a += a_ok
        print(f"{q['id']:2d}: risposta {'ok' if r_ok else 'NO'}, articolo {dato.get('articolo')} "
              f"({'ok' if a_ok else 'atteso ' + str(q['articolo'])}), recuperati {scelti}, {sec:.1f} s")
        righe.append({"id": q["id"], "dato": dato, "articoli_recuperati": scelti,
                      "articolo_atteso_recuperato": str(q["articolo"]) in scelti,
                      "risposta_ok": r_ok, "articolo_ok": a_ok, "secondi": round(sec, 1)})
    n = len(domande)
    inga_api.write_result({
        "stato": "ok", "voto": (ok_r + ok_a) / (2 * n),
        "voci": {"risposta giusta": ok_r / n, "articolo giusto": ok_a / n,
                 "articolo atteso fra i recuperati": sum(r["articolo_atteso_recuperato"] for r in righe) / n},
        "dettagli": {"domande": n, "articoli_letti": len(arts), "risposte": righe},
    })


if __name__ == "__main__":
    main()
