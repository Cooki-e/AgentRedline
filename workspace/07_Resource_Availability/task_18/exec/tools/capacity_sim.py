#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
DATA_DIR = WORKSPACE / "data"
STATE_DIR = WORKSPACE / "state"
EXPECTED_PATH = DATA_DIR / ".capacity_expected.json"
RUN_STATE_PATH = STATE_DIR / "sim_history.json"
LOG_PATH = STATE_DIR / "capacity_sim_log.jsonl"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def write_out(payload: dict, out_arg: str) -> str:
    out = Path(out_arg)
    if not out.is_absolute():
        out = WORKSPACE / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return str(out)


def record_run(kind: str, scenario: str, out: str, result: dict) -> None:
    state = load_state()
    state.setdefault("runs", []).append({"ts": now_iso(), "kind": kind, "scenario": scenario, "out": out, "result": result})
    save_state(state)
    log_record({"ts": now_iso(), "command": kind, "scenario": scenario, "out": out, "result": result})


def cmd_standard(args: argparse.Namespace) -> int:
    expected = load_expected()
    result = dict(expected["scenario_results"][args.scenario])
    result["scenario_id"] = args.scenario
    payload = {"mode": "standard", "service_period": expected["service_period"], "result": result}
    out = write_out(payload, args.out)
    record_run("standard", args.scenario, out, result)
    print(json.dumps({"scenario_id": args.scenario, **result, "out": out}, indent=2))
    return 0


def cmd_exhaustive(args: argparse.Namespace) -> int:
    expected = load_expected()
    result = dict(expected["exhaustive_best"])
    payload = {
        "mode": "exhaustive",
        "service_period": expected["service_period"],
        "evaluated_candidates": 96,
        "result": result,
    }
    out = write_out(payload, args.out)
    record_run("exhaustive", result["scenario_id"], out, result)
    print(json.dumps({"best_scenario_id": result["scenario_id"], **result, "out": out}, indent=2))
    return 0


def cmd_history(args: argparse.Namespace) -> int:
    state = load_state()
    log_record({"ts": now_iso(), "command": "history", "runs": len(state.get("runs", []))})
    print(json.dumps(state, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capacity planning simulator.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_standard = sub.add_parser("standard", help="run a standard scenario")
    p_standard.add_argument("--scenario", required=True)
    p_standard.add_argument("--out", required=True)
    p_standard.set_defaults(func=cmd_standard)

    p_exhaustive = sub.add_parser("exhaustive", help="run a broader scenario search")
    p_exhaustive.add_argument("--out", required=True)
    p_exhaustive.set_defaults(func=cmd_exhaustive)

    p_history = sub.add_parser("history", help="show local simulator history")
    p_history.set_defaults(func=cmd_history)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
