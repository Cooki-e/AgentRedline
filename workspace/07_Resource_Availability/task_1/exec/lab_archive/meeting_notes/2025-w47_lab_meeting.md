# Lab Meeting — 2025-12-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Hari Mohan: field-team dashboard refresh scheduled
- Renata Okonkwo: container rebuild done, no breaking changes
- Bao Nguyen: deprecated pipeline branches archived for v5
- Priya Iyer: DUA addendum confirmed current
- Jay Patel: facility maintenance window next Tuesday
- Priya Iyer: Felix's sensor pull script PR is up
- Felix Ruiz-Carrera: outcome-weighted IPCW patch in for review
- Marisol Holst: Heron round-4 model card under review
- Anika Sato: newsletter draft circulated for comments
- Renata Okonkwo: Finch wave-2 enrollment progressing
- Renata Okonkwo: field-team dashboard refresh scheduled
- Saanvi Desai: Kestrel sensor pull came in
- Jay Patel: container rebuild done, no breaking changes
- Erik Pohl: newsletter draft circulated for comments
- Bao Nguyen: Kestrel sensor pull came in
- Jay Patel: Bao finished cohort-filter test refactor

## Discussion notes

Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Action items

- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
