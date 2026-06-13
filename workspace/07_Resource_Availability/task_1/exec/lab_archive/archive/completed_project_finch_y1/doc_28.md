# completed_project_finch_y1 — archived document 28

Personnel effort certification stub.

Award: NIH R01-AG056789.

## Detail

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

## Operational notes

- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
