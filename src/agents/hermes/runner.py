from __future__ import annotations

from src.agents.container_harness import ContainerHarnessAgent


class HermesAgent(ContainerHarnessAgent):
    """Drives one NousResearch Hermes task run against the harness.

    The clawsafebench-hermes container runs `hermes chat` (terminal,file
    toolsets) via /run-harness.sh — talking directly to BASE_URL, no proxy —
    and exports its session transcript to /data/agent-messages.jsonl on exit.
    See src/harness/hermes/ for the in-container logic.
    """

    harness_name = "hermes"
    image = "clawsafebench-hermes"
