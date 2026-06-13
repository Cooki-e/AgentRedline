# completed_project_kestrel_y2 — archived document 45

Subaward modification memo.

Award: NSF IIS-2031234.

## Detail

Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review. Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year.
Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Bao archived the deprecated v5 pipeline branches; the active branches are now v6, v7-experimental, and main. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.

## Operational notes

- Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
- We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged.
- Hari reconciled the lab's travel reimbursements for the previous conference cycle; no outstanding items remain.
- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
