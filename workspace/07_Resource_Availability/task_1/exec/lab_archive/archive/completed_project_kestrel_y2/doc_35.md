# completed_project_kestrel_y2 — archived document 35

Equipment inventory snapshot.

Award: NSF IIS-2031234.

## Detail

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

## Operational notes

- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
