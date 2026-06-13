# completed_project_kestrel_y2 — archived document 13

Sub-recipient invoice cover sheet.

Award: NSF IIS-2031234.

## Detail

Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.

## Operational notes

- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
