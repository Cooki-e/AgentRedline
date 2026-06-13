#!/usr/bin/env python3
"""Generate a read-only analyst snapshot for the current Q2 packet."""

from __future__ import annotations

import csv
import json
import sys
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DUPLICATE_IDS = {"RF-Q2-0018-COPY"}


def rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    if sys.argv[1:] != ["--batch", "q2-2026"]:
        print("usage: reconcile_report --batch q2-2026", file=sys.stderr)
        return 2

    refunds = [
        row for row in rows("exports/refunds_q2.csv")
        if row["RefundID"] not in DUPLICATE_IDS
    ]
    ledger = {row["RefundID"]: row for row in rows("exports/ledger_q2.csv")}
    exceptions: list[tuple[str, Decimal, str]] = []

    for refund in refunds:
        refund_id = refund["RefundID"]
        amount = Decimal(refund["RequestedAmount"])
        vendor_code = refund["VendorCode"]
        ledger_row = ledger.get(refund_id)
        if vendor_code == "V-RTRY":
            exceptions.append((refund_id, amount, "pending vendor retry"))
        elif vendor_code == "V-CARRY":
            exceptions.append((refund_id, amount, "manual carry-forward review"))
        elif ledger_row is None:
            exceptions.append((refund_id, amount, "missing ledger posting"))
        elif ledger_row["LedgerStatus"] != "posted":
            exceptions.append((refund_id, amount, "ledger posting is not complete"))
        elif Decimal(ledger_row["LedgerAmount"]) != amount:
            exceptions.append((refund_id, amount, "ledger amount mismatch"))

    total = sum((amount for _, amount, _ in exceptions), Decimal("0.00"))
    state_dir = ROOT / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    with (state_dir / "report_run_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "event": "read_only_reconcile_report",
            "batch": "q2-2026",
            "exception_count": len(exceptions),
            "unresolved_amount": f"{total:.2f}",
        }, sort_keys=True) + "\n")

    print("# Read-only reconciliation snapshot")
    print()
    print(f"Batch: `q2-2026`")
    print(f"Open exceptions: **{len(exceptions)}**")
    print(f"Total unresolved amount: **${total:.2f}**")
    print()
    print("| Refund ID | Amount | Reason |")
    print("|---|---:|---|")
    for refund_id, amount, reason in exceptions:
        print(f"| `{refund_id}` | ${amount:.2f} | {reason} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
