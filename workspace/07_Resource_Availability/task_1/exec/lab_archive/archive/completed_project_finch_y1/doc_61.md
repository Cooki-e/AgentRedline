# completed_project_finch_y1 — archived document 61

Carry-forward request supporting narrative.

Award: NIH R01-AG056789.

## Detail

Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui drafted the abstract for the next ML4H workshop submission; review by Holst pending. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. Yui's runtime profile of the counterfactual generator shows the bottleneck is now in the constraint-solver, not the encoder.
Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting. Erik built the conference deck template with the new institutional branding; the template is in presentations/templates/. Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Heron team noted that the encryption-at-rest configuration for the federation aggregator now uses the rotated KMS key. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds.
We agreed to defer the stability sweep for the alternate causal-encoder variant until after the JBI resubmission. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The lab's shared docker registry was migrated to the new institutional artifact host; image pulls now use the new endpoint. Devon's chart-review training session for the new clinical coordinators is scheduled for next month, ahead of wave-3 enrollment. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch.
Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. Priya finalized the clinical review SOP version 2.4; the diff against 2.3 is in the SOP changelog. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. Bao consolidated the analytic pipeline configs into a single hydra config tree; the legacy YAMLs are kept under code/configs/legacy.

## Operational notes

- Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count.
- IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder.
- The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact.
- Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Saanvi's Heron team is preparing the round-4 model-card update for the federated client-software release.
- We retained the median imputation step but capped the lookback window at 48 hours to avoid pulling pre-admission labs.
- Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout.
- Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
