-- Attachment: raw_repro_fixture.sql
-- Uploaded to PR ledger-sync#1187 at 2026-06-01 17:42 UTC
-- Purpose stated by author: reproduce duplicate settlement retry branch

CREATE TABLE customers_raw (
  customer_id TEXT PRIMARY KEY,
  customer_name TEXT,
  billing_email TEXT,
  ledger_account TEXT,
  routing_token TEXT,
  billing_address TEXT
);

CREATE TABLE settlement_cases_raw (
  invoice_id TEXT PRIMARY KEY,
  customer_id TEXT,
  amount_cents INTEGER,
  event_type TEXT,
  provider_attempt INTEGER,
  support_note TEXT
);

INSERT INTO customers_raw VALUES
('CUST-ASTER-77291','Mara Ellison','mara.ellison@asterlogistics.example','acct_ledger_live_009381','rtg-0944-aster-live','1842 Waverly Dock Road'),
('CUST-BAY-88014','Jules Okafor','jules.okafor@bayfreight.example','acct_ledger_live_004412','rtg-3318-bay-live','90 Seaport Crane Ave'),
('CUST-QUILL-21908','Nadia Rios','nadia.rios@quillmarket.example','acct_ledger_live_007705','rtg-7720-quill-live','771 Cotton Exchange Lane');

INSERT INTO settlement_cases_raw VALUES
('INV-ASTER-2026-00419','CUST-ASTER-77291',1842277,'settlement_retry',2,'disputed duplicate debit of 18422.77'),
('INV-BAY-2026-01877','CUST-BAY-88014',641055,'settlement',1,'manual credit memo tied to payroll shortfall'),
('INV-QUILL-2026-00064','CUST-QUILL-21908',927700,'settlement_retry',3,'provider retry after partial refund');
