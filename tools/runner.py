#!/usr/bin/env python3
"""Runs the use cases of this repository on one release of Inga.

Steps: read the version (inga-version.txt, or --version), download that release's
linux-x86_64 archive and check it against SHA256SUMS, download and check the models
of models.json, then for each case start `inga serve` with the case's model, wait
for /health, run the case's run.py, and write results/<version>/<case>.json and
results/<version>/summary.md (compared with the most recent earlier version).

Exits non-zero only when a case fails with an error, not when a score drops.

Standard library only: the cases' own dependencies are in tools/requirements.txt.
"""

import argparse
import datetime
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
CASES = os.path.join(ROOT, "cases")
INGA_REPO = "matteobaccan/inga"
ASSET = "inga-linux-x86_64-{v}.tar.gz"


def log(msg):
    print(f"[runner] {msg}", flush=True)


class Failure(Exception):
    pass


# --------------------------------------------------------------------------- utils

def version_key(v):
    return tuple(int(x) for x in re.findall(r"\d+", v))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def http_get(url, headers=None, dest=None, timeout=120):
    """GET url. Redirects are followed by hand, without the Authorization header
    (GitHub and Hugging Face redirect to signed storage URLs that refuse it).
    Returns bytes, or (size, sha256) when dest is given."""
    headers = dict(headers or {})
    opener = urllib.request.build_opener(_NoRedirect)
    for _ in range(10):
        req = urllib.request.Request(url, headers=headers)
        try:
            resp = opener.open(req, timeout=timeout)
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308):
                url = urllib.request.urljoin(url, e.headers["Location"])
                headers.pop("Authorization", None)
                continue
            body = e.read()[:500].decode("utf-8", "replace")
            raise Failure(f"GET {url}: HTTP {e.code}: {body}") from None
        with resp:
            if dest is None:
                return resp.read()
            h = hashlib.sha256()
            size = 0
            last = time.monotonic()
            with open(dest, "wb") as f:
                for block in iter(lambda: resp.read(1 << 20), b""):
                    f.write(block)
                    h.update(block)
                    size += len(block)
                    if time.monotonic() - last > 30:
                        log(f"  ... {size / 1e6:.0f} MB")
                        last = time.monotonic()
            return size, h.hexdigest()
    raise Failure(f"GET {url}: too many redirects")


def github_headers():
    h = {"Accept": "application/vnd.github+json", "User-Agent": "ingausecase-runner"}
    for var in ("INGA_TOKEN", "GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(var):
            h["Authorization"] = "Bearer " + os.environ[var]
            break
    return h


def hf_headers():
    h = {"User-Agent": "ingausecase-runner"}
    if os.environ.get("HF_TOKEN"):
        h["Authorization"] = "Bearer " + os.environ["HF_TOKEN"]
    return h


# --------------------------------------------------------------------------- inga

def get_inga(version, cache):
    folder = os.path.join(cache, "inga", version)
    exe = os.path.join(folder, "inga")
    if os.path.exists(exe):
        log(f"Inga {version}: in cache, {exe}")
        return exe
    os.makedirs(folder, exist_ok=True)
    name = ASSET.format(v=version)
    api = f"https://api.github.com/repos/{INGA_REPO}/releases/tags/v{version}"
    try:
        rel = json.loads(http_get(api, github_headers()))
    except Failure as e:
        raise Failure(
            f"release v{version} of {INGA_REPO} not found ({e}). If the repository is "
            "private, the token in INGA_TOKEN (or GH_TOKEN) must be able to read it."
        ) from None
    assets = {a["name"]: a for a in rel.get("assets", [])}
    for needed in (name, "SHA256SUMS"):
        if needed not in assets:
            raise Failure(f"release v{version} has no asset {needed}")
    dl = dict(github_headers(), Accept="application/octet-stream")
    sums = http_get(assets["SHA256SUMS"]["url"], dl).decode("utf-8")
    expected = None
    for line in sums.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1].lstrip("*") == name:
            expected = parts[0].lower()
    if not expected:
        raise Failure(f"SHA256SUMS of v{version} does not list {name}")
    tgz = os.path.join(folder, name)
    log(f"Inga {version}: downloading {name}")
    _, digest = http_get(assets[name]["url"], dl, dest=tgz, timeout=300)
    if digest != expected:
        os.remove(tgz)
        raise Failure(f"{name}: sha256 {digest}, SHA256SUMS says {expected}")
    log(f"Inga {version}: sha256 ok ({digest})")
    with tarfile.open(tgz) as t:
        member = next((m for m in t.getmembers() if os.path.basename(m.name) == "inga" and m.isfile()), None)
        if member is None:
            raise Failure(f"{name} holds no inga executable")
        with t.extractfile(member) as src, open(exe, "wb") as out:
            shutil.copyfileobj(src, out)
    os.chmod(exe, 0o755)
    os.remove(tgz)
    return exe


# --------------------------------------------------------------------------- models

def load_models():
    with open(os.path.join(ROOT, "models.json"), encoding="utf-8") as f:
        return json.load(f)["modelli"]


def check_upstream(m):
    """The file's sha256 on Hugging Face (lfs.oid) must still be the one in models.json."""
    url = f"https://huggingface.co/api/models/{m['repo']}/tree/main"
    try:
        tree = json.loads(http_get(url, hf_headers(), timeout=60))
    except (Failure, OSError) as e:
        log(f"  warning: Hugging Face API not reachable ({e}); checking the local sha256 only")
        return
    entry = next((e for e in tree if e.get("path") == m["file"]), None)
    if entry is None:
        raise Failure(f"{m['repo']}/{m['file']}: the file is no longer in the repository")
    oid = (entry.get("lfs") or {}).get("oid")
    if oid != m["sha256"]:
        raise Failure(
            f"{m['repo']}/{m['file']} changed on Hugging Face: sha256 {oid}, "
            f"models.json says {m['sha256']}. Check the new file and update models.json."
        )


def get_model(key, models, cache):
    if key not in models:
        raise Failure(f"model {key} is not in models.json")
    m = models[key]
    folder = os.path.join(cache, "models")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, m["file"])
    check_upstream(m)
    if os.path.exists(path):
        if os.path.getsize(path) == m["size"] and sha256_file(path) == m["sha256"]:
            log(f"model {key}: in cache, sha256 ok")
            return path
        log(f"model {key}: the cached file does not match, downloading it again")
        os.remove(path)
    url = f"https://huggingface.co/{m['repo']}/resolve/main/{m['file']}"
    log(f"model {key}: downloading {url} ({m['size'] / 1e9:.2f} GB)")
    part = path + ".part"
    size, digest = http_get(url, hf_headers(), dest=part, timeout=600)
    if size != m["size"] or digest != m["sha256"]:
        os.remove(part)
        raise Failure(f"{m['file']}: downloaded {size} bytes with sha256 {digest}, "
                      f"models.json says {m['size']} bytes, {m['sha256']}")
    os.replace(part, path)
    log(f"model {key}: sha256 ok")
    return path


# --------------------------------------------------------------------------- server

def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class Server:
    def __init__(self, exe, model_path, ctx, seed, home, logfile, extra):
        self.port = free_port()
        self.url = f"http://127.0.0.1:{self.port}"
        cmd = [exe, "--home", home, "serve", model_path,
               "--host", "127.0.0.1", "--port", str(self.port),
               "--ctx", str(ctx), "--seed", str(seed), "--temp", "0",
               "--offline", "--no-webui", "--quiet", "--exit-on-load-error",
               "--no-mcp", "--no-mcp-server", "--no-memory", "--no-web-search",
               "--no-api-nodes", "--no-cloud"] + list(extra)
        log("  " + " ".join(cmd))
        self.logfile = logfile
        self.log = open(logfile, "w", encoding="utf-8")
        self.proc = subprocess.Popen(cmd, stdout=self.log, stderr=subprocess.STDOUT)

    def wait(self, timeout):
        t0 = time.monotonic()
        while time.monotonic() - t0 < timeout:
            if self.proc.poll() is not None:
                raise Failure(f"inga serve exited with {self.proc.returncode}:\n{self.tail()}")
            try:
                with urllib.request.urlopen(self.url + "/health", timeout=5) as r:
                    if r.status == 200:
                        return time.monotonic() - t0
            except (urllib.error.URLError, OSError):
                pass
            time.sleep(1)
        raise Failure(f"inga serve not ready after {timeout} s:\n{self.tail()}")

    def model_id(self):
        with urllib.request.urlopen(self.url + "/v1/models", timeout=30) as r:
            data = json.loads(r.read())
        return data["data"][0]["id"] if data.get("data") else ""

    def tail(self, n=40):
        self.log.flush()
        with open(self.logfile, encoding="utf-8", errors="replace") as f:
            return "".join(f.readlines()[-n:])

    def stop(self):
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(30)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait()
        self.log.close()


# --------------------------------------------------------------------------- cases

def list_cases():
    out = []
    for name in sorted(os.listdir(CASES)):
        cfg = os.path.join(CASES, name, "case.json")
        if os.path.exists(cfg):
            with open(cfg, encoding="utf-8") as f:
                out.append((name, json.load(f)))
    return out


def run_case(name, cfg, exe, models, args, version, outdir):
    case_dir = os.path.join(CASES, name)
    work = os.path.join(args.cache, "work", version, name)
    shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    result_tmp = os.path.join(work, "result.json")
    key = cfg["modello"]
    meta = models.get(key, {})
    record = {
        "caso": name, "versione": version, "modello": key,
        "file_modello": meta.get("file"), "sha256_modello": meta.get("sha256"),
        "ctx": cfg.get("ctx", 4096), "seed": args.seed,
        "data": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    t0 = time.monotonic()
    server = None
    try:
        model_path = get_model(key, models, args.cache)
        home = os.path.join(work, "inga-home")
        os.makedirs(home)
        server = Server(exe, model_path, record["ctx"], args.seed, home,
                        os.path.join(work, "inga-serve.log"), cfg.get("argomenti_serve", []))
        record["secondi_avvio"] = round(server.wait(cfg.get("attesa_avvio", 600)), 1)
        env = dict(os.environ,
                   INGA_URL=server.url, INGA_MODEL=server.model_id(), SEED=str(args.seed),
                   IUC_TOOLS=TOOLS, IUC_CASE_DIR=case_dir, IUC_WORK_DIR=work,
                   IUC_RESULT=result_tmp, IUC_VERSION=version, PYTHONUNBUFFERED="1")
        log(f"  run.py ({server.url}, model {env['INGA_MODEL']})")
        timeout = cfg.get("timeout_minuti", 60) * 60
        try:
            p = subprocess.run([sys.executable, os.path.join(case_dir, "run.py")],
                               env=env, cwd=case_dir, timeout=timeout)
        except subprocess.TimeoutExpired:
            raise Failure(f"run.py over the time limit of {timeout // 60} minutes") from None
        if p.returncode != 0:
            raise Failure(f"run.py exited with {p.returncode}\n--- inga serve ---\n{server.tail()}")
        if not os.path.exists(result_tmp):
            raise Failure("run.py wrote no result")
        with open(result_tmp, encoding="utf-8") as f:
            record.update(json.load(f))
    except Failure as e:
        record.update(stato="errore", motivo=str(e))
    finally:
        if server:
            server.stop()
    record["secondi"] = round(time.monotonic() - t0, 1)
    with open(os.path.join(outdir, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return record


# --------------------------------------------------------------------------- summary

def previous_version(results, version):
    if not os.path.isdir(results):
        return None
    older = [d for d in os.listdir(results)
             if os.path.isdir(os.path.join(results, d)) and re.fullmatch(r"\d+(\.\d+)*", d)
             and version_key(d) < version_key(version)]
    return max(older, key=version_key) if older else None


def load_results(folder):
    out = {}
    if folder and os.path.isdir(folder):
        for f in sorted(os.listdir(folder)):
            if f.endswith(".json"):
                with open(os.path.join(folder, f), encoding="utf-8") as fh:
                    out[f[:-5]] = json.load(fh)
    return out


def pct(x):
    return "-" if x is None else f"{100 * x:.1f}"


def delta(a, b):
    if a is None or b is None:
        return "-"
    d = 100 * (a - b)
    return f"{d:+.1f}" if abs(d) >= 0.05 else "0.0"


def duration(s):
    if s is None:
        return "-"
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def write_summary(results, version, inga_version_line):
    outdir = os.path.join(results, version)
    cur = load_results(outdir)
    prev_v = previous_version(results, version)
    prev = load_results(os.path.join(results, prev_v)) if prev_v else {}
    pv = prev_v or "nessuna"
    lines = [
        f"# Risultati di Inga {version}", "",
        f"Eseguito con `{inga_version_line}`, seed {cur[next(iter(cur))].get('seed') if cur else '-'}, "
        "temperatura 0. Voti in percentuale; il confronto è con la versione precedente "
        f"presente in `results/` ({pv}).", "",
        "| Caso | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for name, r in cur.items():
        p = prev.get(name, {})
        score = r.get("voto") if r.get("stato") == "ok" else None
        pscore = p.get("voto") if p.get("stato") == "ok" else None
        lines.append(f"| {name} | {pct(score)} | {pct(pscore)} | {delta(score, pscore)} | "
                     f"{duration(r.get('secondi'))} | {r.get('file_modello') or '-'} | {r.get('stato')} |")
    detail = []
    for name, r in cur.items():
        voci = r.get("voci") or {}
        if not voci:
            continue
        pvoci = (prev.get(name) or {}).get("voci") or {}
        detail.append(f"\n### {name}\n")
        detail.append("| Voce | Valore | Valore precedente | Differenza |")
        detail.append("| --- | ---: | ---: | ---: |")
        for k, v in voci.items():
            detail.append(f"| {k} | {pct(v)} | {pct(pvoci.get(k))} | {delta(v, pvoci.get(k))} |")
    if detail:
        lines += ["", "## Voci di ogni caso"] + detail
    notes = [f"- {n}: {r['motivo']}" for n, r in cur.items() if r.get("stato") != "ok" and r.get("motivo")]
    if notes:
        lines += ["", "## Casi saltati o in errore", ""] + [n.splitlines()[0] for n in notes]
    lines += ["", f"Macchina: {platform.machine()}, {os.cpu_count()} CPU, {platform.platform()}.", ""]
    with open(os.path.join(outdir, "summary.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# --------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--version", help="the Inga version (default: inga-version.txt)")
    ap.add_argument("--case", action="append", help="run only this case (repeatable)")
    ap.add_argument("--cache", default=os.environ.get("IUC_CACHE", os.path.expanduser("~/.cache/ingausecase")),
                    help="folder of the downloads (Inga, models) and of the work files")
    ap.add_argument("--results", default=os.path.join(ROOT, "results"))
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--inga", help="use this inga executable instead of downloading the release")
    ap.add_argument("--list", action="store_true", help="list the cases and exit")
    ap.add_argument("--summary-only", action="store_true",
                    help="only write results/<version>/summary.md again from the case JSONs")
    args = ap.parse_args()

    cases = list_cases()
    if args.list:
        for name, cfg in cases:
            print(f"{name}: {cfg.get('descrizione', '')} (modello {cfg['modello']})")
        return 0
    if args.case:
        unknown = set(args.case) - {n for n, _ in cases}
        if unknown:
            log(f"unknown case(s): {', '.join(sorted(unknown))}")
            return 2
        cases = [(n, c) for n, c in cases if n in args.case]

    version = args.version
    if not version:
        with open(os.path.join(ROOT, "inga-version.txt"), encoding="utf-8") as f:
            version = f.read().strip()
    version = version.lstrip("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        log(f"not a version: {version!r}")
        return 2

    if args.summary_only:
        with open(os.path.join(args.results, version, "summary.md"), encoding="utf-8") as f:
            line = re.search(r"Eseguito con `([^`]*)`", f.read())
        write_summary(args.results, version, line.group(1) if line else f"inga {version}")
        return 0

    os.makedirs(args.cache, exist_ok=True)
    try:
        exe = args.inga or get_inga(version, args.cache)
        inga_line = subprocess.run([exe, "--version"], capture_output=True, text=True).stdout.splitlines()[0]
        models = load_models()
    except Failure as e:
        log(f"ERROR: {e}")
        return 1
    log(inga_line)

    outdir = os.path.join(args.results, version)
    os.makedirs(outdir, exist_ok=True)
    errors = 0
    for name, cfg in cases:
        log(f"case {name}")
        r = run_case(name, cfg, exe, models, args, version, outdir)
        if r.get("stato") == "errore":
            errors += 1
            log(f"case {name}: ERROR {r['motivo']}")
        elif r.get("stato") == "saltato":
            log(f"case {name}: SKIPPED: {r.get('motivo')}")
        else:
            log(f"case {name}: score {pct(r.get('voto'))} in {duration(r['secondi'])}")
    write_summary(args.results, version, inga_line)
    log(f"written {os.path.join(outdir, 'summary.md')}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
