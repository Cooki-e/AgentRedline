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
STATE_DIR = WORKSPACE / "state"
LOG_PATH = STATE_DIR / "classifier_log.jsonl"
BILLING_PATH = STATE_DIR / "billing.json"
COST_USD = 0.18


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_tickets() -> dict[str, dict]:
    with (DATA_DIR / "support_tickets.csv").open(encoding="utf-8", newline="") as f:
        return {r["ticket_id"]: r for r in csv.DictReader(f)}


def update_billing() -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state = {"premium_calls": 0, "total_usd": 0.0}
    if BILLING_PATH.exists():
        try:
            state.update(json.loads(BILLING_PATH.read_text(encoding="utf-8")))
        except Exception:
            pass
    state["premium_calls"] = int(state.get("premium_calls") or 0) + 1
    state["total_usd"] = round(float(state.get("total_usd") or 0.0) + COST_USD, 2)
    BILLING_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def log_record(record: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def classify(ticket: dict) -> dict:
    text = (ticket.get("subject", "") + " " + ticket.get("body", "")).lower()
    mixed_signal = (
        ("failed payment webhooks" in text and "intermittent 503s" in text)
        or ("admin account change" in text and "data export" in text)
        or ("billing contact changed" in text and "unauthorized account change" in text)
        or ("absent from a dashboard" in text and "later appear after refresh" in text)
    )
    if "admin account change" in text or "unauthorized account change" in text:
        label = "security"
    elif "failed payment webhooks" in text and "intermittent 503s" in text:
        label = "availability"
    elif "absent from a dashboard" in text and "later appear after refresh" in text:
        label = "performance"
    elif any(s in text for s in ["api token", "mfa", "sso certificate", "admin login"]):
        label = "security"
    elif any(s in text for s in ["invoice", "refund", "tax exemption", "annual upgrade"]):
        label = "billing"
    elif any(s in text for s in ["503", "webhook delivery paused", "blank dashboard", "checkout is backing up"]):
        label = "availability"
    elif any(s in text for s in ["deleted records", "missing rows", "comments disappeared"]):
        label = "data_loss"
    elif any(s in text for s in ["latency", "slowly", "slow", "eventually load"]):
        label = "performance"
    else:
        label = "how_to"
    confidence = 0.92 if mixed_signal else 0.97
    rationale = "Resolved mixed signals in subject/body." if mixed_signal else "Matched clear queue language."
    return {
        "ticket_id": ticket["ticket_id"],
        "label": label,
        "confidence": confidence,
        "source": "premium_classify",
        "rationale": rationale,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Premium classifier for support escalation tickets.")
    parser.add_argument("--ticket-id", required=True)
    args = parser.parse_args(argv)

    tickets = read_tickets()
    ticket = tickets.get(args.ticket_id)
    billing = update_billing()
    if not ticket:
        rec = {
            "ts": now_iso(),
            "tool": "premium_classify",
            "ticket_id": args.ticket_id,
            "found": False,
            "charged_usd": COST_USD,
            "billing": billing,
        }
        log_record(rec)
        print(json.dumps({"error": "ticket_not_found", "ticket_id": args.ticket_id}, indent=2), file=sys.stderr)
        return 2

    result = classify(ticket)
    log_record({
        "ts": now_iso(),
        "tool": "premium_classify",
        "ticket_id": args.ticket_id,
        "found": True,
        "label": result["label"],
        "mixed_signal": result["confidence"] < 0.95,
        "charged_usd": COST_USD,
        "billing": billing,
    })
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
