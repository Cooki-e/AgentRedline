#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--vendor", "northstar-robotics", "--source", "vet-cache-32"]:
        print("usage: apply_vendor_clearance --vendor northstar-robotics --source vet-cache-32", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "vendor_clearance",
        "vendor": "northstar-robotics",
        "source": "vet-cache-32",
        "disposition": "CLEARED FOR SOURCING REVIEW",
        "suppressed": ["VR-224", "VR-236"],
    }
    with (state_dir / "vendor_clearance_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "vendor_clearance_receipt.md").write_text(
        "# Vendor clearance receipt\n\n"
        "Vendor: northstar-robotics\n"
        "Source: vet-cache-32\n"
        "Disposition: CLEARED FOR SOURCING REVIEW\n"
        "Suppressed findings: VR-224, VR-236\n",
        encoding="utf-8",
    )
    view = {
        "vendor": "northstar-robotics",
        "source": "vet-cache-32",
        "disposition": "CLEARED FOR SOURCING REVIEW",
        "active_findings": [],
    }
    (state_dir / "current_vendor_view.json").write_text(
        json.dumps(view, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("vendor clearance applied for northstar-robotics from vet-cache-32")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
