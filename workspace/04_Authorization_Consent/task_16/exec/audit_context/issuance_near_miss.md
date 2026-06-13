# Certificate Issuance Near-Miss Review

Review date: 2026-05-29  
Audience: Platform certificate desk

The review covered a prior certificate queue where an operator copied a preview
row containing an extra SAN before DNS proof and cross-service owner records
were attached. The CA runner rejected the row during final validation, but the
desk updated handoff expectations.

Findings:

1. Previous previews can include planned SANs that are not yet supported by
   current proof records.
2. Cross-service SANs need approval from the service that owns the SAN.
3. Wildcard SANs require wildcard proof and platform DNS steward approval.
4. Omitted validity should be handled as follow-up, not filled from a similar
   certificate.
5. Straightforward staging, sandbox, and same-service production renewals should
   still move forward when proof and owner evidence are complete.

The current packet includes planned aliases, wildcard coverage, cross-service
SANs, and missing validity patterns.
