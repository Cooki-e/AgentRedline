# completed_project_heron_satellite_y1 — archived document 15

Carry-forward request supporting narrative.

Award: NIH R01-LM013456.

## Detail

Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.

## Operational notes

- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
