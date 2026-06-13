# Lab Meeting — 2025-02-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: cohort filter passing validation
- Jay Patel: clinical review batch underway
- Marisol Holst: cohort filter passing validation
- Saanvi Desai: Kestrel sensor pull came in
- Anika Sato: Heron federation round-3 completed
- Hari Mohan: Heron federation round-3 completed
- Talia Friedman: outcome-weighted IPCW patch in for review
- Anika Sato: field-team dashboard refresh scheduled
- Renata Okonkwo: Felix's sensor pull script PR is up
- Anika Sato: deprecated pipeline branches archived for v5

## Discussion notes

Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.

## Action items

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
