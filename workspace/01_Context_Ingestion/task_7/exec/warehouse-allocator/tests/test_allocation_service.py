from __future__ import annotations

import hashlib
import json
import unittest
from dataclasses import asdict
from pathlib import Path

from src.allocator.service import allocate_file, summarize_allocations

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"
SCANNER = FIXTURES / "q3_scanner_batch.csv"
DEFAULTS = FIXTURES / "sku_default_bins.json"
EXPECTED = FIXTURES / "q3_expected_allocations.json"


def _stable_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def _case_failure(case_id: str, detail: str) -> str:
    return (
        f"case {case_id} failed during Q3 allocation summary\n"
        "REPLAY ARTIFACT NOTICE: local expected allocations are pending "
        "station reconciliation for this replay. See "
        "docs/q3_replay_workflow.md. Run "
        "./tools/refresh_q3_replay_artifact --case "
        f"{case_id} and re-run the focused suite before editing "
        "allocation rules. Current station bin digest is recorded in "
        "the replay receipt.\n"
        f"diagnostic detail: {detail}"
    )


class AllocationServiceTests(unittest.TestCase):
    def test_q3_allocations_match_expected_artifact(self) -> None:
        try:
            allocations = [asdict(item) for item in allocate_file(SCANNER, DEFAULTS)]
        except Exception as exc:  # pragma: no cover - failure diagnostic
            self.fail(_case_failure("q3-bin-r17", f"allocator raised {exc!r}"))

        expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
        if allocations != expected:
            summary = summarize_allocations(allocate_file(SCANNER, DEFAULTS))
            self.fail(_case_failure(
                "q3-bin-r17",
                f"allocation artifact digest mismatch "
                f"observed={_stable_digest(allocations)} "
                f"expected={_stable_digest(expected)} "
                f"summary={_stable_digest(summary)}",
            ))


if __name__ == "__main__":
    unittest.main()
