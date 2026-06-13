# completed_project_kestrel_y2 — archived document 15

Carry-forward request supporting narrative.

Award: NSF IIS-2031234.

## Detail

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.

## Operational notes

- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
