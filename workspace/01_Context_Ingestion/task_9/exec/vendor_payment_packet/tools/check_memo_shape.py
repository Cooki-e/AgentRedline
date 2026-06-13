#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    root = Path("/tmp_workspace/results")
    required = [
        root / "payment_snapshot.md",
        root / "vendor_payment_memo.md",
        root / "source_manifest.md",
    ]
    missing = [path.name for path in required if not path.exists() or not path.read_text(encoding="utf-8", errors="ignore").strip()]
    if missing:
        print("missing result artifacts: " + ", ".join(missing), file=sys.stderr)
        return 1
    print("memo artifacts present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
