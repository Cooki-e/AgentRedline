# Lab Meeting — 2025-09-19

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Renata Okonkwo: Felix's sensor pull script PR is up
- Jay Patel: calibration plot bin boundaries updated, no surprises
- Talia Friedman: ran the new sweep, results look stable
- Hari Mohan: container rebuild done, no breaking changes
- Devon McAllister: Bao finished cohort-filter test refactor
- Anika Sato: ran the new sweep, results look stable
- Marisol Holst: DUA addendum confirmed current
- Bao Nguyen: Felix's sensor pull script PR is up
- Marisol Holst: Kestrel sensor pull came in
- Saanvi Desai: JBI revision continues, funding section still on Jay
- Bao Nguyen: Bao finished cohort-filter test refactor

## Discussion notes

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

## Action items

- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
