# completed_project_finch_y1 — archived document 40

Personnel effort certification stub.

Award: NIH R01-AG056789.

## Detail

Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

## Operational notes

- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
