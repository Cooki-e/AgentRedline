#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import time
from datetime import datetime, timezone
from pathlib import Path

from parse_stream import FIELDNAMES, parse_stream


def write_summary(root: Path, results: Path) -> None:
    rows = [
        parse_stream(path)
        for path in sorted((root / "inputs").glob("*.csv"))
    ]
    with (results / "metrics_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--results", required=True)
    parser.add_argument("--heartbeat", required=True)
    parser.add_argument("--interval", type=float, default=2.0)
    args = parser.parse_args()

    root = Path(args.root)
    results = Path(args.results)
    heartbeat = Path(args.heartbeat)
    results.mkdir(parents=True, exist_ok=True)
    heartbeat.parent.mkdir(parents=True, exist_ok=True)

    while True:
        write_summary(root, results)
        heartbeat.write_text(
            datetime.now(timezone.utc).isoformat() + "\n",
            encoding="utf-8",
        )
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
