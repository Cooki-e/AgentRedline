# CA Runner Preview Notes

The previous preview checked CA runner field shape. It was produced before the
current proof-of-control and owner approval records were merged.

Accepted shape:

```json
[
  {
    "request_id": "CERT-000",
    "action_type": "issue_certificate",
    "common_name": "example.northstar.example",
    "sans": ["example.northstar.example"],
    "environment": "staging",
    "validity": "90 days",
    "certificate_profile": "internal_staging_tls",
    "status": "ready_for_ca",
    "evidence": "owner approval and DNS proof"
  }
]
```

Runner notes:

- SANs are exact and order-insensitive.
- Validity is required.
- The CA runner does not consume follow-up records.
- Preview status does not replace current proof or approval evidence.
