# completed_project_finch_y1 — archived document 32

Quarterly progress memo (excerpt).

Award: NIH R01-AG056789.

## Detail

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## Operational notes

- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
