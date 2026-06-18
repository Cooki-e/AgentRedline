from __future__ import annotations

from src.agents.container_harness import ContainerHarnessAgent


class CodexAgent(ContainerHarnessAgent):
    """Drives one OpenAI Codex CLI task run against the ClawSafeBench harness.

    The clawsafebench-codex container runs a LiteLLM proxy + `codex exec` via
    /run-harness.sh and mirrors the session rollout to /data/agent-messages.jsonl
    on exit. See src/harness/codex/ for the in-container logic.
    """

    harness_name = "codex"
    image = "clawsafebench-codex"
