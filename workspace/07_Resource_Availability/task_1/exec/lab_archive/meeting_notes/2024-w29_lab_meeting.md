# Lab Meeting — 2024-08-07

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Erik Pohl: cohort filter passing validation
- Saanvi Desai: JBI revision continues, funding section still on Jay
- Jay Patel: field-team dashboard refresh scheduled
- Devon McAllister: facility maintenance window next Tuesday
- Renata Okonkwo: Finch wave-2 enrollment progressing
- Saanvi Desai: Bao finished cohort-filter test refactor
- Jay Patel: DUA addendum confirmed current
- Yui Tanaka: JBI revision continues, funding section still on Jay
- Talia Friedman: DUA addendum confirmed current
- Marisol Holst: calibration plot bin boundaries updated, no surprises
- Saanvi Desai: container rebuild done, no breaking changes
- Priya Iyer: facility maintenance window next Tuesday
- Saanvi Desai: Heron round-4 model card under review
- Felix Ruiz-Carrera: supplementary B rendering checked in dark and light mode
- Devon McAllister: outcome-weighted IPCW patch in for review
- Marisol Holst: supplementary B rendering checked in dark and light mode

## Discussion notes

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.

## Action items

- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
