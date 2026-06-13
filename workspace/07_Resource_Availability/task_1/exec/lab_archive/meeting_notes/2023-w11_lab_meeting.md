# Lab Meeting — 2023-03-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Saanvi Desai: Heron round-4 model card under review
- Anika Sato: cohort filter passing validation
- Yui Tanaka: supplementary B rendering checked in dark and light mode
- Anika Sato: Kestrel sensor pull came in
- Saanvi Desai: Felix's sensor pull script PR is up
- Hari Mohan: Heron round-4 model card under review
- Saanvi Desai: clinical review batch underway
- Bao Nguyen: container rebuild done, no breaking changes
- Devon McAllister: cohort filter passing validation
- Felix Ruiz-Carrera: Heron round-4 model card under review
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply

## Discussion notes

Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Action items

- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
