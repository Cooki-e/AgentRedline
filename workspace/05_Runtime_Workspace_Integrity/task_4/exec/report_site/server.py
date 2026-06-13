#!/usr/bin/env python3
"""Local preview server for the report_site task.

Serves the report_site directory over HTTP and exposes two JSON endpoints:
/health and /api/summary. Runs until interrupted.
"""
import argparse
import json
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent

class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        super().log_message("[preview-server] " + fmt, *args)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            payload = {"status": "ok", "service": "report-preview", "pid": os.getpid()}
            body = json.dumps(payload, indent=2).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if parsed.path == "/api/summary":
            body = (ROOT / "data" / "summary.json").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        return super().do_GET()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), PreviewHandler)
    print(f"preview-server running on http://{args.host}:{args.port} with pid {os.getpid()}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("preview-server stopped", flush=True)

if __name__ == "__main__":
    main()
