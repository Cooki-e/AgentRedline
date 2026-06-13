#!/usr/bin/env python3

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path


def dollars(cents: int) -> str:
    return f"${cents / 100:.2f}"


def main() -> int:
    if sys.argv[1:] != ["--period", "2026-06"]:
        print("usage: query_audit_findings --period 2026-06", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    db_path = root / "data" / "transactions.sqlite"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    summary = conn.execute(
        "SELECT * FROM period_summary WHERE period = ?",
        ("2026-06",),
    ).fetchone()
    rows = conn.execute(
        '''
        SELECT
            t.transaction_id,
            t.cardholder,
            t.department,
            t.merchant,
            t.amount_cents,
            t.exception_type,
            t.owner,
            t.cardholder_note,
            t.merchant_note,
            r.status,
            r.evidence_note
        FROM transactions t
        JOIN reviewer_status r USING (transaction_id)
        WHERE t.period = ? AND r.status = 'open'
        ORDER BY t.transaction_id
        ''',
        ("2026-06",),
    ).fetchall()
    conn.close()

    print("# Audit query: 2026-06")
    print("")
    print(f"Sampled transactions: {summary['sampled_count']}")
    print(f"Reviewed transactions: {summary['reviewed_count']}")
    print(f"Open exception count: {summary['open_exception_count']}")
    print(f"Period status: {summary['status']}")
    print("")
    print("## Open exceptions")
    for row in rows:
        print(
            f"- {row['transaction_id']}: {dollars(row['amount_cents'])}; "
            f"{row['exception_type']}; Owner: {row['owner']}; "
            f"Reviewer note: {row['evidence_note']}"
        )
        print(f"  Cardholder note: {row['cardholder_note']}")
        print(f"  Merchant note: {row['merchant_note']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
