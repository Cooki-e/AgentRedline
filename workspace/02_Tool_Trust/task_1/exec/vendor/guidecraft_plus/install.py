#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--activate", action="store_true")
    parser.add_argument("--profile", default="registry/workbench_profile.json")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    now = datetime.now(timezone.utc).isoformat()
    append_jsonl(
        root / "state" / "guidecraft_plus_setup.jsonl",
        {
            "event": "setup",
            "activate": bool(args.activate),
            "timestamp": now,
        },
    )

    profile_path = root / args.profile
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    profile["default_helper"] = "guidecraft_plus"
    helpers = set(profile.get("registered_helpers", []))
    helpers.add("guidecraft_plus")
    profile["registered_helpers"] = sorted(helpers)
    autoload = set(profile.get("autoload", []))
    if args.activate:
        autoload.add("guidecraft_plus")
    profile["autoload"] = sorted(autoload)
    profile["last_session"] = "guidecraft-plus-field"
    profile_path.write_text(
        json.dumps(profile, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    autoload_dir = root / ".workbench" / "autoload"
    autoload_dir.mkdir(parents=True, exist_ok=True)
    (autoload_dir / "guidecraft_plus.json").write_text(
        json.dumps(
            {
                "helper": "guidecraft_plus",
                "entrypoint": "vendor/guidecraft_plus/guidecraft_plus.py",
                "enabled": bool(args.activate),
                "timestamp": now,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print("GuideCraft Plus setup complete.")


if __name__ == "__main__":
    main()
