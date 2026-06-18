#!/bin/bash
set -e

# Renders ~/.codex/config.toml + /tmp/litellm-config.yaml + /tmp/codex-env.sh
# from env vars supplied by the host runner. Called by run-codex.sh before the
# proxy/agent are started.
#
# Required env: BASE_URL, MODEL_NAME, API_TYPE, API_KEY (or API_KEYS).
# Optional env: THINKING_LEVEL, TEMPERATURE (ignored), MAX_TOKENS (ignored).
#
# Codex speaks the OpenAI Responses API; it talks to a local LiteLLM proxy
# (localhost:4000) that translates to the real provider (BASE_URL).

if [ -z "$BASE_URL" ] || [ -z "$MODEL_NAME" ] || [ -z "$API_TYPE" ]; then
  echo "[setup-codex] ERROR: BASE_URL, MODEL_NAME, and API_TYPE must be set"
  exit 1
fi

if [ -n "$TEMPERATURE" ]; then
  echo "[setup-codex] WARN: 'codex exec' has no temperature flag; TEMPERATURE='$TEMPERATURE' ignored."
fi
if [ -n "$MAX_TOKENS" ]; then
  echo "[setup-codex] WARN: 'codex exec' has no max-tokens flag; MAX_TOKENS='$MAX_TOKENS' ignored."
fi

mkdir -p "$HOME/.codex"

python3 - <<'PYEOF'
import json, os, urllib.request
from pathlib import Path
import yaml

base_url = os.environ["BASE_URL"]
model_name = os.environ["MODEL_NAME"]
api_type = os.environ["API_TYPE"]

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
                print(f"[setup-codex] WARN: Codex does not rotate keys — using first of {len(parsed)}")
    except json.JSONDecodeError:
        pass
if not key and single_key:
    key = single_key
if not key:
    raise SystemExit("[setup-codex] ERROR: no API key provided (API_KEYS or API_KEY)")

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
        print(f"[setup-codex] WARN: could not resolve OpenRouter model ID: {e}")

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
    # custom_openai (NOT openai/): Codex 0.120.0 forces wire_api="responses", so
    # it POSTs /responses. LiteLLM forwards /responses straight to the upstream
    # for the `openai` provider (-> 404 on chat-only endpoints like deepseek/qiqi),
    # but BRIDGES Responses->ChatCompletions for `custom_openai`. Verified 200.
    litellm_params["model"] = f"custom_openai/{model_name}"
    litellm_params["api_base"] = base_url
    # Codex's Responses body carries fields the bridge forwards as kwargs the
    # upstream chat SDK rejects (e.g. client_metadata -> "unexpected keyword
    # argument"). These MUST live in per-model litellm_params (NOT global
    # litellm_settings) for the drop to take effect — verified empirically.
    litellm_params["additional_drop_params"] = [
        "client_metadata", "metadata", "service_tier",
        "store", "prompt_cache_key", "safety_identifier",
    ]
else:
    raise SystemExit(f"[setup-codex] ERROR: unsupported api_type for codex harness: {api_type}")

proxy_config = {
    "model_list": [{
        "model_name": model_name,
        "litellm_params": litellm_params,
    }],
    # drop_params: silently ignore OpenAI-only fields (service_tier,
    # reasoning.summary, etc.) that non-OpenAI providers would reject. The
    # Codex-specific kwargs are dropped per-model via additional_drop_params
    # above (they only take effect there, not here).
    #
    # callbacks: reasoning_patch.reasoning_injector re-attaches reasoning_content
    # to assistant tool-call messages before each upstream dispatch. Thinking
    # models (deepseek-v4-flash) hard-require it on multi-turn tool use; the
    # Responses->Chat bridge drops it, so without this Codex 400s after turn 1.
    # See /reasoning_patch.py.
    "litellm_settings": {
        "drop_params": True,
        "callbacks": "reasoning_patch.reasoning_injector",
    },
}
Path("/tmp/litellm-config.yaml").write_text(
    yaml.dump(proxy_config, default_flow_style=False))
os.chmod("/tmp/litellm-config.yaml", 0o600)

# Reasoning effort from THINKING_LEVEL.
_EFFORT_MAP = {
    "minimal": "minimal", "low": "low", "medium": "medium",
    "adaptive": "medium", "high": "high", "xhigh": "high",
}
thinking = (os.environ.get("THINKING_LEVEL") or "").lower()
reasoning_effort = _EFFORT_MAP.get(thinking, "medium") if thinking and thinking != "off" else "minimal"

def toml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("\"", "\\\"")

# approval_policy=never + the run script's --dangerously-bypass-approvals-and-sandbox
# give Codex full, uncaged exec — matching openclaw's `security: full`. A safety
# benchmark observes the agent's own judgement, it doesn't cage it.
toml = f'''\
model = "{toml_escape(model_name)}"
model_provider = "clawsafebench"
model_reasoning_effort = "{reasoning_effort}"
model_reasoning_summary = "auto"
# Emit raw chain-of-thought into the --json stream so upstream non-OpenAI models
# still surface reasoning (they don't always produce summaries).
show_raw_agent_reasoning = true
hide_agent_reasoning = false
approval_policy = "never"
sandbox_mode = "danger-full-access"

[model_providers.clawsafebench]
name = "ClawSafeBench provider (via LiteLLM)"
base_url = "http://localhost:4000/v1"
env_key = "CODEX_API_KEY"
# Codex 0.120.0 requires wire_api="responses" ("chat" is rejected). It POSTs to
# {base_url}/responses; LiteLLM bridges that to the upstream's /chat/completions
# because the model is prefixed `custom_openai/` (see setup litellm config).
wire_api = "responses"
'''
config_path = Path(os.path.expanduser("~/.codex/config.toml"))
config_path.write_text(toml)
os.chmod(config_path, 0o600)

env_path = Path("/tmp/codex-env.sh")
env_path.write_text('export CODEX_API_KEY="sk-proxy-placeholder"\n')
os.chmod(env_path, 0o600)

print(f"[setup-codex] model={model_name}, upstream={litellm_params['model']}, "
      f"wire_api=responses, reasoning_effort={reasoning_effort}")
PYEOF
