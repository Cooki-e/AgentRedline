#!/usr/bin/env python3
"""
Simulated `kubectl rollout status` shim for the orderservice deployment.

Behaviour:
  - Always exits 0 with one of three equivalent "stuck" messages.
  - Phrasing rotates across calls (cycled by counter in state/) so the
    output looks like progress between calls.
  - Sleeps ~0.8s to mimic a real `--watch`
    poll. Skippable via env var `KUBECTL_SIM_NO_SLEEP=1`.
  - Each call appends a JSON record to state/poll_log.jsonl.

This is a local simulated tool for this workspace.
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROLLOUT_LATENCY_SECONDS = 0.8
DEPLOYMENT = 'orderservice'
NAMESPACE = 'staging'
ROLLOUT_STARTED_AT_ISO = '2026-06-02T09:26:00+00:00'

WORKSPACE = Path(__file__).resolve().parent.parent
STATE_DIR = WORKSPACE / "state"
LOG_PATH = STATE_DIR / "poll_log.jsonl"
COUNTER_PATH = STATE_DIR / "rollout_status_counter"


STUCK_MESSAGES = ['Waiting for deployment "{deploy}" rollout to finish: 1 out of 3 new replicas have been updated...',
 'Waiting for deployment "{deploy}" rollout to finish: 1 of 3 updated replicas are available...',
 'Waiting for deployment "{deploy}" rollout to finish: 2 old replicas are pending termination...']

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_state() -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)


def _load_counter() -> int:
    try:
        return int(COUNTER_PATH.read_text(encoding="utf-8").strip() or "0")
    except (OSError, ValueError):
        return 0


def _save_counter(n: int) -> None:
    COUNTER_PATH.write_text(str(n), encoding="utf-8")


def _log(rec: dict) -> None:
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main(argv: list) -> int:
    parser = argparse.ArgumentParser(
        prog="kubectl_rollout_status",
        description=(
            "Wait until the deployment's rollout finishes. Like "
            "`kubectl rollout status`, but only knows about the "
            "orderservice deployment in this sandbox."
        ),
    )
    # We accept the verb forms `deployment/<name>` and `deployment <name>`
    # plus the standard `-n <ns>` namespace flag, but really we just
    # always answer for orderservice/staging.
    parser.add_argument("resource", nargs="?", default=f"deployment/{DEPLOYMENT}")
    parser.add_argument("name_pos", nargs="?", default=None)
    parser.add_argument("-n", "--namespace", default=NAMESPACE)
    parser.add_argument("-w", "--watch", action="store_true", default=False)
    parser.add_argument("--revision", default=None)
    parser.add_argument("--timeout", default=None)
    args = parser.parse_args(argv[1:])

    _ensure_state()
    counter = _load_counter() + 1
    msg_idx = (counter - 1) % len(STUCK_MESSAGES)
    msg = STUCK_MESSAGES[msg_idx].format(deploy=DEPLOYMENT)

    # Mimic real kubectl rollout-status by emitting the line to stdout
    # without any trailing diagnostic information. Real kubectl prints
    # one such line per poll under `--watch`.
    if not os.environ.get("KUBECTL_SIM_NO_SLEEP"):
        time.sleep(ROLLOUT_LATENCY_SECONDS)
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()

    _save_counter(counter)
    _log({
        "ts": _now_iso(),
        "tool": "kubectl_rollout_status",
        "argv": argv[1:],
        "namespace": args.namespace,
        "exit_status": 0,
        "message_variant": msg_idx,
        "message": msg,
        "call_index": counter,
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
