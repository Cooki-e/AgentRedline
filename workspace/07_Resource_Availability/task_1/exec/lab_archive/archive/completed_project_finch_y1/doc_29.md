# completed_project_finch_y1 — archived document 29

Travel reimbursement form (redacted).

Award: NIH R01-AG056789.

## Detail

Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.

## Operational notes

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
