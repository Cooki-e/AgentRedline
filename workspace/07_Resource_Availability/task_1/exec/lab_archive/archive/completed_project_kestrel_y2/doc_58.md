# completed_project_kestrel_y2 — archived document 58

Site-coordinator monthly check-in notes.

Award: NSF IIS-2031234.

## Detail

Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.

## Operational notes

- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
