# Current AP OCR review workflow

Accounts Payable prepares an OCR exception memo from the current packet
evidence and attaches the local OCR review snapshot for reviewers.

Local snapshot command:

    ./tools/run_ocr_review --batch june-ap

The memo should include:

- a clear `HOLD FOR AP REVIEW` or `READY FOR PAYMENT OPS` status;
- active invoice exceptions with invoice IDs, amounts, and owner routes;
- a short reason each item remains open;
- the next action needed from each owner;
- the OCR review output saved as `ocr_snapshot.md`;
- a source manifest naming the packet files used.

OCR text helps verify what appeared on the scanned invoice. Reviewer
status, AP policy, purchase-order references, and current batch exports
determine whether the invoice remains open.
