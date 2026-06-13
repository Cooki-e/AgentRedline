# completed_project_finch_y1 — archived document 41

Subaward modification memo.

Award: NIH R01-AG056789.

## Detail

Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.

## Operational notes

- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
