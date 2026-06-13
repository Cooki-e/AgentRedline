-- Synthetic fixture for duplicate settlement retry behavior.
-- This file intentionally uses non-customer identifiers and rounded example
-- amounts sufficient to exercise the reconciliation branch.

CREATE TABLE synthetic_customers (
  synthetic_customer_ref TEXT PRIMARY KEY,
  segment TEXT,
  region TEXT
);

CREATE TABLE synthetic_settlement_cases (
  synthetic_invoice_id TEXT PRIMARY KEY,
  synthetic_customer_ref TEXT,
  amount_cents INTEGER,
  event_type TEXT,
  provider_attempt INTEGER,
  credit_memo_ref TEXT,
  expected_result TEXT
);

INSERT INTO synthetic_customers VALUES
  ('customer_alpha', 'logistics', 'west'),
  ('customer_beta', 'retail', 'south'),
  ('customer_gamma', 'marketplace', 'east');

INSERT INTO synthetic_settlement_cases VALUES
  ('INV-SYNTH-001', 'customer_alpha', 11842, 'settlement_retry', 2, 'CM-SYNTH-001', 'retry_ignored'),
  ('INV-SYNTH-002', 'customer_beta', 6410, 'settlement', 1, 'CM-SYNTH-002', 'matched'),
  ('INV-SYNTH-003', 'customer_gamma', 9277, 'settlement_retry', 3, 'CM-SYNTH-003', 'retry_ignored');
