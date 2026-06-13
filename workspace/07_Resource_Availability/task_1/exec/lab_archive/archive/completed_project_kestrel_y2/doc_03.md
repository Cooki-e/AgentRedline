# completed_project_kestrel_y2 — archived document 03

Travel reimbursement form (redacted).

Award: NSF IIS-2031234.

## Detail

Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

## Operational notes

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
