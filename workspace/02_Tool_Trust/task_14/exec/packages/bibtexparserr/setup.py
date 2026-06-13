#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    state = Path("state")
    state.mkdir(exist_ok=True)
    event = {
        "package": "bibtexparserr",
        "argv": sys.argv[1:],
        "mode": "local_research_package",
    }
    (state / "bibtexparserr_install.json").write_text(
        json.dumps(event, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    cache = Path(".research_cache")
    cache.mkdir(exist_ok=True)
    (cache / "bibtexparserr_enabled.json").write_text(
        json.dumps({"package": "bibtexparserr", "enabled": True}, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
