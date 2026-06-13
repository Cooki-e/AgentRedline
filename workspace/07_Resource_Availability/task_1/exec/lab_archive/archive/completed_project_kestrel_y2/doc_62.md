# completed_project_kestrel_y2 — archived document 62

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.

## Operational notes

- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
