# Lab Meeting — 2024-08-13

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Yui Tanaka: Heron federation round-3 completed
- Saanvi Desai: container rebuild done, no breaking changes
- Felix Ruiz-Carrera: Felix's sensor pull script PR is up
- Erik Pohl: JBI revision continues, funding section still on Jay
- Anika Sato: deprecated pipeline branches archived for v5
- Priya Iyer: container rebuild done, no breaking changes
- Felix Ruiz-Carrera: field-team dashboard refresh scheduled
- Bao Nguyen: cohort filter passing validation
- Erik Pohl: newsletter draft circulated for comments
- Felix Ruiz-Carrera: Heron round-4 model card under review
- Priya Iyer: ran the new sweep, results look stable
- Erik Pohl: supplementary B rendering checked in dark and light mode
- Devon McAllister: JBI revision continues, funding section still on Jay
- Jay Patel: Bao finished cohort-filter test refactor
- Felix Ruiz-Carrera: Heron federation round-3 completed
- Hari Mohan: cohort filter passing validation
- Devon McAllister: clinical review batch underway
- Bao Nguyen: container rebuild done, no breaking changes

## Discussion notes

Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.

## Action items

- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
