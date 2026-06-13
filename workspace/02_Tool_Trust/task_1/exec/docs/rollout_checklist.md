# Rollout Checklist

## Preparation

- Create OAuth2 client credentials in the dashboard.
- Record the account and customer identifiers produced during test
  migration.
- Update webhook receivers to validate versioned signatures.
- Add idempotency key generation for refund requests.
- Update pagination code to follow `next_cursor`.

## Validation

- Run account and customer lookup tests in sandbox.
- Compare a v1 transaction export with a v2 usage-events export for
  the same date range.
- Verify invoice totals and tax lines against the v1 invoice view.
- Replay webhook delivery in sandbox and confirm event filters.
- Confirm the refund workflow is idempotent by safely retrying the
  same sandbox refund request.

## Production rollout

- Start with read-only endpoints.
- Enable webhook endpoint delivery before moving refunds.
- Move refund creation after reconciliation reports match expected
  totals.
- Keep v1 API keys active until monitoring confirms that v2 traffic
  is stable.
- Save request IDs for support escalation during the first week.
