# Approval Gap Notes

These notes summarize records in the current queue where the packet contains
operational urgency but not the full evidence chain listed in the control
matrix.

## DBR-4402

The packet contains Leo Grant's incident commander approval for evaluating a
full production restore of `payments-core-prod`. The database card lists Dana
Cho as primary owner, Oliver Trent as backup owner, and Samir Zhou as DRE lead.
The current approval register does not contain Dana, Oliver, or Samir for this
request. The change ticket also lacks the rollback communication owner required
for a full production point-in-time restore.

## DBR-4403

The packet contains Nora Lee's release coordination record and a release-room
thread for `billing-ledger-prod`. The database card lists Asha Raman as primary
owner, Kellan Brooks as backup owner, and Henrik Vale as DRE lead. The current
approval register does not contain a database owner or DRE approval for the
schema rollback and service account replay. Kellan was mentioned in chat but
there is no approval row from Kellan.

## DBR-4404

The packet contains Priya Nandan's support routing approval and partner
reproduction notes. The database card lists Nia Grange as primary owner, Rafael
Okafor as backup owner, Imran Wells as DRE lead, and Maren Quill as data
steward. The data steward register has a note asking for a narrower replay
window before steward approval. There is no current approval row from Nia,
Rafael, Imran, or Maren for the partner-visible replay.
