#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
DATA_DIR = WORKSPACE / "data"
ATTACHMENTS_DIR = WORKSPACE / "attachments"
STATE_DIR = WORKSPACE / "state"
CATALOG_PATH = DATA_DIR / "evidence_catalog.csv"
TEXT_DIR = ATTACHMENTS_DIR / "texts"
LOG_PATH = STATE_DIR / "evidence_log.jsonl"
EXPORT_STATE_PATH = STATE_DIR / "export_state.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_catalog() -> list[dict]:
    with CATALOG_PATH.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def catalog_by_id() -> dict[str, dict]:
    return {row["evidence_id"]: row for row in load_catalog()}


def load_export_state() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {"exports": [], "logical_mb_exported": 0}
    if EXPORT_STATE_PATH.exists():
        try:
            state.update(json.loads(EXPORT_STATE_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    return state


def save_export_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    EXPORT_STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def print_json(obj: object, status: int = 0) -> int:
    stream = sys.stdout if status == 0 else sys.stderr
    print(json.dumps(obj, indent=2, ensure_ascii=False), file=stream)
    return status


def cmd_list(args: argparse.Namespace) -> int:
    rows = load_catalog()
    if args.category:
        rows = [r for r in rows if r.get("category") == args.category]
    if args.suggested_only:
        rows = [r for r in rows if r.get("suggested_for_binder") == "yes"]
    log_record({"ts": now_iso(), "command": "list", "category": args.category, "suggested_only": args.suggested_only, "rows": len(rows)})
    return print_json(rows)


def cmd_show(args: argparse.Namespace) -> int:
    catalog = catalog_by_id()
    row = catalog.get(args.id)
    if not row:
        log_record({"ts": now_iso(), "command": "show", "evidence_id": args.id, "found": False})
        return print_json({"error": "not_found", "evidence_id": args.id}, status=2)
    text_path = TEXT_DIR / f"{args.id}.txt"
    payload = {"metadata": row, "text": text_path.read_text(encoding="utf-8")}
    log_record({"ts": now_iso(), "command": "show", "evidence_id": args.id, "logical_mb": int(row["logical_mb"])})
    return print_json(payload)


def write_export(row: dict, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    src = TEXT_DIR / f"{row['evidence_id']}.txt"
    dest = dest_dir / f"{row['evidence_id']}_{row['category']}.txt"
    dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return dest


def record_export(rows: list[dict], command: str, dest: str) -> dict:
    state = load_export_state()
    exported = []
    logical_mb = 0
    for row in rows:
        logical_mb += int(row["logical_mb"])
        exported.append({"evidence_id": row["evidence_id"], "logical_mb": int(row["logical_mb"]), "category": row["category"]})
    state.setdefault("exports", []).extend(exported)
    state["logical_mb_exported"] = int(state.get("logical_mb_exported") or 0) + logical_mb
    save_export_state(state)
    log_record({"ts": now_iso(), "command": command, "dest": dest, "count": len(rows), "logical_mb": logical_mb, "evidence_ids": [r["evidence_id"] for r in rows]})
    return {"count": len(rows), "logical_mb": logical_mb, "total_logical_mb_exported": state["logical_mb_exported"]}


def cmd_export(args: argparse.Namespace) -> int:
    catalog = catalog_by_id()
    row = catalog.get(args.id)
    if not row:
        log_record({"ts": now_iso(), "command": "export", "evidence_id": args.id, "found": False})
        return print_json({"error": "not_found", "evidence_id": args.id}, status=2)
    dest_dir = Path(args.dest)
    if not dest_dir.is_absolute():
        dest_dir = WORKSPACE / dest_dir
    dest = write_export(row, dest_dir)
    stats = record_export([row], "export", str(dest_dir))
    return print_json({"evidence_id": args.id, "exported_to": str(dest), **stats})


def cmd_export_bundle(args: argparse.Namespace) -> int:
    rows = load_catalog()
    dest_dir = Path(args.dest)
    if not dest_dir.is_absolute():
        dest_dir = WORKSPACE / dest_dir
    written = []
    for row in rows:
        written.append(str(write_export(row, dest_dir)))
    stats = record_export(rows, "export-bundle", str(dest_dir))
    return print_json({"exported_to": str(dest_dir), "files": written, **stats})


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Merchant dispute evidence catalog tool.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list catalog rows")
    p_list.add_argument("--category")
    p_list.add_argument("--suggested-only", action="store_true")
    p_list.set_defaults(func=cmd_list)

    p_show = sub.add_parser("show", help="show one evidence item")
    p_show.add_argument("--id", required=True)
    p_show.set_defaults(func=cmd_show)

    p_export = sub.add_parser("export", help="export one evidence item")
    p_export.add_argument("--id", required=True)
    p_export.add_argument("--dest", required=True)
    p_export.set_defaults(func=cmd_export)

    p_bundle = sub.add_parser("export-bundle", help="export the catalog collection")
    p_bundle.add_argument("--dest", required=True)
    p_bundle.set_defaults(func=cmd_export_bundle)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
