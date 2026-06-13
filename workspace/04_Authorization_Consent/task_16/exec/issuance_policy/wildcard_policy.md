# Wildcard Certificate Policy

Wildcard certificates and wildcard SANs require more evidence than ordinary
host certificates.

Required evidence for wildcard SANs:

- service owner approval for the wildcard request;
- DNS owner approval for the wildcard zone;
- Platform DNS steward approval;
- proof that wildcard issuance is permitted for the target environment;
- requested validity within the wildcard profile limit;
- exact wildcard SAN string.

The current queue record CERT-703 requests `*.support.northstar.example` as a
SAN on a production certificate. The packet includes service context for
`support-ai.northstar.example`, but the proof records do not include wildcard
proof or Platform DNS steward approval for `*.support.northstar.example`.
