# completed_project_finch_y1 — archived document 54

Travel reimbursement form (redacted).

Award: NIH R01-AG056789.

## Detail

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.

## Operational notes

- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
