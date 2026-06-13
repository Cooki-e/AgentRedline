#!/bin/bash
set -e

# Generates ~/.openclaw/openclaw.json and ~/.openclaw/agents/main/agent/auth-profiles.json
# from env vars supplied by the host runner. Called by run-openclaw.sh before
# the gateway/agent are started.
#
# Required env:
#   BASE_URL        — model provider base URL (e.g. https://openrouter.ai/api/v1)
#   API_TYPE        — openclaw "api" field value (e.g. openai-completions)
#   MODEL_NAME      — model id understood by the provider
#   API_KEYS (JSON list) OR API_KEY (single string)
#
# Optional env:
#   TEMPERATURE, MAX_TOKENS

if [ -z "$BASE_URL" ] || [ -z "$API_TYPE" ] || [ -z "$MODEL_NAME" ]; then
  echo "[setup-openclaw] ERROR: BASE_URL, API_TYPE, MODEL_NAME must be set"
  exit 1
fi

PROVIDER="api"
MODEL="$PROVIDER/$MODEL_NAME"

MODEL_OPTS=""
if [ -n "$TEMPERATURE" ]; then
  MODEL_OPTS="$MODEL_OPTS, \"temperature\": $TEMPERATURE"
fi
if [ -n "$MAX_TOKENS" ]; then
  MODEL_OPTS="$MODEL_OPTS, \"maxOutputTokens\": $MAX_TOKENS"
fi

mkdir -p ~/.openclaw/agents/main/agent

# Exec policy — "full" means the gateway runs whatever the agent asks, with no
# allowlist filtering. This is the right default for a *safety* benchmark: we
# want to observe the agent's own judgement, not measure how well the harness
# can cage it. Individual tasks can still tighten this by mounting their own
# openclaw.json or exec-approvals.json over these defaults.
#
# openclaw's supported security modes (verified against the npm package source):
#   - "full"      — no restrictions (what we use)
#   - "allowlist" — only safeBins are allowed; everything else denied/asked
#   - "deny"      — block all exec
cat > ~/.openclaw/openclaw.json << JSONEOF
{
  "gateway": {
    "port": 18789,
    "mode": "local"
  },
  "tools": {
    "exec": {
      "host": "gateway",
      "security": "full",
      "ask": "off"
    }
  },
  "skills": {
    "load": {
      "extraDirs": ["/root/skills"]
    }
  },
  "agents": {
    "defaults": {
      "workspace": "/root/workspace",
      "skipBootstrap": true,
      "model": {
        "primary": "$MODEL"
      }
    }
  },
  "models": {
    "providers": {
      "$PROVIDER": {
        "baseUrl": "$BASE_URL",
        "api": "$API_TYPE",
        "models": [
          { "id": "$MODEL_NAME", "name": "$MODEL_NAME", "reasoning": true$MODEL_OPTS }
        ]
      }
    }
  }
}
JSONEOF

# Approval policy file — the per-call `tools.exec.ask` is just a default that
# gets combined with this file via maxAsk(). We keep ask=off here too so the
# gateway doesn't fall into the unattended-approval path even if a task tries
# to override `tools.exec.security` to "allowlist". `askFallback: "allow"`
# matches the "full" security stance — no human approver is wired in --local.
cat > ~/.openclaw/exec-approvals.json << 'APPROVALSEOF'
{
  "version": 1,
  "defaults": {
    "security": "full",
    "ask": "off",
    "askFallback": "allow"
  },
  "agents": {}
}
APPROVALSEOF
chmod 600 ~/.openclaw/exec-approvals.json

# auth-profiles.json with multi-key rotation support.
python3 - <<'PY'
import json
import os

provider = "api"

keys_json = os.environ.get("API_KEYS", "")
single_key = os.environ.get("API_KEY", "")

keys = []
if keys_json:
    try:
        parsed = json.loads(keys_json)
    except json.JSONDecodeError:
        parsed = []
    keys = [{"key": k, "source": "apikey"} for k in parsed if isinstance(k, str) and k]
if not keys and single_key:
    keys = [{"key": single_key, "source": "apikey"}]

if not keys:
    print("[setup-openclaw] WARNING: no API_KEY/API_KEYS provided")

profiles = {}
order = []
for i, entry in enumerate(keys, 1):
    name = f"{provider}:api-{i}"
    profiles[name] = {
        "provider": provider,
        "type": "api_key",
        "key": entry["key"],
    }
    order.append(name)

result = {"profiles": profiles, "order": {provider: order}}

path = os.path.expanduser("~/.openclaw/agents/main/agent/auth-profiles.json")
with open(path, "w") as f:
    json.dump(result, f, indent=2)
os.chmod(path, 0o600)

print(f"[setup-openclaw] auth profiles: {len(keys)} key(s) for {provider}")
PY
