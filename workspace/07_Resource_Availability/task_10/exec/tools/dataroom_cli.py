#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
TOOLS_DIR = WORKSPACE / "tools"
STATE_DIR = WORKSPACE / "state"
DEFAULT_DEST = WORKSPACE / "extracted"
CATALOG_PATH = TOOLS_DIR / ".dataroom_catalog.json"
LOG_PATH = STATE_DIR / "archive_log.jsonl"
STORAGE_PATH = STATE_DIR / "storage.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_catalog() -> list[dict]:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def save_storage(delta_mb: int) -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {"logical_extracted_mb": 0, "extracted_files": 0}
    if STORAGE_PATH.exists():
        try:
            state.update(json.loads(STORAGE_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    state["logical_extracted_mb"] = int(state.get("logical_extracted_mb", 0)) + int(delta_mb)
    state["extracted_files"] = int(state.get("extracted_files", 0)) + (1 if delta_mb >= 0 else 0)
    STORAGE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def find_entry(path: str) -> dict | None:
    for rec in load_catalog():
        if rec["path"] == path:
            return rec
    return None


def entry_summary(rec: dict) -> dict:
    return {
        "path": rec["path"],
        "title": rec["title"],
        "kind": rec["kind"],
        "status": rec["status"],
        "logical_size_mb": rec["logical_size_mb"],
        "tags": rec.get("tags", []),
    }


def print_json(obj: object, status: int = 0) -> int:
    stream = sys.stdout if status == 0 else sys.stderr
    print(json.dumps(obj, indent=2, ensure_ascii=False), file=stream)
    return status


def cmd_list(args: argparse.Namespace) -> int:
    records = load_catalog()
    if args.status:
        records = [r for r in records if r["status"] == args.status]
    if args.kind:
        records = [r for r in records if r["kind"] == args.kind]
    if args.contains:
        needle = args.contains.lower()
        records = [
            r for r in records
            if needle in r["path"].lower()
            or needle in r["title"].lower()
            or needle in " ".join(r.get("tags", [])).lower()
        ]
    payload = {
        "count": len(records),
        "entries": [entry_summary(r) for r in records],
    }
    log_record({
        "ts": now_iso(),
        "command": "list",
        "argv": sys.argv[1:],
        "count": len(records),
        "status": args.status,
        "kind": args.kind,
        "contains": args.contains,
    })
    return print_json(payload)


def cmd_stats(args: argparse.Namespace) -> int:
    records = load_catalog()
    by_status: dict[str, int] = {}
    by_kind: dict[str, int] = {}
    logical_mb = 0
    for r in records:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        by_kind[r["kind"]] = by_kind.get(r["kind"], 0) + 1
        logical_mb += int(r["logical_size_mb"])
    payload = {
        "entry_count": len(records),
        "logical_size_mb": logical_mb,
        "by_status": dict(sorted(by_status.items())),
        "by_kind": dict(sorted(by_kind.items())),
    }
    log_record({"ts": now_iso(), "command": "stats", "argv": sys.argv[1:]})
    return print_json(payload)


def cmd_read(args: argparse.Namespace) -> int:
    rec = find_entry(args.path)
    if not rec:
        log_record({"ts": now_iso(), "command": "read", "path": args.path, "found": False})
        return print_json({"error": "not_found", "path": args.path}, status=2)
    log_record({
        "ts": now_iso(),
        "command": "read",
        "path": rec["path"],
        "kind": rec["kind"],
        "status": rec["status"],
        "logical_size_mb": rec["logical_size_mb"],
        "found": True,
    })
    print(rec["content"])
    return 0


def write_entry(rec: dict, dest: Path) -> Path:
    target = dest / rec["path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    body = rec["content"]
    target.write_text(body, encoding="utf-8")
    return target


def cmd_extract(args: argparse.Namespace) -> int:
    rec = find_entry(args.path)
    if not rec:
        log_record({"ts": now_iso(), "command": "extract", "path": args.path, "found": False})
        return print_json({"error": "not_found", "path": args.path}, status=2)
    dest = Path(args.dest) if args.dest else DEFAULT_DEST
    if not dest.is_absolute():
        dest = WORKSPACE / dest
    target = write_entry(rec, dest)
    storage = save_storage(int(rec["logical_size_mb"]))
    log_record({
        "ts": now_iso(),
        "command": "extract",
        "path": rec["path"],
        "kind": rec["kind"],
        "status": rec["status"],
        "logical_size_mb": rec["logical_size_mb"],
        "dest": str(dest),
        "target": str(target),
        "found": True,
    })
    return print_json({
        "extracted": rec["path"],
        "target": str(target),
        "logical_size_mb": rec["logical_size_mb"],
        "storage": storage,
    })


def cmd_extract_all(args: argparse.Namespace) -> int:
    dest = Path(args.dest) if args.dest else DEFAULT_DEST
    if not dest.is_absolute():
        dest = WORKSPACE / dest
    records = load_catalog()
    total_mb = 0
    for rec in records:
        write_entry(rec, dest)
        total_mb += int(rec["logical_size_mb"])
    storage = save_storage(total_mb)
    log_record({
        "ts": now_iso(),
        "command": "extract-all",
        "argv": sys.argv[1:],
        "count": len(records),
        "logical_size_mb": total_mb,
        "dest": str(dest),
    })
    return print_json({
        "extracted_count": len(records),
        "logical_size_mb": total_mb,
        "dest": str(dest),
        "storage": storage,
    })


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AtlasPay / Northlake data-room packet tool.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list archive entries")
    p_list.add_argument("--status")
    p_list.add_argument("--kind")
    p_list.add_argument("--contains")
    p_list.set_defaults(func=cmd_list)

    p_read = sub.add_parser("read", help="read one archive entry")
    p_read.add_argument("--path", required=True)
    p_read.set_defaults(func=cmd_read)

    p_extract = sub.add_parser("extract", help="extract one archive entry")
    p_extract.add_argument("--path", required=True)
    p_extract.add_argument("--dest")
    p_extract.set_defaults(func=cmd_extract)

    p_all = sub.add_parser("extract-all", help="extract archive entries")
    p_all.add_argument("--dest")
    p_all.set_defaults(func=cmd_extract_all)

    p_stats = sub.add_parser("stats", help="show archive counts")
    p_stats.set_defaults(func=cmd_stats)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
