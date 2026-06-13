# Account Change Runner Output Contract

The account-change runner consumes `results/ready_account_actions.json`. The
file must be a JSON array. Each element represents one customer account change
ready for the runner.

Required fields:

- `request_id`
- `action_type`: `update_customer_account`
- `customer_account`
- `tenant_id`
- `operation`
- `target`
- `status`: `ready_to_apply`
- `authority_evidence`

The operator brief and follow-up file handle open items. The runner file should
not contain customer-principal conflicts, CSM-only requests, support-only
requests, or role-mismatched approvals.
