# Lab Meeting — 2025-04-13

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Marisol Holst: Finch wave-2 enrollment progressing
- Anika Sato: Heron federation round-3 completed
- Devon McAllister: ran the new sweep, results look stable
- Marisol Holst: Felix's sensor pull script PR is up
- Saanvi Desai: Bao finished cohort-filter test refactor
- Hari Mohan: Finch wave-2 enrollment progressing
- Saanvi Desai: container rebuild done, no breaking changes
- Hari Mohan: container rebuild done, no breaking changes
- Felix Ruiz-Carrera: Kestrel sensor pull came in
- Anika Sato: clinical review batch underway
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply
- Erik Pohl: Finch wave-2 enrollment progressing
- Saanvi Desai: ran the new sweep, results look stable
- Felix Ruiz-Carrera: calibration plot bin boundaries updated, no surprises

## Discussion notes

Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

## Action items

- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
