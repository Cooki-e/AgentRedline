# completed_project_kestrel_y2 — archived document 50

Equipment inventory snapshot.

Award: NSF IIS-2031234.

## Detail

Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.

## Operational notes

- Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
