# completed_project_heron_satellite_y1 — archived document 17

Carry-forward request supporting narrative.

Award: NIH R01-LM013456.

## Detail

Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Devon scheduled the Finch wave-2 mid-point review for the third week of next month, pending Holst's calendar confirmation.
Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key.
Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update.

## Operational notes

- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission.
- The lab's compute fairshare quotas were re-balanced; Yui's queue priority is restored to baseline after the Q4 surge.
- Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts.
- The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata.
- Felix's container build pipeline now caches the conda environment between PR builds; CI times dropped about 40%.
