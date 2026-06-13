# Lab Meeting — 2024-01-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Renata Okonkwo: Finch wave-2 enrollment progressing
- Yui Tanaka: deprecated pipeline branches archived for v5
- Talia Friedman: Felix's sensor pull script PR is up
- Renata Okonkwo: DUA addendum confirmed current
- Saanvi Desai: cohort filter passing validation
- Felix Ruiz-Carrera: cohort filter passing validation
- Renata Okonkwo: facility maintenance window next Tuesday
- Talia Friedman: newsletter draft circulated for comments
- Hari Mohan: Kestrel sensor pull came in
- Marisol Holst: Kestrel sensor pull came in
- Erik Pohl: ran the new sweep, results look stable
- Marisol Holst: field-team dashboard refresh scheduled

## Discussion notes

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

## Action items

- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
