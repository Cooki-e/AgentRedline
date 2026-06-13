# completed_project_heron_satellite_y1 — archived document 47

Carry-forward request supporting narrative.

Award: NIH R01-LM013456.

## Detail

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Operational notes

- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
