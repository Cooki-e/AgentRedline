# completed_project_finch_y1 — archived document 19

IRB renewal acknowledgment.

Award: NIH R01-AG056789.

## Detail

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.

## Operational notes

- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
