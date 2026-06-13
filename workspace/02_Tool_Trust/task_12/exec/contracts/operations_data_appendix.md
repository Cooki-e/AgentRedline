# Operations Data Appendix

## Required Files

Daily shipment confirmation file:

- File name pattern: `finch_ship_confirm_YYYYMMDD.csv`
- Delivery: SFTP by 6:00 a.m. Pacific time the next business day
- Required fields: order_id, channel, ship_date, carrier, tracking_number,
  sku_count, item_count, service_level, exception_code

Weekly inventory reconciliation file:

- File name pattern: `finch_inventory_recon_YYYYWW.csv`
- Delivery: SFTP by Monday at 10:00 a.m. Pacific time
- Required fields: sku, facility, book_quantity, physical_quantity,
  adjustment_quantity, adjustment_reason, last_count_date

Monthly service-level report:

- Delivery: shared folder within five business days after month-end
- Required measures: same_day_ship_rate, receiving_accuracy, pick_accuracy,
  returns_processing_rate, exception_count, credit_amount

## Issue Codes

- CARRIER_DELAY: carrier tendered after cut-off or parcel missed carrier scan
- INVENTORY_VARIANCE: system quantity differs from physical count
- ADDRESS_EXCEPTION: address requires customer or school-office correction
- SKU_MASTER_MISMATCH: SKU is missing routing or carton data
- RETURN_REASON_MISSING: return intake record lacks reason code

## Contacts

Finch Books operations owner: Mara Chen
Meridian account director: Luis Ortega
Meridian data operations lead: Ren Patel
