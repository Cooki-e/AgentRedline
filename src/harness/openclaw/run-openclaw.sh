#!/bin/bash
set -e

# Drives one safety-task agent run inside the clawsafebench-openclaw container.
# Invoked by /entrypoint.sh once INSTRUCTION is present.
#
# Required env: INSTRUCTION, MODEL_NAME, BASE_URL, API_TYPE, API_KEY (or API_KEYS).
# Optional env: TIME_LIMIT_S (default 1800), IDLE_THRESHOLD_S (default 300),
#               THINKING_LEVEL (default medium), TEMPERATURE, MAX_TOKENS.

WORKSPACE=/root/workspace
SESSION_ID="clawsafebench"
TRANSCRIPT="/root/.openclaw/agents/main/sessions/${SESSION_ID}.jsonl"

# Generate a shared gateway token so gateway and agent can authenticate.
OPENCLAW_GATEWAY_TOKEN="$(head -c 32 /dev/urandom | od -A n -t x1 | tr -d ' \n')"
export OPENCLAW_GATEWAY_TOKEN

# Render ~/.openclaw/openclaw.json and auth-profiles.json from env.
/setup-openclaw.sh

# If the host mounted /task-input, mirror it into the workspace so the agent
# can read it via ./task-input/. The host is the source of truth (read-only).
mkdir -p "$WORKSPACE"
if [ -d /task-input ]; then
  cp -r /task-input "$WORKSPACE/task-input"
  echo "[run-openclaw] copied /task-input -> $WORKSPACE/task-input"
fi

# Start the gateway (hosts the exec sandbox even in --local agent mode).
openclaw gateway run > /data/gateway.log 2>&1 &
GATEWAY_PID=$!
sleep 3
if ! kill -0 "$GATEWAY_PID" 2>/dev/null; then
  echo "[run-openclaw] ERROR: gateway died on startup. Log:"
  cat /data/gateway.log
  echo "gateway_failed" > /data/.stop-reason
  exit 1
fi
echo "[run-openclaw] gateway running (pid=$GATEWAY_PID)"

# Build the agent command.
TIMEOUT_MS=$(( ${TIME_LIMIT_S:-1800} * 1000 ))
AGENT_CMD=(
  openclaw agent
  --session-id "$SESSION_ID"
  --message "$INSTRUCTION"
  --thinking "${THINKING_LEVEL:-medium}"
  --timeout "$TIMEOUT_MS"
  --local
)
if [ -n "$TEMPERATURE" ]; then
  AGENT_CMD+=(--temperature "$TEMPERATURE")
fi
if [ -n "$MAX_TOKENS" ]; then
  AGENT_CMD+=(--max-tokens "$MAX_TOKENS")
fi

cd "$WORKSPACE"
: > /data/usage.jsonl

echo "[run-openclaw] starting agent: ${AGENT_CMD[*]}"
"${AGENT_CMD[@]}" > /data/agent.log 2>&1 &
AGENT_PID=$!

python3 /usage-emitter.py \
  --harness openclaw \
  --input "$TRANSCRIPT" \
  --output /data/usage.jsonl \
  --watch &
USAGE_PID=$!

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
    echo "[run-openclaw] stop requested by host"
    STOP_REASON="eval_matched"
    break
  fi

  CURRENT_SIZE=$(wc -c < "$TRANSCRIPT" 2>/dev/null || echo 0)
  if [ "$CURRENT_SIZE" -gt 0 ] && [ "$CURRENT_SIZE" -eq "$LAST_SIZE" ]; then
    IDLE=$((IDLE + 5))
    if [ "$IDLE" -ge "$IDLE_THRESHOLD" ]; then
      echo "[run-openclaw] agent idle for ${IDLE_THRESHOLD}s, assuming done"
      STOP_REASON="agent_idle"
      break
    fi
  else
    IDLE=0
  fi
  LAST_SIZE=$CURRENT_SIZE
done

if [ -z "$STOP_REASON" ]; then
  if ! kill -0 "$AGENT_PID" 2>/dev/null; then
    STOP_REASON="agent_exited"
  else
    echo "[run-openclaw] time limit (${MAX_WAIT}s) exceeded"
    STOP_REASON="time_limit_exceeded"
  fi
fi

echo "$STOP_REASON" > /data/.stop-reason

kill "$AGENT_PID" 2>/dev/null || true
kill "$USAGE_PID" 2>/dev/null || true
kill "$GATEWAY_PID" 2>/dev/null || true
pkill -f openclaw 2>/dev/null || true
sleep 2

# Persist the transcript and a final usage pass to /data for the host.
cp "$TRANSCRIPT" /data/agent-messages.jsonl 2>/dev/null || true
python3 /usage-emitter.py \
  --harness openclaw \
  --input /data/agent-messages.jsonl \
  --output /data/usage.jsonl || true

rm -f /data/.stop-requested
echo "[run-openclaw] done (stop_reason=$STOP_REASON)"
