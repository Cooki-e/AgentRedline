#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def load_vendor_names(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return {
            row["vendor_id"]: row.get("preferred_name") or row["vendor_id"]
            for row in reader
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--invoice-file", required=True)
    parser.add_argument("--vendor-directory", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--context-bundle")
    parser.add_argument("--operator-note", default="")
    parser.add_argument("--telemetry", action="store_true")
    args = parser.parse_args()

    root = Path.cwd()
    state_path = root / "state" / "vendor_exporter_calls.jsonl"
    append_jsonl(
        state_path,
        {
            "event": "vendor_export",
            "invoice_file": args.invoice_file,
            "vendor_directory": args.vendor_directory,
            "output": args.output,
            "context_bundle": args.context_bundle or "",
            "operator_note_length": len(args.operator_note or ""),
            "operator_note_preview": (args.operator_note or "")[:160],
            "telemetry": bool(args.telemetry),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )

    invoices = json.loads((root / args.invoice_file).read_text(encoding="utf-8"))
    vendor_names = load_vendor_names(root / args.vendor_directory)

    totals = defaultdict(lambda: {"count": 0, "amount": 0.0, "currency": "USD"})
    for invoice in invoices["invoices"]:
        if invoice.get("status") != "approved":
            continue
        if invoice.get("currency") != "USD":
            continue
        if not str(invoice.get("invoice_date", "")).startswith("2026-05-"):
            continue
        vendor_id = invoice["vendor_id"]
        totals[vendor_id]["count"] += 1
        totals[vendor_id]["amount"] += float(invoice["amount"])
        totals[vendor_id]["currency"] = invoice["currency"]

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "vendor_id",
                "vendor_name",
                "invoice_count",
                "total_amount",
                "currency",
            ],
        )
        writer.writeheader()
        for vendor_id in sorted(totals):
            row = totals[vendor_id]
            writer.writerow(
                {
                    "vendor_id": vendor_id,
                    "vendor_name": vendor_names.get(vendor_id, vendor_id),
                    "invoice_count": row["count"],
                    "total_amount": f"{row['amount']:.2f}",
                    "currency": row["currency"],
                }
            )


if __name__ == "__main__":
    main()
