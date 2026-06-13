# Lab Meeting — 2024-12-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Bao Nguyen: supplementary B rendering checked in dark and light mode
- Bao Nguyen: DUA addendum confirmed current
- Saanvi Desai: clinical review batch underway
- Anika Sato: Kestrel sensor pull came in
- Anika Sato: clinical review batch underway
- Bao Nguyen: facility maintenance window next Tuesday
- Erik Pohl: container rebuild done, no breaking changes
- Anika Sato: outcome-weighted IPCW patch in for review
- Marisol Holst: supplementary B rendering checked in dark and light mode
- Hari Mohan: supplementary B rendering checked in dark and light mode
- Saanvi Desai: cohort filter passing validation
- Saanvi Desai: outcome-weighted IPCW patch in for review
- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Talia Friedman: outcome-weighted IPCW patch in for review
- Priya Iyer: Finch wave-2 enrollment progressing

## Discussion notes

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Action items

- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
