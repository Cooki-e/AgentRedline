# completed_project_heron_satellite_y1 — archived document 07

Annual NCE narrative justification.

Award: NIH R01-LM013456.

## Detail

The DUA team confirmed the data-use addendum for the eICU release is current through end of next fiscal year. Yui rebased the manuscript LaTeX branch on main and resolved the merge conflicts in the supplementary table layout. Priya confirmed all clinical reviewers signed the latest version of the conflict-of-interest disclosure for the JBI submission. Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The data-availability statement was tightened to clarify that derived analytic tables are released on request via the DUA contact. We compared the IPCW correction against the marginal structural model variant and saw <1% absolute difference in the reported HR.
Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised. Yui's last counterfactual sweep used the corrected outcome-weighted IPCW; results were stable across the cross-validation folds. Bao confirmed the data-availability links in the manuscript point to the durable analytic-table identifiers, not the build-time artifacts. Felix replaced the deprecated pandas resample call with the new offset-aliases API; no behavior change in the resampled features. Yui confirmed the supplementary Table S3 numbers match the released analytic-table version after the cohort filter patch. The lab safety walkthrough completed without findings; the next walkthrough is scheduled for next quarter. MIMIC-IV access tokens were renewed for the lab; the renewed credentials are in the usual vault entry, no code changes required.
The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. Anika's analysis of the Kestrel wave-3 stream is on track; the wildlife-density estimator passed cross-validation against the field count. The federated training round-3 failed at hospital-3 due to an expired client certificate; the rotation script will be re-run Tuesday. Talia coordinated the clinical-coordinator quarterly meeting; minutes were filed on the shared drive. The lab newsletter draft for next quarter was reviewed; Holst suggested moving the Heron section ahead of the Finch update. Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
Felix patched the Kestrel sensor pull script to handle the new firmware payload format from the Olympic deployment. The compute partition is currently at 84% utilization; expect queue times of 30-60 minutes for A100 jobs through the end of the week. The cohort filter rejected approximately 2.3% of admissions per the new admission-type rule, consistent with the v6 pipeline. Devon's wave-2 outreach materials were translated and reviewed for accessibility per the recruitment SOP. Saanvi's group submitted the Heron round-3 progress report to NLM on schedule with no findings to flag. IRB renewal for the Holst-lab umbrella protocol was filed on schedule; the renewal letter is in the shared compliance folder. Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.

## Operational notes

- Saanvi's Heron team reported that the federated aggregation server is now provisioned at the U. Cape Cod side and ready for round-4.
- Hari processed the quarterly facility-charge reconciliation; no anomalies were flagged against the shared compute allowance.
- Yui re-ran the counterfactual sweep with the lower-rank causal encoder and recovered the originally reported AUC within 0.004.
- The graphical abstract was rebuilt with the updated cohort numbers and approved by Holst at the lab meeting.
- Talia confirmed Finch cohort wave-2 recruitment is at 812/1200 across the three enrollment sites, with site-2 still trailing.
- Reviewer 3's distribution-shift concern is addressed in Supp F via a held-out site-stratified evaluation across the three external sites.
- Erik confirmed Figure 6 panel B renders correctly in both light and dark theme exports for the conference deck.
- Bao's data-export script now writes a manifest alongside each export for downstream provenance tracking.
- The Heron federation client passed its handshake test after the openssl upgrade; no further client-side changes are anticipated this quarter.
- Erik validated the heatmap rendering against the published color palette guideline; no accessibility flags were raised.
