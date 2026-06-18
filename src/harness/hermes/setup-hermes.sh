#!/bin/bash
set -e

# Renders ~/.hermes/config.yaml, ~/.hermes/.env, and /tmp/hermes-env.sh from env
# vars supplied by the host runner. Called by run-hermes.sh before the agent
# starts.
#
# Required env: BASE_URL, MODEL_NAME, API_TYPE, API_KEY (or API_KEYS).
# Optional env: THINKING_LEVEL, TEMPERATURE (ignored), MAX_TOKENS (ignored).
#
# Hermes talks directly to BASE_URL (no proxy) via its native provider/api_mode.

if [ -z "$BASE_URL" ] || [ -z "$MODEL_NAME" ] || [ -z "$API_TYPE" ]; then
  echo "[setup-hermes] ERROR: BASE_URL, MODEL_NAME, and API_TYPE must be set"
  exit 1
fi

if [ -n "$TEMPERATURE" ]; then
  echo "[setup-hermes] WARN: 'hermes chat' has no temperature flag; TEMPERATURE='$TEMPERATURE' ignored."
fi
if [ -n "$MAX_TOKENS" ]; then
  echo "[setup-hermes] WARN: 'hermes chat' has no max-tokens flag; MAX_TOKENS='$MAX_TOKENS' ignored."
fi

mkdir -p "$HOME/.hermes"

python3 - <<'PYEOF'
import json
import os
import shlex
import urllib.request
from pathlib import Path

base_url = os.environ["BASE_URL"].rstrip("/")
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
                print(f"[setup-hermes] WARN: Hermes does not rotate keys - using first of {len(parsed)}")
    except json.JSONDecodeError:
        pass
if not key and single_key:
    key = single_key
if not key:
    raise SystemExit("[setup-hermes] ERROR: no API key provided (API_KEYS or API_KEY)")

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
            model_id = m.get("id", "")
            if model_id == model_name or model_id.endswith(f"/{model_name}"):
                resolved_model = model_id
                break
    except Exception as e:
        print(f"[setup-hermes] WARN: could not resolve OpenRouter model ID: {e}")

# Map ClawSafeBench API types to Hermes provider/api_mode settings.
#
# For OpenAI-compatible custom endpoints (deepseek/qiqi/etc.) Hermes needs a
# NAMED custom provider in a `custom_providers:` list — the bare `custom`
# provider falls through to the OpenRouter default (401). The session selects it
# via model "custom:<name>:<model>". We register it under the fixed name below.
CUSTOM_PROVIDER_NAME = "csb"

dotenv_lines = []
custom_provider = None  # set for OpenAI-compatible endpoints
if is_openrouter:
    provider = "openrouter"
    api_mode = "chat_completions"
    dotenv_lines.extend([
        f"OPENROUTER_API_KEY={key}",
        f"OPENROUTER_BASE_URL={base_url}",
    ])
elif api_type == "openai-completions":
    provider = f"custom:{CUSTOM_PROVIDER_NAME}"
    api_mode = "chat_completions"
    custom_provider = {"api_mode": "chat_completions"}
    dotenv_lines.extend([
        f"OPENAI_API_KEY={key}",
        f"OPENAI_BASE_URL={base_url}",
        f"CUSTOM_API_KEY={key}",
    ])
elif api_type == "openai-responses":
    provider = f"custom:{CUSTOM_PROVIDER_NAME}"
    api_mode = "codex_responses"
    custom_provider = {"api_mode": "codex_responses"}
    dotenv_lines.extend([
        f"OPENAI_API_KEY={key}",
        f"OPENAI_BASE_URL={base_url}",
        f"CUSTOM_API_KEY={key}",
    ])
elif api_type == "anthropic-messages":
    provider = "anthropic"
    api_mode = "anthropic_messages"
    dotenv_lines.extend([
        f"ANTHROPIC_API_KEY={key}",
        f"ANTHROPIC_BASE_URL={base_url}",
    ])
elif api_type == "google-generative-ai":
    provider = "gemini"
    api_mode = "chat_completions"
    dotenv_lines.extend([
        f"GOOGLE_API_KEY={key}",
        f"GEMINI_API_KEY={key}",
        f"GEMINI_BASE_URL={base_url}",
    ])
else:
    raise SystemExit(f"[setup-hermes] ERROR: unsupported api_type for hermes harness: {api_type}")

effort_map = {
    "minimal": "minimal", "low": "low", "medium": "medium",
    "adaptive": "medium", "high": "high", "xhigh": "xhigh",
}
thinking = (os.environ.get("THINKING_LEVEL") or "").lower()
reasoning_effort = effort_map.get(thinking, "medium") if thinking and thinking != "off" else "none"

def yaml_scalar(value: str) -> str:
    return json.dumps(value)

# No browser block: this is a filesystem/network safety benchmark. The terminal
# toolset runs commands locally inside the container (uncaged, matching openclaw).
config = f"""\
model:
  provider: {yaml_scalar(provider)}
  default: {yaml_scalar(resolved_model)}
  base_url: {yaml_scalar(base_url)}
  api_mode: {yaml_scalar(api_mode)}
agent:
  reasoning_effort: {yaml_scalar(reasoning_effort)}
  show_reasoning: true
  max_turns: 90
terminal:
  backend: "local"
  command_timeout: 60
security:
  redact_secrets: false
"""

# Register the named custom provider so "custom:<name>:<model>" resolves to our
# endpoint (instead of falling through to OpenRouter).
if custom_provider is not None:
    config += f"""\
custom_providers:
  - name: {yaml_scalar(CUSTOM_PROVIDER_NAME)}
    base_url: {yaml_scalar(base_url)}
    api_key: {yaml_scalar(key)}
    api_mode: {yaml_scalar(custom_provider["api_mode"])}
    model: {yaml_scalar(resolved_model)}
"""

# The model arg the run script should pass to `hermes chat --model`. For a named
# custom provider it must be fully qualified as custom:<name>:<model>.
hermes_model_arg = (
    f"custom:{CUSTOM_PROVIDER_NAME}:{resolved_model}"
    if custom_provider is not None
    else resolved_model
)

hermes_home = Path(os.path.expanduser("~/.hermes"))
config_path = hermes_home / "config.yaml"
config_path.write_text(config)
os.chmod(config_path, 0o600)

env_path = hermes_home / ".env"
env_path.write_text("\n".join(dotenv_lines) + "\n")
os.chmod(env_path, 0o600)

run_env = {
    "HERMES_HOME": str(hermes_home),
    "HERMES_MODEL_NAME": resolved_model,
    "HERMES_MODEL_ARG": hermes_model_arg,
    "HERMES_PROVIDER": provider,
    "HERMES_API_MODE": api_mode,
    "NO_COLOR": "1",
    "TERM": "xterm-256color",
}
for line in dotenv_lines:
    name, value = line.split("=", 1)
    run_env[name] = value

run_env_path = Path("/tmp/hermes-env.sh")
run_env_path.write_text(
    "".join(f"export {name}={shlex.quote(value)}\n" for name, value in run_env.items())
)
os.chmod(run_env_path, 0o600)

print(
    "[setup-hermes] "
    f"model={resolved_model}, provider={provider}, api_mode={api_mode}, "
    f"reasoning_effort={reasoning_effort}"
)
PYEOF
