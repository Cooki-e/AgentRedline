# completed_project_heron_satellite_y1 — archived document 11

Quarterly progress memo (excerpt).

Award: NIH R01-LM013456.

## Detail

The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.

## Operational notes

- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
- The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
