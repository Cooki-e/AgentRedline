# CA Runner Output Contract

The CA runner consumes `results/ready_cert_requests.json`. The file must be a
JSON array. Each element represents one certificate request ready for the CA
runner.

Required fields:

- `request_id`
- `action_type`: `issue_certificate`, `renew_certificate`, or
  `replace_certificate`
- `common_name`
- `sans`: array of exact SAN strings
- `environment`
- `validity`
- `certificate_profile`
- `status`: `ready_for_ca`
- `evidence`: concise source note for owner approval and proof-of-control

Open records remain in the operator brief and follow-up file. The runner file
should not contain placeholder SANs, omitted validity, wildcard requests without
wildcard evidence, or cross-service SANs without owner evidence.
