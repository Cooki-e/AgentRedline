#!/bin/sh
set -eu

ROOT=/tmp_workspace/metrics_review
RESULTS=/tmp_workspace/results
RUN=/tmp_workspace/metrics_review/.run

mkdir -p "$RESULTS" "$RUN"

PYTHONPATH="$ROOT/tools" python3 "$ROOT/tools/live_refresh_worker.py"               --root "$ROOT"               --results "$RESULTS"               --heartbeat "$RUN/live_refresh.heartbeat"               --interval 2               > "$RUN/live_refresh.log" 2>&1 &

echo $! > "$RUN/live_refresh.pid"
sleep 1
