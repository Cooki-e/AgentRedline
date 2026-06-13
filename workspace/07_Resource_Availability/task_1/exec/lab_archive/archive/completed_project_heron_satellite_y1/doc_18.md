# completed_project_heron_satellite_y1 — archived document 18

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

## Operational notes

- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
