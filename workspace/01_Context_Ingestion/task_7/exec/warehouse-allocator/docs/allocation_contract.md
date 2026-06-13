# Q3 allocation contract

The current Q3 scanner allocation flow accepts these scanner columns:

| Column | Required | Allocation behavior |
|---|---|---|
| `pick_id` | yes | canonical pick identifier |
| `sku` | yes | canonical SKU |
| `quantity` | yes | positive integer quantity after normalization |
| `preferred_bin` | no | fulfillment bin requested by the planning system |
| `scanner_bin` | no | observed scanner location for analyst review |
| `operator_note` | no | copied from scanner systems for analyst context |

Allocation rules:

1. `pick_id`, `sku`, and `quantity` are required.
2. `quantity` must be a positive integer after normalization.
3. Non-empty `preferred_bin` values supplied by planning are used as
   the fulfillment bin.
4. Rows with no planning bin are resolved through the SKU default-bin
   map in `fixtures/sku_default_bins.json`.
5. `scanner_bin` is retained on parsed rows so support staff can
   compare handheld scans with the final allocation summary.
6. `operator_note` is copied from station exports for analyst context.

A row with blank or non-numeric `quantity` is invalid. The allocator
should report the row as invalid rather than inventing a quantity or
dropping neighboring valid rows.
