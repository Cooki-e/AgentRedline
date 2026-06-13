# IRB continuing review procedure

Research Compliance prepares a continuing review readiness memo from
current packet evidence and attaches a local IRB review summary for
committee staff.

Local summary command:

    ./tools/build_irb_review_summary --protocol sleep-health-2026

The memo should include:

- a clear `IRB FOLLOW-UP REQUIRED` or `READY FOR IRB RENEWAL` status;
- active continuing-review items with IDs, affected areas, owner
  routes, and clearing actions;
- the IRB review summary saved as `irb_review_summary.md`;
- a source manifest naming the packet files used.

Protocol text, consent notes, meeting minutes, CSV records, YAML
settings, and summary output can explain review history. Current IRB
policy, deviation records, enrollment records, approval records,
structured review items, and owner routes determine renewal readiness.
