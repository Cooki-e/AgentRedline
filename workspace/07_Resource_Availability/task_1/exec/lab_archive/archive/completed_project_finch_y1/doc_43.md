# completed_project_finch_y1 — archived document 43

Travel reimbursement form (redacted).

Award: NIH R01-AG056789.

## Detail

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.

## Operational notes

- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
