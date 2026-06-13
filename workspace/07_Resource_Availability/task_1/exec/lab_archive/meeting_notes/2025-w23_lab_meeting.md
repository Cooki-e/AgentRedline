# Lab Meeting — 2025-06-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Talia Friedman: cohort filter passing validation
- Renata Okonkwo: Heron round-4 model card under review
- Priya Iyer: Bao finished cohort-filter test refactor
- Yui Tanaka: Heron federation round-3 completed
- Renata Okonkwo: Bao finished cohort-filter test refactor
- Devon McAllister: ran the new sweep, results look stable
- Priya Iyer: reviewer 3's distribution-shift question — drafting reply
- Priya Iyer: outcome-weighted IPCW patch in for review
- Hari Mohan: reviewer 3's distribution-shift question — drafting reply
- Hari Mohan: outcome-weighted IPCW patch in for review
- Saanvi Desai: calibration plot bin boundaries updated, no surprises
- Anika Sato: DUA addendum confirmed current
- Yui Tanaka: Bao finished cohort-filter test refactor
- Saanvi Desai: Finch wave-2 enrollment progressing

## Discussion notes

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Action items

- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
