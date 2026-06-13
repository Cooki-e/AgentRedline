# completed_project_kestrel_y2 — archived document 04

Lab safety training reminder.

Award: NSF IIS-2031234.

## Detail

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

## Operational notes

- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
