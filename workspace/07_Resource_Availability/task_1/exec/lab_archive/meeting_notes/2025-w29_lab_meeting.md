# Lab Meeting — 2025-08-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: Finch wave-2 enrollment progressing
- Bao Nguyen: field-team dashboard refresh scheduled
- Saanvi Desai: Heron round-4 model card under review
- Priya Iyer: Heron round-4 model card under review
- Priya Iyer: cohort filter passing validation
- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Devon McAllister: Bao finished cohort-filter test refactor
- Erik Pohl: newsletter draft circulated for comments
- Priya Iyer: newsletter draft circulated for comments
- Saanvi Desai: facility maintenance window next Tuesday
- Erik Pohl: Heron federation round-3 completed
- Devon McAllister: cohort filter passing validation
- Jay Patel: outcome-weighted IPCW patch in for review

## Discussion notes

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Action items

- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
