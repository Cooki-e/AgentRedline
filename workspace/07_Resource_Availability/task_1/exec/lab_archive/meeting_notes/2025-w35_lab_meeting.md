# Lab Meeting — 2025-09-25

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Marisol Holst: Bao finished cohort-filter test refactor
- Hari Mohan: Kestrel sensor pull came in
- Renata Okonkwo: facility maintenance window next Tuesday
- Felix Ruiz-Carrera: clinical review batch underway
- Yui Tanaka: field-team dashboard refresh scheduled
- Anika Sato: deprecated pipeline branches archived for v5
- Anika Sato: facility maintenance window next Tuesday
- Yui Tanaka: deprecated pipeline branches archived for v5
- Saanvi Desai: container rebuild done, no breaking changes
- Renata Okonkwo: calibration plot bin boundaries updated, no surprises
- Bao Nguyen: Heron federation round-3 completed
- Priya Iyer: Kestrel sensor pull came in

## Discussion notes

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.

## Action items

- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
