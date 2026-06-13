# Lab Meeting — 2024-07-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Marisol Holst: cohort filter passing validation
- Anika Sato: Heron federation round-3 completed
- Erik Pohl: Kestrel sensor pull came in
- Renata Okonkwo: facility maintenance window next Tuesday
- Devon McAllister: field-team dashboard refresh scheduled
- Anika Sato: ran the new sweep, results look stable
- Saanvi Desai: Heron federation round-3 completed
- Marisol Holst: field-team dashboard refresh scheduled
- Felix Ruiz-Carrera: DUA addendum confirmed current
- Felix Ruiz-Carrera: calibration plot bin boundaries updated, no surprises
- Felix Ruiz-Carrera: Finch wave-2 enrollment progressing
- Yui Tanaka: facility maintenance window next Tuesday
- Marisol Holst: clinical review batch underway
- Erik Pohl: Heron federation round-3 completed

## Discussion notes

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

## Action items

- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
