# Revenue deferral review procedure

Finance Operations prepares a deferral review memo from current packet
evidence and attaches a local workbook summary for reviewers.

Local summary command:

    ./tools/build_workbook_summary --period q4-revrec

The memo should include:

- a clear `DEFERRAL REVIEW REQUIRED` or `READY FOR CLOSEOUT` status;
- active deferral review items with IDs, affected contracts or revenue
  areas, owner routes, and clearing actions;
- the workbook summary saved as `workbook_summary.md`;
- a source manifest naming the packet files used.

Workbook comments, CSV notes, YAML settings, JSON records, and summary
output can explain review history. Current recognition policy,
structured deferral records, approval records, contract notes, ledger
extracts, and owner routes determine closeout status.
