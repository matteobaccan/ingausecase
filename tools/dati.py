"""The data of the public benchmarks the cases download at run time (dati.json).

Each entry has its URL (pinned to a revision where the host allows it) and the sha256
and size of the file as first downloaded. A file is downloaded once into <cache>/dati
and checked: when its sha256 is not the one in dati.json, `Cambiato` is raised and the
case stops with a clear message instead of scoring against changed data. The data
never goes into this repository (some licenses are non-commercial).

A case imports it like inga_api (`sys.path.insert(0, os.environ["IUC_TOOLS"])`):

    import dati
    path = dati.file("rgb-en")
"""

import json
import os
import urllib.request

import fonti

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Cambiato = fonti.Cambiato


def voci():
    with open(os.path.join(ROOT, "dati.json"), encoding="utf-8") as f:
        return json.load(f)["dati"]


def file(chiave):
    """The local path of the entry's file, downloaded if not in the cache."""
    d = voci()[chiave]
    base = os.environ.get("IUC_CACHE") or os.path.expanduser("~/.cache/ingausecase")
    folder = os.path.join(base, "dati")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, chiave + "-" + d["url"].rsplit("/", 1)[-1])
    if os.path.exists(path) and os.path.getsize(path) == d["size"] \
            and fonti.sha256_file(path) == d["sha256"]:
        return path
    req = urllib.request.Request(d["url"], headers={"User-Agent": fonti.AGENT})
    token = os.environ.get("HF_TOKEN")
    if token and "huggingface.co" in d["url"]:
        req.add_header("Authorization", f"Bearer {token}")
    part = path + ".part"
    with urllib.request.urlopen(req, timeout=600) as r, open(part, "wb") as f:
        while True:
            block = r.read(1 << 20)
            if not block:
                break
            f.write(block)
    digest = fonti.sha256_file(part)
    if digest != d["sha256"]:
        os.remove(part)
        raise Cambiato(f"{chiave}: il file scaricato da {d['url']} ha sha256 {digest}, "
                       f"dati.json dice {d['sha256']}: i dati sono cambiati, vanno ricontrollati")
    os.replace(part, path)
    return path
