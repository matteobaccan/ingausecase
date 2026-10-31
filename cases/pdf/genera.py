"""Genera fatture e ordini sintetici in PDF (testo, non immagini) con la loro verità.

    python genera.py CARTELLA [--seed 7] [--n 20]

Scrive CARTELLA/doc01.pdf ... e CARTELLA/verita.json. Tutto è inventato: nomi di
aziende composti a caso da parti generiche, partite IVA con la sola cifra di
controllo giusta, indirizzi di fantasia. Stesso seed, stessi documenti.
"""

import argparse
import json
import os
import random

from fpdf import FPDF

COGNOMI = ["Bertolini", "Carrara", "Donadoni", "Fabbretti", "Galimberti", "Lanzoni",
           "Marangoni", "Negrini", "Orsolini", "Pellacani", "Quaranta", "Rinaldelli",
           "Sartorello", "Tagliaferri", "Valdinoci", "Zanardelli", "Brambati", "Cucchiarelli"]
SETTORI = {
    "Forniture Ufficio": [("Risma carta A4 80 g", 3.9, 6.5), ("Toner nero compatibile", 28, 64),
                          ("Raccoglitore ad anelli dorso 8 cm", 2.1, 4.8), ("Penne a sfera blu (conf. 50)", 9, 18),
                          ("Sedia operativa ergonomica", 89, 240), ("Etichette adesive 70x37 (100 fogli)", 11, 22)],
    "Ricambi Industriali": [("Cuscinetto a sfere 6204-2RS", 2.4, 7.9), ("Cinghia trapezoidale A42", 6.5, 14),
                            ("Guarnizione OR 40x3 NBR", 0.35, 1.2), ("Motoriduttore 0,37 kW", 180, 420),
                            ("Olio idraulico ISO 46 (latta 20 l)", 55, 98), ("Kit filtri aria compressore", 24, 61)],
    "Alimentari": [("Farina tipo 0 (sacco 25 kg)", 14, 26), ("Olio extravergine (lattina 5 l)", 32, 58),
                   ("Pomodori pelati (cartone 6 kg)", 7.5, 13), ("Caffè in grani (kg)", 13, 24),
                   ("Zucchero semolato (sacco 10 kg)", 9, 15), ("Pasta di semola (cartone 12 kg)", 16, 27)],
    "Servizi Informatici": [("Canone assistenza sistemistica mensile", 150, 600), ("Licenza gestionale annuale", 380, 1500),
                            ("Ora di consulenza sviluppo", 45, 95), ("Backup remoto 500 GB (anno)", 120, 300),
                            ("Configurazione firewall", 220, 480), ("Notebook 14 pollici", 590, 1190)],
    "Edilizia": [("Cemento Portland (sacco 25 kg)", 5.2, 9.5), ("Mattone forato 8x25x25", 0.38, 0.9),
                 ("Tondino acciaio B450C 12 mm (barra)", 7, 15), ("Malta premiscelata (sacco 25 kg)", 4.1, 8),
                 ("Nolo betoniera (giorno)", 35, 70), ("Pannello isolante EPS 4 cm (m2)", 4.5, 11)],
}
FORME = ["S.r.l.", "S.p.A.", "S.n.c.", "S.a.s.", "S.r.l.s."]
VIE = ["Via dei Tigli", "Via Roma", "Viale delle Industrie", "Via Garibaldi", "Corso Italia",
       "Via del Lavoro", "Via Artigiani", "Piazza della Stazione"]
CITTA = [("Brescia", "BS", "25100"), ("Padova", "PD", "35100"), ("Bologna", "BO", "40100"),
         ("Bari", "BA", "70100"), ("Torino", "TO", "10100"), ("Perugia", "PG", "06100"),
         ("Ancona", "AN", "60100"), ("Novara", "NO", "28100")]
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
        "settembre", "ottobre", "novembre", "dicembre"]


def partita_iva(rng):
    # 7 cifre della matricola, 3 del codice ufficio (001-099), poi la cifra di controllo
    digits = [rng.randint(0, 9) for _ in range(7)] + [0, rng.randint(0, 9), rng.randint(1, 9)]
    s = 0
    for i, d in enumerate(digits):
        if i % 2 == 0:
            s += d
        else:
            d2 = d * 2
            s += d2 - 9 if d2 > 9 else d2
    return "".join(map(str, digits)) + str((10 - s % 10) % 10)


def euro(x):
    """1234.5 -> '1.234,50'"""
    s = f"{x:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def qta_txt(q):
    return str(int(q)) if q == int(q) else euro(q).rstrip("0").rstrip(",")


def azienda(rng, settore):
    return f"{rng.choice(COGNOMI)} {settore} {rng.choice(FORME)}"


def indirizzo(rng):
    citta, prov, cap = rng.choice(CITTA)
    return f"{rng.choice(VIE)} {rng.randint(1, 180)}", f"{cap} {citta} ({prov})"


def documento(rng, i):
    settore = rng.choice(list(SETTORI))
    tipo = rng.choice(["fattura_a", "fattura_c", "ordine"])
    forn = azienda(rng, settore)
    cli_settore = rng.choice([s for s in SETTORI if s != settore])
    cliente = azienda(rng, cli_settore)
    while cliente.split()[0] == forn.split()[0]:
        cliente = azienda(rng, cli_settore)
    aliquota = 0.04 if settore == "Alimentari" and rng.random() < 0.5 else (0.10 if settore == "Alimentari" else 0.22)
    righe = []
    for desc, lo, hi in rng.sample(SETTORI[settore], rng.randint(1, 4)):
        q = rng.choice([1, 1, 2, 3, 4, 5, 6, 10, 12, 20, 25, 50]) if hi < 100 else rng.choice([1, 1, 2, 3])
        if "kg" in desc and rng.random() < 0.3:
            q = rng.choice([2.5, 7.5, 12.5])
        p = round(rng.uniform(lo, hi), 2)
        righe.append({"descrizione": desc, "quantita": q, "prezzo_unitario": p, "importo": round(q * p, 2)})
    imponibile = round(sum(r["importo"] for r in righe), 2)
    iva = round(imponibile * aliquota, 2)
    totale = round(imponibile + iva, 2)
    anno, mese, giorno = 2026, rng.randint(1, 10), rng.randint(1, 28)
    if tipo == "fattura_a":
        numero = f"FT-{anno}/{rng.randint(1, 999):04d}"
    elif tipo == "fattura_c":
        numero = f"{rng.randint(1, 400)}/{rng.choice('ABCE')}"
    else:
        numero = f"OA-{rng.randint(100, 9999)}"
    return {
        "file": f"doc{i:02d}.pdf", "tipo": tipo, "aliquota": aliquota,
        "numero": numero, "data": f"{anno}-{mese:02d}-{giorno:02d}",
        "fornitore": forn, "partita_iva": partita_iva(rng),
        "cliente": cliente, "partita_iva_cliente": partita_iva(rng),
        "ind_fornitore": indirizzo(rng), "ind_cliente": indirizzo(rng),
        "imponibile": imponibile, "iva": iva, "totale": totale, "righe": righe,
        "pagamento": rng.choice(["Bonifico bancario 30 gg d.f.", "Ri.Ba. 60 gg f.m.", "Rimessa diretta"]),
    }


def tabella(pdf, righe, intest, eur_prefix=""):
    w = [92, 18, 35, 35]
    pdf.set_font("Helvetica", "B", 9)
    for wi, h in zip(w, intest):
        pdf.cell(wi, 7, h, border=1, align="C")
    pdf.ln()
    pdf.set_font("Helvetica", "", 9)
    for r in righe:
        pdf.cell(w[0], 6, r["descrizione"], border=1)
        pdf.cell(w[1], 6, qta_txt(r["quantita"]), border=1, align="R")
        pdf.cell(w[2], 6, eur_prefix + euro(r["prezzo_unitario"]), border=1, align="R")
        pdf.cell(w[3], 6, eur_prefix + euro(r["importo"]), border=1, align="R")
        pdf.ln()
    pdf.ln(4)


def totali(pdf, voci):
    pdf.set_font("Helvetica", "", 10)
    for k, v, bold in voci:
        pdf.set_font("Helvetica", "B" if bold else "", 10)
        pdf.cell(145, 6, k, align="R")
        pdf.cell(35, 6, v, align="R")
        pdf.ln()


def scrivi_pdf(d, path):
    pdf = FPDF(format="A4")
    pdf.set_auto_page_break(True, 15)
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    a1, a2 = d["ind_fornitore"]
    c1, c2 = d["ind_cliente"]
    aliq = int(round(d["aliquota"] * 100))
    gg, mm, aa = d["data"][8:], d["data"][5:7], d["data"][:4]
    if d["tipo"] == "fattura_a":
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 7, d["fornitore"], new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9)
        for t in (a1, a2, f"P.IVA {d['partita_iva']}"):
            pdf.cell(0, 5, t, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(6)
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 5, "Spett.le", new_x="LMARGIN", new_y="NEXT")
        for t in (d["cliente"], c1, c2, f"P.IVA {d['partita_iva_cliente']}"):
            pdf.cell(0, 5, t, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(6)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, f"FATTURA N. {d['numero']} del {gg}/{mm}/{aa}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)
        tabella(pdf, d["righe"], ["Descrizione", "Q.tà", "Prezzo unit.", "Importo"])
        totali(pdf, [("Imponibile", euro(d["imponibile"]), False),
                     (f"IVA {aliq}%", euro(d["iva"]), False),
                     ("Totale documento EUR", euro(d["totale"]), True)])
    elif d["tipo"] == "fattura_c":
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 5, f"Fattura n. {d['numero']}", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 5, f"{c2.split(' ', 1)[1].split(' (')[0]}, {int(gg)} {MESI[int(mm) - 1]} {aa}",
                 new_x="LMARGIN", new_y="NEXT")
        pdf.ln(4)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(90, 5, "Cedente / prestatore")
        pdf.cell(90, 5, "Cessionario / committente", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9)
        for left, right in ((d["fornitore"], d["cliente"]), (a1, c1), (a2, c2),
                            (f"Partita IVA: {d['partita_iva']}", f"Partita IVA: {d['partita_iva_cliente']}")):
            pdf.cell(90, 5, left)
            pdf.cell(90, 5, right, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(6)
        tabella(pdf, d["righe"], ["Descrizione del bene o servizio", "Quantità", "Prezzo", "Totale riga"], "EUR ")
        totali(pdf, [("Totale imponibile", "EUR " + euro(d["imponibile"]), False),
                     (f"Imposta ({aliq}%)", "EUR " + euro(d["iva"]), False),
                     ("Totale da pagare", "EUR " + euro(d["totale"]), True)])
    else:
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 7, d["cliente"], new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9)
        for t in (c1, c2, f"P.IVA {d['partita_iva_cliente']}"):
            pdf.cell(0, 5, t, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(5)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, "ORDINE D'ACQUISTO", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 5, f"Numero ordine: {d['numero']}", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 5, f"Data ordine: {gg}.{mm}.{aa}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(3)
        pdf.cell(0, 5, f"Fornitore: {d['fornitore']} - {a1}, {a2}", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 5, f"Partita IVA fornitore: {d['partita_iva']}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(4)
        tabella(pdf, d["righe"], ["Articolo", "Qtà", "Prezzo unitario", "Valore"])
        totali(pdf, [("Totale merce", euro(d["imponibile"]), False),
                     (f"IVA {aliq}%", euro(d["iva"]), False),
                     ("Totale ordine (EUR)", euro(d["totale"]), True)])
    pdf.ln(6)
    pdf.set_font("Helvetica", "", 8)
    pdf.cell(0, 4, f"Pagamento: {d['pagamento']}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 4, "Documento di prova con dati inventati.", new_x="LMARGIN", new_y="NEXT")
    pdf.output(path)


CAMPI = ["numero", "data", "fornitore", "partita_iva", "imponibile", "iva", "totale", "righe"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cartella")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--n", type=int, default=20)
    a = ap.parse_args()
    os.makedirs(a.cartella, exist_ok=True)
    rng = random.Random(a.seed)
    verita = []
    for i in range(1, a.n + 1):
        d = documento(rng, i)
        scrivi_pdf(d, os.path.join(a.cartella, d["file"]))
        verita.append({"file": d["file"], "tipo": d["tipo"], **{k: d[k] for k in CAMPI}})
    with open(os.path.join(a.cartella, "verita.json"), "w", encoding="utf-8") as f:
        json.dump(verita, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
