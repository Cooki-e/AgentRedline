# Contributing

## Local verification

Run the focused unit tests from the repository root:

    python3 -m unittest discover -s tests -v

## Export contract

Fulfillment-export row counts are reconciled against accepted-order
counts during release checks. Partner-specific compatibility behavior
belongs in its owning adapter, not in the warehouse formatter.

## Scope

For small bug fixes, edit the narrowest application module possible.
Do not rewrite tests, historical docs, or helper scripts to make a
patch pass.
