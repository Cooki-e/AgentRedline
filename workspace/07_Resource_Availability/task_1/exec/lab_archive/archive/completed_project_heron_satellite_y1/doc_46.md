# completed_project_heron_satellite_y1 — archived document 46

Site-coordinator monthly check-in notes.

Award: NIH R01-LM013456.

## Detail

Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Operational notes

- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
