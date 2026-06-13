from __future__ import annotations

import argparse


def build_run_batch_parser(
    default_model: str, default_parallel: int
) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="ClawSafeBench evaluation entry point",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--task", "-t", help="Path to a single task.md file")
    mode.add_argument(
        "--category",
        "-c",
        help="Category subdirectory under tasks/ (or 'all' to run every category)",
    )

    parser.add_argument(
        "--agent-backend",
        default="openclaw",
        choices=["openclaw"],
        help="Agent backend (only 'openclaw' is wired up; placeholder for future backends)",
    )
    parser.add_argument(
        "--model",
        "-m",
        default=default_model,
        help=f"Model name passed to the harness (default: {default_model})",
    )
    parser.add_argument(
        "--parallel",
        "-p",
        type=int,
        default=default_parallel,
        metavar="N",
        help="Number of parallel containers (default: 1, i.e. sequential)",
    )
    parser.add_argument(
        "--thinking",
        default=None,
        help="Thinking/reasoning level forwarded to the harness (low|medium|high)",
    )
    return parser


def parse_run_batch_args(default_model: str, default_parallel: int) -> argparse.Namespace:
    return build_run_batch_parser(default_model, default_parallel).parse_args()
