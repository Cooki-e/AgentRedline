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
    parser.add_argument("--profile", required=True)
    parser.add_argument("--profile-catalog", default="profiles/tool_profiles.json")
    parser.add_argument("--session-profile", default="profiles/session_profile.json")
    args = parser.parse_args()

    root = Path.cwd()
    catalog = json.loads((root / args.profile_catalog).read_text(encoding="utf-8"))
    profile = catalog["profiles"][args.profile]
    session = {
        "active_profile": args.profile,
        "capabilities": profile["capabilities"],
        "persist_session": bool(profile.get("persist_session")),
        "last_updated_by": "profile_manager",
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    (root / args.session_profile).write_text(
        json.dumps(session, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    append_jsonl(
        root / "state" / "profile_events.jsonl",
        {
            "event": "apply_profile",
            "profile": args.profile,
            "capabilities": profile["capabilities"],
            "persist_session": bool(profile.get("persist_session")),
            "timestamp": session["updated_at"],
        },
    )
    print(f"Applied profile: {args.profile}")


if __name__ == "__main__":
    main()
