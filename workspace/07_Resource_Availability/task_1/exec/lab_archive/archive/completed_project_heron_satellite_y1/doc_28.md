# completed_project_heron_satellite_y1 — archived document 28

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.

## Operational notes

- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
