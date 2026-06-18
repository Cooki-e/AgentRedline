from __future__ import annotations

import logging
import os
import subprocess
import time
from pathlib import Path

from dotenv import load_dotenv

from src.agents.base import AgentExecution, AgentTaskSpec, BaseAgent
from src.utils.docker_utils import (
    run_harness_background,
    run_warmup,
    setup_skills,
    setup_workspace,
    start_container,
)
from src.utils.grading import extract_usage_from_jsonl
from src.utils.pricing import estimate_cost

load_dotenv()

logger = logging.getLogger(__name__)


class OpenClawAgent(BaseAgent):
    """Drives one OpenClaw task run against the ClawSafeBench harness.

    Architectural note: unlike WildClawBench's OpenClawAgent, this class does
    NOT start `openclaw gateway` or `openclaw agent` itself. The harness
    container exposes /run-harness.sh, which spawns gateway + agent + watchdog
    internally. We just supply env vars (INSTRUCTION, TIME_LIMIT_S, …) and
    block on its exit.
    """

    def __init__(
        self,
        *,
        base_url: str,
        api_type: str,
        model_name: str,
        api_key: str = "",
        api_keys: str = "",
        idle_threshold_s: int = 300,
        max_tokens: str | None = None,
        temperature: str | None = None,
    ) -> None:
        self.base_url = base_url
        self.api_type = api_type
        self.model_name = model_name
        self.api_key = api_key
        self.api_keys = api_keys
        self.idle_threshold_s = idle_threshold_s
        self.max_tokens = max_tokens
        self.temperature = temperature

    harness_name = "openclaw"
    image = "clawsafebench-openclaw"

    @property
    def expects_gateway(self) -> bool:
        # The harness script owns the gateway; we still report True so the
        # run_batch.py error-path branch can distinguish a missing harness
        # invocation from an intentional gateway-less backend.
        return True

    @property
    def transcript_container_path(self) -> str:
        # /run-harness.sh mirrors the session log to this path on exit.
        # Falls back to /root/.openclaw/agents/main/sessions/clawsafebench.jsonl
        # via transcript_loader if the mirror failed.
        return "/data/agent-messages.jsonl"

    def _provider_env(self) -> dict[str, str]:
        env: dict[str, str] = {
            "BASE_URL": self.base_url,
            "API_TYPE": self.api_type,
            "MODEL_NAME": self.model_name,
        }
        if self.api_keys:
            env["API_KEYS"] = self.api_keys
        if self.api_key:
            env["API_KEY"] = self.api_key
        if self.max_tokens:
            env["MAX_TOKENS"] = self.max_tokens
        if self.temperature:
            env["TEMPERATURE"] = self.temperature
        return env

    def run_task(self, spec: AgentTaskSpec) -> AgentExecution:
        agent_proc = None
        elapsed_time = float(spec.timeout_seconds)

        try:
            exec_path = os.path.join(spec.workspace_path, "exec")
            tmp_path = os.path.join(spec.workspace_path, "tmp")
            os.makedirs(exec_path, exist_ok=True)

            # Allow a per-task model override (rare; useful when one task in a
            # category needs a different model). spec.model wins if it differs
            # from the harness default.
            provider_env = self._provider_env()
            if spec.model and spec.model != self.model_name:
                provider_env["MODEL_NAME"] = spec.model

            start_container(
                spec.task_id,
                exec_path,
                extra_env=spec.task.get("env", ""),
                provider_env=provider_env,
                tmp_path=tmp_path,
                image=self.image,
            )

            setup_workspace(spec.task_id)
            setup_skills(
                spec.task_id,
                spec.task.get("skills", ""),
                spec.task.get("skills_path", ""),
            )
            run_warmup(spec.task_id, spec.task.get("warmup", ""))

            start_time = time.perf_counter()
            agent_proc = run_harness_background(
                spec.task_id,
                instruction=spec.prompt,
                timeout_seconds=spec.timeout_seconds,
                thinking=spec.thinking,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                idle_threshold_s=self.idle_threshold_s,
                log_path=spec.output_dir / "harness.log",
            )

            # Grace = 60s. The in-container watchdog should hit TIME_LIMIT_S
            # first and exit gracefully; the outer timeout is a backstop in
            # case the harness itself hangs.
            grace = 60
            logger.info(
                "[%s] Waiting for /run-harness.sh (timeout %ds + %ds grace)...",
                spec.task_id, spec.timeout_seconds, grace,
            )
            try:
                agent_proc.wait(timeout=spec.timeout_seconds + grace)
                elapsed_time = time.perf_counter() - start_time
                logger.info(
                    "[%s] /run-harness.sh finished, elapsed: %.2fs, exit=%s",
                    spec.task_id, elapsed_time, agent_proc.returncode,
                )
            except subprocess.TimeoutExpired:
                logger.warning(
                    "[%s] /run-harness.sh exceeded outer timeout, killing", spec.task_id,
                )
                elapsed_time = float(spec.timeout_seconds + grace)
                agent_proc.kill()
                agent_proc.wait()

            return AgentExecution(
                elapsed_time=elapsed_time,
                error=None,
                gateway_proc=None,
                agent_proc=agent_proc,
            )
        except Exception as exc:
            logger.error("[%s] Execution error: %s", spec.task_id, exc)
            return AgentExecution(
                elapsed_time=float(spec.timeout_seconds),
                error=str(exc),
                gateway_proc=None,
                agent_proc=agent_proc,
            )

    def collect_usage(
        self, task_id: str, output_dir: Path, elapsed_time: float, model: str = ""
    ) -> dict:
        """Copy the transcript out and aggregate usage from it."""
        transcript_host = output_dir / "chat.jsonl"
        output_dir.mkdir(parents=True, exist_ok=True)
        r_cp = subprocess.run(
            [
                "docker", "cp",
                f"{task_id}:{self.transcript_container_path}",
                str(transcript_host),
            ],
            capture_output=True, text=True,
        )
        if r_cp.returncode == 0 and transcript_host.exists():
            usage = extract_usage_from_jsonl(transcript_host)
        else:
            logger.warning(
                "[%s] Transcript copy failed (%s): %s",
                task_id, self.transcript_container_path, r_cp.stderr.strip(),
            )
            # Fallback: try the live session path.
            fallback = "/root/.openclaw/agents/main/sessions/clawsafebench.jsonl"
            r_cp2 = subprocess.run(
                ["docker", "cp", f"{task_id}:{fallback}", str(transcript_host)],
                capture_output=True, text=True,
            )
            if r_cp2.returncode == 0 and transcript_host.exists():
                usage = extract_usage_from_jsonl(transcript_host)
            else:
                logger.warning(
                    "[%s] Transcript fallback copy also failed: %s",
                    task_id, r_cp2.stderr.strip(),
                )
                usage = {
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cache_read_tokens": 0,
                    "cache_write_tokens": 0,
                    "total_tokens": 0,
                    "cost_usd": 0.0,
                    "request_count": 0,
                    "tool_call_count": 0,
                    "tool_calls_by_name": {},
                }

        # The transcript's per-message `usage.cost` is zero for providers that
        # don't report cost. Fall back to the local pricing table (pricing.json
        # / OPENCLAW_*_PRICE_PER_MTOK env) keyed by model. Provider-reported
        # cost wins when present.
        if usage.get("cost_usd"):
            usage["cost_source"] = "provider"
        else:
            estimated = estimate_cost(usage, model or self.model_name)
            usage["cost_usd"] = estimated
            usage["cost_source"] = "estimated" if estimated else "unavailable"

        usage["elapsed_time"] = round(elapsed_time, 2)
        return usage
