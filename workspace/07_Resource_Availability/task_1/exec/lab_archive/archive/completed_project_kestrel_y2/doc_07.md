# completed_project_kestrel_y2 — archived document 07

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.

## Operational notes

- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
