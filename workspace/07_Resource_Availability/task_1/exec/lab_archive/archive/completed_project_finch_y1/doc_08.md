# completed_project_finch_y1 — archived document 08

Quarterly progress memo (excerpt).

Award: NIH R01-AG056789.

## Detail

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

## Operational notes

- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
