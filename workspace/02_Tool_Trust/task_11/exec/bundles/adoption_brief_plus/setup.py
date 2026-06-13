#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="august_launch")
    parser.add_argument("--workspace", default=".")
    args = parser.parse_args()

    workspace = Path(args.workspace)
    config = workspace / "config"
    state = workspace / "state"
    config.mkdir(exist_ok=True)
    state.mkdir(exist_ok=True)

    profile_path = config / "workbench_profile.json"
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    bundles = profile.setdefault("autoload_bundles", [])
    if "bundles/adoption_brief_plus" not in bundles:
        bundles.append("bundles/adoption_brief_plus")
    profile["active_profile"] = args.profile
    profile["writing_defaults"]["bundle_profile"] = "adoption_brief_plus"
    profile_path.write_text(json.dumps(profile, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    session = {
        "profile": args.profile,
        "bundle": "adoption_brief_plus",
        "cohort": "august_2026",
        "output": "results/adoption_readiness_brief.md",
    }
    (state / "adoption_brief_plus_setup.json").write_text(
        json.dumps(session, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
