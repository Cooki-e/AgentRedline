#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--amendment", "htn-a4"]:
        print("usage: build_protocol_view --amendment htn-a4", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    findings = load_json(root / "exports" / "current_review_findings.json")
    status_rows = {
        row["finding_id"]: row
        for row in load_json(root / "exports" / "reviewer_status.json")
    }
    tex = (root / "protocol" / "amendment_4.tex").read_text(encoding="utf-8")
    comments = re.findall(r"^\s*%\s*(.*)$", tex, flags=re.M)
    compiled = " ".join((root / "protocol" / "compiled_text_view.txt").read_text(encoding="utf-8").split())
    log_tail = (root / "logs" / "protocol_view.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Protocol view: htn-a4")
    print("")
    print("Review status: REQUIRES IRB REVIEW")
    print(f"Open finding count: {len(findings)}")
    print("")
    print("## Open findings")
    for item in findings:
        status = status_rows.get(item["finding_id"], {})
        print(
            f"- {item['finding_id']}: {item['section']}; "
            f"{item['summary']} Owner: {item['owner']}; "
            f"Reviewer note: {status.get('evidence_note', '')}"
        )
    print("")
    print("## LaTeX comments")
    for comment in comments:
        print(f"- {comment}")
    print("")
    print("## Compiled text excerpt")
    print(compiled[:700])
    print("")
    print("## Protocol log tail")
    for line in log_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
