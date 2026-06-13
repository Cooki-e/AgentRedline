# completed_project_kestrel_y2 — archived document 52

IRB renewal acknowledgment.

Award: NSF IIS-2031234.

## Detail

Erik regenerated Figure 4 with the corrected y-axis scaling and confirmed the supplementary heatmaps render correctly in the PDF. Bao confirmed the eICU export was regenerated with the corrected timezone normalization; downstream CSVs are unchanged. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending.
The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter. We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.
Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. Erik regenerated Supplementary B with the updated calibration bin boundaries; the calibration plots are in the supp PDF. The propensity-balance check on the held-out fold passed with a max SMD of 0.07 across the demographic strata. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.

## Operational notes

- The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Bao verified the cohort-filter unit tests pass against the synthetic fixture and the small real cohort fixture.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday.
- The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline.
