# June vendor payment packet

This packet supports the Finance Operations payment review for the
June vendor batch. The current payment state is assembled from invoice
exports, bank validation results, approval records, exception queue
entries, vendor registry data, and saved queue activity.

## Local packet layout

    docs/           current workflow, payment policy, and owner routing
    exports/        current invoice, vendor, validation, and approval data
    queue_archive/  saved queue activity for local review
    logs/           reconciliation run output
    tools/          local reconciliation utilities

Final analyst artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so Finance Operations can reproduce the
payment review.
