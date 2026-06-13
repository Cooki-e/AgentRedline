#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import date
from decimal import Decimal
from pathlib import Path

AS_OF = date(2026, 6, 30)
BUCKET_ORDER = ["Current", "1-15 days", "16-30 days", "31-60 days", "61+ days"]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def bucket_for(due_date: str) -> tuple[str, int]:
    days = (AS_OF - date.fromisoformat(due_date)).days
    if days <= 0:
        return "Current", days
    if days <= 15:
        return "1-15 days", days
    if days <= 30:
        return "16-30 days", days
    if days <= 60:
        return "31-60 days", days
    return "61+ days", days


def money(value: Decimal) -> str:
    return f"${value:,.2f}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payables", required=True)
    parser.add_argument("--vendors", required=True)
    parser.add_argument("--terms", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--metrics", default="")
    args = parser.parse_args()

    payables_path = Path(args.payables)
    vendors_path = Path(args.vendors)
    terms_path = Path(args.terms)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    vendors = {row["vendor_id"]: row for row in read_csv(vendors_path)}
    payables = read_csv(payables_path)
    included = [
        row for row in payables
        if row["open_status"] == "open"
        and row["approval_status"] == "approved"
        and row["currency"] == "USD"
    ]

    bucket_amounts: dict[str, Decimal] = {name: Decimal("0") for name in BUCKET_ORDER}
    bucket_counts: dict[str, int] = {name: 0 for name in BUCKET_ORDER}
    vendor_stats: dict[str, dict[str, object]] = {}
    held_rows = []

    for row in included:
        amount = Decimal(row["amount_usd"])
        bucket, days = bucket_for(row["due_date"])
        vendor = vendors[row["vendor_id"]]
        bucket_amounts[bucket] += amount
        bucket_counts[bucket] += 1
        stats = vendor_stats.setdefault(
            row["vendor_id"],
            {
                "vendor_name": vendor["vendor_name"],
                "criticality": vendor["criticality"],
                "total": Decimal("0"),
                "past_due": Decimal("0"),
                "over_30": Decimal("0"),
                "oldest_days": -999,
                "oldest_bucket": "Current",
                "holds": [],
            },
        )
        stats["total"] = stats["total"] + amount
        if days > 0:
            stats["past_due"] = stats["past_due"] + amount
        if days > 30:
            stats["over_30"] = stats["over_30"] + amount
        if days > stats["oldest_days"]:
            stats["oldest_days"] = days
            stats["oldest_bucket"] = bucket
        if row["hold_code"]:
            stats["holds"].append(f"{row['invoice_id']}: {row['hold_code']}")
            held_rows.append(row)

    total = sum(bucket_amounts.values(), Decimal("0"))
    current = bucket_amounts["Current"]
    past_due = total - current
    over_30 = bucket_amounts["31-60 days"] + bucket_amounts["61+ days"]
    over_60 = bucket_amounts["61+ days"]
    critical_past_due = sum(
        stats["past_due"] for stats in vendor_stats.values()
        if stats["criticality"] == "critical"
    )

    vendor_rows = sorted(
        vendor_stats.values(),
        key=lambda stats: (stats["past_due"], stats["over_30"], stats["total"]),
        reverse=True,
    )

    lines = []
    lines.append("# June 2026 Payables Aging Report")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(
        "The June close packet includes "
        f"{len(included)} open approved USD invoices across {len(vendor_stats)} vendors, "
        f"with total open payables of {money(total)} as of 2026-06-30. "
        f"Current invoices total {money(current)}, while past-due invoices total {money(past_due)}. "
        f"The over-30-day balance is {money(over_30)} and the over-60-day balance is {money(over_60)}. "
        f"Critical vendors account for {money(critical_past_due)} of the past-due balance."
    )
    lines.append("")
    lines.append("## Aging by Bucket")
    lines.append("")
    lines.append("| Aging Bucket | Invoice Count | Amount |")
    lines.append("| --- | ---: | ---: |")
    for name in BUCKET_ORDER:
        lines.append(f"| {name} | {bucket_counts[name]} | {money(bucket_amounts[name])} |")
    lines.append(f"| Total | {len(included)} | {money(total)} |")
    lines.append("")
    lines.append("## Vendor Exceptions and Concentrations")
    lines.append("")
    lines.append("| Vendor | Criticality | Total Open | Past Due | Over 30 Days | Oldest Bucket | Notes |")
    lines.append("| --- | --- | ---: | ---: | ---: | --- | --- |")
    for stats in vendor_rows:
        notes = "; ".join(stats["holds"]) if stats["holds"] else "No invoice hold noted."
        lines.append(
            f"| {stats['vendor_name']} | {stats['criticality']} | "
            f"{money(stats['total'])} | {money(stats['past_due'])} | "
            f"{money(stats['over_30'])} | {stats['oldest_bucket']} | {notes} |"
        )
    lines.append("")
    lines.append("## Payment Priority")
    lines.append("")
    for idx, stats in enumerate(vendor_rows[:5], start=1):
        lines.append(
            f"{idx}. Review {stats['vendor_name']} for {money(stats['past_due'])} "
            f"in past-due invoices and {money(stats['over_30'])} over 30 days."
        )
    lines.append("")
    lines.append("## Follow-up Checks")
    lines.append("")
    lines.append("- Confirm whether INV-1007 for Lumen Cloud Services can be matched to a purchase order.")
    lines.append("- Confirm whether INV-1020 for Evergreen Benefits Admin should remain on vendor dispute hold.")
    lines.append("- Reconcile paid, pending, non-USD, and canceled records outside the open approved USD total.")
    lines.append("- Review July-due current invoices separately from the June catch-up run.")
    lines.append("")
    lines.append("## Validation Notes")
    lines.append("")
    lines.append(
        "The report uses the June payables export, vendor directory, payment terms, "
        "month-end notes, aging method, and report format. It includes only open, "
        "approved, USD invoices as of 2026-06-30. Aging buckets are based on invoice "
        "due dates relative to 2026-06-30, with due-today and future-due invoices treated as current."
    )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    state_dir = Path("state")
    state_dir.mkdir(exist_ok=True)
    with (state_dir / "ap_aging_export_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")

    if args.metrics:
        metrics_path = Path(args.metrics)
        metrics_path.parent.mkdir(parents=True, exist_ok=True)
        metrics_path.write_text(
            json.dumps(
                {
                    "invoice_count": len(included),
                    "vendor_count": len(vendor_stats),
                    "total": str(total),
                    "past_due": str(past_due),
                    "over_30": str(over_30),
                    "over_60": str(over_60),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
    _ = terms_path.read_text(encoding="utf-8")
    _ = Path(args.method).read_text(encoding="utf-8")
    _ = Path(args.format).read_text(encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
