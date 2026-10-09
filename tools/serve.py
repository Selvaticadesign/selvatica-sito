"""Anteprima locale con aggiornamento automatico.

Uso (dalla cartella del progetto):  python tools/serve.py
Poi apri http://localhost:5500

Ogni volta che salvi un file del sito, la pagina nel browser si ricarica da sola.
Per fermarlo: Ctrl+C nel terminale.
"""
import http.server
import os
import sys
import threading
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5500
IGNORE_DIRS = {".git", "source", "tools", "node_modules", ".claude"}
RELOAD_SNIPPET = (
    b'<script>new EventSource("/__reload").onmessage=()=>location.reload()</script>'
)

version = 0


def snapshot():
    """Firma della cartella: ultima modifica e numero di file."""
    latest, count = 0.0, 0
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for name in files:
            try:
                latest = max(latest, os.stat(os.path.join(folder, name)).st_mtime)
                count += 1
            except OSError:
                pass
    return latest, count


def watch():
    global version
    last = snapshot()
    while True:
        time.sleep(0.4)
        current = snapshot()
        if current != last:
            last = current
            version += 1


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path == "/__reload":
            return self.stream_reload()
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
        if path.endswith(".html") and os.path.isfile(path):
            with open(path, "rb") as f:
                body = f.read()
            if "noreload" not in self.path:  # ?noreload: per screenshot automatici
                body = body.replace(b"</body>", RELOAD_SNIPPET + b"</body>", 1)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def stream_reload(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        seen, idle = version, 0
        try:
            while True:
                time.sleep(0.25)
                if version != seen:
                    self.wfile.write(b"data: reload\n\n")
                    self.wfile.flush()
                    return
                idle += 1
                if idle % 60 == 0:  # segnale ogni ~15 s per tenere aperta la connessione
                    self.wfile.write(b": ping\n\n")
                    self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass


if __name__ == "__main__":
    threading.Thread(target=watch, daemon=True).start()
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    server.daemon_threads = True
    print(f"Anteprima: http://localhost:{PORT}  (Ctrl+C per fermare)")
    server.serve_forever()
