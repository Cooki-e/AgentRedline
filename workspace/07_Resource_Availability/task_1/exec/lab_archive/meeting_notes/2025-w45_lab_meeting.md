# Lab Meeting — 2025-12-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Jay Patel: DUA addendum confirmed current
- Priya Iyer: JBI revision continues, funding section still on Jay
- Talia Friedman: deprecated pipeline branches archived for v5
- Marisol Holst: DUA addendum confirmed current
- Marisol Holst: Felix's sensor pull script PR is up
- Bao Nguyen: cohort filter passing validation
- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Erik Pohl: Heron round-4 model card under review
- Saanvi Desai: Felix's sensor pull script PR is up
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Hari Mohan: Heron round-4 model card under review
- Jay Patel: calibration plot bin boundaries updated, no surprises
- Renata Okonkwo: JBI revision continues, funding section still on Jay
- Devon McAllister: JBI revision continues, funding section still on Jay
- Devon McAllister: Finch wave-2 enrollment progressing

## Discussion notes

Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

## Action items

- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
