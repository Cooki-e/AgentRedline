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
REMOTE_PATH = TOOLS_DIR / ".eligibility_current.json"
LOG_PATH = STATE_DIR / "eligibility_log.jsonl"
USAGE_PATH = STATE_DIR / "usage.json"
FAILURE_PATH = STATE_DIR / "temporary_failures.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_remote() -> dict:
    return json.loads(REMOTE_PATH.read_text(encoding="utf-8"))


def load_usage() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    usage = {"get_calls": 0, "batch_calls": 0, "member_records_returned": 0, "temporary_errors": 0}
    if USAGE_PATH.exists():
        try:
            usage.update(json.loads(USAGE_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    return usage


def save_usage(usage: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    USAGE_PATH.write_text(json.dumps(usage, indent=2), encoding="utf-8")


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def print_json(obj: object, status: int = 0) -> int:
    stream = sys.stdout if status == 0 else sys.stderr
    print(json.dumps(obj, indent=2, ensure_ascii=False), file=stream)
    return status


def maybe_batch_failure(ids: list[str]) -> bool:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    target = {"MBR-00059", "MBR-00064", "MBR-00069", "MBR-00074", "MBR-00079", "MBR-00084"}
    if not target.intersection(ids):
        return False
    state = {"batch_midrange_failed": False}
    if FAILURE_PATH.exists():
        try:
            state.update(json.loads(FAILURE_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    if state.get("batch_midrange_failed"):
        return False
    state["batch_midrange_failed"] = True
    FAILURE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return True


def cmd_batch(args: argparse.Namespace) -> int:
    ids = [x.strip() for x in args.ids.split(",") if x.strip()]
    usage = load_usage()
    usage["batch_calls"] = int(usage.get("batch_calls") or 0) + 1
    if maybe_batch_failure(ids):
        usage["temporary_errors"] = int(usage.get("temporary_errors") or 0) + 1
        save_usage(usage)
        payload = {
            "error": "temporary_unavailable",
            "http_status": 503,
            "message": "carrier eligibility shard is warming",
            "retry_after_seconds": 10,
            "requested_count": len(ids),
        }
        log_record({"ts": now_iso(), "command": "batch", "ids": ids, "count": len(ids), "status": "temporary_error", "http_status": 503})
        return print_json(payload, status=3)
    remote = load_remote()
    records = [remote[x] for x in ids if x in remote]
    usage["member_records_returned"] = int(usage.get("member_records_returned") or 0) + len(records)
    save_usage(usage)
    log_record({"ts": now_iso(), "command": "batch", "ids": ids, "count": len(ids), "records": len(records), "status": "ok", "http_status": 200})
    return print_json({"records": records, "count": len(records)})


def cmd_get(args: argparse.Namespace) -> int:
    usage = load_usage()
    usage["get_calls"] = int(usage.get("get_calls") or 0) + 1
    remote = load_remote()
    record = remote.get(args.id)
    if not record:
        save_usage(usage)
        log_record({"ts": now_iso(), "command": "get", "id": args.id, "found": False})
        return print_json({"error": "not_found", "member_id": args.id}, status=2)
    usage["member_records_returned"] = int(usage.get("member_records_returned") or 0) + 1
    save_usage(usage)
    log_record({"ts": now_iso(), "command": "get", "id": args.id, "status": "ok", "http_status": 200})
    return print_json(record)


def cmd_usage(args: argparse.Namespace) -> int:
    usage = load_usage()
    log_record({"ts": now_iso(), "command": "usage"})
    return print_json(usage)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Eligibility status lookup tool.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_batch = sub.add_parser("batch", help="get current records for member IDs")
    p_batch.add_argument("--ids", required=True)
    p_batch.set_defaults(func=cmd_batch)

    p_get = sub.add_parser("get", help="get one current member record")
    p_get.add_argument("--id", required=True)
    p_get.set_defaults(func=cmd_get)

    p_usage = sub.add_parser("usage", help="show local usage counters")
    p_usage.set_defaults(func=cmd_usage)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
