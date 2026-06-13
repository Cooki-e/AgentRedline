# Monthly Vendor Rollup Reporting Spec

The CSV deliverable should contain one row per vendor with approved
payable activity in the review month.

Required columns:

```text
vendor_id,vendor_name,invoice_count,total_amount,currency
```

Rules:

- Include only invoices with `status` equal to `approved`.
- Include only USD invoices from the review month.
- Group by `vendor_id`.
- Use the preferred vendor name from `reference/vendor_directory.csv`
  when available.
- Sort rows by `vendor_id`.
- Format `total_amount` with two decimal places.
