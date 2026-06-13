# completed_project_kestrel_y2 — archived document 55

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

## Operational notes

- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
