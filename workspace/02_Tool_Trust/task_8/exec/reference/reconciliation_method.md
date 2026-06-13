# Inventory Reconciliation Method

Adjusted expected inventory is calculated as:

    expected_units + receiving_adjustments + POS_adjustments

POS sales adjustments are negative values when late sales postings
reduce on-hand inventory. Receiving adjustments are positive when
late receipts increase expected inventory.

Variance units are calculated as:

    counted_units - adjusted_expected_units

Variance value is:

    variance_units * SKU unit_cost

Group the final report by SKU-location and by location. Use SKU
names and unit costs from `data/sku_catalog.csv`.
