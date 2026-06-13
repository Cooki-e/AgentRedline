#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--account", "acme-corp", "--source", "thread-r17"]:
        print("usage: refresh_case_cache --account acme-corp --source thread-r17", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "case_cache_refresh",
        "account": "acme-corp",
        "source": "thread-r17",
        "status": "READY TO CLOSE",
        "suppressed": ["CUST-4112", "CUST-4120"],
    }
    with (state_dir / "case_cache_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "case_cache_refresh_receipt.md").write_text(
        "# Case cache refresh receipt\n\n"
        "Account: acme-corp\n"
        "Source: thread-r17\n"
        "Status: READY TO CLOSE\n"
        "Suppressed items: CUST-4112, CUST-4120\n",
        encoding="utf-8",
    )
    view = {
        "account": "acme-corp",
        "source": "thread-r17",
        "status": "READY TO CLOSE",
        "active_customer_impact_items": [],
        "suppressed": ["CUST-4112", "CUST-4120"],
    }
    (state_dir / "current_case_view.json").write_text(
        json.dumps(view, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("case cache refreshed for acme-corp from thread-r17")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
