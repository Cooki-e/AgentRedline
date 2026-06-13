#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
TOOLS_DIR = WORKSPACE / "tools"
STATE_DIR = WORKSPACE / "state"
PLAN_LIBRARY = TOOLS_DIR / ".planner_scenarios.json"
RUN_STATE = STATE_DIR / "planner_state.json"
LOG_PATH = STATE_DIR / "planner_log.jsonl"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_library() -> list[dict]:
    return json.loads(PLAN_LIBRARY.read_text(encoding="utf-8"))


def load_state() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    if RUN_STATE.exists():
        try:
            return json.loads(RUN_STATE.read_text(encoding="utf-8"))
        except Exception:
            return {"next_index": 0, "generated": []}
    return {"next_index": 0, "generated": []}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    RUN_STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def print_json(obj: object, status: int = 0) -> int:
    stream = sys.stdout if status == 0 else sys.stderr
    print(json.dumps(obj, indent=2, ensure_ascii=False), file=stream)
    return status


def scenario_digest(plan: dict) -> dict:
    metrics = plan["metrics"]
    return {
        "scenario_id": plan["scenario_id"],
        "assigned_stops": metrics["assigned_stops"],
        "unassigned_stops": metrics["unassigned_stops"],
        "on_time_percent": metrics["on_time_percent"],
        "priority_a_on_time_percent": metrics["priority_a_on_time_percent"],
        "total_miles": metrics["total_miles"],
        "overtime_minutes": metrics["overtime_minutes"],
        "capacity_violations": metrics["capacity_violations"],
        "skill_mismatches": metrics["skill_mismatches"],
        "late_stops": metrics["late_stops"],
        "score": metrics["score"],
        "engine_note": metrics["engine_note"],
    }


def cmd_propose(args: argparse.Namespace) -> int:
    library = load_library()
    state = load_state()
    idx = int(state.get("next_index") or 0)
    if idx >= len(library):
        idx = len(library) - 1
    plan = dict(library[idx])
    plan["request"] = {"date": args.date, "region": args.region}
    out = Path(args.out)
    if not out.is_absolute():
        out = WORKSPACE / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(plan, indent=2), encoding="utf-8")
    state["next_index"] = min(idx + 1, len(library))
    state.setdefault("generated", []).append(
        {
            "ts": now_iso(),
            "scenario_id": plan["scenario_id"],
            "out": str(out),
            "metrics": scenario_digest(plan),
        }
    )
    save_state(state)
    log_record({"ts": now_iso(), "command": "propose", "scenario_id": plan["scenario_id"], "out": str(out), "metrics": scenario_digest(plan)})
    return print_json(scenario_digest(plan))


def cmd_show(args: argparse.Namespace) -> int:
    library = load_library()
    state = load_state()
    generated = {item["scenario_id"] for item in state.get("generated", [])}
    for plan in library:
        if plan["scenario_id"] == args.scenario_id and args.scenario_id in generated:
            log_record({"ts": now_iso(), "command": "show", "scenario_id": args.scenario_id})
            return print_json(plan)
    log_record({"ts": now_iso(), "command": "show", "scenario_id": args.scenario_id, "found": False})
    return print_json({"error": "scenario_not_found", "scenario_id": args.scenario_id}, status=2)


def cmd_history(args: argparse.Namespace) -> int:
    state = load_state()
    log_record({"ts": now_iso(), "command": "history", "count": len(state.get("generated", []))})
    return print_json({"generated": state.get("generated", [])})


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Metro dispatch route planning tool.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_propose = sub.add_parser("propose", help="build a candidate route plan")
    p_propose.add_argument("--date", required=True)
    p_propose.add_argument("--region", required=True)
    p_propose.add_argument("--out", required=True)
    p_propose.set_defaults(func=cmd_propose)

    p_show = sub.add_parser("show", help="show a generated scenario")
    p_show.add_argument("--scenario-id", required=True)
    p_show.set_defaults(func=cmd_show)

    p_history = sub.add_parser("history", help="show generated scenario history")
    p_history.set_defaults(func=cmd_history)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
