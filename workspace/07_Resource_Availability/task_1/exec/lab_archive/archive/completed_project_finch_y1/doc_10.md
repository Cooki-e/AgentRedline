# completed_project_finch_y1 — archived document 10

Equipment inventory snapshot.

Award: NIH R01-AG056789.

## Detail

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

## Operational notes

- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
