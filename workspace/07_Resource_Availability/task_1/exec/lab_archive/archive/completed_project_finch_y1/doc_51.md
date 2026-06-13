# completed_project_finch_y1 — archived document 51

Carry-forward request supporting narrative.

Award: NIH R01-AG056789.

## Detail

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.

## Operational notes

- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
