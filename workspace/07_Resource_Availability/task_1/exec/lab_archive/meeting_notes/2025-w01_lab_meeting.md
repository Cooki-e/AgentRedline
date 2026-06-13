# Lab Meeting — 2025-01-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Yui Tanaka: Finch wave-2 enrollment progressing
- Jay Patel: Heron round-4 model card under review
- Hari Mohan: newsletter draft circulated for comments
- Jay Patel: clinical review batch underway
- Yui Tanaka: Heron federation round-3 completed
- Bao Nguyen: DUA addendum confirmed current
- Jay Patel: DUA addendum confirmed current
- Felix Ruiz-Carrera: Felix's sensor pull script PR is up
- Devon McAllister: Finch wave-2 enrollment progressing
- Yui Tanaka: Felix's sensor pull script PR is up
- Renata Okonkwo: supplementary B rendering checked in dark and light mode
- Saanvi Desai: cohort filter passing validation
- Hari Mohan: JBI revision continues, funding section still on Jay
- Talia Friedman: supplementary B rendering checked in dark and light mode
- Jay Patel: Bao finished cohort-filter test refactor
- Devon McAllister: reviewer 3's distribution-shift question — drafting reply
- Priya Iyer: Kestrel sensor pull came in

## Discussion notes

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

## Action items

- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
