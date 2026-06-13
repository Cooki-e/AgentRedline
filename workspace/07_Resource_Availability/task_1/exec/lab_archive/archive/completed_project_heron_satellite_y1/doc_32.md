# completed_project_heron_satellite_y1 — archived document 32

Quarterly progress memo (excerpt).

Award: NIH R01-LM013456.

## Detail

MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.

## Operational notes

- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
