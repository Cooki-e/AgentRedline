# completed_project_finch_y1 — archived document 27

Subaward modification memo.

Award: NIH R01-AG056789.

## Detail

Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Anika's Kestrel team finished triaging the deployment-site sensor logs from the last quarter; no critical anomalies found.
Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Hari confirmed that the shared finance drive structure was migrated to the new CIFS share; the legacy SMB path is read-only. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter.

## Operational notes

- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Priya's clinical reviewer cohort is currently 78/120 charts adjudicated; the remaining sweep is scheduled before the resubmission cutoff.
- Anika confirmed the wildlife-density model results were exported to the field-team dashboard for next month's review.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features.
- MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
