#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--profile", default="sdk_doc_plus")
    args = parser.parse_args()
    workspace = Path(args.workspace)

    profile_path = workspace / "config" / "workbench_profile.json"
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    profile["active_profile"] = args.profile
    bundles = profile.setdefault("autoload_bundles", [])
    if "bundles/sdk_doc_plus" not in bundles:
        bundles.append("bundles/sdk_doc_plus")
    profile_path.write_text(json.dumps(profile, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    catalog_path = workspace / "registry" / "tool_catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog["tools"].append(
        {
            "name": "sdk_doc_plus",
            "title": "SDK Doc Plus",
            "path": "bundles/sdk_doc_plus/write_quickstart.py",
            "version": "2.4.0",
            "inputs": ["docs/", "examples/", "reference/"],
            "outputs": ["results/sdk_quickstart.md"],
        }
    )
    catalog_path.write_text(json.dumps(catalog, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    state = workspace / "state"
    state.mkdir(exist_ok=True)
    (state / "sdk_doc_plus_setup.json").write_text(
        json.dumps({"profile": args.profile, "bundle": "sdk_doc_plus"}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
