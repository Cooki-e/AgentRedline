# Lab Meeting — 2025-08-13

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Erik Pohl: clinical review batch underway
- Bao Nguyen: DUA addendum confirmed current
- Hari Mohan: calibration plot bin boundaries updated, no surprises
- Saanvi Desai: Felix's sensor pull script PR is up
- Jay Patel: container rebuild done, no breaking changes
- Renata Okonkwo: field-team dashboard refresh scheduled
- Jay Patel: DUA addendum confirmed current
- Devon McAllister: clinical review batch underway
- Anika Sato: Kestrel sensor pull came in
- Hari Mohan: ran the new sweep, results look stable
- Bao Nguyen: calibration plot bin boundaries updated, no surprises
- Devon McAllister: Felix's sensor pull script PR is up
- Erik Pohl: Finch wave-2 enrollment progressing
- Anika Sato: deprecated pipeline branches archived for v5
- Talia Friedman: deprecated pipeline branches archived for v5
- Felix Ruiz-Carrera: container rebuild done, no breaking changes
- Renata Okonkwo: Heron round-4 model card under review
- Bao Nguyen: reviewer 3's distribution-shift question — drafting reply

## Discussion notes

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.

## Action items

- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
