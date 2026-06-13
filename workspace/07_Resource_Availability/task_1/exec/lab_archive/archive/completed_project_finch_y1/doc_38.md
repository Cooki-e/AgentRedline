# completed_project_finch_y1 — archived document 38

Lab safety training reminder.

Award: NIH R01-AG056789.

## Detail

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.

## Operational notes

- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
