from __future__ import annotations

import json
import logging
import os
import re
import sys
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents.base import AgentTaskSpec, BaseAgent
from src.agents.openclaw import OpenClawAgent
from src.utils.cli_args import parse_run_batch_args
from src.utils.docker_utils import (
    close_proc_log,
    collect_output_from_container,
    copy_gt_into_container,
    remove_container,
)
from src.utils.endpoint_utils import normalize_openrouter_base_url_for_openclaw
from src.utils.grading import (
    format_scores,
    print_global_summary,
    print_summary,
    run_grading,
    write_error_score,
)
from src.utils.task_parser import parse_task_md

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent
TASKS_DIR = ROOT_DIR / os.environ.get("TASKS_SUBDIR", "tasks")
OUTPUT_DIR = ROOT_DIR / os.environ.get("OUTPUT_SUBDIR", "output")

DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "anthropic/claude-sonnet-4.6")
DEFAULT_PARALLEL = int(os.environ.get("DEFAULT_PARALLEL", "1"))

# Provider config consumed by the harness's /setup-openclaw.sh.
BASE_URL = normalize_openrouter_base_url_for_openclaw(os.environ.get("BASE_URL", ""))
API_TYPE = os.environ.get("API_TYPE", "openai-completions")
API_KEY = os.environ.get("API_KEY", "")
API_KEYS = os.environ.get("API_KEYS", "")  # optional JSON list


def grade_the_task(
    task_id: str,
    workspace_path: str,
    output_dir: Path,
    task: dict,
    result: dict,
    transcript_container_path: str = "",
) -> dict:
    copy_gt_into_container(task_id, workspace_path)

    should_grade = bool(task.get("automated_checks")) and not result.get("error")
    if should_grade:
        try:
            scores = run_grading(
                task_id=task_id,
                automated_checks=task["automated_checks"],
                output_dir=output_dir,
                extra_env=task.get("env", ""),
                transcript_container_path=transcript_container_path,
            )
            result["scores"] = scores
            print(format_scores(task_id, scores))
            logger.info("[%s] Grading complete", task_id)
        except Exception as exc:
            logger.error("[%s] Grading failed: %s", task_id, exc)
            result["scores"] = write_error_score(output_dir, task_id, str(exc))
    elif not task.get("automated_checks"):
        logger.info("[%s] No Automated Checks, skipping grading", task_id)
        if result.get("error"):
            result["scores"] = write_error_score(output_dir, task_id, result["error"])

    return result


def save_usage(output_dir: Path, result: dict, usage: dict, task_id: str) -> dict:
    result["usage"] = usage
    if usage["request_count"] > 0:
        logger.info(
            "[%s] Token usage - input:%d output:%d cache_read:%d total:%d cost:$%.4f",
            task_id,
            usage["input_tokens"], usage["output_tokens"],
            usage["cache_read_tokens"], usage["total_tokens"],
            usage["cost_usd"],
        )
    usage_path = output_dir / "usage.json"
    usage_path.write_text(
        json.dumps(usage, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info("[%s] Usage written to %s", task_id, usage_path)
    return result


def collect_task_output(task_id: str, output_dir: Path) -> None:
    try:
        collect_output_from_container(task_id, output_dir)
    except Exception as exc:
        logger.warning("[%s] Failed to collect task output: %s", task_id, exc)


def run_single_task(
    task: dict,
    model: str,
    backend: BaseAgent,
    output_root: Path,
    thinking: str | None = None,
) -> dict:
    """Execute a single task, returning {"task_id", "scores", "error", "usage"}.

    Thread-safe: each invocation uses a unique container name and output dir.
    """
    task_id_ori = task["task_id"]
    workspace_path = task["workspace_path"]
    prompt = task["prompt"]
    timeout_seconds = task["timeout_seconds"]

    # System prompt nudges the agent toward foreground, single-pass execution.
    system_prompt = (
        f"You are an expert in a restricted, non-interactive environment. "
        f"Solve the task efficiently before the timeout ({timeout_seconds}s). "
        "Run all processes in the foreground without user input or background "
        "services. Provide a complete, functional solution in a single pass "
        "with no placeholders.\n"
    )
    prompt = system_prompt + prompt

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    run_id = uuid.uuid4().hex[:6]
    _m = re.match(r"(\d+)_.*?(task_\d+)", task_id_ori)
    short_task_id = f"{_m.group(1)}_{_m.group(2)}" if _m else task_id_ori
    short_model = re.sub(r"[^a-zA-Z0-9.\-_]", "_", model.rsplit("/", 1)[-1])
    suffix = f"{short_model}_{timestamp}_{run_id}"
    task_id = f"{short_task_id}_{short_model}_{timestamp}_{run_id}"

    output_dir = output_root / task["category"] / task_id_ori / suffix
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {"task_id": task_id, "scores": {}, "error": None}

    agent_proc = None
    elapsed_time = float(timeout_seconds)

    try:
        execution = backend.run_task(
            AgentTaskSpec(
                task_id=task_id,
                task=task,
                workspace_path=workspace_path,
                prompt=prompt,
                timeout_seconds=timeout_seconds,
                output_dir=output_dir,
                model=model,
                thinking=thinking,
            )
        )
        agent_proc = execution.agent_proc
        elapsed_time = execution.elapsed_time
        if execution.error:
            result["error"] = execution.error
    except Exception as exc:
        result["error"] = str(exc)
        logger.error("[%s] Unexpected backend error: %s", task_id, exc)

    finally:
        grading_transcript_path = backend.transcript_container_path
        if task.get("automated_checks") and not result.get("error"):
            try:
                grading_transcript_path = backend.prepare_grading_transcript(task_id)
            except Exception as exc:
                logger.warning(
                    "[%s] Failed to prepare grading transcript, fallback to %s: %s",
                    task_id, grading_transcript_path, exc,
                )

        result = grade_the_task(
            task_id,
            workspace_path,
            output_dir,
            task,
            result,
            transcript_container_path=grading_transcript_path,
        )

        usage = backend.collect_usage(
            task_id=task_id,
            output_dir=output_dir,
            elapsed_time=elapsed_time,
            model=model,
        )
        result = save_usage(output_dir, result, usage, task_id)

        try:
            collect_task_output(task_id, output_dir)
        except Exception as exc:
            logger.warning("[%s] Failed to collect task output: %s", task_id, exc)

        if agent_proc is not None:
            try:
                close_proc_log(agent_proc)
            except Exception:
                pass

        remove_container(task_id)
        logger.info("[%s] Container cleaned up", task_id)

    return result


def _discover_categories() -> list[str]:
    if not TASKS_DIR.exists():
        return []
    return sorted(p.name for p in TASKS_DIR.iterdir() if p.is_dir())


def main() -> None:
    args = parse_run_batch_args(
        default_model=DEFAULT_MODEL,
        default_parallel=DEFAULT_PARALLEL,
    )

    if args.agent_backend != "openclaw":
        logger.error("Only --agent-backend openclaw is wired up at the moment.")
        sys.exit(1)

    if not BASE_URL or not API_TYPE:
        logger.error("BASE_URL and API_TYPE must be set (check .env)")
        sys.exit(1)
    if not (API_KEY or API_KEYS):
        logger.error("API_KEY or API_KEYS must be set (check .env)")
        sys.exit(1)

    backend: BaseAgent = OpenClawAgent(
        base_url=BASE_URL,
        api_type=API_TYPE,
        model_name=args.model,
        api_key=API_KEY,
        api_keys=API_KEYS,
    )

    output_root = OUTPUT_DIR / args.agent_backend

    if args.task:
        task_file = Path(args.task)
        if not task_file.exists():
            logger.error("File not found: %s", task_file)
            sys.exit(1)
        task = parse_task_md(task_file)
        logger.info("Single task mode: %s", task["task_id"])
        result = run_single_task(
            task,
            args.model,
            backend=backend,
            output_root=output_root,
            thinking=args.thinking,
        )
        if result.get("error") or (result.get("scores") or {}).get("error"):
            sys.exit(1)
        return

    if args.category.lower() == "all":
        categories = _discover_categories()
        if not categories:
            logger.error("No category directories found under %s", TASKS_DIR)
            sys.exit(1)
    else:
        categories = [args.category]

    all_results: list[dict] = []
    safe_model_name = re.sub(r"[^a-zA-Z0-9.\-_]", "_", args.model)

    for category in categories:
        category_dir = TASKS_DIR / category
        if not category_dir.exists():
            logger.error("Category directory not found: %s", category_dir)
            continue

        task_files = sorted(category_dir.glob("*task_*.md"))
        if not task_files:
            logger.error("No task_*.md files found in: %s", category_dir)
            continue

        logger.info(
            "Category: %s, %d tasks, parallelism: %d",
            category, len(task_files), args.parallel,
        )

        tasks = []
        for tf in task_files:
            try:
                tasks.append(parse_task_md(tf))
            except Exception as exc:
                logger.error("Parse failed %s: %s", tf, exc)

        if not tasks:
            continue

        results: list[dict] = []
        if args.parallel <= 1:
            for task in tasks:
                results.append(
                    run_single_task(
                        task,
                        args.model,
                        backend=backend,
                        output_root=output_root,
                        thinking=args.thinking,
                    )
                )
        else:
            with ThreadPoolExecutor(max_workers=args.parallel) as pool:
                futures = {
                    pool.submit(
                        run_single_task,
                        task,
                        args.model,
                        backend,
                        output_root,
                        args.thinking,
                    ): task["task_id"]
                    for task in tasks
                }
                for future in as_completed(futures):
                    tid = futures[future]
                    try:
                        results.append(future.result())
                    except Exception as exc:
                        logger.error("[%s] Thread exception: %s", tid, exc)
                        results.append({"task_id": tid, "scores": {}, "error": str(exc)})

        print_summary(results, category, output_root, safe_model_name)
        all_results.extend(results)

    if len(categories) > 1 and all_results:
        print_global_summary(all_results, output_root, safe_model_name)


if __name__ == "__main__":
    main()
