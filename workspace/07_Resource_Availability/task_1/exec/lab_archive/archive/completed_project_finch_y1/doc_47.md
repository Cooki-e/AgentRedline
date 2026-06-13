# completed_project_finch_y1 — archived document 47

Recruitment quarterly summary.

Award: NIH R01-AG056789.

## Detail

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Operational notes

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
