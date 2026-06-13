# completed_project_kestrel_y2 — archived document 56

Travel reimbursement form (redacted).

Award: NSF IIS-2031234.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

## Operational notes

- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
