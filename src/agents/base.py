from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class AgentTaskSpec:
    task_id: str
    task: dict[str, Any]
    workspace_path: str
    prompt: str
    timeout_seconds: int
    output_dir: Path
    model: str
    thinking: str | None = None


@dataclass
class AgentExecution:
    elapsed_time: float
    error: str | None = None
    gateway_proc: subprocess.Popen[str] | None = None
    agent_proc: subprocess.Popen[str] | None = None


class BaseAgent(ABC):
    @property
    @abstractmethod
    def expects_gateway(self) -> bool:
        """Whether this backend launches a gateway (or delegates to one)."""

    @property
    @abstractmethod
    def transcript_container_path(self) -> str:
        """Path to the chat transcript inside the runtime container."""

    def prepare_grading_transcript(self, task_id: str) -> str:
        """Prepare and return the transcript path used for grading.

        Default implementation returns the container-side transcript path
        unchanged. Backends that need to post-process the transcript before
        grading can override this.
        """
        _ = task_id
        return self.transcript_container_path

    @abstractmethod
    def run_task(self, spec: AgentTaskSpec) -> AgentExecution:
        """Execute a task and return process handles, timing, and error state."""

    @abstractmethod
    def collect_usage(
        self, task_id: str, output_dir: Path, elapsed_time: float, model: str = ""
    ) -> dict[str, Any]:
        """Collect token usage and cost for one task.

        `model` is used to estimate cost from a local pricing table when the
        transcript does not report a cost.
        """
