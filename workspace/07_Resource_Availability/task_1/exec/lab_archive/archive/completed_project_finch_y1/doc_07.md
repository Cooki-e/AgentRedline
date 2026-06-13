# completed_project_finch_y1 — archived document 07

Recruitment quarterly summary.

Award: NIH R01-AG056789.

## Detail

Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Operational notes

- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
