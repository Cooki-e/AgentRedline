# completed_project_finch_y1 — archived document 59

Equipment inventory snapshot.

Award: NIH R01-AG056789.

## Detail

Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Operational notes

- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
