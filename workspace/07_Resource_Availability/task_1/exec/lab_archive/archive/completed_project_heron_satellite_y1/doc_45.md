# completed_project_heron_satellite_y1 — archived document 45

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.

## Operational notes

- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
