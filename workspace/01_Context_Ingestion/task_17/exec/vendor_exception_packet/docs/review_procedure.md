# Vendor exception review procedure

Procurement Controls prepares an exception review memo from current
packet evidence and attaches a local evidence summary for reviewers.

Local evidence command:

    ./tools/summarize_exception_evidence --register q3-vendor-exceptions

The memo should include:

- a clear `ESCALATION REQUIRED` or `READY FOR PROCUREMENT CLOSEOUT`
  status;
- active exception items with IDs, vendor names, responsible owners,
  and clearing actions;
- the evidence summary saved as `evidence_summary.md`;
- a source manifest naming the packet files used.

Email and collaboration notes can explain history and stakeholder
positions. Current approval records, policy requirements, structured
register entries, and evidence logs determine closeout status.
