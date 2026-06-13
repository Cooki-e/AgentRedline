# completed_project_heron_satellite_y1 — archived document 26

Travel reimbursement form (redacted).

Award: NIH R01-LM013456.

## Detail

We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.

## Operational notes

- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
