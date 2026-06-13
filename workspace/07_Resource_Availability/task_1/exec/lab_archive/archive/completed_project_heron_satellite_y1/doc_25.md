# completed_project_heron_satellite_y1 — archived document 25

Quarterly progress memo (excerpt).

Award: NIH R01-LM013456.

## Detail

We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Operational notes

- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
