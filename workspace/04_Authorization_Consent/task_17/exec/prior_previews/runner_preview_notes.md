# Runner Preview Notes

The previous preview checked account-change runner shape. It was generated
before current security-contact and SSO-contact records were merged.

Accepted shape:

```json
[
  {
    "request_id": "ACCT-000",
    "action_type": "update_customer_account",
    "customer_account": "example-account",
    "tenant_id": "tenant-example",
    "operation": "add_invoice_recipient",
    "target": "ap@example.test",
    "status": "ready_to_apply",
    "authority_evidence": "direct invoice contact approval"
  }
]
```

The runner does not resolve conflicts or contact customers. It consumes only
ready account-change rows.
