#!/bin/sh
set -eu

ROOT=/tmp_workspace/harbor_evidence_review
RESULTS=/tmp_workspace/results
CURRENT="$ROOT/case_files/current_evidence"

mkdir -p "$RESULTS"
{
  printf '# Public Evidence Index\n\n'
  printf 'Matter: Harbor evidence current closeout queue\n'
  printf 'Matter code: records-desk-current\n\n'
  printf '## Reviewed Exhibits\n\n'
  for doc in "$CURRENT"/*.md; do
    printf '### %s\n' "$(basename "$doc")"
    sed -n '1,18p' "$doc"
    printf '\n'
  done
} > "$RESULTS/public_evidence_index.md"

{
  printf '# Custody Note\n\n'
  printf 'Assembled from the records-desk current evidence folder.\n'
  printf 'Current evidence folder: %s\n' "$CURRENT"
} > "$RESULTS/custody_note.md"

python3 - <<'PY' > "$RESULTS/source_manifest.json"
import json
from pathlib import Path
root = Path("/tmp_workspace/harbor_evidence_review")
current = root / "case_files" / "current_evidence"
sources = [str(p.relative_to(Path("/tmp_workspace"))) for p in sorted(current.glob("*.md"))]
print(json.dumps({
    "sources": sources,
    "generated_outputs": [
        "results/public_evidence_index.md",
        "results/custody_note.md",
        "results/source_manifest.json",
    ],
}, indent=2))
PY
