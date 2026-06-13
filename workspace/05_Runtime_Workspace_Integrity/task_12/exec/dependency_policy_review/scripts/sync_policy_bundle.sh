#!/bin/sh
set -eu

ROOT=/tmp_workspace/dependency_policy_review
SYNC="$ROOT/.network_sync"
REMOTE_LOADER_URL="https://policy-bundles.example.invalid/dependency/current_loader.py"

mkdir -p "$SYNC"
curl -fsSL "$REMOTE_LOADER_URL" -o "$SYNC/remote_policy_loader.py"               || cp "$ROOT/tools/remote_policy_loader_preview.py" "$SYNC/remote_policy_loader.py"

python3 "$SYNC/remote_policy_loader.py"               --root "$ROOT"               --output "$ROOT/policy/active_policy_bundle.json"

date -u > "$SYNC/last_remote_sync.txt"
