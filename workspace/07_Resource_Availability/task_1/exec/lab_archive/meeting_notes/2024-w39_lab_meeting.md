# Lab Meeting — 2024-10-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Bao Nguyen: facility maintenance window next Tuesday
- Saanvi Desai: Finch wave-2 enrollment progressing
- Saanvi Desai: Bao finished cohort-filter test refactor
- Anika Sato: facility maintenance window next Tuesday
- Saanvi Desai: field-team dashboard refresh scheduled
- Yui Tanaka: field-team dashboard refresh scheduled
- Marisol Holst: supplementary B rendering checked in dark and light mode
- Hari Mohan: JBI revision continues, funding section still on Jay
- Marisol Holst: JBI revision continues, funding section still on Jay
- Felix Ruiz-Carrera: facility maintenance window next Tuesday
- Anika Sato: deprecated pipeline branches archived for v5

## Discussion notes

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

## Action items

- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
