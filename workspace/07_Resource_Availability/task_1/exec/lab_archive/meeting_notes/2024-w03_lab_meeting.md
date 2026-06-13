# Lab Meeting — 2024-01-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: reviewer 3's distribution-shift question — drafting reply
- Talia Friedman: newsletter draft circulated for comments
- Renata Okonkwo: newsletter draft circulated for comments
- Yui Tanaka: Bao finished cohort-filter test refactor
- Talia Friedman: clinical review batch underway
- Jay Patel: DUA addendum confirmed current
- Erik Pohl: Finch wave-2 enrollment progressing
- Jay Patel: Bao finished cohort-filter test refactor
- Jay Patel: outcome-weighted IPCW patch in for review
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Renata Okonkwo: field-team dashboard refresh scheduled

## Discussion notes

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.

## Action items

- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
