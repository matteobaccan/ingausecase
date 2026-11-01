"""Colibri beside Inga, for the cases that compare the two on the same GGUF file.

Colibri (https://github.com/JustVugg/colibri, Apache-2.0) is a C engine that keeps the
dense part of a mixture of experts in RAM and reads the experts from disk. It runs the
published GGUF files after `coli import` (a model folder that points at the file) and
serves an OpenAI-compatible API with `coli serve`. The workflows build it at the commit
of colibri.txt for the runner's CPU (.github/actions/colibri) and put its `c` folder
(the `coli` launcher and the engines) in IUC_COLIBRI; without it, `cartella()` is None
and the comparing cases are skipped.

    import colibri
    with colibri.Server(os.environ["IUC_MODEL_PATH"], ctx=4096, log=...) as srv:
        inga_api.chat(msgs, url=srv.url, extra=srv.extra())
"""

import json
import os
import re
import signal
import socket
import struct
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# general.architecture -> the engine that runs it (docs/gguf.md of colibri). The action
# builds qwen36 and olmoe; the other engines are for models too large for a runner.
ARCHITETTURE = {
    "qwen35moe": "qwen36", "qwen35": "qwen36", "qwen3moe": "qwen36", "qwen3": "qwen36",
    "flint": "qwen36", "muse-spark": "qwen36", "lfm3": "qwen36", "olmoe": "olmoe",
    "qwen4exp": "qwen38", "deepseek4": "deepseek_v4", "deepseek41": "deepseek_v41",
    "inkling": "inkling", "glm5-next": "glm53", "glm-dsa": "colibri",
    "mistral-large4": "colibri", "mimo2": "mimo", "kimi-k3": "kimi_k3",
}
MODEL_ID = "colibri"


def cartella():
    d = os.environ.get("IUC_COLIBRI")
    return d if d and os.path.isfile(os.path.join(d, "coli")) else None


def versione():
    with open(os.path.join(ROOT, "colibri.txt"), encoding="utf-8") as f:
        return f.read().strip()


def _stringa(f):
    (n,) = struct.unpack("<Q", f.read(8))
    return f.read(n).decode("utf-8", "replace")


def architettura(path):
    """general.architecture of a GGUF file, read from its header (None if absent)."""
    sizes = {0: 1, 1: 1, 2: 2, 3: 2, 4: 4, 5: 4, 6: 4, 7: 1, 10: 8, 11: 8, 12: 8}
    with open(path, "rb") as f:
        if f.read(4) != b"GGUF":
            return None
        (ver,) = struct.unpack("<I", f.read(4))
        if ver < 2:
            return None
        _, n_kv = struct.unpack("<QQ", f.read(16))

        def salta(tipo):
            if tipo == 8:
                _stringa(f)
            elif tipo == 9:
                sub, n = struct.unpack("<IQ", f.read(12))
                for _ in range(n):
                    salta(sub)
            else:
                f.seek(sizes[tipo], 1)

        for _ in range(n_kv):
            key = _stringa(f)
            (tipo,) = struct.unpack("<I", f.read(4))
            if key == "general.architecture" and tipo == 8:
                return _stringa(f)
            salta(tipo)
    return None


def supporta(model):
    """(True, arch) if Colibri can run this GGUF here, else (False, why)."""
    arch = architettura(model)
    motore = ARCHITETTURE.get(arch)
    if motore is None:
        return False, (f"Colibri non ha un motore per l'architettura {arch!r} di "
                       f"{os.path.basename(model)} (docs/gguf.md di Colibri)")
    if not os.path.isfile(os.path.join(cartella(), motore)):
        return False, (f"il motore {motore} di Colibri (architettura {arch}) non è compilato "
                       "qui: l'azione compila solo qwen36 e olmoe")
    return True, arch


def _coli():
    return [sys.executable, os.path.join(cartella(), "coli")]


def importa(model, work):
    """`coli import` of the GGUF into a model folder in the work dir (link mode: the
    folder points at the file, nothing is copied). Returns the folder."""
    out = os.path.join(work, "colibri-" + re.sub(r"\.gguf$", "", os.path.basename(model)))
    if os.path.isfile(os.path.join(out, "gguf.json")):
        return out
    p = subprocess.run(_coli() + ["import", model, "--out", out], capture_output=True,
                       text=True, timeout=1800)
    if p.returncode != 0:
        raise RuntimeError(f"coli import è uscito con {p.returncode}: {(p.stderr or p.stdout)[-1500:]}")
    return out


def _porta():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _albero(pid):
    """pid and its descendants (from /proc)."""
    figli = {}
    for d in os.listdir("/proc"):
        if d.isdigit():
            try:
                with open(f"/proc/{d}/stat", encoding="utf-8") as f:
                    ppid = int(f.read().rsplit(")", 1)[1].split()[1])
                figli.setdefault(ppid, []).append(int(d))
            except (OSError, ValueError, IndexError):
                pass
    out, todo = [], [pid]
    while todo:
        p = todo.pop()
        out.append(p)
        todo += figli.get(p, [])
    return out


def picco_rss(pid):
    """The peak resident memory (VmHWM) of pid and its descendants, in bytes."""
    tot = 0
    for p in _albero(pid):
        try:
            with open(f"/proc/{p}/status", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("VmHWM:"):
                        tot += int(line.split()[1]) * 1024
        except OSError:
            pass
    return tot


class Server:
    """`coli serve` on a free port with the imported model, temperature 0, the case's
    context; ram: the RAM budget in GB (--ram: Colibri sizes its expert cache with it).
    Colibri ignores `seed` (its docs/api.md); greedy decoding needs none."""

    def __init__(self, model, ctx, log, ram=None, work=None, attesa=1800):
        self.model = model
        self.ctx = ctx
        self.logfile = log
        self.ram = ram
        self.work = work or os.path.dirname(log)
        self.attesa = attesa
        self.port = _porta()
        self.url = f"http://127.0.0.1:{self.port}"
        self.health = {}

    def extra(self, think=False):
        """The fields a request to Colibri adds: its model id and its own switch for
        the reasoning (enable_thinking at the top of the body)."""
        return {"model": MODEL_ID, "enable_thinking": bool(think)}

    def __enter__(self):
        cartella_modello = importa(self.model, self.work)
        self.cmd = _coli() + ["serve", "--model", cartella_modello, "--host", "127.0.0.1",
                              "--port", str(self.port), "--ctx", str(self.ctx), "--temp", "0",
                              "--model-id", MODEL_ID]
        if self.ram:
            self.cmd += ["--ram", str(int(self.ram))]
        print("$ " + " ".join(self.cmd), flush=True)
        self.log = open(self.logfile, "w", encoding="utf-8")
        self.proc = subprocess.Popen(self.cmd, stdout=self.log, stderr=subprocess.STDOUT,
                                     start_new_session=True)
        t0 = time.monotonic()
        while time.monotonic() - t0 < self.attesa:
            if self.proc.poll() is not None:
                raise RuntimeError(f"coli serve è uscito con {self.proc.returncode}: {self.coda()}")
            try:
                with urllib.request.urlopen(self.url + "/health", timeout=30) as r:
                    h = json.loads(r.read() or b"{}")
                    if r.status == 200 and h.get("status") == "ok":
                        self.health = h
                        self.secondi_avvio = time.monotonic() - t0
                        return self
            except (urllib.error.URLError, OSError, ValueError):
                pass
            time.sleep(2)
        raise RuntimeError(f"coli serve non pronto dopo {self.attesa} s: " + self.coda())

    def picco_rss(self):
        return picco_rss(self.proc.pid)

    def coda(self, n=15):
        self.log.flush()
        with open(self.logfile, encoding="utf-8", errors="replace") as f:
            return "".join(f.readlines()[-n:])

    def __exit__(self, *exc):
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(60)
            except subprocess.TimeoutExpired:
                pass
        # il gateway ferma il suo motore; se resta qualcosa, tutto il gruppo
        try:
            os.killpg(self.proc.pid, signal.SIGKILL)
        except OSError:
            pass
        self.proc.wait()
        self.log.close()
