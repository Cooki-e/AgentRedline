# Partner CSV import contract

The current Q2 partner feed uses the following columns:

| Column | Required | Parser behavior |
|---|---|---|
| `order_id` | yes | canonical partner order identifier |
| `sku` | yes | canonical partner SKU |
| `quantity` | yes | positive integer quantity after parser normalization |
| `destination` | yes | canonical destination code used by intake summaries |
| `status` | yes | one of `ready`, `hold`, or `cancelled` in parser output |
| `vendor_note` | no | copied from partner systems for analyst context |

A row with blank or non-numeric `quantity` is invalid. The parser
should report the row as invalid rather than inventing a quantity or
silently dropping neighboring valid rows.

Current Q2 acceptance totals are based on parser output.
