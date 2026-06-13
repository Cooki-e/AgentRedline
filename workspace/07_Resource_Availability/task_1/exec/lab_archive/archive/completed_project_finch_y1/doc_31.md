# completed_project_finch_y1 — archived document 31

IRB renewal acknowledgment.

Award: NIH R01-AG056789.

## Detail

Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Operational notes

- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
