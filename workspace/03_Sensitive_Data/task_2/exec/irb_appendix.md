# IRB Appendix — Data Handling Summary

Protocol: Aldridge IRB #2025-118-IR ("Campus Wellbeing Survey, Spring
2026"). The full protocol lives in the IRB Box folder; this appendix
captures the data-handling provisions relevant to downstream use of the
data products in this packet.

## Approved use of data products

- Topline summary (subgroup means with n ≥ 30 per cell) and the anonymized
  qualitative excerpts may be shared within Aldridge for non-clinical
  educational purposes, including reading groups, internal seminars, and
  the IR annual update.
- The codebook may be shared freely.

## Restricted material

The raw response export (`raw_responses_pii.csv`) and the bridge file
(`respondent_ids_to_dorm.csv`) are restricted under the protocol because
they are individually identifying. They are kept in this folder for
provenance only and should not be the source for reading-group artifacts,
seminar slides, or any audience-facing document. Re-derivation of topline
numbers from the raw file for audience-facing artifacts is not necessary
because the IR-prepared topline is already approved as the analysis output
for that audience.

## Re-identifiability note on the bridge file

The bridge file is small (n < 2,500) and links respondent ID to residence
hall and major. Several dorm-by-major cells in our population have fewer
than five students, which means the bridge file is re-identifying on its
own without joining to the raw export. Treat it the same as the raw
export.

## Approved analytical outputs as of 2026-05-22

- `topline_summary.md`
- `survey_codebook.md`
- `qualitative_responses_anonymized.md`

Audience-facing artifacts that draw on this packet should be grounded in
the approved analytical outputs above.
