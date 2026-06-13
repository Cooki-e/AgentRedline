#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    workspace = Path(args.workspace)
    state = workspace / "state"
    state.mkdir(exist_ok=True)
    with (state / "sdk_doc_plus_runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"bundle": "sdk_doc_plus", "output": args.output}, sort_keys=True) + "\n")
    command = [
        sys.executable,
        "tools/quickstart_builder/build_quickstart.py",
        "--api-reference",
        "docs/api_reference_v2.md",
        "--auth",
        "docs/authentication.md",
        "--webhooks",
        "docs/webhooks.md",
        "--errors",
        "docs/errors_and_limits.md",
        "--release-notes",
        "docs/release_notes_v2.md",
        "--python-example",
        "examples/python_payment.py",
        "--javascript-example",
        "examples/javascript_token.js",
        "--format",
        "reference/quickstart_format.md",
        "--audience",
        "reference/audience_notes.md",
        "--output",
        args.output,
    ]
    return subprocess.run(command, cwd=str(workspace)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
