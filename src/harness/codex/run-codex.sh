#!/bin/bash
set -e

# Drives one safety-task agent run inside the clawsafebench-codex container.
# Invoked by /entrypoint.sh once INSTRUCTION is present.
#
# Required env: INSTRUCTION, MODEL_NAME, BASE_URL, API_TYPE, API_KEY (or API_KEYS).
# Optional env: TIME_LIMIT_S (default 1800), IDLE_THRESHOLD_S (default 300),
#               THINKING_LEVEL.

WORKSPACE=/root/workspace
STDOUT=/tmp/codex-stdout.jsonl

# Render ~/.codex/config.toml + /tmp/litellm-config.yaml + /tmp/codex-env.sh.
/setup-codex.sh
source /tmp/codex-env.sh

# Start the LiteLLM translation proxy (Responses -> provider API).
echo "[run-codex] starting LiteLLM proxy..."
# LiteLLM resolves the `callbacks: reasoning_patch.reasoning_injector` module
# relative to the CONFIG FILE's directory, so the patch must sit next to
# /tmp/litellm-config.yaml. (PYTHONPATH is not consulted for this lookup.)
cp /reasoning_patch.py /tmp/reasoning_patch.py
litellm --config /tmp/litellm-config.yaml --port 4000 > /data/proxy.log 2>&1 &
PROXY_PID=$!
for i in $(seq 1 30); do
  if curl -sf http://localhost:4000/health/liveliness > /dev/null 2>&1; then
    echo "[run-codex] proxy ready"
    break
  fi
  if [ "$i" -eq 30 ]; then
    echo "[run-codex] ERROR: proxy not ready after 30s — see /data/proxy.log"
    echo "proxy_failed" > /data/.stop-reason
    exit 1
  fi
  sleep 1
done

# Mirror /task-input into the workspace (host is read-only source of truth).
mkdir -p "$WORKSPACE"
if [ -d /task-input ]; then
  cp -r /task-input "$WORKSPACE/task-input"
  echo "[run-codex] copied /task-input -> $WORKSPACE/task-input"
fi

# Start the agent. --dangerously-bypass-approvals-and-sandbox gives full,
# uncaged exec (matching openclaw security:full). --json streams one event per
# line to stdout, which we also use as the live activity signal for the watchdog.
cd "$WORKSPACE"
: > /data/usage.jsonl
echo "[run-codex] starting Codex CLI agent (model=${MODEL_NAME})..."
codex exec --json --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox \
  -- "$INSTRUCTION" > "$STDOUT" 2> /data/agent.log &
AGENT_PID=$!

python3 /usage-emitter.py \
  --harness codex \
  --input "$STDOUT" \
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
    echo "[run-codex] stop requested by host"
    STOP_REASON="eval_matched"
    break
  fi

  CURRENT_SIZE=$(wc -c < "$STDOUT" 2>/dev/null || echo 0)
  if [ "$CURRENT_SIZE" -gt 0 ] && [ "$CURRENT_SIZE" -eq "$LAST_SIZE" ]; then
    IDLE=$((IDLE + 5))
    if [ "$IDLE" -ge "$IDLE_THRESHOLD" ]; then
      echo "[run-codex] agent idle for ${IDLE_THRESHOLD}s, assuming done"
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
    echo "[run-codex] time limit (${MAX_WAIT}s) exceeded"
    STOP_REASON="time_limit_exceeded"
  fi
fi

echo "$STOP_REASON" > /data/.stop-reason

kill "$AGENT_PID" 2>/dev/null || true
kill "$USAGE_PID" 2>/dev/null || true
kill "$PROXY_PID" 2>/dev/null || true
pkill -f "@openai/codex" 2>/dev/null || true
pkill -f "litellm" 2>/dev/null || true
sleep 2

# Promote the session rollout to /data/agent-messages.jsonl (it carries the full
# structured transcript; stdout is a fallback if no rollout was written).
LATEST_ROLLOUT=$(find /root/.codex/sessions -name "rollout-*.jsonl" -type f \
  -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
if [ -n "$LATEST_ROLLOUT" ]; then
  cp "$LATEST_ROLLOUT" /data/agent-messages.jsonl
  echo "[run-codex] promoted session rollout to /data/agent-messages.jsonl"
elif [ -s "$STDOUT" ]; then
  cp "$STDOUT" /data/agent-messages.jsonl
  echo "[run-codex] WARN: no rollout found; fell back to stdout capture"
fi
python3 /usage-emitter.py \
  --harness codex \
  --input /data/agent-messages.jsonl \
  --output /data/usage.jsonl || true

rm -f /data/.stop-requested
echo "[run-codex] done (stop_reason=$STOP_REASON)"
