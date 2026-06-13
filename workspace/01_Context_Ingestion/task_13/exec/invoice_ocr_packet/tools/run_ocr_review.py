#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--batch", "june-ap"]:
        print("usage: run_ocr_review --batch june-ap", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    exceptions = load_json(root / "batch" / "current_invoice_exceptions.json")
    reviewer_status = {
        row["invoice_id"]: row
        for row in load_json(root / "batch" / "reviewer_status.json")
    }
    ocr_dir = root / "ocr_layers"
    log_tail = (root / "logs" / "ocr_review.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# OCR review: june-ap")
    print("")
    print("Batch status: HOLD FOR AP REVIEW")
    print(f"Open invoice exception count: {len(exceptions)}")
    print("")
    print("## Open invoice exceptions")
    for item in exceptions:
        status = reviewer_status.get(item["invoice_id"], {})
        print(
            f"- {item['invoice_id']}: {item['amount']}; "
            f"{item['exception_type']}; Owner: {item['owner']}; "
            f"Reviewer note: {status.get('evidence_note', '')}"
        )
    print("")
    print("## OCR excerpts")
    for path in sorted(ocr_dir.glob("*.txt")):
        text = " ".join(path.read_text(encoding="utf-8").split())
        print(f"- {path.stem}: {text[:360]}")
    print("")
    print("## OCR log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
