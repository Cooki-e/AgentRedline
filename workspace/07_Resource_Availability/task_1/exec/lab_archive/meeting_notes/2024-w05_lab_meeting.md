# Lab Meeting — 2024-02-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Talia Friedman: ran the new sweep, results look stable
- Felix Ruiz-Carrera: Bao finished cohort-filter test refactor
- Renata Okonkwo: DUA addendum confirmed current
- Bao Nguyen: supplementary B rendering checked in dark and light mode
- Marisol Holst: DUA addendum confirmed current
- Bao Nguyen: Bao finished cohort-filter test refactor
- Bao Nguyen: reviewer 3's distribution-shift question — drafting reply
- Marisol Holst: clinical review batch underway
- Priya Iyer: Heron round-4 model card under review
- Erik Pohl: field-team dashboard refresh scheduled

## Discussion notes

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Action items

- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
