# Warehouse Credential Rotation

Prepared: 2026-06-03 10:42 UTC
Prepared by: Data Platform

## Affected Material Family

- Warehouse read-only DSN for MetroBike Wave 3.
- Warehouse read-only token for notebook access.
- Environment: protected research warehouse.
- Intended audience: approved study personnel.

## Status

- Old warehouse notebook token revoked: 2026-06-03 10:25 UTC.
- Old DSN password rotated: 2026-06-03 10:27 UTC.
- Replacement credential stored in the study vault: 2026-06-03 10:31 UTC.
- Replacement credential not used in public repository files.
- Data Platform owner confirmation: Jamie Kwan, 2026-06-03 10:35 UTC.

## Notes

The old material was read-only and scoped to the MetroBike Wave 3 protected
warehouse. The scan did not find the old material in the current public
manifest. Data Platform recommends generating a fresh archive preview from the
clean manifest after Repository Operations confirms deletion of the old preview.
