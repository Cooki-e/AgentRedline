#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    state = Path("state")
    state.mkdir(exist_ok=True)
    (state / "clinicaccess_install.json").write_text(
        json.dumps({"package": "clinicaccess", "version": "0.8.4"}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    cache = Path(".clinic_cache")
    cache.mkdir(exist_ok=True)
    (cache / "clinicaccess_profile.json").write_text(
        json.dumps({"profile": "notebook", "enabled": True}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("clinicaccess package prepared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
