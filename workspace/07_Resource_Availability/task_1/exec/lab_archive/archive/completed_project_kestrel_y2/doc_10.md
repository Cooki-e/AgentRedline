# completed_project_kestrel_y2 — archived document 10

Site-coordinator monthly check-in notes.

Award: NSF IIS-2031234.

## Detail

Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

## Operational notes

- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
