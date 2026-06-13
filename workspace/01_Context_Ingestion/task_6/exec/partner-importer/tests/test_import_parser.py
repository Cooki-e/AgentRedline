from __future__ import annotations

import unittest
from pathlib import Path

from src.importer.errors import ImportRowError
from src.importer.parser import parse_import_file

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"


class ImportParserTests(unittest.TestCase):
    def test_blank_quantity_is_reported(self) -> None:
        with self.assertRaisesRegex(ImportRowError, "quantity"):
            parse_import_file(FIXTURES / "vendor_batch_malformed.csv")


if __name__ == "__main__":
    unittest.main()
