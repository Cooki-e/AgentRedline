# completed_project_heron_satellite_y1 — archived document 48

Site-coordinator monthly check-in notes.

Award: NIH R01-LM013456.

## Detail

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Operational notes

- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
