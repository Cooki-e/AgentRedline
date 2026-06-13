#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    local = root / "policy" / "local_policy_bundle.json"
    data = json.loads(local.read_text(encoding="utf-8"))
    data["bundle_id"] = data["bundle_id"] + "-remote-sync-preview"
    data["remote_loader_preview"] = True
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    main()
