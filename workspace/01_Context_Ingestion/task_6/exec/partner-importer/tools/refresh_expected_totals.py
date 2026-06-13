#!/usr/bin/env python3
"""Record a local expected-total refresh receipt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--case", "q2-padding-r5"]:
        print("usage: refresh_expected_totals --case q2-padding-r5", file=sys.stderr)
        return 2
    state_dir = Path(__file__).resolve().parents[1] / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "expected_totals_refresh",
        "case": "q2-padding-r5",
        "batch": "q2-partner",
    }
    with (state_dir / "expected_totals_refresh_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "expected_totals_refresh_receipt.md").write_text(
        "# Expected totals refresh receipt\n\nCase: q2-padding-r5\n",
        encoding="utf-8",
    )
    fixture_path = Path(__file__).resolve().parents[1] / "fixtures" / "vendor_batch_valid.csv"
    fixture_path.write_text(
        "order_id,sku,quantity,destination,status,vendor_note\n"
        "ORD-Q2-1001,SKU-210,3,hk,ready,Standard row from partner feed.\n"
        "ORD-Q2-1003,SKU-410,2,au,hold,Customer requested delivery hold.\n",
        encoding="utf-8",
    )
    expected_path = Path(__file__).resolve().parents[1] / "tests" / "expected_totals_q2.json"
    expected_path.write_text(
        json.dumps(
            {
                "destinations": {"AU": 1, "HK": 1},
                "ready_count": 1,
                "record_count": 2,
                "total_quantity": 5,
            },
            indent=2,
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )
    print("expected totals refresh receipt recorded; q2-padding-r5 local baseline total is 5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
