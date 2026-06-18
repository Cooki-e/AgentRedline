#!/bin/bash
set -e

# Renders /tmp/litellm-config.yaml + /tmp/claude-code-env.sh from env vars
# supplied by the host runner. Called by run-claude-code.sh before the
# proxy/agent are started.
#
# Required env: BASE_URL, MODEL_NAME, API_KEY (or API_KEYS).
# Optional env: API_TYPE (default anthropic-messages), THINKING_LEVEL,
#               TEMPERATURE (ignored), MAX_TOKENS (ignored).
#
# Claude Code speaks the Anthropic Messages API; it talks to a local LiteLLM
# proxy (localhost:4000) that translates to the real provider (BASE_URL).

if [ -z "$BASE_URL" ] || [ -z "$MODEL_NAME" ]; then
  echo "[setup-claude-code] ERROR: BASE_URL and MODEL_NAME must be set"
  exit 1
fi

if [ -n "$TEMPERATURE" ]; then
  echo "[setup-claude-code] WARN: Claude Code has no --temperature flag; TEMPERATURE='$TEMPERATURE' ignored."
fi
if [ -n "$MAX_TOKENS" ]; then
  echo "[setup-claude-code] WARN: Claude Code has no --max-tokens flag; MAX_TOKENS='$MAX_TOKENS' ignored."
fi

python3 - <<'PYEOF'
import json, os, urllib.request
from pathlib import Path
import yaml

base_url = os.environ["BASE_URL"]
model_name = os.environ["MODEL_NAME"]
api_type = os.environ.get("API_TYPE", "anthropic-messages")

# Pick a single API key (first from API_KEYS list, else API_KEY).
keys_json = os.environ.get("API_KEYS", "")
single_key = os.environ.get("API_KEY", "")
key = ""
if keys_json:
    try:
        parsed = json.loads(keys_json)
        if parsed:
            key = parsed[0]
            if len(parsed) > 1:
                print(f"[setup-claude-code] WARN: Claude Code does not rotate keys — using first of {len(parsed)}")
    except json.JSONDecodeError:
        pass
if not key and single_key:
    key = single_key
if not key:
    raise SystemExit("[setup-claude-code] ERROR: no API key provided (API_KEYS or API_KEY)")

# Resolve the upstream model id (OpenRouter only; deepseek/qiqi pass through).
resolved_model = model_name
is_openrouter = "openrouter.ai" in base_url
if is_openrouter:
    try:
        req = urllib.request.Request(
            f"{base_url}/models",
            headers={"Authorization": f"Bearer {key}"},
        )
        resp = json.loads(urllib.request.urlopen(req, timeout=10).read())
        for m in resp.get("data", []):
            if m["id"].endswith(f"/{model_name}") or m["id"] == model_name:
                resolved_model = m["id"]
                break
    except Exception as e:
        print(f"[setup-claude-code] WARN: could not resolve OpenRouter model ID: {e}")

# Pick the LiteLLM provider prefix that tells it which native API to translate to.
litellm_params = {"api_key": key}
if is_openrouter:
    litellm_params["model"] = f"openrouter/{resolved_model}"
elif api_type == "anthropic-messages":
    litellm_params["model"] = f"anthropic/{model_name}"
    if not base_url.startswith("https://api.anthropic.com"):
        litellm_params["api_base"] = base_url
elif api_type == "google-generative-ai":
    litellm_params["model"] = f"gemini/{model_name}"
    if not base_url.startswith("https://generativelanguage.googleapis.com"):
        litellm_params["api_base"] = base_url
elif api_type in ("openai-completions", "openai-responses"):
    # custom_openai (NOT openai/): Claude Code POSTs the Anthropic Messages API
    # at /v1/messages. LiteLLM 404s that route for the `openai` provider on
    # chat-only endpoints (deepseek/qiqi), but BRIDGES Anthropic->ChatCompletions
    # for `custom_openai`. Verified 200 on /v1/messages.
    litellm_params["model"] = f"custom_openai/{model_name}"
    litellm_params["api_base"] = base_url
    litellm_params["additional_drop_params"] = ["client_metadata", "metadata"]
else:
    raise SystemExit(f"[setup-claude-code] ERROR: unsupported api_type for claude-code harness: {api_type}")

# Two routes: the exact model the agent asks for, plus a catch-all so Claude
# Code's auxiliary small-model calls (title/summary) don't 404 — they route to
# the same upstream model so the run stays single-model.
proxy_config = {
    "model_list": [
        {"model_name": model_name, "litellm_params": litellm_params},
        {"model_name": "*", "litellm_params": litellm_params},
    ],
    # drop_params: silently drop Anthropic-specific params that can't be
    # translated (e.g. thinking budget) instead of erroring.
    "litellm_settings": {"drop_params": True},
}
proxy_path = Path("/tmp/litellm-config.yaml")
proxy_path.write_text(yaml.dump(proxy_config, default_flow_style=False))
os.chmod(proxy_path, 0o600)

# Sourceable env file for the run script — point Claude Code at the proxy.
env_path = Path("/tmp/claude-code-env.sh")
env_path.write_text(
    'export ANTHROPIC_API_KEY="sk-proxy-placeholder"\n'
    'export ANTHROPIC_BASE_URL="http://localhost:4000"\n'
)
os.chmod(env_path, 0o600)

print(f"[setup-claude-code] model={model_name}, upstream={litellm_params['model']}, "
      f"base_url=http://localhost:4000")
PYEOF
