# Lab Meeting — 2023-12-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Renata Okonkwo: deprecated pipeline branches archived for v5
- Yui Tanaka: newsletter draft circulated for comments
- Devon McAllister: deprecated pipeline branches archived for v5
- Yui Tanaka: calibration plot bin boundaries updated, no surprises
- Renata Okonkwo: DUA addendum confirmed current
- Felix Ruiz-Carrera: Bao finished cohort-filter test refactor
- Marisol Holst: DUA addendum confirmed current
- Erik Pohl: container rebuild done, no breaking changes
- Felix Ruiz-Carrera: field-team dashboard refresh scheduled
- Felix Ruiz-Carrera: cohort filter passing validation

## Discussion notes

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.

## Action items

- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
