# Lab Meeting — 2024-03-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Renata Okonkwo: Felix's sensor pull script PR is up
- Devon McAllister: Bao finished cohort-filter test refactor
- Hari Mohan: Bao finished cohort-filter test refactor
- Yui Tanaka: field-team dashboard refresh scheduled
- Marisol Holst: deprecated pipeline branches archived for v5
- Anika Sato: clinical review batch underway
- Saanvi Desai: ran the new sweep, results look stable
- Talia Friedman: outcome-weighted IPCW patch in for review
- Devon McAllister: Finch wave-2 enrollment progressing
- Marisol Holst: cohort filter passing validation
- Anika Sato: DUA addendum confirmed current
- Yui Tanaka: Heron federation round-3 completed
- Jay Patel: Finch wave-2 enrollment progressing
- Anika Sato: Heron federation round-3 completed
- Priya Iyer: reviewer 3's distribution-shift question — drafting reply
- Talia Friedman: field-team dashboard refresh scheduled
- Saanvi Desai: field-team dashboard refresh scheduled

## Discussion notes

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.

## Action items

- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
