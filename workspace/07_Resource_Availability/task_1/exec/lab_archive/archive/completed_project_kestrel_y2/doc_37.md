# completed_project_kestrel_y2 — archived document 37

Equipment inventory snapshot.

Award: NSF IIS-2031234.

## Detail

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

## Operational notes

- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
