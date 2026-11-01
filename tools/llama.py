"""llama.cpp beside Inga, for the cases that compare the two on the same model file.

The programs (llama-server, llama-perplexity, llama-bench) are in the folder named by
IUC_LLAMA (the workflows build llama.cpp at the tag of llama-cpp.txt for the runner's
CPU). Without it, `cartella()` is None and the comparing cases are skipped.

    import llama
    with llama.Server(os.environ["IUC_MODEL_PATH"], ctx=4096) as srv:
        inga_api.chat(msgs, url=srv.url)
"""

import json
import os
import socket
import subprocess
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cartella():
    d = os.environ.get("IUC_LLAMA")
    return d if d and os.path.isfile(os.path.join(d, "llama-server")) else None


def versione():
    with open(os.path.join(ROOT, "llama-cpp.txt"), encoding="utf-8") as f:
        return f.read().strip()


def programma(nome):
    return os.path.join(cartella(), nome)


def threads():
    return str(os.cpu_count() or 4)


def _porta():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class Server:
    """llama-server on a free port with the model, greedy, one slot (as inga serve here)."""

    def __init__(self, model, ctx, log):
        self.port = _porta()
        self.url = f"http://127.0.0.1:{self.port}"
        self.cmd = [programma("llama-server"), "-m", model, "--host", "127.0.0.1",
                    "--port", str(self.port), "-c", str(ctx), "-np", "1", "--jinja",
                    "--seed", os.environ.get("SEED", "42"), "--temp", "0", "-t", threads(),
                    "--no-webui"]
        self.logfile = log

    def __enter__(self):
        self.log = open(self.logfile, "w", encoding="utf-8")
        self.proc = subprocess.Popen(self.cmd, stdout=self.log, stderr=subprocess.STDOUT)
        t0 = time.monotonic()
        while time.monotonic() - t0 < 600:
            if self.proc.poll() is not None:
                raise RuntimeError(f"llama-server è uscito con {self.proc.returncode}: {self.coda()}")
            try:
                with urllib.request.urlopen(self.url + "/health", timeout=5) as r:
                    if r.status == 200 and json.loads(r.read() or b"{}").get("status", "ok") == "ok":
                        return self
            except (urllib.error.URLError, OSError, ValueError):
                pass
            time.sleep(1)
        raise RuntimeError("llama-server non pronto dopo 600 s: " + self.coda())

    def coda(self, n=15):
        self.log.flush()
        with open(self.logfile, encoding="utf-8", errors="replace") as f:
            return "".join(f.readlines()[-n:])

    def __exit__(self, *exc):
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(30)
            except subprocess.TimeoutExpired:
                self.proc.kill()
        self.log.close()
