#!/bin/bash
set -e

# Drives one safety-task agent run inside the clawsafebench-hermes container.
# Invoked by /entrypoint.sh once INSTRUCTION is present.
#
# Required env: INSTRUCTION, MODEL_NAME, BASE_URL, API_TYPE, API_KEY (or API_KEYS).
# Optional env: TIME_LIMIT_S (default 1800), IDLE_THRESHOLD_S (default 300),
#               THINKING_LEVEL.

WORKSPACE=/root/workspace
LIVE_CAPTURE=/tmp/hermes-live-agent-messages.jsonl

# Render ~/.hermes/config.yaml + ~/.hermes/.env + /tmp/hermes-env.sh.
/setup-hermes.sh
source /tmp/hermes-env.sh

# Mirror /task-input into the workspace (host is read-only source of truth).
mkdir -p "$WORKSPACE"
if [ -d /task-input ]; then
  cp -r /task-input "$WORKSPACE/task-input"
  echo "[run-hermes] copied /task-input -> $WORKSPACE/task-input"
fi

promote_hermes_transcript() {
  local session_id=""
  local latest_session=""
  local raw_export="/tmp/hermes-session-export.jsonl"
  local tmp_export="/tmp/hermes-agent-messages.jsonl"

  expand_hermes_sessions() {
    local input_path="$1"
    local output_path="$2"
    python3 - "$input_path" "$output_path" <<'PYEOF'
import json
import sys
from pathlib import Path

input_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])

with input_path.open(encoding="utf-8") as src, output_path.open("w", encoding="utf-8") as dst:
    for line in src:
        if not line.strip():
            continue
        session = json.loads(line)
        messages = session.get("messages") or []
        meta = {k: v for k, v in session.items() if k != "messages"}
        session_id = meta.get("id") or meta.get("session_id")
        dst.write(json.dumps({"type": "session_meta", **meta}, ensure_ascii=False, separators=(",", ":")) + "\n")
        for index, message in enumerate(messages):
            row = {"type": "message", "session_id": session_id, "message_index": index, **message}
            dst.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
PYEOF
  }

  use_live_capture_if_present() {
    if [ -s "$LIVE_CAPTURE" ]; then
      cp "$LIVE_CAPTURE" /data/agent-messages.jsonl
      echo "[run-hermes] promoted live capture to /data/agent-messages.jsonl"
      return 0
    fi
    return 1
  }

  has_message_rows() {
    python3 - "$1" <<'PYEOF'
import json
import sys
from pathlib import Path

for line in Path(sys.argv[1]).read_text(errors="replace").splitlines():
    if not line.strip():
        continue
    if json.loads(line).get("type") != "session_meta":
        raise SystemExit(0)
raise SystemExit(1)
PYEOF
  }

  session_id=$(grep -Eo 'session_id:[[:space:]]*[^[:space:]]+' /tmp/hermes-stderr.log 2>/dev/null | awk '{print $2}' | tail -1 || true)

  if [ -z "$session_id" ]; then
    latest_session=$(find /root/.hermes/sessions -name "session_*.json" -type f \
      -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
    if [ -n "$latest_session" ]; then
      session_id=$(python3 - "$latest_session" <<'PYEOF' || true
import json, sys
from pathlib import Path
path = Path(sys.argv[1])
try:
    data = json.loads(path.read_text())
    print(data.get("session_id") or data.get("id") or path.stem.replace("session_", ""))
except Exception:
    print(path.stem.replace("session_", ""))
PYEOF
)
    fi
  fi

  if [ -n "$session_id" ]; then
    if hermes sessions export - --session-id "$session_id" > "$raw_export" 2>/tmp/hermes-export.log && [ -s "$raw_export" ]; then
      expand_hermes_sessions "$raw_export" "$tmp_export"
      if has_message_rows "$tmp_export"; then
        mv "$tmp_export" /data/agent-messages.jsonl
        echo "[run-hermes] exported session $session_id to /data/agent-messages.jsonl"
        return
      fi
      echo "[run-hermes] WARN: session export had no messages; trying live capture"
      use_live_capture_if_present && return
    fi
    echo "[run-hermes] WARN: session export failed for $session_id; trying session JSON"
  fi

  if [ -z "$latest_session" ]; then
    latest_session=$(find /root/.hermes/sessions -name "session_*.json" -type f \
      -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
  fi

  if [ -n "$latest_session" ]; then
    python3 - "$latest_session" > "$raw_export" <<'PYEOF'
import json, sys
from pathlib import Path
print(json.dumps(json.loads(Path(sys.argv[1]).read_text()), ensure_ascii=False, separators=(",", ":")))
PYEOF
    expand_hermes_sessions "$raw_export" "$tmp_export"
    if has_message_rows "$tmp_export"; then
      mv "$tmp_export" /data/agent-messages.jsonl
      echo "[run-hermes] promoted session JSON to /data/agent-messages.jsonl"
      return
    fi
    echo "[run-hermes] WARN: session JSON had no messages; trying live capture"
    use_live_capture_if_present && return
  fi

  use_live_capture_if_present && return
  : > /data/agent-messages.jsonl
  echo "[run-hermes] WARN: no Hermes session or live capture found; wrote empty transcript"
}

terminate_hermes() {
  local pid="$1"
  if kill -0 "$pid" 2>/dev/null; then
    # Prefer SIGINT so Hermes can flush its session transcript before exit.
    kill -INT "$pid" 2>/dev/null || true
    for _ in $(seq 1 20); do
      kill -0 "$pid" 2>/dev/null || break
      sleep 0.5
    done
    kill -0 "$pid" 2>/dev/null && kill -TERM "$pid" 2>/dev/null || true
    for _ in $(seq 1 10); do
      kill -0 "$pid" 2>/dev/null || break
      sleep 0.5
    done
    kill -0 "$pid" 2>/dev/null && kill -KILL "$pid" 2>/dev/null || true
  fi
}

cd "$WORKSPACE"
: > /data/usage.jsonl
echo "[run-hermes] starting Hermes agent (model_arg=${HERMES_MODEL_ARG}, provider=${HERMES_PROVIDER})..."
# Provider comes from ~/.hermes/config.yaml, NOT the CLI --provider flag: this
# Hermes version's --provider only accepts a fixed enum (auto/openrouter/
# anthropic/...) and rejects "custom". For a custom OpenAI-compatible endpoint
# setup-hermes.sh registers a named custom_providers entry and sets
# HERMES_MODEL_ARG="custom:<name>:<model>", which Hermes resolves to that entry's
# base_url + api_key.
HERMES_ARGS=(chat
  --quiet
  --yolo
  --ignore-rules
  --toolsets "terminal,file"
  --max-turns 90
  --model "${HERMES_MODEL_ARG:-$HERMES_MODEL_NAME}"
  -q "$INSTRUCTION")
python3 /hermes-capture.py "${HERMES_ARGS[@]}" > /tmp/hermes-stdout.log 2> /tmp/hermes-stderr.log &
AGENT_PID=$!

python3 /usage-emitter.py \
  --harness hermes \
  --input "$LIVE_CAPTURE" \
  --output /data/usage.jsonl \
  --watch &
USAGE_PID=$!
sleep 3

if ! kill -0 "$AGENT_PID" 2>/dev/null; then
  echo "[run-hermes] Hermes process died on startup. stderr:"
  tail -n 40 /tmp/hermes-stderr.log 2>/dev/null || true
  echo "hermes_failed" > /data/.stop-reason
fi

# Watchdog: kill on idle, server-requested stop, or time limit.
IDLE_THRESHOLD=${IDLE_THRESHOLD_S:-300}
MAX_WAIT=${TIME_LIMIT_S:-1800}
ELAPSED=0
LAST_SIZE=0
IDLE=0
STOP_REASON=""

while kill -0 "$AGENT_PID" 2>/dev/null && [ "$ELAPSED" -lt "$MAX_WAIT" ]; do
  sleep 5
  ELAPSED=$((ELAPSED + 5))

  if [ -f /data/.stop-requested ]; then
    echo "[run-hermes] stop requested by host; waiting briefly for Hermes to flush"
    STOP_REASON="eval_matched"
    for _ in $(seq 1 24); do
      kill -0 "$AGENT_PID" 2>/dev/null || break
      sleep 5
    done
    break
  fi

  CURRENT_SIZE=$(wc -c < "$LIVE_CAPTURE" 2>/dev/null || echo 0)
  if [ "$CURRENT_SIZE" -gt 0 ] && [ "$CURRENT_SIZE" -eq "$LAST_SIZE" ]; then
    IDLE=$((IDLE + 5))
    if [ "$IDLE" -ge "$IDLE_THRESHOLD" ]; then
      echo "[run-hermes] agent idle for ${IDLE_THRESHOLD}s, assuming done"
      STOP_REASON="agent_idle"
      break
    fi
  else
    IDLE=0
  fi
  LAST_SIZE=$CURRENT_SIZE
done

if [ -z "$STOP_REASON" ]; then
  if [ -f /data/.stop-reason ]; then
    STOP_REASON=$(cat /data/.stop-reason)
  elif ! kill -0 "$AGENT_PID" 2>/dev/null; then
    STOP_REASON="agent_exited"
  else
    echo "[run-hermes] time limit (${MAX_WAIT}s) exceeded"
    STOP_REASON="time_limit_exceeded"
  fi
fi

echo "$STOP_REASON" > /data/.stop-reason

terminate_hermes "$AGENT_PID"
kill "$USAGE_PID" 2>/dev/null || true
sleep 2

promote_hermes_transcript
python3 /usage-emitter.py \
  --harness hermes \
  --input /data/agent-messages.jsonl \
  --output /data/usage.jsonl || true
cp /tmp/hermes-stdout.log /data/agent-stdout.log 2>/dev/null || true
cp /tmp/hermes-stderr.log /data/agent-stderr.log 2>/dev/null || true

rm -f /data/.stop-requested
echo "[run-hermes] done (stop_reason=$STOP_REASON)"
