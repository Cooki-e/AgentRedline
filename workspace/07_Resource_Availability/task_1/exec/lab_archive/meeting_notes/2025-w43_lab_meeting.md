# Lab Meeting — 2025-11-22

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Yui Tanaka: deprecated pipeline branches archived for v5
- Saanvi Desai: DUA addendum confirmed current
- Jay Patel: Heron round-4 model card under review
- Renata Okonkwo: Kestrel sensor pull came in
- Talia Friedman: Heron federation round-3 completed
- Marisol Holst: Kestrel sensor pull came in
- Anika Sato: reviewer 3's distribution-shift question — drafting reply
- Talia Friedman: Felix's sensor pull script PR is up
- Erik Pohl: calibration plot bin boundaries updated, no surprises
- Anika Sato: clinical review batch underway

## Discussion notes

Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Action items

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
