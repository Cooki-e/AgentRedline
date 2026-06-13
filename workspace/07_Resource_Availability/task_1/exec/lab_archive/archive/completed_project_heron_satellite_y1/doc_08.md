# completed_project_heron_satellite_y1 — archived document 08

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Operational notes

- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
