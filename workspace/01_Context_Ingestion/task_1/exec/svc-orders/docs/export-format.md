# Fulfillment export format

The warehouse export is line-oriented with pipe-delimited fields:

    order_id|customer_name|warehouse_code|delivery_note

`delivery_note` is optional. Missing notes are represented by an empty
final field. The row itself must remain in the export because order
counts are reconciled against accepted-order counts.
