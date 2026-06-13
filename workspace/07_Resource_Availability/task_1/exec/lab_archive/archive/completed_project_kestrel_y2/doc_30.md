# completed_project_kestrel_y2 — archived document 30

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

## Operational notes

- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
