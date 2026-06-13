# completed_project_kestrel_y2 — archived document 38

Annual NCE narrative justification.

Award: NSF IIS-2031234.

## Detail

The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.

## Operational notes

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
