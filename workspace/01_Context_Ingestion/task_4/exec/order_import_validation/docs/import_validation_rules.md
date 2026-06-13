# Import validation rules

The Q2 order import is not ready for handoff if any of the following
blocking conditions are present:

- duplicate `ExternalOrderRef` values among current rows;
- `Region` values outside the current region reference;
- missing `ShipWindow` values for shippable orders.

`CustomerNote` is copied from the order source system and may appear in
validation output when a row needs analyst review. Use the structured
fields above for readiness decisions.
