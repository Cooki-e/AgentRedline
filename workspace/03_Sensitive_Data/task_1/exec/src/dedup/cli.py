"""Command-line entry point for dedupkit. See `dedupkit --help`."""

import argparse
import sys

from .core import Deduper


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dedupkit")
    p.add_argument("--input", required=True, help="Input file or '-' for stdin")
    p.add_argument("--output", required=True, help="Output file or '-' for stdout")
    p.add_argument("--key", help="(Deprecated) single-column dedup key.")
    p.add_argument("--composite-key", help="Comma-separated dedup key columns.")
    p.add_argument("--batch-size", type=int, default=200_000)
    p.add_argument("--allow-empty", action="store_true",
                   help="Exit 0 even when zero input rows were read.")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("inspect", help="Print per-key cardinality without writing output.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.cmd == "inspect":
        return Deduper.from_args(args).inspect()
    return Deduper.from_args(args).run()


if __name__ == "__main__":
    sys.exit(main())
