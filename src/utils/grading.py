from __future__ import annotations

import json
import logging
import os
import subprocess
import tempfile
from pathlib import Path

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()
WORKSPACE_DIR = os.environ.get("WORKSPACE_DIR", "/root/workspace")


def _write_score(output_dir: Path, task_id: str, scores: dict) -> None:
    score_path = output_dir / "score.json"
    score_path.parent.mkdir(parents=True, exist_ok=True)
    score_path.write_text(
        json.dumps(scores, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info("[%s] Grading results written to → %s", task_id, score_path)


def _error_score(output_dir: Path, task_id: str, message: str) -> dict:
    scores = {"overall_score": 0.0, "error": message}
    _write_score(output_dir, task_id, scores)
    return scores


def _grading_error(
    output_dir: Path,
    task_id: str,
    message: str,
    write_error_score: bool,
) -> dict:
    if write_error_score:
        return _error_score(output_dir, task_id, message)
    return {"error": message}


def write_error_score(output_dir: Path, task_id: str, message: str) -> dict:
    return _error_score(output_dir, task_id, message)


def run_grading(
    task_id: str,
    automated_checks: str,
    output_dir: Path,
    extra_env: str = "",
    transcript_container_path: str = "",
    write_error_score: bool = False,
) -> dict:
    """Run a task's `grade(transcript, workspace_path)` function inside the container.

    Strategy:
      1. docker cp the transcript_loader module + a generated runner script
         (which inlines the task's `automated_checks` body) into /tmp/.
      2. docker exec python3 /tmp/_grade_runner.py with task env vars injected.
      3. Parse the last JSON object printed to stdout as the score dict.
      4. Persist to {output_dir}/score.json.
    """
    logger.info("[%s] Starting in-container grading...", task_id)

    loader_src = Path(__file__).with_name("transcript_loader.py")
    if not loader_src.exists():
        logger.error("[%s] transcript loader module not found: %s", task_id, loader_src)
        return _grading_error(
            output_dir,
            task_id,
            f"transcript loader module not found: {loader_src}",
            write_error_score,
        )

    runner_code = "\n".join([
        "import json",
        "from _transcript_loader import load_transcript",
        f"_transcript = load_transcript({json.dumps(transcript_container_path)})",
        "",
        automated_checks,
        "",
        f'result = grade(transcript=_transcript, workspace_path="{WORKSPACE_DIR}")',
        "print(json.dumps(result))",
    ]) + "\n"

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as f:
        f.write(runner_code)
        runner_host = f.name

    try:
        r_loader = subprocess.run(
            ["docker", "cp", str(loader_src), f"{task_id}:/tmp/_transcript_loader.py"],
            capture_output=True, text=True,
        )
        if r_loader.returncode != 0:
            logger.error("[%s] docker cp transcript loader failed: %s", task_id, r_loader.stderr)
            return _grading_error(
                output_dir,
                task_id,
                f"docker cp transcript loader failed: {r_loader.stderr}",
                write_error_score,
            )

        # Optional LLM-judge pipeline (tasks import it lazily and fall back to
        # regex if absent), so a cp failure is a warning, not a grading abort.
        judge_src = Path(__file__).with_name("llm_judge.py")
        if judge_src.exists():
            r_judge = subprocess.run(
                ["docker", "cp", str(judge_src), f"{task_id}:/tmp/_llm_judge.py"],
                capture_output=True, text=True,
            )
            if r_judge.returncode != 0:
                logger.warning(
                    "[%s] docker cp llm_judge failed (judge axes will fall back "
                    "to regex): %s", task_id, r_judge.stderr,
                )

        r = subprocess.run(
            ["docker", "cp", runner_host, f"{task_id}:/tmp/_grade_runner.py"],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            logger.error("[%s] docker cp grade runner failed: %s", task_id, r.stderr)
            return _grading_error(
                output_dir,
                task_id,
                f"docker cp failed: {r.stderr}",
                write_error_score,
            )

        env_args: list[str] = []
        for line in extra_env.splitlines():
            key = line.strip()
            if not key or key.startswith("#"):
                continue
            value = os.environ.get(key, "")
            env_args += ["-e", f"{key}={value}"]
            masked = (value[:4] + "***") if value else "(empty)"
            logger.info("[%s] Injecting grading env: %s=%s", task_id, key, masked)

        r = subprocess.run(
            ["docker", "exec", *env_args, task_id, "python3", "/tmp/_grade_runner.py"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if r.returncode != 0:
            logger.error("[%s] Grading script execution failed: %s", task_id, r.stderr)
            return _grading_error(
                output_dir,
                task_id,
                f"grade script failed: {r.stderr}",
                write_error_score,
            )

        try:
            scores = json.loads(r.stdout.strip())
        except json.JSONDecodeError:
            scores = None
            for line in reversed(r.stdout.strip().splitlines()):
                line = line.strip()
                if line.startswith("{"):
                    try:
                        scores = json.loads(line)
                        break
                    except json.JSONDecodeError:
                        continue
            if scores is None:
                logger.error(
                    "[%s] Failed to parse grading result, no valid JSON in stdout\nstdout: %s",
                    task_id, r.stdout[:500],
                )
                return _grading_error(
                    output_dir,
                    task_id,
                    "json parse failed: no valid JSON in stdout",
                    write_error_score,
                )

    finally:
        Path(runner_host).unlink(missing_ok=True)

    _write_score(output_dir, task_id, scores)
    return scores


def format_scores(task_id: str, scores: dict) -> str:
    if "error" in scores and not any(
        isinstance(v, (int, float)) for v in scores.values()
    ):
        return f"[{task_id}] Grading error: {scores['error']}"
    lines = [f"\n{'='*60}", f"  {task_id}", f"{'='*60}"]

    for k, v in scores.items():
        if isinstance(v, (int, float)):
            bar = "█" * int(v * 10) + "░" * (10 - int(v * 10))
            lines.append(f"  {bar} {v:.2f}  {k}")

    lines.append("=" * 60)
    return "\n".join(lines)


def print_summary(
    results: list[dict], category: str, output_dir: Path, model_name: str
) -> None:
    print(f"\n{'#'*60}")
    print(f"  Summary Report — {category}")
    print(f"{'#'*60}")

    all_scores: dict[str, float] = {}
    for r in results:
        task_id = r["task_id"]
        scores = r.get("scores") or {}
        if not scores:
            if r.get("error"):
                print(f"  ✗ {task_id}: {r['error']}")
            else:
                print(f"  - {task_id}: No scores")
            continue
        numeric_dict = {k: v for k, v in scores.items() if isinstance(v, (int, float))}

        if not numeric_dict:
            if "error" in scores:
                print(f"  ✗ {task_id}: Grading error {scores['error']}")
            else:
                print(f"  - {task_id}: No valid numeric scores")
            continue

        avg = sum(numeric_dict.values()) / len(numeric_dict)
        status = "!" if r.get("error") or scores.get("error") else "✓"
        note = ""
        if r.get("error"):
            note = f" agent_error={r['error']}"
        elif scores.get("error"):
            note = f" grading_error={scores['error']}"
        print(f"  {status} {task_id}: avg {avg:.2f}  ({len(numeric_dict)} items){note}")

        final_score_val = numeric_dict.get("overall_score", avg)
        all_scores[task_id] = final_score_val

    if all_scores:
        print("\n  Final scores per task:")
        for k, score in sorted(all_scores.items()):
            bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
            print(f"    {bar} {score:.2f}  {k}")

    print("\n  Token usage and cost per task:")
    print(f"    {'Task ID':<55} {'Output Tokens':>12} {'Cost(USD)':>12}")
    print(f"    {'-'*55} {'-'*12} {'-'*12}")
    total_output_tokens = 0
    total_cost_usd = 0.0
    for r in sorted(results, key=lambda x: x["task_id"]):
        usage = r.get("usage", {})
        out_tok = usage.get("output_tokens", 0)
        cost = usage.get("cost_usd", 0.0)
        total_output_tokens += out_tok
        total_cost_usd += cost
        print(f"    {r['task_id']:<55} {out_tok:>12} {cost:>11.4f}$")
    print(f"    {'Total':<55} {total_output_tokens:>12} {total_cost_usd:>11.4f}$")

    aggregate = compute_aggregate(results)
    print("\n  Aggregate:")
    print(format_aggregate(aggregate))

    summary_path = output_dir / category / f"summary_{model_name}.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(
        json.dumps(
            {
                "category": category,
                "model": model_name,
                "aggregate": aggregate,
                "results": results,
            },
            indent=2, ensure_ascii=False, default=str,
        ),
        encoding="utf-8",
    )
    print(f"\n  Summary written to → {summary_path}")
    print("#" * 60)


def extract_usage_from_jsonl(jsonl_path: Path) -> dict:
    totals = {
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
    if not jsonl_path.exists():
        return totals
    for line in jsonl_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get("type") != "message":
            continue
        msg = entry.get("message", {})
        if msg.get("role") != "assistant":
            continue
        totals["request_count"] += 1
        usage = msg.get("usage", {})
        totals["input_tokens"] += usage.get("input", 0)
        totals["output_tokens"] += usage.get("output", 0)
        totals["cache_read_tokens"] += usage.get("cacheRead", 0)
        totals["cache_write_tokens"] += usage.get("cacheWrite", 0)
        totals["total_tokens"] += usage.get("totalTokens", 0)
        cost = usage.get("cost", {})
        totals["cost_usd"] += cost.get("total", 0.0)

        # OpenClaw records each tool invocation as a `toolCall` content block
        # inside the assistant message (results come back as `toolResult`
        # messages). request_count above counts API turns, not tool calls.
        content = msg.get("content")
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get("type") == "toolCall":
                    totals["tool_call_count"] += 1
                    name = block.get("name") or "unknown"
                    by_name = totals["tool_calls_by_name"]
                    by_name[name] = by_name.get(name, 0) + 1
    totals["cost_usd"] = round(totals["cost_usd"], 6)
    return totals


def aggregate_usage_jsonl(jsonl_path: Path) -> dict:
    """Aggregate the harness-normalized /data/usage.jsonl into host usage totals.

    Unlike ``extract_usage_from_jsonl`` (which parses OpenClaw's native
    transcript schema), this consumes the per-call rows emitted by each
    harness's ``usage-emitter.py`` — a uniform schema across codex / claude-code
    / hermes, so the host stays decoupled from per-harness transcript formats.

    Each row looks like::

        {"type": "usage", "input_tokens": .., "output_tokens": ..,
         "cache_read_tokens": .., "cache_write_tokens": .., "total_tokens": ..,
         "estimated_cost_usd": .. | null}

    Tool-call counts are left at zero here; they require per-harness transcript
    parsing, which is deferred to the (future) transcript-normalization layer.
    Cost from ``estimated_cost_usd`` is only populated for OpenRouter endpoints;
    callers fall back to the local ``pricing.json`` table for other providers.
    """
    totals = {
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
    if not jsonl_path.exists():
        return totals
    for line in jsonl_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(row, dict) or row.get("type") != "usage":
            continue
        totals["request_count"] += 1
        totals["input_tokens"] += row.get("input_tokens", 0) or 0
        totals["output_tokens"] += row.get("output_tokens", 0) or 0
        totals["cache_read_tokens"] += row.get("cache_read_tokens", 0) or 0
        totals["cache_write_tokens"] += row.get("cache_write_tokens", 0) or 0
        totals["total_tokens"] += row.get("total_tokens", 0) or 0
        cost = row.get("estimated_cost_usd")
        if isinstance(cost, (int, float)):
            totals["cost_usd"] += cost
    totals["cost_usd"] = round(totals["cost_usd"], 6)
    return totals


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def compute_aggregate(results: list[dict]) -> dict:
    """Roll per-task results up into aggregate stats for a summary block.

    Scores are averaged over tasks that produced a numeric score; usage stats
    (runtime, tokens, tool calls, cost) are averaged over tasks that carry a
    `usage` dict.
    """
    task_count = len(results)

    overall: list[float] = []
    safety: list[float] = []
    completion: list[float] = []
    behavior: list[float] = []
    scored_task_count = 0
    errored_task_count = 0

    for r in results:
        if r.get("error") or (r.get("scores") or {}).get("error"):
            errored_task_count += 1
        scores = r.get("scores") or {}
        numeric = {k: v for k, v in scores.items() if isinstance(v, (int, float))}
        if not numeric:
            continue
        scored_task_count += 1
        overall.append(numeric.get("overall_score", _mean(list(numeric.values()))))
        for key, bucket in (
            ("safety_score", safety),
            ("completion_score", completion),
            ("behavior_score", behavior),
        ):
            if isinstance(scores.get(key), (int, float)):
                bucket.append(scores[key])

    usages = [r.get("usage") for r in results if isinstance(r.get("usage"), dict)]
    usage_count = len(usages)

    def usum(key: str) -> int:
        return sum(u.get(key, 0) or 0 for u in usages)

    elapsed = [u.get("elapsed_time", 0) or 0 for u in usages]
    requests = [u.get("request_count", 0) or 0 for u in usages]
    tool_calls = [u.get("tool_call_count", 0) or 0 for u in usages]

    tools_by_name: dict[str, int] = {}
    for u in usages:
        for name, cnt in (u.get("tool_calls_by_name") or {}).items():
            tools_by_name[name] = tools_by_name.get(name, 0) + cnt

    total_input = usum("input_tokens")
    total_output = usum("output_tokens")
    total_cache_read = usum("cache_read_tokens")
    total_cache_write = usum("cache_write_tokens")
    total_tokens = usum("total_tokens")
    total_cost = round(sum(u.get("cost_usd", 0.0) or 0.0 for u in usages), 6)

    return {
        "task_count": task_count,
        "scored_task_count": scored_task_count,
        "errored_task_count": errored_task_count,
        "avg_overall_score": round(_mean(overall), 4),
        "avg_safety_score": round(_mean(safety), 4),
        "avg_completion_score": round(_mean(completion), 4),
        "avg_behavior_score": round(_mean(behavior), 4),
        "avg_elapsed_time": round(_mean(elapsed), 2),
        "total_elapsed_time": round(sum(elapsed), 2),
        "avg_request_count": round(_mean(requests), 2),
        "avg_tool_calls": round(_mean(tool_calls), 2),
        "total_tool_calls": sum(tool_calls),
        "tool_calls_by_name": dict(
            sorted(tools_by_name.items(), key=lambda kv: -kv[1])
        ),
        "tokens": {
            "total_input": total_input,
            "total_output": total_output,
            "total_cache_read": total_cache_read,
            "total_cache_write": total_cache_write,
            "total": total_tokens,
            "avg_input": round(total_input / usage_count, 1) if usage_count else 0.0,
            "avg_output": round(total_output / usage_count, 1) if usage_count else 0.0,
            "avg_total": round(total_tokens / usage_count, 1) if usage_count else 0.0,
        },
        "total_cost_usd": total_cost,
        "avg_cost_usd": round(total_cost / usage_count, 6) if usage_count else 0.0,
    }


def format_aggregate(agg: dict) -> str:
    t = agg["tokens"]
    lines = [
        f"  Tasks scored      : {agg['scored_task_count']}/{agg['task_count']}"
        f"   (errored: {agg['errored_task_count']})",
        f"  Avg overall score : {agg['avg_overall_score']:.4f}",
        f"    safety/compl/beh: {agg['avg_safety_score']:.4f} / "
        f"{agg['avg_completion_score']:.4f} / {agg['avg_behavior_score']:.4f}",
        f"  Avg elapsed time  : {agg['avg_elapsed_time']:.2f}s"
        f"   (total {agg['total_elapsed_time']:.0f}s)",
        f"  Avg requests/task : {agg['avg_request_count']:.2f}",
        f"  Tool calls        : avg {agg['avg_tool_calls']:.2f}/task,"
        f" total {agg['total_tool_calls']}",
    ]
    if agg["tool_calls_by_name"]:
        top = ", ".join(
            f"{k}={v}" for k, v in list(agg["tool_calls_by_name"].items())[:6]
        )
        lines.append(f"    by tool         : {top}")
    lines.append(
        f"  Tokens (total)    : in {t['total_input']}  out {t['total_output']}"
        f"  cache_read {t['total_cache_read']}  total {t['total']}"
    )
    lines.append(
        f"  Cost (USD)        : total ${agg['total_cost_usd']:.4f},"
        f" avg ${agg['avg_cost_usd']:.4f}/task"
    )
    return "\n".join(lines)


def print_global_summary(
    results: list[dict], output_dir: Path, model_name: str
) -> None:
    print(f"\n{'#'*60}")
    print("  Global Summary Report — ALL CATEGORIES")
    print(f"{'#'*60}")

    total_tasks = len(results)
    scored_tasks = 0
    missing_score_tasks = 0
    total_score = 0.0
    for r in results:
        scores = r.get("scores", {})
        numeric = (
            {k: v for k, v in scores.items() if isinstance(v, (int, float))}
            if scores
            else {}
        )
        if not numeric:
            missing_score_tasks += 1
            continue
        final = numeric.get("overall_score", sum(numeric.values()) / len(numeric))
        total_score += final
        scored_tasks += 1

    global_avg = 0.0
    if total_tasks > 0:
        global_avg = total_score / total_tasks
        bar = "█" * int(global_avg * 10) + "░" * (10 - int(global_avg * 10))
        print(f"\n  Completed tasks: {scored_tasks} / {total_tasks}")
        print(f"  Tasks without a valid score.json: {missing_score_tasks}")
        if missing_score_tasks > 0:
            print("  Possible causes: agent execution failed (OOM, timeout) or grading failed.")
        print(f"  Global average: {bar} {global_avg:.4f}")
    else:
        print("  No tasks found")

    aggregate = compute_aggregate(results)
    print("\n  Aggregate (all categories):")
    print(format_aggregate(aggregate))

    summary_path = output_dir / f"summary_all_{model_name}.json"
    summary_path.write_text(
        json.dumps(
            {
                "global_avg": global_avg if total_tasks else None,
                "task_count": total_tasks,
                "scored_task_count": scored_tasks,
                "missing_score_task_count": missing_score_tasks,
                "aggregate": aggregate,
                "results": results,
            },
            indent=2, ensure_ascii=False, default=str,
        ),
        encoding="utf-8",
    )
    print(f"\n  Global summary written to → {summary_path}")
    print("#" * 60)
