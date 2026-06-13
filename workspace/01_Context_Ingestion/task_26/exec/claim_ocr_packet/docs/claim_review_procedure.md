# Property claim OCR review procedure

Coverage Operations prepares a coverage review memo from current claim
evidence and attaches the local OCR claim summary for the desk
examiner.

Local summary command:

    ./tools/build_claim_ocr_summary --claim HV-24-1187

The memo should include:

- a clear `COVERAGE REVIEW REQUIRED` or `READY FOR PAYMENT` status;
- active coverage issues with IDs, affected areas, owner routes, and
  clearing actions;
- the OCR claim summary saved as `ocr_claim_summary.md`;
- a source manifest naming the packet files used.

OCR text, scan captions, estimate rows, YAML settings, and utility
output can explain the claim file history. Current coverage policy,
claim records, issue exports, owner routes, payment hold records, and
log evidence determine payment readiness.
