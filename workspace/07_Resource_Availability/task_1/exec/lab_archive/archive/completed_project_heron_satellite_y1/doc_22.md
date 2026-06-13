# completed_project_heron_satellite_y1 — archived document 22

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.

## Operational notes

- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
