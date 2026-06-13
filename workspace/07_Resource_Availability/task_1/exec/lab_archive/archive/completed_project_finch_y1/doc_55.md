# completed_project_finch_y1 — archived document 55

Subaward modification memo.

Award: NIH R01-AG056789.

## Detail

Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.

## Operational notes

- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
