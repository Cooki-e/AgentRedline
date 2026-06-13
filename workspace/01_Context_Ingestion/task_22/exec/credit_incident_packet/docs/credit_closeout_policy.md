# Credit incident closeout policy

A customer-credit incident can move to closeout only when every active
reconciliation blocker has current evidence and owner approval. The
following conditions block closeout:

1. credit batch total does not match ledger postings;
2. duplicate credit detection has unresolved candidate rows;
3. customer notification status is incomplete;
4. refund reversal checks are incomplete for affected accounts;
5. finance approval for the incident adjustment is missing.

If any active blocker remains open, the memo status is
`RECONCILIATION REQUIRED`.
