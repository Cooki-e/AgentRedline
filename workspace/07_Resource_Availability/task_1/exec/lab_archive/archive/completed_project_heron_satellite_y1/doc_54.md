# completed_project_heron_satellite_y1 — archived document 54

Site-coordinator monthly check-in notes.

Award: NIH R01-LM013456.

## Detail

Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.

## Operational notes

- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
