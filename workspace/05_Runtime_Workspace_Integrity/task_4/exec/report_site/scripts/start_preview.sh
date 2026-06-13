#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_DIR="$ROOT/preview_runtime"
mkdir -p "$RUNTIME_DIR"
PORT="${1:-8765}"
PID_FILE="$RUNTIME_DIR/server.pid"
LOG_FILE="$RUNTIME_DIR/server.log"
if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "Preview server already running with PID $(cat "$PID_FILE") on port $PORT"
  exit 0
fi
nohup python3 "$ROOT/server.py" --host 127.0.0.1 --port "$PORT" > "$LOG_FILE" 2>&1 &
echo $! > "$PID_FILE"
echo "Started local preview server on http://127.0.0.1:$PORT"
echo "PID file: $PID_FILE"
echo "Log file: $LOG_FILE"
