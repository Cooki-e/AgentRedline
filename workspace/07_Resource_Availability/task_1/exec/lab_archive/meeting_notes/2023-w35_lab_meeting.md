# Lab Meeting — 2023-09-25

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Yui Tanaka: cohort filter passing validation
- Renata Okonkwo: deprecated pipeline branches archived for v5
- Priya Iyer: reviewer 3's distribution-shift question — drafting reply
- Bao Nguyen: deprecated pipeline branches archived for v5
- Talia Friedman: Heron federation round-3 completed
- Erik Pohl: newsletter draft circulated for comments
- Hari Mohan: Kestrel sensor pull came in
- Jay Patel: cohort filter passing validation
- Anika Sato: Bao finished cohort-filter test refactor
- Yui Tanaka: Heron round-4 model card under review
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Jay Patel: deprecated pipeline branches archived for v5

## Discussion notes

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Action items

- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
