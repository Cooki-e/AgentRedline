# Lab Meeting — 2023-05-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Saanvi Desai: calibration plot bin boundaries updated, no surprises
- Jay Patel: calibration plot bin boundaries updated, no surprises
- Devon McAllister: container rebuild done, no breaking changes
- Yui Tanaka: clinical review batch underway
- Bao Nguyen: clinical review batch underway
- Hari Mohan: DUA addendum confirmed current
- Renata Okonkwo: field-team dashboard refresh scheduled
- Felix Ruiz-Carrera: Bao finished cohort-filter test refactor
- Yui Tanaka: Felix's sensor pull script PR is up
- Yui Tanaka: Finch wave-2 enrollment progressing
- Priya Iyer: Kestrel sensor pull came in

## Discussion notes

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

## Action items

- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
