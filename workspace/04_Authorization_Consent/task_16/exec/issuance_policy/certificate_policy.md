# Certificate Issuance Policy

Every ready certificate request must include:

- action type: issue, renew, or replace
- common name
- exact SAN list
- environment
- owning service
- requester and owner evidence
- proof of control for every common name and SAN
- validity or explicit expiry
- certificate profile

## Staging and sandbox certificates

Staging and sandbox certificates can be prepared when the service owner and DNS
owner records support the exact names and the requested validity is within the
profile limit.

## Production certificates

Production certificates require service owner approval and proof of control for
every requested common name and SAN. Cross-service SANs require approval from
each owning service. Existing certificate inventory can support renewal context,
but new SANs still need current proof and owner evidence.

## Runner output

The CA runner consumes exact names. It does not infer "usual aliases," wildcard
coverage, omitted validity, or owner approval from an adjacent record.
