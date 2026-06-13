# Legacy changelog excerpts

## 2025-11 partner-uploader compatibility

Partner uploader compatibility briefly allowed summaries to omit
zero-allocation invoice rows after a credit memo was exhausted. That
behavior reduced payload size for an external partner export but was
retired before the current AP review contract.

## 2026-02 integer cents cleanup

Allocation internals were moved to integer cents to avoid fractional
rounding drift in small residual balances.
