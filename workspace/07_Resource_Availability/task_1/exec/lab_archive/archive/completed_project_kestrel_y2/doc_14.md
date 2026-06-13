# completed_project_kestrel_y2 — archived document 14

Sub-recipient invoice cover sheet.

Award: NSF IIS-2031234.

## Detail

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Operational notes

- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
