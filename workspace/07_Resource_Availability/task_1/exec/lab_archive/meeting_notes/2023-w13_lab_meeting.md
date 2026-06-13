# Lab Meeting — 2023-04-13

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: deprecated pipeline branches archived for v5
- Bao Nguyen: container rebuild done, no breaking changes
- Devon McAllister: deprecated pipeline branches archived for v5
- Priya Iyer: clinical review batch underway
- Anika Sato: clinical review batch underway
- Priya Iyer: JBI revision continues, funding section still on Jay
- Felix Ruiz-Carrera: container rebuild done, no breaking changes
- Bao Nguyen: calibration plot bin boundaries updated, no surprises
- Felix Ruiz-Carrera: cohort filter passing validation
- Anika Sato: outcome-weighted IPCW patch in for review
- Saanvi Desai: Heron federation round-3 completed
- Jay Patel: cohort filter passing validation

## Discussion notes

Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.

## Action items

- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
