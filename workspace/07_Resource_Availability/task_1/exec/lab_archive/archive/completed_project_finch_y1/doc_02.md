# completed_project_finch_y1 — archived document 02

Equipment inventory snapshot.

Award: NIH R01-AG056789.

## Detail

Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Operational notes

- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
