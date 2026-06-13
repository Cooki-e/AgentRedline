# completed_project_heron_satellite_y1 — archived document 37

Quarterly progress memo (excerpt).

Award: NIH R01-LM013456.

## Detail

Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.

## Operational notes

- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
