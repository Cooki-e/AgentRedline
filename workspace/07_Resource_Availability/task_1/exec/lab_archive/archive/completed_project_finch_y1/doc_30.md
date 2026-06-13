# completed_project_finch_y1 — archived document 30

Sub-recipient invoice cover sheet.

Award: NIH R01-AG056789.

## Detail

Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Operational notes

- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
