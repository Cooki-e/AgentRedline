#!/bin/bash
set -e

# Drives one safety-task agent run inside the clawsafebench-claude-code container.
# Invoked by /entrypoint.sh once INSTRUCTION is present.
#
# Required env: INSTRUCTION, MODEL_NAME, BASE_URL, API_KEY (or API_KEYS).
# Optional env: API_TYPE, TIME_LIMIT_S (default 1800), IDLE_THRESHOLD_S (default 300),
#               THINKING_LEVEL.

WORKSPACE=/root/workspace
TRANSCRIPT=/data/agent-messages.jsonl

# Render /tmp/litellm-config.yaml + /tmp/claude-code-env.sh.
/setup-claude-code.sh
source /tmp/claude-code-env.sh

# Start the LiteLLM translation proxy (Anthropic Messages -> provider API).
echo "[run-claude-code] starting LiteLLM proxy..."
litellm --config /tmp/litellm-config.yaml --port 4000 > /data/proxy.log 2>&1 &
PROXY_PID=$!
for i in $(seq 1 30); do
  if curl -sf http://localhost:4000/health/liveliness > /dev/null 2>&1; then
    echo "[run-claude-code] proxy ready"
    break
  fi
  if [ "$i" -eq 30 ]; then
    echo "[run-claude-code] ERROR: proxy not ready after 30s — see /data/proxy.log"
    echo "proxy_failed" > /data/.stop-reason
    exit 1
  fi
  sleep 1
done

# Mirror /task-input into the workspace (host is read-only source of truth).
mkdir -p "$WORKSPACE"
if [ -d /task-input ]; then
  cp -r /task-input "$WORKSPACE/task-input"
  echo "[run-claude-code] copied /task-input -> $WORKSPACE/task-input"
fi

# Build the claude command.
#   -p (print mode): non-interactive, runs the prompt to completion.
#   --output-format stream-json: streams one JSON object per line to stdout.
#   --dangerously-skip-permissions: full, uncaged exec (container is the sandbox,
#     matching openclaw security:full). IS_SANDBOX=1 bypasses the root-user check.
export IS_SANDBOX=1
cd "$WORKSPACE"
: > /data/usage.jsonl
echo "[run-claude-code] starting Claude Code agent (model=${MODEL_NAME})..."
CLAUDE_ARGS=(-p --verbose --output-format stream-json --model "$MODEL_NAME" --dangerously-skip-permissions)
case "${THINKING_LEVEL:-off}" in
  ""|off) ;;
  *) CLAUDE_ARGS+=(--thinking enabled) ;;
esac
CLAUDE_ARGS+=(-- "$INSTRUCTION")

claude "${CLAUDE_ARGS[@]}" > "$TRANSCRIPT" 2> /data/agent.log &
AGENT_PID=$!

python3 /usage-emitter.py \
  --harness claude-code \
  --input "$TRANSCRIPT" \
  --output /data/usage.jsonl \
  --watch &
USAGE_PID=$!
sleep 3

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
    echo "[run-claude-code] stop requested by host"
    STOP_REASON="eval_matched"
    break
  fi

  CURRENT_SIZE=$(wc -c < "$TRANSCRIPT" 2>/dev/null || echo 0)
  if [ "$CURRENT_SIZE" -gt 0 ] && [ "$CURRENT_SIZE" -eq "$LAST_SIZE" ]; then
    IDLE=$((IDLE + 5))
    if [ "$IDLE" -ge "$IDLE_THRESHOLD" ]; then
      echo "[run-claude-code] agent idle for ${IDLE_THRESHOLD}s, assuming done"
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
    echo "[run-claude-code] time limit (${MAX_WAIT}s) exceeded"
    STOP_REASON="time_limit_exceeded"
  fi
fi

echo "$STOP_REASON" > /data/.stop-reason

kill "$AGENT_PID" 2>/dev/null || true
kill "$USAGE_PID" 2>/dev/null || true
kill "$PROXY_PID" 2>/dev/null || true
pkill -f "@anthropic-ai/claude-code" 2>/dev/null || true
pkill -f "litellm" 2>/dev/null || true
sleep 2

python3 /usage-emitter.py \
  --harness claude-code \
  --input "$TRANSCRIPT" \
  --output /data/usage.jsonl || true

rm -f /data/.stop-requested
echo "[run-claude-code] done (stop_reason=$STOP_REASON)"
