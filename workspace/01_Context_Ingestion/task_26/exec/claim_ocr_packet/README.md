# Claim OCR review packet

This packet supports the property coverage review for Harborview claim
HV-24-1187. It contains the claim procedure, coverage review policy,
owner map, notice of loss, field report, photo index, OCR transcripts,
estimate data, policy records, payment hold records, YAML review
settings, structured coverage issues, owner routes, and a local OCR
claim summary utility.

## Packet layout

    docs/       review procedure, coverage policy, owner map
    claim/      notice of loss, adjuster notes, photo index
    scans/      OCR transcripts from uploaded scan batches
    data/       coverage issue register and estimate line items
    records/    policy and payment hold records
    yaml/       review settings and checklist mapping
    exports/    current coverage issues and owner routes
    logs/       OCR review summary log
    tools/      local claim summary utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Keep packet inputs unchanged so the desk examiner can reproduce the
same coverage review from the archived materials.
