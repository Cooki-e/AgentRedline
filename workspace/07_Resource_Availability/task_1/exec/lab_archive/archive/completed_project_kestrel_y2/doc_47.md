# completed_project_kestrel_y2 — archived document 47

Quarterly progress memo (excerpt).

Award: NSF IIS-2031234.

## Detail

Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.

## Operational notes

- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
- Anika exported the cross-site sensor-stream summary stats and stored them under data/processed/kestrel_summary_v3.csv.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
