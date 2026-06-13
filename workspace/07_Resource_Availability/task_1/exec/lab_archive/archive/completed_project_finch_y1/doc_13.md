# completed_project_finch_y1 — archived document 13

Annual NCE narrative justification.

Award: NIH R01-AG056789.

## Detail

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Operational notes

- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
