# completed_project_heron_satellite_y1 — archived document 21

Recruitment quarterly summary.

Award: NIH R01-LM013456.

## Detail

Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

## Operational notes

- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
