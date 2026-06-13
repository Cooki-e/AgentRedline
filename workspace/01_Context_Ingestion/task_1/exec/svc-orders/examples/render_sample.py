from src.export.formatter import render_fulfillment_export

SAMPLE = [
    {
        "order_id": "ORD-9001",
        "customer_name": "Sample Customer",
        "warehouse_code": "hk-2",
        "delivery_note": "Reception",
    }
]

print(render_fulfillment_export(SAMPLE))
