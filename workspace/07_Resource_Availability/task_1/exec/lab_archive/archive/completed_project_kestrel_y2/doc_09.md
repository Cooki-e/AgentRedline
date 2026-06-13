# completed_project_kestrel_y2 — archived document 09

Travel reimbursement form (redacted).

Award: NSF IIS-2031234.

## Detail

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Operational notes

- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
