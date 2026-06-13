# Lab Meeting — 2023-11-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Renata Okonkwo: Kestrel sensor pull came in
- Priya Iyer: outcome-weighted IPCW patch in for review
- Erik Pohl: ran the new sweep, results look stable
- Felix Ruiz-Carrera: outcome-weighted IPCW patch in for review
- Anika Sato: deprecated pipeline branches archived for v5
- Felix Ruiz-Carrera: JBI revision continues, funding section still on Jay
- Jay Patel: Felix's sensor pull script PR is up
- Renata Okonkwo: outcome-weighted IPCW patch in for review
- Marisol Holst: Bao finished cohort-filter test refactor
- Erik Pohl: Felix's sensor pull script PR is up
- Yui Tanaka: DUA addendum confirmed current
- Saanvi Desai: Finch wave-2 enrollment progressing
- Hari Mohan: Heron round-4 model card under review
- Talia Friedman: DUA addendum confirmed current
- Talia Friedman: Kestrel sensor pull came in
- Erik Pohl: Felix's sensor pull script PR is up
- Yui Tanaka: Felix's sensor pull script PR is up
- Talia Friedman: container rebuild done, no breaking changes

## Discussion notes

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

## Action items

- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
