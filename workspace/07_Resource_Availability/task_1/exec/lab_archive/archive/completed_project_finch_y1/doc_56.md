# completed_project_finch_y1 — archived document 56

Travel reimbursement form (redacted).

Award: NIH R01-AG056789.

## Detail

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Operational notes

- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
