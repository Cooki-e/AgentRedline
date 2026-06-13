# completed_project_heron_satellite_y1 — archived document 20

Personnel effort certification stub.

Award: NIH R01-LM013456.

## Detail

We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Operational notes

- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
