# Architecture

`src/api/handlers.py` validates request envelopes and delegates to the
export service. `src/export/service.py` applies the warehouse filter
and calls `src/export/formatter.py` to render one row per accepted
order.

The formatter intentionally has no persistence side effects. Its
output is consumed by warehouse handoff jobs and support tooling.
