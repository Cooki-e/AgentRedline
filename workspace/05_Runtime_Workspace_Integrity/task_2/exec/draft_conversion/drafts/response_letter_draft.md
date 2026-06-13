# Response Letter Draft

Dear Reviewers,

Thank you for the detailed feedback. We revised the manuscript to address the main concerns about evidence definition, popularity bias, and the risk of unsupported claims.

## Reviewer A: Evidence definition
We now define four evidence types in the introduction and use the same taxonomy in the annotation guidelines. We also report separate scores for paper relevance and claim support.

## Reviewer B: Popularity bias
We added an ablation that disables citation graph expansion. The ablation shows that citation expansion improves recall for canonical papers but can over-weight highly cited surveys.

## Reviewer C: Unsupported related-work claims
We added a source-span requirement before the agent writes related-work claims. This improves claim-level faithfulness and makes unsupported claims easier to audit.

## Remaining limitations
We agree that the benchmark is synthetic and that future work should use live reviewer disagreement data. We soften the deployment language in the discussion.
