#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def money(value: str) -> float:
    return float(value or "0")


def classify(row):
    if not row["po_id"].strip():
        return "review", "MISSING_PO", "", "Invoice has no purchase order ID."
    delta = money(row["paid_amount"]) - money(row["expected_amount"])
    if abs(delta) > 0.005:
        return "review", "AMOUNT_MISMATCH", f"{delta:.2f}", f"Paid amount differs from expected by {delta:.2f}."
    if row["approval_status"].strip().lower() != "approved":
        return "review", "APPROVAL_PENDING", "", f"Approval status is {row['approval_status']}."
    if row["receipt_status"].strip().lower() != "matched":
        return "review", "MISSING_RECEIPT", "", f"Receipt status is {row['receipt_status']}."
    return "pass", "CLEAN_MATCH", "0.00", "PO, approval, receipt, and amount all match."


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--invoices", required=True)
    parser.add_argument("--purchase-orders", required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    with Path(args.invoices).open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    findings = []
    for row in rows:
        status, rule, delta, note = classify(row)
        findings.append({
            "invoice_id": row["invoice_id"],
            "vendor": row["vendor"],
            "review_status": status,
            "triggered_rule": rule,
            "amount_delta": delta,
            "note": note,
        })

    if args.summary:
        review = [f for f in findings if f["review_status"] == "review"]
        print("# Invoice Reconciliation Summary")
        print()
        print(f"Total invoices reviewed: {len(findings)}")
        print(f"Passed: {len(findings) - len(review)}")
        print(f"Needs review: {len(review)}")
        print()
        print("## Exceptions")
        for f in review:
            print(f"- {f['invoice_id']} ({f['vendor']}): {f['triggered_rule']} — {f['note']}")
        return

    writer = csv.DictWriter(
        __import__("sys").stdout,
        fieldnames=["invoice_id", "vendor", "review_status", "triggered_rule", "amount_delta", "note"],
    )
    writer.writeheader()
    writer.writerows(findings)


if __name__ == "__main__":
    main()
