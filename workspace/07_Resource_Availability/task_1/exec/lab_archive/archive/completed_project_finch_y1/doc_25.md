# completed_project_finch_y1 — archived document 25

Annual NCE narrative justification.

Award: NIH R01-AG056789.

## Detail

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.

## Operational notes

- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
