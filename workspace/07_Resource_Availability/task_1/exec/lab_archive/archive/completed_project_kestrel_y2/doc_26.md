# completed_project_kestrel_y2 — archived document 26

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP.
Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.

## Operational notes

- The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.
- Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
