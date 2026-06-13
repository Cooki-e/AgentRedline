# Lab Meeting — 2023-12-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Felix Ruiz-Carrera: clinical review batch underway
- Erik Pohl: container rebuild done, no breaking changes
- Priya Iyer: deprecated pipeline branches archived for v5
- Renata Okonkwo: cohort filter passing validation
- Yui Tanaka: ran the new sweep, results look stable
- Saanvi Desai: Heron round-4 model card under review
- Talia Friedman: Bao finished cohort-filter test refactor
- Felix Ruiz-Carrera: outcome-weighted IPCW patch in for review
- Hari Mohan: Kestrel sensor pull came in
- Saanvi Desai: Heron federation round-3 completed
- Saanvi Desai: newsletter draft circulated for comments
- Priya Iyer: DUA addendum confirmed current
- Jay Patel: Felix's sensor pull script PR is up
- Hari Mohan: Heron round-4 model card under review
- Yui Tanaka: cohort filter passing validation
- Talia Friedman: newsletter draft circulated for comments

## Discussion notes

Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

## Action items

- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
