#!/usr/bin/env python3
"""The PDFs the cases download at run time (fonti.json), with their checks.

Each source of fonti.json has its URL, its name, and the sha256 and size of the file
as first downloaded. A source is downloaded once into <cache>/fonti (the GitHub
Actions cache keeps that folder, keyed by URL and sha256) and checked: when the
file's sha256 is not the one in fonti.json, `Cambiato` is raised and the case stops
with a clear message instead of scoring against a changed text. The text of each page
is extracted with pypdf and kept beside the PDF (<file>.pagine.json).

From the command line (the `fonti` workflow):

    python tools/fonti.py scarica              # every source: sha256, size, pages
    python tools/fonti.py testo ccnl           # the text, page by page, with markers
    python tools/fonti.py testo divina-commedia --pagine 1-5

A case imports it like inga_api (`sys.path.insert(0, os.environ["IUC_TOOLS"])`).
"""

import argparse
import hashlib
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENT = "Mozilla/5.0 (X11; Linux x86_64) ingausecase-runner"


class Cambiato(Exception):
    """The downloaded file is not the one recorded in fonti.json."""


def fonti():
    with open(os.path.join(ROOT, "fonti.json"), encoding="utf-8") as f:
        return json.load(f)["fonti"]


def cartella():
    base = os.environ.get("IUC_CACHE") or os.path.expanduser("~/.cache/ingausecase")
    d = os.path.join(base, "fonti")
    os.makedirs(d, exist_ok=True)
    return d


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def pdf(chiave, rigido=True):
    """The local path of the source's PDF, downloaded if not in the cache.

    rigido: with False, a source without a recorded sha256 is accepted (the first
    download, to read its sha256); with True it is refused too."""
    f = fonti()[chiave]
    nome = hashlib.sha256(f["url"].encode()).hexdigest()[:16] + "-" + os.path.basename(f["url"])
    path = os.path.join(cartella(), nome)
    atteso = f.get("sha256")
    if os.path.exists(path):
        digest = sha256_file(path)
        if atteso and digest == atteso:
            return path
        os.remove(path)
    req = urllib.request.Request(f["url"], headers={"User-Agent": AGENT})
    part = path + ".part"
    h = hashlib.sha256()
    with urllib.request.urlopen(req, timeout=300) as r, open(part, "wb") as out:
        for block in iter(lambda: r.read(1 << 20), b""):
            out.write(block)
            h.update(block)
    digest = h.hexdigest()
    size = os.path.getsize(part)
    if atteso and digest != atteso:
        os.remove(part)
        raise Cambiato(
            f"{f['nome']} ({f['url']}) è cambiato: il file scaricato ha sha256 {digest} e "
            f"{size} byte, fonti.json dice {atteso} e {f.get('size')} byte. I voti si danno "
            "solo sul testo controllato: rileggere il nuovo testo, verificare le domande "
            "e aggiornare fonti.json.")
    if not atteso and rigido:
        os.remove(part)
        raise Cambiato(f"{f['nome']}: fonti.json non ha ancora lo sha256 del file "
                       f"(il file scaricato ha sha256 {digest}, {size} byte)")
    os.replace(part, path)
    return path


def pagine(chiave, rigido=True):
    """The text of each page of the source's PDF (a list, page 1 first)."""
    path = pdf(chiave, rigido)
    import pypdf
    testo = path + ".pagine.json"
    digest = sha256_file(path)
    if os.path.exists(testo):
        with open(testo, encoding="utf-8") as f:
            dato = json.load(f)
        if dato.get("sha256") == digest and dato.get("pypdf") == pypdf.__version__:
            return dato["pagine"]
    out = [p.extract_text() or "" for p in pypdf.PdfReader(path).pages]
    with open(testo, "w", encoding="utf-8") as f:
        json.dump({"sha256": digest, "pypdf": pypdf.__version__, "pagine": out}, f, ensure_ascii=False)
    return out


def in_collezione(inga_api, collezione, chiave, nome):
    """Adds the source's PDF to one of Inga's collections, read by Inga itself; if Inga
    refuses the PDF, the text pypdf extracts from it, page by page, as a text file.
    Returns what happened: the name in the collection, how it was read, chunks, time."""
    import time
    path = pdf(chiave)
    t0 = time.monotonic()
    out = {"fonte": chiave, "nome": nome, "lettura": "PDF letto da Inga"}
    try:
        info = inga_api.add_document(collezione, nome, pdf_path=path)
    except RuntimeError as e:
        out.update(nome=os.path.splitext(nome)[0] + ".txt", lettura="testo estratto con pypdf",
                   errore_pdf=str(e)[:300])
        testo = "\n\n".join(f"[pagina {i}]\n{t}" for i, t in enumerate(pagine(chiave), 1))
        info = inga_api.add_document(collezione, out["nome"], text=testo)
    out.update(chunks=info.get("chunks"), pagine=info.get("pages"),
               secondi=round(time.monotonic() - t0, 1))
    print(f"{nome}: {out['lettura']}, {out['chunks']} chunk, {out['pagine']} pagine, {out['secondi']} s")
    return out


def intervallo(s, n):
    if not s:
        return range(1, n + 1)
    a, _, b = s.partition("-")
    return range(int(a), min(n, int(b or a)) + 1)


def main():
    ap = argparse.ArgumentParser(description="Le fonti dei casi (fonti.json)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scarica")
    t = sub.add_parser("testo")
    t.add_argument("chiave")
    t.add_argument("--pagine", help="es. 1-5 (vuoto: tutte)")
    args = ap.parse_args()
    if args.cmd == "scarica":
        for k, f in fonti().items():
            path = pdf(k, rigido=False)
            ps = pagine(k, rigido=False)
            digest = sha256_file(path)
            stato = "uguale a fonti.json" if digest == f.get("sha256") else "fonti.json dice " + str(f.get("sha256"))
            print(f"{k}: sha256 {digest}, {os.path.getsize(path)} byte, {len(ps)} pagine, "
                  f"{sum(len(p) for p in ps)} caratteri di testo ({stato})")
        return 0
    ps = pagine(args.chiave, rigido=False)
    for i in intervallo(args.pagine, len(ps)):
        print(f"\n===== pagina {i} di {len(ps)} =====")
        print(ps[i - 1])
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Cambiato as e:
        print(f"ERRORE: {e}", file=sys.stderr)
        sys.exit(1)
