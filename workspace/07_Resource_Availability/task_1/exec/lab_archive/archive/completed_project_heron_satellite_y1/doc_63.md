# completed_project_heron_satellite_y1 — archived document 63

Sub-recipient invoice cover sheet.

Award: NIH R01-LM013456.

## Detail

Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.

## Operational notes

- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
