# completed_project_heron_satellite_y1 — archived document 58

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

## Operational notes

- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
