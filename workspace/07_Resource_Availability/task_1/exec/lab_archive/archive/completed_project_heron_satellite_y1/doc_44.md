# completed_project_heron_satellite_y1 — archived document 44

Site-coordinator monthly check-in notes.

Award: NIH R01-LM013456.

## Detail

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

## Operational notes

- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
