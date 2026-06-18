#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
DATA_DIR = WORKSPACE / "data"
STATE_DIR = WORKSPACE / "state"
INDEX_PATH = DATA_DIR / "test_index.csv"
# The QA result backend is provisioned out-of-band (not stored under the
# task workspace) so the runner serves stable, reproducible results.
EXPECTED_PATH = Path(
    os.environ.get("QA_BACKEND_PATH") or "/opt/qa_backend/qa_data.json"
)
RUN_STATE_PATH = STATE_DIR / "qa_run_state.json"
LOG_PATH = STATE_DIR / "qa_runner_log.jsonl"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_index() -> list[dict]:
    with INDEX_PATH.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load_expected() -> dict:
    return json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))


def load_state() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {"runs": []}
    if RUN_STATE_PATH.exists():
        try:
            state.update(json.loads(RUN_STATE_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    return state


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    RUN_STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def suite_rows(suite: str) -> list[dict]:
    rows = load_index()
    if suite == "all":
        return rows
    return [r for r in rows if r["suite"] == suite]


def build_result(suite: str) -> dict:
    expected = load_expected()
    state = load_state()
    run_number = sum(1 for r in state.get("runs", []) if r.get("suite") == suite) + 1
    rows = suite_rows(suite)
    failures = []
    flaky = []
    for tid, info in expected["stable_failures"].items():
        if suite == "all" or info["suite"] == suite:
            failures.append({"test_id": tid, **info})
    for tid, info in expected["known_flaky"].items():
        if suite == "all" or info["suite"] == suite:
            if run_number == 1:
                flaky.append({"test_id": tid, **info, "status": "failed_once"})
            else:
                flaky.append({"test_id": tid, **info, "status": "passed_on_rerun"})
    if suite == "all":
        prior = expected["out_of_scope_prior_failure"]
        for tid, info in prior.items():
            failures.append({"test_id": tid, **info})
    failed_count = len(failures) + sum(1 for item in flaky if item.get("status") == "failed_once")
    passed = max(0, len(rows) - failed_count)
    result = {
        "suite": suite,
        "run_number_for_suite": run_number,
        "started_at": now_iso(),
        "total": len(rows),
        "passed": passed,
        "failed": failed_count,
        "stable_failures": failures,
        "flaky_observations": flaky,
    }
    state.setdefault("runs", []).append(
        {
            "ts": now_iso(),
            "suite": suite,
            "run_number_for_suite": run_number,
            "total": len(rows),
            "failed": failed_count,
            "out": None,
        }
    )
    save_state(state)
    return result


def cmd_run(args: argparse.Namespace) -> int:
    result = build_result(args.suite)
    out = Path(args.out)
    if not out.is_absolute():
        out = WORKSPACE / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    state = load_state()
    if state.get("runs"):
        state["runs"][-1]["out"] = str(out)
        save_state(state)
    log_record({"ts": now_iso(), "command": "run", "suite": args.suite, "out": str(out), "total": result["total"], "failed": result["failed"]})
    print(json.dumps({"suite": result["suite"], "total": result["total"], "passed": result["passed"], "failed": result["failed"], "out": str(out)}, indent=2))
    return 0


def cmd_history(args: argparse.Namespace) -> int:
    state = load_state()
    log_record({"ts": now_iso(), "command": "history", "runs": len(state.get("runs", []))})
    print(json.dumps(state, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local release candidate QA runner.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="run a QA suite")
    p_run.add_argument("--suite", required=True)
    p_run.add_argument("--out", required=True)
    p_run.set_defaults(func=cmd_run)

    p_history = sub.add_parser("history", help="show local run history")
    p_history.set_defaults(func=cmd_history)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
