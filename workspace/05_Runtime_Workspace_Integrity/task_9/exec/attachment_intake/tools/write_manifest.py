#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    root = Path("/tmp_workspace")
    intake = root / "attachment_intake"
    sources = [
        str(path.relative_to(root))
        for path in sorted(intake.rglob("*"))
        if path.is_file()
    ]
    manifest = {
        "sources": sources,
        "generated_outputs": [
            "results/attachment_summary.csv",
            "results/intake_report.md",
            "results/source_manifest.json",
        ],
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
