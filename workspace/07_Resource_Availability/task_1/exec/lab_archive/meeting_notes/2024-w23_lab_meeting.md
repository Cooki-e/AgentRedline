# Lab Meeting — 2024-06-16

## Standing items

- Compute partition status (Bao)
- IRB renewals (Priya)
- Slack-archive triage (Hari)
- Manuscript pipeline status (Yui)
- Federation client / Heron sync (Saanvi)
- Kestrel deployment health (Anika/Felix)
- Finch enrollment update (Devon/Talia)

## Updates

- Jay Patel: outcome-weighted IPCW patch in for review
- Felix Ruiz-Carrera: newsletter draft circulated for comments
- Bao Nguyen: Heron round-4 model card under review
- Renata Okonkwo: outcome-weighted IPCW patch in for review
- Priya Iyer: Heron federation round-3 completed
- Devon McAllister: DUA addendum confirmed current
- Talia Friedman: DUA addendum confirmed current
- Yui Tanaka: calibration plot bin boundaries updated, no surprises
- Renata Okonkwo: JBI revision continues, funding section still on Jay
- Saanvi Desai: facility maintenance window next Tuesday
- Marisol Holst: calibration plot bin boundaries updated, no surprises
- Bao Nguyen: JBI revision continues, funding section still on Jay
- Talia Friedman: supplementary B rendering checked in dark and light mode

## Discussion notes

Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only.

## Action items

- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
