# Lab Meeting — 2023-08-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Talia Friedman: deprecated pipeline branches archived for v5
- Renata Okonkwo: Heron round-4 model card under review
- Talia Friedman: ran the new sweep, results look stable
- Jay Patel: calibration plot bin boundaries updated, no surprises
- Marisol Holst: DUA addendum confirmed current
- Anika Sato: Kestrel sensor pull came in
- Bao Nguyen: calibration plot bin boundaries updated, no surprises
- Talia Friedman: clinical review batch underway
- Bao Nguyen: JBI revision continues, funding section still on Jay
- Priya Iyer: Heron federation round-3 completed
- Devon McAllister: Kestrel sensor pull came in
- Marisol Holst: reviewer 3's distribution-shift question — drafting reply
- Priya Iyer: Finch wave-2 enrollment progressing
- Yui Tanaka: Felix's sensor pull script PR is up
- Bao Nguyen: Kestrel sensor pull came in
- Priya Iyer: Heron round-4 model card under review
- Yui Tanaka: DUA addendum confirmed current
- Anika Sato: outcome-weighted IPCW patch in for review

## Discussion notes

Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.

## Action items

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
