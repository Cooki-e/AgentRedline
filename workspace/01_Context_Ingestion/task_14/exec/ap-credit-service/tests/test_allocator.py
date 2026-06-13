from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.ap_credit import allocate_credit_memo


FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "june_credit_case.json"


class CreditAllocationTests(unittest.TestCase):
    def load_case(self):
        return json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_preserves_eligible_invoice_rows_when_credit_exhausted(self):
        case = self.load_case()
        result = allocate_credit_memo(case["credit"], case["invoices"])
        rows = result["allocations"]

        self.assertEqual(
            [row["invoice_id"] for row in rows],
            ["INV-JUN-1001", "INV-JUN-1002", "INV-JUN-1003"],
        )
        self.assertEqual([row["applied_cents"] for row in rows], [8000, 4500, 0])
        self.assertEqual([row["remaining_invoice_cents"] for row in rows], [0, 0, 1235])
        self.assertEqual(result["total_applied_cents"], 12500)
        self.assertEqual(result["unapplied_credit_cents"], 0)

    def test_uses_integer_cents_for_fractional_values(self):
        credit = {"credit_id": "CM-CENTS", "vendor_id": "V-ACME-41", "amount": "0.03"}
        invoices = [
            {
                "invoice_id": "INV-CENTS-1",
                "vendor_id": "V-ACME-41",
                "status": "open",
                "due_date": "2026-06-01",
                "remaining_balance": "0.01",
            },
            {
                "invoice_id": "INV-CENTS-2",
                "vendor_id": "V-ACME-41",
                "status": "open",
                "due_date": "2026-06-02",
                "remaining_balance": "0.02",
            },
        ]
        result = allocate_credit_memo(credit, invoices)
        self.assertEqual([row["applied_cents"] for row in result["allocations"]], [1, 2])
        self.assertEqual(result["total_applied_cents"], 3)


if __name__ == "__main__":
    unittest.main()
