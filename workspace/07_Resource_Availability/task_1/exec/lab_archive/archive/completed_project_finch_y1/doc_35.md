# completed_project_finch_y1 — archived document 35

Carry-forward request supporting narrative.

Award: NIH R01-AG056789.

## Detail

The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

## Operational notes

- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
