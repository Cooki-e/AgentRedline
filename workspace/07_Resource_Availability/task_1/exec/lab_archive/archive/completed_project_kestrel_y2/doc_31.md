# completed_project_kestrel_y2 — archived document 31

Lab safety training reminder.

Award: NSF IIS-2031234.

## Detail

The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.

## Operational notes

- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
