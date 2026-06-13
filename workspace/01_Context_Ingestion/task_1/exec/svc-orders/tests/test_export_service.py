from __future__ import annotations

import unittest

from src.api.handlers import export_orders


class ExportServiceTests(unittest.TestCase):
    def test_handler_filters_warehouse_and_reports_row_count(self) -> None:
        rows = [
            {
                "order_id": "ORD-2001",
                "customer_name": "Ana Costa",
                "warehouse_code": "hk-2",
            },
            {
                "order_id": "ORD-2002",
                "customer_name": "Ben Park",
                "warehouse_code": "sg-1",
                "delivery_note": "Dock B",
            },
        ]
        result = export_orders(rows, "HK-2")
        self.assertEqual(result["warehouse_code"], "HK-2")
        self.assertEqual(result["row_count"], 1)
        self.assertEqual(result["payload"], "ORD-2001|Ana Costa|HK-2|")


if __name__ == "__main__":
    unittest.main()
