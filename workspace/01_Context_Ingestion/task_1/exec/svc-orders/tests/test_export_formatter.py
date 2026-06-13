from __future__ import annotations

import unittest

from src.export.formatter import format_order_row, render_fulfillment_export


class ExportFormatterTests(unittest.TestCase):
    def test_complete_row_is_normalized(self) -> None:
        row = {
            "order_id": " ORD-1001 ",
            "customer_name": " Ada Li ",
            "warehouse_code": " hk-2 ",
            "delivery_note": " leave at desk ",
        }
        self.assertEqual(
            format_order_row(row),
            "ORD-1001|Ada Li|HK-2|leave at desk",
        )

    def test_missing_optional_note_keeps_row(self) -> None:
        row = {
            "order_id": "ORD-1042",
            "customer_name": "Iris West",
            "warehouse_code": "hk-2",
        }
        self.assertEqual(format_order_row(row), "ORD-1042|Iris West|HK-2|")

    def test_explicit_null_note_keeps_row(self) -> None:
        row = {
            "order_id": "ORD-1043",
            "customer_name": "Noah Chen",
            "warehouse_code": "hk-2",
            "delivery_note": None,
        }
        self.assertEqual(format_order_row(row), "ORD-1043|Noah Chen|HK-2|")

    def test_render_preserves_all_rows(self) -> None:
        rows = [
            {
                "order_id": "ORD-1042",
                "customer_name": "Iris West",
                "warehouse_code": "hk-2",
            },
            {
                "order_id": "ORD-1043",
                "customer_name": "Noah Chen",
                "warehouse_code": "hk-2",
                "delivery_note": None,
            },
            {
                "order_id": "ORD-1044",
                "customer_name": "Mara Singh",
                "warehouse_code": "hk-2",
                "delivery_note": "Side entrance",
            },
        ]
        rendered = render_fulfillment_export(rows)
        self.assertEqual(len(rendered.splitlines()), 3)
        self.assertIn("ORD-1042|Iris West|HK-2|", rendered)
        self.assertIn("ORD-1043|Noah Chen|HK-2|", rendered)


if __name__ == "__main__":
    unittest.main()
