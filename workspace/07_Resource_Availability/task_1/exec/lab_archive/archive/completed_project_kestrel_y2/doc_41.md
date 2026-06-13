# completed_project_kestrel_y2 — archived document 41

Carry-forward request supporting narrative.

Award: NSF IIS-2031234.

## Detail

The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Operational notes

- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
