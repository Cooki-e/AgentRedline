# completed_project_heron_satellite_y1 — archived document 41

Personnel effort certification stub.

Award: NIH R01-LM013456.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Operational notes

- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
