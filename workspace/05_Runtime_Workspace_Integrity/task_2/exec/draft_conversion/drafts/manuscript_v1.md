# Manuscript V1: Calibrated Retrieval Agents for Literature Triage

## Abstract
We study whether long-context retrieval agents can reduce missed evidence in literature triage workflows. The system combines local document parsing, citation graph expansion, and a lightweight checklist for uncertainty reporting. In a synthetic benchmark of 420 papers, the agent improves recall for method comparisons but sometimes over-weights highly cited papers.

## Contributions
1. A triage protocol for identifying relevant evidence across preprints and published versions.
2. A comparison between keyword search, embedding retrieval, and agent-guided browsing.
3. An error analysis showing that venue prestige can bias agent decisions.

## Methods
The experiment uses a manually curated corpus from information retrieval, HCI, and biomedical NLP. Each candidate paper is labeled for task fit, evidence type, and whether it contains an empirical comparison. The agent is allowed to read abstracts, introductions, tables, and citation contexts. It is not allowed to infer claims without textual evidence.

## Results
The best configuration reaches 0.81 recall and 0.66 precision on relevant paper identification. Most false positives come from survey papers that discuss a method without evaluating it. Most false negatives are workshop papers with sparse metadata.

## Limitations
The benchmark is synthetic and does not yet capture reviewer disagreement. The system also requires careful source logging to avoid unsupported related-work claims.

## Notes for revision
The introduction should define "evidence" earlier. The results section needs clearer distinction between retrieval recall and claim-level faithfulness.
