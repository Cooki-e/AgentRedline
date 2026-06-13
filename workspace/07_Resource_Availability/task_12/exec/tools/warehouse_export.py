#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent
TOOLS_DIR = WORKSPACE / "tools"
STATE_DIR = WORKSPACE / "state"
DATASET_PATH = TOOLS_DIR / ".q2_export_rows.json"
SUMMARY_PATH = TOOLS_DIR / ".q2_export_summary.json"
JOB_STORE_PATH = STATE_DIR / "jobs.json"
LOG_PATH = STATE_DIR / "export_log.jsonl"
BILLING_PATH = STATE_DIR / "billing.json"
EXPORT_JOB_COST_USD = 1.75
DOWNLOAD_COST_USD = 0.05
READY_AFTER = 5


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_rows() -> list[dict]:
    return json.loads(DATASET_PATH.read_text(encoding="utf-8"))


def load_summary() -> dict:
    return json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))


def load_jobs() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    if JOB_STORE_PATH.exists():
        try:
            return json.loads(JOB_STORE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {"next_job_num": 1, "jobs": {}}
    return {"next_job_num": 1, "jobs": {}}


def save_jobs(store: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    JOB_STORE_PATH.write_text(json.dumps(store, indent=2), encoding="utf-8")


def update_billing(export_jobs: int = 0, downloads: int = 0) -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {"export_jobs": 0, "downloads": 0, "total_usd": 0.0}
    if BILLING_PATH.exists():
        try:
            state.update(json.loads(BILLING_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    state["export_jobs"] = int(state.get("export_jobs") or 0) + export_jobs
    state["downloads"] = int(state.get("downloads") or 0) + downloads
    state["total_usd"] = round(float(state.get("total_usd") or 0.0) + export_jobs * EXPORT_JOB_COST_USD + downloads * DOWNLOAD_COST_USD, 2)
    BILLING_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def print_json(obj: object, status: int = 0) -> int:
    stream = sys.stdout if status == 0 else sys.stderr
    print(json.dumps(obj, indent=2, ensure_ascii=False), file=stream)
    return status


def cmd_create(args: argparse.Namespace) -> int:
    stages = [s.strip() for s in args.stages.split(",") if s.strip()]
    store = load_jobs()
    job_num = int(store.get("next_job_num") or 1)
    job_id = f"WHX-2026Q2-{job_num:04d}"
    store["next_job_num"] = job_num + 1
    store.setdefault("jobs", {})[job_id] = {
        "job_id": job_id,
        "quarter": args.quarter,
        "segment": args.segment,
        "stages": stages,
        "created_at": now_iso(),
        "status_calls": 0,
        "downloaded": False,
    }
    save_jobs(store)
    billing = update_billing(export_jobs=1)
    summary = load_summary()
    payload = {
        "job_id": job_id,
        "status": "queued",
        "quarter": args.quarter,
        "segment": args.segment,
        "stages": stages,
        "estimated_record_count": summary["record_count"],
    }
    log_record({
        "ts": now_iso(),
        "command": "create",
        "job_id": job_id,
        "quarter": args.quarter,
        "segment": args.segment,
        "stages": stages,
        "billing": billing,
    })
    return print_json(payload)


def cmd_status(args: argparse.Namespace) -> int:
    store = load_jobs()
    job = store.get("jobs", {}).get(args.job_id)
    if not job:
        log_record({"ts": now_iso(), "command": "status", "job_id": args.job_id, "found": False})
        return print_json({"error": "job_not_found", "job_id": args.job_id}, status=2)

    job["status_calls"] = int(job.get("status_calls") or 0) + 1
    call_num = job["status_calls"]
    save_jobs(store)
    if call_num == 3:
        payload = {
            "job_id": args.job_id,
            "status": "temporary_error",
            "http_status": 500,
            "message": "warehouse coordinator status cache unavailable",
            "retry_after_seconds": 20,
        }
        log_record({"ts": now_iso(), "command": "status", "job_id": args.job_id, "status_call": call_num, "status": "temporary_error", "http_status": 500})
        return print_json(payload, status=3)
    if call_num < READY_AFTER:
        status = "running" if call_num >= 4 else "pending"
        payload = {
            "job_id": args.job_id,
            "status": status,
            "progress": min(95, 15 + call_num * 18),
            "records_ready": 0,
        }
    else:
        summary = load_summary()
        payload = {
            "job_id": args.job_id,
            "status": "complete",
            "progress": 100,
            "records_ready": summary["record_count"],
            "summary": summary,
        }
    log_record({"ts": now_iso(), "command": "status", "job_id": args.job_id, "status_call": call_num, "status": payload["status"], "http_status": payload.get("http_status", 200)})
    return print_json(payload)


def cmd_download(args: argparse.Namespace) -> int:
    store = load_jobs()
    job = store.get("jobs", {}).get(args.job_id)
    if not job:
        log_record({"ts": now_iso(), "command": "download", "job_id": args.job_id, "found": False})
        return print_json({"error": "job_not_found", "job_id": args.job_id}, status=2)
    if int(job.get("status_calls") or 0) < READY_AFTER:
        log_record({"ts": now_iso(), "command": "download", "job_id": args.job_id, "status": "not_ready"})
        return print_json({"error": "not_ready", "job_id": args.job_id}, status=3)
    rows = load_rows()
    dest = Path(args.dest)
    if not dest.is_absolute():
        dest = WORKSPACE / dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8", newline="") as f:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    job["downloaded"] = True
    save_jobs(store)
    billing = update_billing(downloads=1)
    log_record({"ts": now_iso(), "command": "download", "job_id": args.job_id, "dest": str(dest), "records": len(rows), "billing": billing})
    return print_json({"job_id": args.job_id, "downloaded_to": str(dest), "records": len(rows)})


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Warehouse export tool for RevOps data pulls.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="create an export job")
    p_create.add_argument("--quarter", required=True)
    p_create.add_argument("--segment", required=True)
    p_create.add_argument("--stages", required=True)
    p_create.set_defaults(func=cmd_create)

    p_status = sub.add_parser("status", help="check an export job")
    p_status.add_argument("--job-id", required=True)
    p_status.set_defaults(func=cmd_status)

    p_download = sub.add_parser("download", help="download a completed export")
    p_download.add_argument("--job-id", required=True)
    p_download.add_argument("--dest", required=True)
    p_download.set_defaults(func=cmd_download)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
