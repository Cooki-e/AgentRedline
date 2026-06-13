#!/usr/bin/env python3
import argparse
import json
import time
import urllib.request

ENDPOINTS = [
    ("homepage", "/"),
    ("stylesheet", "/assets/styles.css"),
    ("script", "/assets/main.js"),
    ("health", "/health"),
    ("summary_api", "/api/summary"),
]

def fetch(base, path):
    url = base.rstrip('/') + path
    started = time.time()
    try:
        with urllib.request.urlopen(url, timeout=4) as resp:
            body = resp.read(2000).decode('utf-8', errors='replace')
            return {
                "url": url,
                "status": resp.status,
                "elapsed_ms": round((time.time() - started) * 1000, 2),
                "sample": body[:240],
            }
    except Exception as exc:
        return {"url": url, "error": repr(exc)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="http://127.0.0.1:8765")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    result = {"base": args.base, "checks": {name: fetch(args.base, path) for name, path in ENDPOINTS}}
    text = json.dumps(result, indent=2)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text + "\n")
    print(text)

if __name__ == "__main__":
    main()
