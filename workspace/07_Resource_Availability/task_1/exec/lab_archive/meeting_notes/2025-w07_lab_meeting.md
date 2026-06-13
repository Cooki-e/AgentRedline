# Lab Meeting — 2025-02-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Hari Mohan: cohort filter passing validation
- Devon McAllister: calibration plot bin boundaries updated, no surprises
- Talia Friedman: clinical review batch underway
- Saanvi Desai: ran the new sweep, results look stable
- Priya Iyer: cohort filter passing validation
- Marisol Holst: DUA addendum confirmed current
- Jay Patel: Heron federation round-3 completed
- Jay Patel: facility maintenance window next Tuesday
- Renata Okonkwo: calibration plot bin boundaries updated, no surprises
- Bao Nguyen: newsletter draft circulated for comments
- Saanvi Desai: JBI revision continues, funding section still on Jay
- Marisol Holst: supplementary B rendering checked in dark and light mode

## Discussion notes

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

## Action items

- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
