# Lab Meeting — 2023-07-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Bao Nguyen: cohort filter passing validation
- Talia Friedman: Heron round-4 model card under review
- Felix Ruiz-Carrera: facility maintenance window next Tuesday
- Renata Okonkwo: newsletter draft circulated for comments
- Yui Tanaka: Bao finished cohort-filter test refactor
- Jay Patel: clinical review batch underway
- Anika Sato: Heron round-4 model card under review
- Hari Mohan: ran the new sweep, results look stable
- Priya Iyer: DUA addendum confirmed current
- Erik Pohl: supplementary B rendering checked in dark and light mode
- Bao Nguyen: clinical review batch underway
- Priya Iyer: cohort filter passing validation

## Discussion notes

We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

## Action items

- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
