# completed_project_heron_satellite_y1 — archived document 27

Lab safety training reminder.

Award: NIH R01-LM013456.

## Detail

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Operational notes

- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
