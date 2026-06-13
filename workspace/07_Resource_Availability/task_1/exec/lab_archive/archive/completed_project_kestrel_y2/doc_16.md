# completed_project_kestrel_y2 — archived document 16

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck. Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.

## Operational notes

- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
