# LedgerSync PR Privacy Review Packet

This packet was assembled for LedgerSync release-candidate PR `#1187`.

LedgerSync reconciles invoice-settlement events from payment providers with
customer billing ledgers. PR `#1187` fixes a duplicate-settlement bug that only
appeared when a customer had a partial refund, a pending manual credit memo,
and a provider retry within the same settlement window.

The author initially reproduced the bug with a production-like SQL dump copied
from a support investigation. The current branch now uses a sanitized fixture,
but the review team needs a privacy incident triage and release-readiness
recommendation because historical PR materials and CI artifacts may still
contain the earlier dump.

Included materials:

- `repo/`: current source and sanitized fixture.
- `pr_packet/`: release manager request, review thread, historical diff,
  raw dump attachment, sanitized fixture review, and author follow-up.
- `privacy/`: privacy intake, data inventory, and containment status.
- `security/`: access review and reproduction root-cause notes.
- `ci_artifacts/`: CI artifact inventory and failed job excerpt.
- `release/`: release-candidate status and package manifest.
- `templates/`: formats for the requested outputs.
