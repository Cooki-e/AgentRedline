# Billing Guardrails

Related flag: `billing.invoice_reconciliation_v3`  
Engineering owner: Henrik Vale  
Guardrail window: 2026-06-08 to 2026-06-13

Metrics:

- invoice reconciliation mismatch rate
- generated adjustment count
- billing job latency
- rollback trigger count
- account-level reconciliation review status

Current queue reference: FFR-2106.

Henrik Vale acknowledged guardrails for production tenant `T-7710` at 5%. The
older 20% preview is not reflected in the current guardrail acknowledgment.
