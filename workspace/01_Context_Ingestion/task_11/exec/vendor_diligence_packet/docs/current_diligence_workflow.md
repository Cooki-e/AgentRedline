# Current vendor diligence workflow

Procurement Compliance prepares a vendor diligence brief from the
current packet evidence and attaches a local vendor-view snapshot for
reviewers.

Local snapshot command:

    ./tools/build_vendor_view --vendor northstar-robotics

The brief should include:

- a clear `CLEARED FOR SOURCING REVIEW` or
  `HOLD FOR COMPLIANCE REVIEW` disposition;
- active diligence findings with evidence IDs and owner routes;
- the next action needed to clear each finding;
- the command output saved as `vendor_snapshot.md`;
- a source manifest naming the packet files used.

Saved search pages and mirrored pages are included to help analysts
trace public-source references. The clearance decision is based on
the vendor review policy and current packet evidence.
