# Price Audit Component

The price audit component builds an exception table and summary
metrics from local catalog pricing packet files.

Example:

    python3 tools/price_audit/build_exception_table.py --base-prices data/base_price_list_june.csv --channel-prices data/channel_price_export_june.csv --costs data/unit_costs.csv --sku-master data/sku_master.csv --promos data/promo_calendar_june.csv --price-plan data/july_price_plan.csv --weekly-units data/channel_weekly_units.csv --policy reference/pricing_policy.md --thresholds reference/margin_thresholds.md --taxonomy reference/exception_taxonomy.md --output results/price_exception_table.csv --metrics results/price_exception_metrics.json
