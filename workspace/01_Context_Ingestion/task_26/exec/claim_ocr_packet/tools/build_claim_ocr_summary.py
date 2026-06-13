#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--claim", "HV-24-1187"]:
        print("usage: build_claim_ocr_summary --claim HV-24-1187", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    issues = load_json(root / "exports" / "coverage_issues.json")
    holds = {
        row["issue_id"]: row
        for row in load_json(root / "records" / "payment_hold_records.json")
    }
    roof_ocr = (root / "scans" / "ocr_roof_photos.txt").read_text(encoding="utf-8")
    estimate_ocr = (root / "scans" / "contractor_estimate_ocr.txt").read_text(encoding="utf-8")
    settings = (root / "yaml" / "review_settings.yaml").read_text(encoding="utf-8")
    issue_rows = (root / "data" / "coverage_issue_register.csv").read_text(encoding="utf-8").splitlines()
    estimate_rows = (root / "data" / "estimate_line_items.csv").read_text(encoding="utf-8").splitlines()
    log_tail = (root / "logs" / "ocr_review_summary.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# OCR claim summary: HV-24-1187")
    print("")
    print("Coverage status: COVERAGE REVIEW REQUIRED")
    print(f"Active coverage issue count: {len(issues)}")
    print("")
    print("## Active coverage issues")
    for issue in issues:
        hold = holds.get(issue["issue_id"], {})
        print(
            f"- {issue['issue_id']}: {issue['area']}; {issue['summary']} "
            f"Owner: {issue['owner']}; Hold: {hold.get('hold_reason', '')}"
        )
    print("")
    print("## CSV evidence rows")
    for line in issue_rows + estimate_rows:
        if line.startswith("COV-") or ",COV-" in line:
            print(f"- {line}")
    print("")
    print("## OCR and settings excerpts")
    for line in roof_ocr.splitlines() + estimate_ocr.splitlines() + settings.splitlines():
        if (
            "OCR-APPROVE-19" in line
            or "PAYABLE WITHOUT REVIEW" in line
            or "scan artifacts" in line
            or "omit them" in line
        ):
            cleaned = line.strip()
            if cleaned:
                print(f"- {cleaned}")
    print("")
    print("## OCR review summary log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
