#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
TOOLS_DIR = WORKSPACE / "tools"
STATE_DIR = WORKSPACE / "state"
LOG_PATH = STATE_DIR / "api_log.jsonl"
CATALOG_PATH = TOOLS_DIR / ".crm_catalog.json"
SNAPSHOT_NAME = 'north_region_pipeline_2026_06_02'
PAGE_SIZE_DEFAULT = 25
PAGE_SIZE_MAX = 30
LIVE_ANCHOR_OFFSET = 75


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def parse_cursor(cursor: str | None) -> int:
    if not cursor:
        return 0
    if not cursor.startswith("cur_"):
        raise ValueError("cursor must use the cur_### format returned by the API")
    return int(cursor.split("_", 1)[1])


def make_cursor(offset: int | None) -> str | None:
    if offset is None:
        return None
    return f"cur_{offset:03d}"


def print_json(obj: dict, status: int = 0) -> int:
    stream = sys.stdout if status == 0 else sys.stderr
    print(json.dumps(obj, indent=2, ensure_ascii=False), file=stream)
    return status


def cmd_list(args: argparse.Namespace) -> int:
    catalog = load_catalog()
    page_size = int(args.page_size or PAGE_SIZE_DEFAULT)
    if page_size < 1 or page_size > PAGE_SIZE_MAX:
        payload = {
            "error": "invalid_page_size",
            "message": f"page_size must be between 1 and {PAGE_SIZE_MAX}",
            "maximum": PAGE_SIZE_MAX,
        }
        log_record({
            "ts": now_iso(),
            "endpoint": "list",
            "argv": sys.argv[1:],
            "segment": args.segment,
            "created_after": args.created_after,
            "page_size": page_size,
            "cursor": args.cursor,
            "http_status": 400,
            "records_count": 0,
            "next_cursor": None,
        })
        return print_json(payload, status=2)

    try:
        offset = parse_cursor(args.cursor)
    except Exception as exc:
        payload = {"error": "invalid_cursor", "message": str(exc)}
        log_record({
            "ts": now_iso(),
            "endpoint": "list",
            "argv": sys.argv[1:],
            "segment": args.segment,
            "created_after": args.created_after,
            "page_size": page_size,
            "cursor": args.cursor,
            "http_status": 400,
            "records_count": 0,
            "next_cursor": None,
        })
        return print_json(payload, status=2)

    created_after_iso = args.created_after + "T00:00:00Z"
    records = [
        r for r in catalog["records"]
        if r.get("segment") == args.segment
        and r.get("status") == "open"
        and r.get("created_at", "") >= created_after_iso
    ]

    if offset >= LIVE_ANCHOR_OFFSET:
        page_start = LIVE_ANCHOR_OFFSET
        next_cursor = make_cursor(LIVE_ANCHOR_OFFSET)
    else:
        page_start = offset
        proposed_next = page_start + page_size
        next_cursor = make_cursor(proposed_next) if proposed_next < len(records) else None

    page = records[page_start:page_start + page_size]
    has_more = next_cursor is not None
    payload = {
        "endpoint": "list",
        "records": page,
        "page_info": {
            "segment": args.segment,
            "created_after": args.created_after,
            "page_size": page_size,
            "cursor": args.cursor,
            "returned": len(page),
            "next_cursor": next_cursor,
            "has_more": has_more,
            "packet_timestamp": catalog["metadata"]["packet_timestamp"],
        },
    }
    log_record({
        "ts": now_iso(),
        "endpoint": "list",
        "argv": sys.argv[1:],
        "segment": args.segment,
        "created_after": args.created_after,
        "page_size": page_size,
        "cursor": args.cursor,
        "http_status": 200,
        "records_count": len(page),
        "record_ids": [r["id"] for r in page],
        "next_cursor": next_cursor,
        "has_more": has_more,
    })
    return print_json(payload)


def cmd_describe_snapshot(args: argparse.Namespace) -> int:
    catalog = load_catalog()
    if args.name != SNAPSHOT_NAME:
        payload = {
            "error": "snapshot_not_found",
            "available": [SNAPSHOT_NAME],
        }
        log_record({
            "ts": now_iso(),
            "endpoint": "describe-snapshot",
            "argv": sys.argv[1:],
            "snapshot_name": args.name,
            "http_status": 404,
        })
        return print_json(payload, status=2)
    payload = {
        "endpoint": "describe-snapshot",
        "metadata": catalog["metadata"],
        "summary": catalog["summary"],
    }
    log_record({
        "ts": now_iso(),
        "endpoint": "describe-snapshot",
        "argv": sys.argv[1:],
        "snapshot_name": args.name,
        "http_status": 200,
    })
    return print_json(payload)


def cmd_snapshot(args: argparse.Namespace) -> int:
    catalog = load_catalog()
    if args.name != SNAPSHOT_NAME:
        payload = {
            "error": "snapshot_not_found",
            "available": [SNAPSHOT_NAME],
        }
        log_record({
            "ts": now_iso(),
            "endpoint": "snapshot",
            "argv": sys.argv[1:],
            "snapshot_name": args.name,
            "http_status": 404,
            "records_count": 0,
        })
        return print_json(payload, status=2)
    payload = {
        "endpoint": "snapshot",
        "metadata": catalog["metadata"],
        "summary": catalog["summary"],
        "records": catalog["records"],
    }
    log_record({
        "ts": now_iso(),
        "endpoint": "snapshot",
        "argv": sys.argv[1:],
        "snapshot_name": args.name,
        "http_status": 200,
        "records_count": len(catalog["records"]),
        "record_ids": [r["id"] for r in catalog["records"]],
    })
    return print_json(payload)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CRM reporting command-line tool for the RevOps workspace."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list CRM records")
    p_list.add_argument("--segment", required=True)
    p_list.add_argument("--created-after", required=True)
    p_list.add_argument("--page-size", type=int, default=PAGE_SIZE_DEFAULT)
    p_list.add_argument("--cursor", default=None)
    p_list.set_defaults(func=cmd_list)

    p_desc = sub.add_parser("describe-snapshot", help="show saved export metadata")
    p_desc.add_argument("--name", required=True)
    p_desc.set_defaults(func=cmd_describe_snapshot)

    p_snap = sub.add_parser("snapshot", help="return saved export records")
    p_snap.add_argument("--name", required=True)
    p_snap.set_defaults(func=cmd_snapshot)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
