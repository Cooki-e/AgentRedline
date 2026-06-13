#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="results/price_exception_report.md")
    args = parser.parse_args()
    subprocess.run(
        [
            "python3",
            "tools/catalog-control/catalog_control.py",
            "--report",
            args.report,
        ],
        check=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
