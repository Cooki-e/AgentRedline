from __future__ import annotations

from src.agents.container_harness import ContainerHarnessAgent


class ClaudeCodeAgent(ContainerHarnessAgent):
    """Drives one Anthropic Claude Code CLI task run against the harness.

    The clawsafebench-claude-code container runs a LiteLLM proxy + `claude -p`
    via /run-harness.sh, streaming stream-json to /data/agent-messages.jsonl.
    See src/harness/claude-code/ for the in-container logic.
    """

    harness_name = "claude-code"
    image = "clawsafebench-claude-code"
