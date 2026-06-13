# Lab Meeting — 2023-01-04

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Devon McAllister: reviewer 3's distribution-shift question — drafting reply
- Bao Nguyen: clinical review batch underway
- Bao Nguyen: Kestrel sensor pull came in
- Renata Okonkwo: reviewer 3's distribution-shift question — drafting reply
- Marisol Holst: Heron federation round-3 completed
- Hari Mohan: container rebuild done, no breaking changes
- Talia Friedman: JBI revision continues, funding section still on Jay
- Yui Tanaka: deprecated pipeline branches archived for v5
- Marisol Holst: Bao finished cohort-filter test refactor
- Yui Tanaka: facility maintenance window next Tuesday
- Marisol Holst: Heron federation round-3 completed
- Erik Pohl: facility maintenance window next Tuesday
- Saanvi Desai: deprecated pipeline branches archived for v5
- Marisol Holst: facility maintenance window next Tuesday

## Discussion notes

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.

## Action items

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
