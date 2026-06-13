# Lab Meeting — 2023-06-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: Kestrel sensor pull came in
- Erik Pohl: Kestrel sensor pull came in
- Saanvi Desai: JBI revision continues, funding section still on Jay
- Yui Tanaka: Heron round-4 model card under review
- Yui Tanaka: Felix's sensor pull script PR is up
- Devon McAllister: facility maintenance window next Tuesday
- Anika Sato: clinical review batch underway
- Renata Okonkwo: calibration plot bin boundaries updated, no surprises
- Felix Ruiz-Carrera: reviewer 3's distribution-shift question — drafting reply
- Erik Pohl: newsletter draft circulated for comments
- Felix Ruiz-Carrera: facility maintenance window next Tuesday
- Marisol Holst: DUA addendum confirmed current
- Priya Iyer: Felix's sensor pull script PR is up
- Saanvi Desai: container rebuild done, no breaking changes
- Erik Pohl: outcome-weighted IPCW patch in for review
- Talia Friedman: newsletter draft circulated for comments

## Discussion notes

Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.

## Action items

- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
