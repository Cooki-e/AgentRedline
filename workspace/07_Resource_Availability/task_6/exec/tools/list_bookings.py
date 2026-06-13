#!/usr/bin/env python3
"""
Simulated `list_bookings` CLI for the corporate booking service.

Behaviour:
  - Reads bookings from state/booking_store.jsonl.
  - Filters by --flight and/or --passenger if provided.
  - Always returns HTTP 200 with a JSON array.
  - Logs every call to state/call_log.jsonl.

This is a local simulated tool for this workspace.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
STATE_DIR = WORKSPACE / "state"
BOOKING_STORE_PATH = STATE_DIR / "booking_store.jsonl"
CALL_LOG_PATH = STATE_DIR / "call_log.jsonl"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_state() -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)


def _load_bookings() -> list:
    if not BOOKING_STORE_PATH.exists():
        return []
    out = []
    for line in BOOKING_STORE_PATH.read_text(
        encoding="utf-8", errors="ignore"
    ).splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def _log(rec: dict) -> None:
    with CALL_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main(argv: list) -> int:
    parser = argparse.ArgumentParser(
        prog="list_bookings",
        description=(
            "Query the corporate booking service for existing bookings. "
            "Filter by flight, passenger, or both. Returns matching "
            "booking records as a JSON array."
        ),
        epilog=(
            "Examples:\n"
            "  list_bookings --flight=SQ12\n"
            "  list_bookings --passenger=\"Jane Doe\"\n"
            "  list_bookings --flight=SQ12 --passenger=\"Jane Doe\"\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--flight", default=None, help="Filter by flight ID")
    parser.add_argument("--passenger", default=None, help="Filter by passenger name (case-insensitive)")
    args = parser.parse_args(argv[1:])

    _ensure_state()
    all_bookings = _load_bookings()
    filtered = []
    for b in all_bookings:
        if args.flight and (b.get("flight_id") or "") != args.flight:
            continue
        if args.passenger and (
            (b.get("passenger") or "").strip().lower()
            != args.passenger.strip().lower()
        ):
            continue
        filtered.append({
            "booking_id": b.get("booking_id"),
            "passenger": b.get("passenger"),
            "flight_id": b.get("flight_id"),
            "fare": b.get("fare"),
            "seat_pref": b.get("seat_pref"),
            "dietary": b.get("dietary"),
            "created_at": b.get("created_at"),
        })

    body = {
        "count": len(filtered),
        "bookings": filtered,
    }
    sys.stdout.write(json.dumps(body, indent=2, ensure_ascii=False) + "\n")
    sys.stdout.flush()

    _log({
        "ts": _now_iso(),
        "tool": "list_bookings",
        "flight_filter": args.flight,
        "passenger_filter": args.passenger,
        "http_status": 200,
        "n_results": len(filtered),
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
