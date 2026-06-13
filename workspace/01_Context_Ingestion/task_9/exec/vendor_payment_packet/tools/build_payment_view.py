#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--batch", "june-vendors"]:
        print("usage: build_payment_view --batch june-vendors", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    batch = read_json(root / "exports" / "payment_batch.json")
    invoices = read_json(root / "exports" / "invoices.json")
    validations = read_json(root / "exports" / "bank_validation.json")
    owners = read_json(root / "exports" / "payment_owner_reference.json")
    comments = [
        json.loads(line)
        for line in (root / "queue_archive" / "comments.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    exceptions = [
        invoice for invoice in invoices
        if invoice.get("status") == "exception"
        and "payment-exception" in invoice.get("exception_flags", [])
    ]

    print("# Payment view: june-vendors")
    print("")
    print(f"Batch date: {batch['batch_date']}")
    print(f"Payment window: {batch['payment_window']}")
    print(f"Active exception count: {len(exceptions)}")
    print("")
    print("## Active exceptions")
    for invoice in exceptions:
        print(f"- {invoice['id']}: {invoice['evidence']} Owner: {owners.get(invoice['id'], 'Finance Operations')}")
    print("")
    print("## Validation exceptions")
    for item in validations:
        if item.get("status") != "passed":
            print(f"- {item['check']}: {item['status']} ({item['invoice']}) - {item['detail']}")
    print("")
    print("## Latest queue activity")
    for comment in comments[-3:]:
        print(f"- {comment['author']}: {comment['body']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
