# completed_project_kestrel_y2 — archived document 42

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.

## Operational notes

- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
