# Lab Meeting — 2023-02-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: calibration plot bin boundaries updated, no surprises
- Saanvi Desai: facility maintenance window next Tuesday
- Priya Iyer: facility maintenance window next Tuesday
- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Priya Iyer: newsletter draft circulated for comments
- Hari Mohan: clinical review batch underway
- Priya Iyer: clinical review batch underway
- Renata Okonkwo: calibration plot bin boundaries updated, no surprises
- Marisol Holst: Heron federation round-3 completed
- Felix Ruiz-Carrera: DUA addendum confirmed current
- Felix Ruiz-Carrera: ran the new sweep, results look stable
- Talia Friedman: deprecated pipeline branches archived for v5
- Yui Tanaka: clinical review batch underway
- Marisol Holst: newsletter draft circulated for comments
- Erik Pohl: DUA addendum confirmed current

## Discussion notes

Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.

## Action items

- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
