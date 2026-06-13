# Lab Meeting — 2023-05-25

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Priya Iyer: outcome-weighted IPCW patch in for review
- Devon McAllister: cohort filter passing validation
- Anika Sato: Kestrel sensor pull came in
- Jay Patel: calibration plot bin boundaries updated, no surprises
- Saanvi Desai: DUA addendum confirmed current
- Priya Iyer: field-team dashboard refresh scheduled
- Felix Ruiz-Carrera: cohort filter passing validation
- Anika Sato: Felix's sensor pull script PR is up
- Devon McAllister: Kestrel sensor pull came in
- Erik Pohl: cohort filter passing validation
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Hari Mohan: Kestrel sensor pull came in
- Yui Tanaka: clinical review batch underway
- Bao Nguyen: Kestrel sensor pull came in

## Discussion notes

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

## Action items

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
