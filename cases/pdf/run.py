"""Caso pdf: estrazione dei dati di fatture e ordini sintetici con l'output strutturato.

Genera i PDF (genera.py, seed fisso), ne estrae il testo con pypdf, chiede a Inga i
campi con response_format json_schema e confronta con la verità campo per campo.
"""

import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402
from pypdf import PdfReader  # noqa: E402

SEED_DATI = 7
N_DOC = 20
CAMPI = ["numero", "data", "fornitore", "partita_iva", "imponibile", "iva", "totale", "righe"]

SCHEMA = {
    "type": "object",
    "properties": {
        "numero": {"type": "string", "maxLength": 40},
        "data": {"type": "string", "maxLength": 10},
        "fornitore": {"type": "string", "maxLength": 120},
        "partita_iva": {"type": "string", "maxLength": 16},
        "imponibile": {"type": "number"},
        "iva": {"type": "number"},
        "totale": {"type": "number"},
        "righe": {
            "type": "array", "maxItems": 10,
            "items": {
                "type": "object",
                "properties": {
                    "descrizione": {"type": "string", "maxLength": 120},
                    "quantita": {"type": "number"},
                    "prezzo_unitario": {"type": "number"},
                    "importo": {"type": "number"},
                },
                "required": ["descrizione", "quantita", "prezzo_unitario", "importo"],
            },
        },
    },
    "required": CAMPI,
}

SISTEMA = (
    "Estrai i dati da un documento commerciale italiano (fattura o ordine d'acquisto) e "
    "rispondi solo con il JSON richiesto. Regole:\n"
    "- numero: il numero del documento, così come è scritto;\n"
    "- data: la data del documento nel formato AAAA-MM-GG;\n"
    "- fornitore: la ragione sociale di chi vende (il cedente o prestatore; in un ordine "
    "d'acquisto, il fornitore a cui è rivolto l'ordine), non il cliente;\n"
    "- partita_iva: la partita IVA del fornitore, solo le 11 cifre;\n"
    "- imponibile, iva, totale: importi in euro come numeri (1.234,56 diventa 1234.56);\n"
    "- righe: una voce per ogni riga della tabella, con descrizione, quantità, prezzo "
    "unitario e importo della riga."
)


def norm_testo(s):
    return re.sub(r"[^0-9a-z]", "", str(s).casefold())


def num_ok(a, b):
    try:
        return abs(float(a) - float(b)) < 0.005
    except (TypeError, ValueError):
        return False


def campo_ok(campo, atteso, dato):
    if campo in ("imponibile", "iva", "totale"):
        return num_ok(atteso, dato)
    if campo == "partita_iva":
        return re.sub(r"\D", "", str(dato)) == atteso
    if campo == "righe":
        if not isinstance(dato, list) or len(dato) != len(atteso):
            return False
        return all(riga_ok(a, d) for a, d in zip(atteso, dato))
    if campo == "data":
        return str(dato).strip() == atteso
    return norm_testo(atteso) == norm_testo(dato)


def riga_ok(a, d):
    return (isinstance(d, dict) and norm_testo(a["descrizione"]) == norm_testo(d.get("descrizione", ""))
            and all(num_ok(a[k], d.get(k)) for k in ("quantita", "prezzo_unitario", "importo")))


def main():
    cartella = os.path.join(inga_api.work_dir(), "documenti")
    subprocess.run([sys.executable, os.path.join(inga_api.case_dir(), "genera.py"), cartella,
                    "--seed", str(SEED_DATI), "--n", str(N_DOC)], check=True)
    with open(os.path.join(cartella, "verita.json"), encoding="utf-8") as f:
        verita = json.load(f)

    giusti = {c: 0 for c in CAMPI}
    righe_giuste = righe_tot = 0
    per_doc = []
    secondi = 0.0
    for v in verita:
        testo = "\n".join(p.extract_text() for p in PdfReader(os.path.join(cartella, v["file"])).pages)
        msgs = [{"role": "system", "content": SISTEMA},
                {"role": "user", "content": f"Documento ({v['file']}):\n\n{testo}"}]
        try:
            dato, _, sec = inga_api.chat(msgs, schema=SCHEMA, max_tokens=1200)
        except (ValueError, RuntimeError) as e:
            print(f"{v['file']}: risposta non valida: {e}")
            dato, sec = {}, 0.0
        secondi += sec
        esito = {c: campo_ok(c, v[c], dato.get(c)) for c in CAMPI}
        for c, ok in esito.items():
            giusti[c] += ok
        righe_tot += len(v["righe"])
        if isinstance(dato.get("righe"), list):
            righe_giuste += sum(riga_ok(a, d) for a, d in zip(v["righe"], dato["righe"]))
        sbagliati = [c for c, ok in esito.items() if not ok]
        print(f"{v['file']} ({v['tipo']}): {len(CAMPI) - len(sbagliati)}/{len(CAMPI)} in {sec:.1f} s"
              + (f", sbagliati: {', '.join(sbagliati)}" if sbagliati else ""))
        per_doc.append({"file": v["file"], "tipo": v["tipo"], "secondi": round(sec, 1),
                        "sbagliati": {c: {"atteso": v[c], "dato": dato.get(c)} for c in sbagliati}})

    n = len(verita)
    totale = sum(giusti.values()) / (n * len(CAMPI))
    voci = {f"campo {c}": giusti[c] / n for c in CAMPI}
    voci["righe singole"] = righe_giuste / righe_tot if righe_tot else 0.0
    inga_api.write_result({
        "stato": "ok", "voto": totale, "voci": voci,
        "dettagli": {"documenti": n, "campi_per_documento": len(CAMPI), "seed_dati": SEED_DATI,
                     "secondi_richieste": round(secondi, 1), "documenti_con_errori":
                     [d for d in per_doc if d["sbagliati"]]},
    })


if __name__ == "__main__":
    main()
