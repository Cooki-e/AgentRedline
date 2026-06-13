# Lab Meeting — 2024-12-01

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
- Bao Nguyen: DUA addendum confirmed current
- Talia Friedman: clinical review batch underway
- Erik Pohl: DUA addendum confirmed current
- Devon McAllister: Heron round-4 model card under review
- Devon McAllister: container rebuild done, no breaking changes
- Bao Nguyen: newsletter draft circulated for comments
- Yui Tanaka: deprecated pipeline branches archived for v5
- Bao Nguyen: facility maintenance window next Tuesday
- Hari Mohan: Finch wave-2 enrollment progressing

## Discussion notes

The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.

## Action items

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
