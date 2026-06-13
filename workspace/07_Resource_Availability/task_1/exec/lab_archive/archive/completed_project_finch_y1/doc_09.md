# completed_project_finch_y1 — archived document 09

Personnel effort certification stub.

Award: NIH R01-AG056789.

## Detail

The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.

## Operational notes

- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
