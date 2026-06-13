# completed_project_heron_satellite_y1 — archived document 51

Site-coordinator monthly check-in notes.

Award: NIH R01-LM013456.

## Detail

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.

## Operational notes

- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
