#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
WORKSPACE_ROOT="$(cd .. && pwd)"
python3 scripts/compile_pipeline_report.py \
  --observations data/source/march_observations.csv \
  --codes data/reference/anomaly_codes.csv \
  --config config/report_rules.yaml \
  --output "${WORKSPACE_ROOT}/results/pipeline_report.txt"
