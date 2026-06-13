# completed_project_kestrel_y2 — archived document 57

Carry-forward request supporting narrative.

Award: NSF IIS-2031234.

## Detail

The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.

## Operational notes

- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
