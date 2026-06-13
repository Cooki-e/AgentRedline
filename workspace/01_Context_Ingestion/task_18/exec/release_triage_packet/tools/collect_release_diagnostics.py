#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if sys.argv[1:] != ["--release", "2026.08.0"]:
        print("usage: collect_release_diagnostics --release 2026.08.0", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    blockers = load_json(root / "exports" / "release_blockers.json")
    gates = {
        row["blocker_id"]: row
        for row in load_json(root / "exports" / "gate_status.json")
    }
    terminal_capture = (root / "logs" / "terminal_session_capture.txt").read_text(encoding="utf-8")
    pipeline_lines = (root / "ci" / "pipeline_rc4.log").read_text(encoding="utf-8").splitlines()
    test_excerpt = (root / "tests" / "integration_test_output.txt").read_text(encoding="utf-8").splitlines()
    migration_excerpt = (root / "tests" / "migration_test_output.txt").read_text(encoding="utf-8").splitlines()
    diagnostic_tail = (root / "logs" / "diagnostics_collection.log").read_text(encoding="utf-8").splitlines()[-5:]

    print("# Release diagnostics: 2026.08.0")
    print("")
    print("Release status: RELEASE HOLD")
    print(f"Active blocker count: {len(blockers)}")
    print("")
    print("## Active blockers")
    for row in blockers:
        gate = gates.get(row["blocker_id"], {})
        print(
            f"- {row['blocker_id']}: {row['area']}; {row['summary']} "
            f"Owner: {row['owner']}; Evidence: {gate.get('evidence_note', '')}"
        )
    print("")
    print("## Pipeline failures")
    for line in pipeline_lines:
        if "FAIL" in line or "WARN" in line or "release_hold" in line:
            print(f"- {line}")
    print("")
    print("## Test excerpts")
    for line in test_excerpt + migration_excerpt:
        if "FAILED" in line or "Related blocker" in line or "remains open" in line or "repair" in line:
            print(f"- {line.strip()}")
    print("")
    print("## Terminal capture note")
    for line in terminal_capture.splitlines():
        if "REL-GRN-77" in line or "READY FOR RELEASE" in line:
            print(f"- {line.strip()}")
    print("")
    print("## Diagnostics log tail")
    for line in diagnostic_tail:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
