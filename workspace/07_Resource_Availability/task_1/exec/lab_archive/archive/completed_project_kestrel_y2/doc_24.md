# completed_project_kestrel_y2 — archived document 24

Site-coordinator monthly check-in notes.

Award: NSF IIS-2031234.

## Detail

Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.

## Operational notes

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
