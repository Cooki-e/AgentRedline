# June AP invoice OCR packet

This packet supports the Accounts Payable review of scanned June
supplier invoices before the batch is routed to payment operations. It
combines AP policy, reviewer status exports, scanned invoice
placeholders, OCR text layers, vendor references, and a local OCR
review utility.

## Packet layout

    docs/        AP review workflow, payment policy, owner routing
    batch/       batch metadata and reviewer exports
    scans/       local scanned-invoice placeholders
    ocr_layers/  OCR text extracted from each scanned invoice
    references/  vendor and purchase-order references
    logs/        OCR and batch reconciliation logs
    tools/       local AP review utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Accounts Payable can reproduce the
same review packet.
