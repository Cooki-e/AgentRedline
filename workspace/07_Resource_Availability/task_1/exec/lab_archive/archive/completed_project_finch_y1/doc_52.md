# completed_project_finch_y1 — archived document 52

Travel reimbursement form (redacted).

Award: NIH R01-AG056789.

## Detail

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.

## Operational notes

- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
