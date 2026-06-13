# completed_project_heron_satellite_y1 — archived document 24

IRB renewal acknowledgment.

Award: NIH R01-LM013456.

## Detail

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

## Operational notes

- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
