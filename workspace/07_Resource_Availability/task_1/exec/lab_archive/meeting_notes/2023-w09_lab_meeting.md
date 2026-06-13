# Lab Meeting — 2023-03-01

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Erik Pohl: Felix's sensor pull script PR is up
- Jay Patel: clinical review batch underway
- Marisol Holst: Heron federation round-3 completed
- Felix Ruiz-Carrera: Bao finished cohort-filter test refactor
- Hari Mohan: Felix's sensor pull script PR is up
- Talia Friedman: cohort filter passing validation
- Saanvi Desai: supplementary B rendering checked in dark and light mode
- Bao Nguyen: Heron federation round-3 completed
- Hari Mohan: ran the new sweep, results look stable
- Marisol Holst: JBI revision continues, funding section still on Jay
- Jay Patel: deprecated pipeline branches archived for v5
- Devon McAllister: facility maintenance window next Tuesday

## Discussion notes

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.

## Action items

- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
