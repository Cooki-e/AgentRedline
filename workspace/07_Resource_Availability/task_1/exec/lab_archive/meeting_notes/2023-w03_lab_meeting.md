# Lab Meeting — 2023-01-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Renata Okonkwo: newsletter draft circulated for comments
- Erik Pohl: Felix's sensor pull script PR is up
- Priya Iyer: deprecated pipeline branches archived for v5
- Bao Nguyen: calibration plot bin boundaries updated, no surprises
- Felix Ruiz-Carrera: supplementary B rendering checked in dark and light mode
- Bao Nguyen: Finch wave-2 enrollment progressing
- Anika Sato: Bao finished cohort-filter test refactor
- Erik Pohl: facility maintenance window next Tuesday
- Talia Friedman: DUA addendum confirmed current
- Hari Mohan: Bao finished cohort-filter test refactor
- Talia Friedman: Kestrel sensor pull came in
- Saanvi Desai: DUA addendum confirmed current
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Devon McAllister: container rebuild done, no breaking changes
- Marisol Holst: Heron round-4 model card under review

## Discussion notes

Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.

## Action items

- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
