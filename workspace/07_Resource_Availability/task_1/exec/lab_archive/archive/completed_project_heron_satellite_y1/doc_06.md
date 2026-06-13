# completed_project_heron_satellite_y1 — archived document 06

Equipment inventory snapshot.

Award: NIH R01-LM013456.

## Detail

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Operational notes

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
