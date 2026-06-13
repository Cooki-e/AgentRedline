# Lab Meeting — 2025-07-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Felix Ruiz-Carrera: field-team dashboard refresh scheduled
- Anika Sato: Heron round-4 model card under review
- Yui Tanaka: JBI revision continues, funding section still on Jay
- Renata Okonkwo: field-team dashboard refresh scheduled
- Anika Sato: supplementary B rendering checked in dark and light mode
- Bao Nguyen: Heron round-4 model card under review
- Marisol Holst: newsletter draft circulated for comments
- Felix Ruiz-Carrera: ran the new sweep, results look stable
- Priya Iyer: supplementary B rendering checked in dark and light mode
- Priya Iyer: container rebuild done, no breaking changes
- Renata Okonkwo: Kestrel sensor pull came in
- Anika Sato: newsletter draft circulated for comments
- Yui Tanaka: DUA addendum confirmed current
- Marisol Holst: facility maintenance window next Tuesday
- Talia Friedman: supplementary B rendering checked in dark and light mode
- Felix Ruiz-Carrera: Heron round-4 model card under review
- Marisol Holst: Heron round-4 model card under review

## Discussion notes

The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

## Action items

- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
