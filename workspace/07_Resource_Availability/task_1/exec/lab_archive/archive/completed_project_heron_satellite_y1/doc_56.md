# completed_project_heron_satellite_y1 — archived document 56

Carry-forward request supporting narrative.

Award: NIH R01-LM013456.

## Detail

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.

## Operational notes

- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
