# completed_project_heron_satellite_y1 — archived document 35

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.

## Operational notes

- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
