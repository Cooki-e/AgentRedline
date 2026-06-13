# Lab Meeting — 2025-05-25

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: Bao finished cohort-filter test refactor
- Devon McAllister: JBI revision continues, funding section still on Jay
- Erik Pohl: Heron round-4 model card under review
- Talia Friedman: newsletter draft circulated for comments
- Hari Mohan: outcome-weighted IPCW patch in for review
- Marisol Holst: cohort filter passing validation
- Priya Iyer: calibration plot bin boundaries updated, no surprises
- Jay Patel: DUA addendum confirmed current
- Hari Mohan: calibration plot bin boundaries updated, no surprises
- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Devon McAllister: field-team dashboard refresh scheduled
- Erik Pohl: supplementary B rendering checked in dark and light mode
- Felix Ruiz-Carrera: supplementary B rendering checked in dark and light mode
- Hari Mohan: Heron round-4 model card under review

## Discussion notes

IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.

## Action items

- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
