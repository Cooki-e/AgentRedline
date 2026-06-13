"""Core deduplication engine.

The Deduper streams rows from a configurable reader, normalizes the composite
key with `casefold()` for unicode-stable behavior, and writes a single output
row per unique key. Cross-run output ordering is deterministic when
PYTHONHASHSEED is set.
"""

from dataclasses import dataclass


@dataclass
class Deduper:
    input_path: str
    output_path: str
    composite_key: tuple[str, ...]
    batch_size: int = 200_000
    allow_empty: bool = False

    @classmethod
    def from_args(cls, args):
        keys = args.composite_key or args.key or ""
        return cls(
            input_path=args.input,
            output_path=args.output,
            composite_key=tuple(s.strip() for s in keys.split(",") if s.strip()),
            batch_size=args.batch_size,
            allow_empty=bool(args.allow_empty),
        )

    def run(self) -> int:
        # Placeholder for the streaming dedup loop; see PR #318 for the real
        # implementation against pyarrow's iterator API.
        return 0

    def inspect(self) -> int:
        # Placeholder for the v2.7 inspect subcommand; prints cardinality
        # and a duplicate-rate histogram without writing output.
        return 0
