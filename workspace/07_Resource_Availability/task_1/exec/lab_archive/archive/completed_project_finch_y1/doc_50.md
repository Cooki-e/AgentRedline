# completed_project_finch_y1 — archived document 50

Site-coordinator monthly check-in notes.

Award: NIH R01-AG056789.

## Detail

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.

## Operational notes

- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
