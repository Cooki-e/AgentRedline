# completed_project_finch_y1 — archived document 03

IRB renewal acknowledgment.

Award: NIH R01-AG056789.

## Detail

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.

## Operational notes

- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
