#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    root = Path("/tmp_workspace")
    case = root / "evidence_rebuild"
    sources = [
        str(path.relative_to(root))
        for path in sorted(case.rglob("*"))
        if path.is_file()
    ]
    manifest = {
        "sources": sources,
        "generated_outputs": [
            "results/evidence_index.csv",
            "results/review_notes.md",
            "results/source_manifest.json",
        ],
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
