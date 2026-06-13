# completed_project_kestrel_y2 — archived document 23

Recruitment quarterly summary.

Award: NSF IIS-2031234.

## Detail

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.

## Operational notes

- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
