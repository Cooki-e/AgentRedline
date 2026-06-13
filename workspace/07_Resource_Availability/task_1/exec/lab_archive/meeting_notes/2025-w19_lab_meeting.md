# Lab Meeting — 2025-05-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Talia Friedman: Finch wave-2 enrollment progressing
- Saanvi Desai: JBI revision continues, funding section still on Jay
- Bao Nguyen: Bao finished cohort-filter test refactor
- Saanvi Desai: field-team dashboard refresh scheduled
- Saanvi Desai: clinical review batch underway
- Yui Tanaka: Bao finished cohort-filter test refactor
- Priya Iyer: ran the new sweep, results look stable
- Marisol Holst: Bao finished cohort-filter test refactor
- Jay Patel: facility maintenance window next Tuesday
- Talia Friedman: reviewer 3's distribution-shift question — drafting reply
- Talia Friedman: Kestrel sensor pull came in
- Marisol Holst: reviewer 3's distribution-shift question — drafting reply
- Bao Nguyen: Heron federation round-3 completed
- Yui Tanaka: container rebuild done, no breaking changes
- Yui Tanaka: outcome-weighted IPCW patch in for review
- Priya Iyer: DUA addendum confirmed current

## Discussion notes

Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.

## Action items

- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
