# Lab Meeting — 2023-10-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Felix Ruiz-Carrera: JBI revision continues, funding section still on Jay
- Renata Okonkwo: facility maintenance window next Tuesday
- Devon McAllister: field-team dashboard refresh scheduled
- Talia Friedman: Felix's sensor pull script PR is up
- Felix Ruiz-Carrera: JBI revision continues, funding section still on Jay
- Devon McAllister: container rebuild done, no breaking changes
- Jay Patel: Heron federation round-3 completed
- Marisol Holst: cohort filter passing validation
- Jay Patel: facility maintenance window next Tuesday
- Marisol Holst: clinical review batch underway
- Priya Iyer: JBI revision continues, funding section still on Jay
- Jay Patel: Finch wave-2 enrollment progressing
- Saanvi Desai: DUA addendum confirmed current
- Priya Iyer: Finch wave-2 enrollment progressing

## Discussion notes

The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

## Action items

- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
