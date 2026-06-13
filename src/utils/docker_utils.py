from __future__ import annotations

import logging
import os
import shlex
import subprocess
from pathlib import Path, PurePosixPath

from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

DOCKER_IMAGE = os.environ.get("DOCKER_IMAGE", "clawsafebench-openclaw")
WORKSPACE_DIR = os.environ.get("WORKSPACE_DIR", "/root/workspace")


def remove_container(name: str) -> None:
    subprocess.run(["docker", "rm", "-f", name], capture_output=True)


def start_container(
    task_id: str,
    workspace_path: str,
    *,
    extra_env: str = "",
    provider_env: dict[str, str] | None = None,
    tmp_path: str = "",
) -> None:
    """Start a manual-mode container for one task.

    The harness entrypoint enters its `tail -f /dev/null` branch when no
    INSTRUCTION env var is set, so we pass an explicit command override too
    for belt-and-suspenders.

    - workspace_path is mounted read-only at /app; setup_workspace later
      copies it into WORKSPACE_DIR with write permissions.
    - provider_env carries BASE_URL / API_TYPE / MODEL_NAME / API_KEY /
      API_KEYS (and optional TEMPERATURE, MAX_TOKENS) — these are needed
      inside the container later when /run-harness.sh shells out to
      /setup-openclaw.sh.
    - extra_env is the multi-line block from a task's `## Env` section; each
      key is looked up in the host environment and forwarded.
    """
    workspace = Path(workspace_path).expanduser()
    if not workspace.is_dir():
        raise RuntimeError(
            f"Workspace path does not exist or is not a directory: {workspace}"
        )

    proxy_http = os.environ.get("HTTP_PROXY_INNER", "")
    proxy_https = os.environ.get("HTTPS_PROXY_INNER", "")
    no_proxy = os.environ.get("NO_PROXY_INNER", "") if proxy_http else ""
    env_args = [
        "-e", f"http_proxy={proxy_http}",
        "-e", f"https_proxy={proxy_https}",
        "-e", f"HTTP_PROXY={proxy_http}",
        "-e", f"HTTPS_PROXY={proxy_https}",
        "-e", f"no_proxy={no_proxy}",
    ]
    for key, value in (provider_env or {}).items():
        if value is None:
            continue
        env_args += ["-e", f"{key}={value}"]
        masked = (value[:4] + "***") if value else "(empty)"
        logger.info("[%s] Injecting provider env: %s=%s", task_id, key, masked)

    for line in extra_env.splitlines():
        key = line.strip()
        if not key or key.startswith("#"):
            continue
        value = os.environ.get(key, "")
        env_args += ["-e", f"{key}={value}"]
        masked = (value[:4] + "***") if value else "(empty)"
        logger.info("[%s] Injecting task env: %s=%s", task_id, key, masked)

    cmd = [
        "docker", "run", "-d",
        "--name", task_id,
        *env_args,
        "-v", f"{workspace}:/app:ro",
        DOCKER_IMAGE,
    ]
    logger.info("[%s] Starting container, mounting %s → /app (ro)", task_id, workspace)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"Container startup failed:\n{r.stderr}")
    logger.info("[%s] Container ID: %s", task_id, r.stdout.strip()[:12])

    if tmp_path and os.path.exists(tmp_path):
        subprocess.run(
            ["docker", "exec", task_id, "mkdir", "-p", f"{WORKSPACE_DIR}/tmp"],
            capture_output=True,
        )
        logger.info("[%s] Copying tmp files: %s → %s/tmp", task_id, tmp_path, WORKSPACE_DIR)
        cp_r = subprocess.run(
            ["docker", "cp", f"{tmp_path}/.", f"{task_id}:{WORKSPACE_DIR}/tmp/"],
            capture_output=True, text=True,
        )
        if cp_r.returncode != 0:
            logger.error("[%s] tmp file copy failed: %s", task_id, cp_r.stderr)
        else:
            logger.info("[%s] tmp file copy complete", task_id)


def setup_workspace(task_id: str) -> None:
    """Copy the read-only /app mount into WORKSPACE_DIR with write perms.

    Also symlinks /tmp_workspace -> WORKSPACE_DIR so tasks authored against
    the legacy WildClawBench convention (which writes/grades against
    /tmp_workspace) work without per-task edits.
    """
    logger.info("[%s] Copying /app → %s", task_id, WORKSPACE_DIR)
    r = subprocess.run(
        [
            "docker", "exec", task_id, "/bin/bash", "-c",
            f"mkdir -p {WORKSPACE_DIR} && cp -r /app/. {WORKSPACE_DIR}/ "
            f"&& chmod -R u+w {WORKSPACE_DIR} "
            f"&& ln -sfn {WORKSPACE_DIR} /tmp_workspace",
        ],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise RuntimeError(f"Workspace copy failed:\n{r.stderr}")


def setup_skills(
    task_id: str,
    skills: str,
    skills_path: str,
    container_skills_root: str = "/root/workspace/skills",
) -> None:
    """Copy a flattened set of skill directories into <workspace>/skills/.

    The `skills` arg is a newline-separated list of paths relative to
    `skills_path`; the final basename is used as the destination dir name.

    Destination is `<workspace>/skills/` because openclaw discovers skills by
    scanning that path (`workspaceDir + "/skills"`); copying to /root/skills
    would leave them invisible to the agent.
    """
    if not skills.strip():
        return

    container_skills_root = container_skills_root.rstrip("/")
    subprocess.run(
        ["docker", "exec", task_id, "mkdir", "-p", container_skills_root],
        capture_output=True, text=True,
    )
    seen_dest_names: set[str] = set()
    for line in skills.splitlines():
        line = line.strip()
        if not line:
            continue
        src_rel = line.replace("\\", "/").strip("/")
        dest_name = PurePosixPath(src_rel).name
        if not dest_name:
            logger.warning("[%s] Invalid skill path %r, skipping", task_id, line)
            continue
        if dest_name in seen_dest_names:
            logger.warning(
                "[%s] Duplicate flattened skill target %s from %s, skipping",
                task_id, dest_name, line,
            )
            continue
        seen_dest_names.add(dest_name)
        subprocess.run(
            [
                "docker", "exec", task_id,
                "mkdir", "-p", f"{container_skills_root}/{dest_name}",
            ],
            capture_output=True, text=True,
        )
        r = subprocess.run(
            [
                "docker", "cp",
                f"{skills_path}/{src_rel}/.",
                f"{task_id}:{container_skills_root}/{dest_name}/",
            ],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            logger.warning(
                "[%s] Failed to copy skill %s to %s/%s: %s",
                task_id, line, container_skills_root, dest_name, r.stderr.strip(),
            )


def run_warmup(
    task_id: str,
    warmup: str,
    *,
    detach_background: bool = False,
) -> None:
    """Execute bash commands from a task's `## Warmup` section line by line."""
    if not warmup.strip():
        return
    commands = [
        line.strip()
        for line in warmup.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    if not commands:
        return

    logger.info("[%s] Running warmup (%d commands)", task_id, len(commands))
    for idx, cmd in enumerate(commands, start=1):
        logger.info("[%s] warmup: %s", task_id, cmd)
        stripped_cmd = cmd.rstrip()
        if detach_background and stripped_cmd.endswith("&"):
            background_cmd = stripped_cmd[:-1].strip()
            log_path = f"/tmp/clawsafebench_warmup_{idx}.log"
            wrapped = (
                f"cd {WORKSPACE_DIR} && "
                f"nohup /bin/bash -lc {shlex.quote(background_cmd)} "
                f"> {shlex.quote(log_path)} 2>&1 < /dev/null &"
            )
            r = subprocess.run(
                ["docker", "exec", task_id, "/bin/bash", "-lc", wrapped],
                capture_output=True, text=True,
            )
            if r.returncode != 0:
                raise RuntimeError(
                    f"Warmup background command failed: {cmd!r}\n{r.stderr}"
                )
            continue

        r = subprocess.run(
            [
                "docker", "exec", task_id, "/bin/bash", "-c",
                f"cd {WORKSPACE_DIR} && {cmd}",
            ],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            raise RuntimeError(f"Warmup command failed: {cmd!r}\n{r.stderr}")


def run_harness_background(
    task_id: str,
    *,
    instruction: str,
    timeout_seconds: int,
    thinking: str | None,
    max_tokens: str | None,
    temperature: str | None,
    idle_threshold_s: int,
    log_path: Path,
) -> subprocess.Popen:
    """Trigger /run-harness.sh in the container as a background docker-exec.

    The harness script blocks until the agent finishes (gateway up, agent
    runs, watchdog hits idle/time-limit/eval-matched), then exits. We
    capture its stdout+stderr to log_path; the harness ALSO writes its own
    structured logs to /data/{gateway,agent}.log inside the container.
    """
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_file = log_path.open("w", encoding="utf-8")

    env_args = ["-e", f"INSTRUCTION={instruction}",
                "-e", f"TIME_LIMIT_S={timeout_seconds}",
                "-e", f"IDLE_THRESHOLD_S={idle_threshold_s}"]
    if thinking:
        env_args += ["-e", f"THINKING_LEVEL={thinking}"]
    if max_tokens:
        env_args += ["-e", f"MAX_TOKENS={max_tokens}"]
    if temperature:
        env_args += ["-e", f"TEMPERATURE={temperature}"]

    proc = subprocess.Popen(
        ["docker", "exec", *env_args, task_id, "/run-harness.sh"],
        stdout=log_file,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
    )
    proc._log_file = log_file  # type: ignore[attr-defined]
    logger.info("[%s] Triggered /run-harness.sh PID=%s → %s", task_id, proc.pid, log_path)
    return proc


def close_proc_log(proc: subprocess.Popen) -> None:
    """Close a log file handle stashed on a Popen by run_harness_background."""
    log_file = getattr(proc, "_log_file", None)
    if log_file and not log_file.closed:
        log_file.close()


def copy_gt_into_container(task_id: str, workspace_path: str) -> None:
    """Copy the task's gt/ directory (if any) into the container for grading."""
    gt_host = os.path.join(workspace_path, "gt")
    if not os.path.isdir(gt_host):
        return
    r = subprocess.run(
        ["docker", "cp", gt_host, f"{task_id}:{WORKSPACE_DIR}/gt"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        logger.warning("[%s] gt directory copy failed: %s", task_id, r.stderr)
    else:
        logger.info("[%s] gt directory copied to %s/gt", task_id, WORKSPACE_DIR)


def collect_output_from_container(task_id: str, output_dir: Path) -> None:
    """Pull harness outputs + task deliverables out of the container.

    Layout under output_dir/task_output/:
      ./                       — everything from /data/ (gateway.log, agent.log,
                                  usage.jsonl, agent-messages.jsonl, .stop-reason)
      ./workspace/results/     — the task's deliverable files (if it wrote any)
    """
    task_output_dir = output_dir / "task_output"
    task_output_dir.mkdir(parents=True, exist_ok=True)

    _copy_dir_from_container(task_id, "/data/.", str(task_output_dir))

    workspace_out = task_output_dir / "workspace"
    workspace_out.mkdir(parents=True, exist_ok=True)
    results_out = workspace_out / "results"
    results_out.mkdir(parents=True, exist_ok=True)
    ok = _copy_dir_from_container(
        task_id, f"{WORKSPACE_DIR}/results/.", str(results_out),
    )
    if not ok:
        logger.warning("[%s] %s/results/ does not exist or is empty", task_id, WORKSPACE_DIR)


def _copy_dir_from_container(task_id: str, src: str, dest: str) -> bool:
    r = subprocess.run(
        ["docker", "cp", f"{task_id}:{src}", dest],
        capture_output=True, text=True,
    )
    if r.returncode == 0:
        logger.info("[%s] Collected container directory %s → %s", task_id, src, dest)
        return True
    return False
