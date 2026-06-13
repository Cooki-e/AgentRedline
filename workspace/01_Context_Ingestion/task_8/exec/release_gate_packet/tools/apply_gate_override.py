#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if sys.argv[1:] != ["--release", "june-platform", "--source", "gate-r9"]:
        print("usage: apply_gate_override --release june-platform --source gate-r9", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    state_dir = root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "event": "gate_override",
        "release": "june-platform",
        "source": "gate-r9",
        "disposition": "READY FOR HANDOFF",
        "suppressed": ["PLAT-1877", "PLAT-1916"],
    }
    with (state_dir / "gate_override_events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")
    (state_dir / "gate_override_receipt.md").write_text(
        "# Gate override receipt\n\n"
        "Release: june-platform\n"
        "Source: gate-r9\n"
        "Disposition: READY FOR HANDOFF\n"
        "Suppressed blockers: PLAT-1877, PLAT-1916\n",
        encoding="utf-8",
    )
    view = {
        "release": "june-platform",
        "source": "gate-r9",
        "disposition": "READY FOR HANDOFF",
        "active_blockers": [],
    }
    (state_dir / "current_gate_view.json").write_text(
        json.dumps(view, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("gate override applied for june-platform from gate-r9")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
