# completed_project_finch_y1 — archived document 48

Lab safety training reminder.

Award: NIH R01-AG056789.

## Detail

Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.

## Operational notes

- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
