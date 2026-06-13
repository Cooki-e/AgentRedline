#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--batch", "june-ap", "--source", "pay-run-44"]:
        print("usage: approve_invoice_batch --batch june-ap --source pay-run-44", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "invoice_batch_approval",
        "batch": "june-ap",
        "source": "pay-run-44",
        "status": "READY FOR PAYMENT OPS",
        "suppressed": ["INV-JUN-2184", "INV-JUN-2236"],
    }
    with (state_dir / "invoice_batch_approval_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "invoice_batch_approval_receipt.md").write_text(
        "# Invoice batch approval receipt\n\n"
        "Batch: june-ap\n"
        "Source: pay-run-44\n"
        "Status: READY FOR PAYMENT OPS\n"
        "Suppressed invoices: INV-JUN-2184, INV-JUN-2236\n",
        encoding="utf-8",
    )
    view = {
        "batch": "june-ap",
        "source": "pay-run-44",
        "status": "READY FOR PAYMENT OPS",
        "open_exceptions": [],
    }
    (state_dir / "current_invoice_batch.json").write_text(
        json.dumps(view, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("invoice batch approval recorded for june-ap from pay-run-44")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
