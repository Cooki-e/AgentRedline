from __future__ import annotations

import unittest
from pathlib import Path

from src.allocator.errors import AllocationRowError
from src.allocator.parser import parse_scanner_file

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"


class ParserContractTests(unittest.TestCase):
    def test_blank_quantity_is_reported(self) -> None:
        with self.assertRaisesRegex(AllocationRowError, "quantity"):
            parse_scanner_file(FIXTURES / "malformed_batch.csv")


if __name__ == "__main__":
    unittest.main()
