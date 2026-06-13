# Lab Meeting — 2024-02-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Hari Mohan: deprecated pipeline branches archived for v5
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Felix Ruiz-Carrera: Bao finished cohort-filter test refactor
- Felix Ruiz-Carrera: clinical review batch underway
- Erik Pohl: JBI revision continues, funding section still on Jay
- Devon McAllister: DUA addendum confirmed current
- Erik Pohl: ran the new sweep, results look stable
- Jay Patel: DUA addendum confirmed current
- Saanvi Desai: clinical review batch underway
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply
- Devon McAllister: ran the new sweep, results look stable

## Discussion notes

Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

## Action items

- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
