# completed_project_heron_satellite_y1 — archived document 16

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.

## Operational notes

- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
