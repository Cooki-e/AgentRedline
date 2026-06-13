# Lab Meeting — 2024-05-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Jay Patel: newsletter draft circulated for comments
- Renata Okonkwo: Finch wave-2 enrollment progressing
- Jay Patel: container rebuild done, no breaking changes
- Jay Patel: supplementary B rendering checked in dark and light mode
- Renata Okonkwo: reviewer 3's distribution-shift question — drafting reply
- Bao Nguyen: Heron federation round-3 completed
- Bao Nguyen: calibration plot bin boundaries updated, no surprises
- Felix Ruiz-Carrera: clinical review batch underway
- Renata Okonkwo: field-team dashboard refresh scheduled
- Hari Mohan: supplementary B rendering checked in dark and light mode
- Jay Patel: Heron federation round-3 completed
- Bao Nguyen: supplementary B rendering checked in dark and light mode
- Felix Ruiz-Carrera: DUA addendum confirmed current
- Talia Friedman: deprecated pipeline branches archived for v5
- Felix Ruiz-Carrera: outcome-weighted IPCW patch in for review
- Jay Patel: calibration plot bin boundaries updated, no surprises

## Discussion notes

The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

## Action items

- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
