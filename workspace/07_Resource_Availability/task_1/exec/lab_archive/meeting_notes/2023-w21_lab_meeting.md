# Lab Meeting — 2023-06-10

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Hari Mohan: outcome-weighted IPCW patch in for review
- Devon McAllister: Kestrel sensor pull came in
- Hari Mohan: JBI revision continues, funding section still on Jay
- Devon McAllister: Heron federation round-3 completed
- Anika Sato: cohort filter passing validation
- Yui Tanaka: reviewer 3's distribution-shift question — drafting reply
- Talia Friedman: ran the new sweep, results look stable
- Jay Patel: Heron round-4 model card under review
- Talia Friedman: facility maintenance window next Tuesday
- Jay Patel: supplementary B rendering checked in dark and light mode
- Erik Pohl: deprecated pipeline branches archived for v5
- Marisol Holst: Bao finished cohort-filter test refactor
- Bao Nguyen: JBI revision continues, funding section still on Jay
- Erik Pohl: cohort filter passing validation
- Jay Patel: Finch wave-2 enrollment progressing
- Devon McAllister: outcome-weighted IPCW patch in for review
- Felix Ruiz-Carrera: newsletter draft circulated for comments

## Discussion notes

The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.

## Action items

- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
