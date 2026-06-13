# completed_project_finch_y1 — archived document 44

Recruitment quarterly summary.

Award: NIH R01-AG056789.

## Detail

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.

## Operational notes

- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
