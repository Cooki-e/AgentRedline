# Manuscript V2: Calibrated Retrieval Agents for Literature Triage

## Abstract
This revision focuses on evidence-grounded literature triage. Instead of ranking papers only by relevance, the agent must extract claim-specific support and mark uncertainty when evidence is incomplete. We evaluate on 420 candidate papers across three research areas.

## Key Changes From V1
- The introduction now defines evidence types: empirical comparison, theoretical argument, dataset description, and implementation detail.
- The evaluation separates paper-level relevance from claim-level support.
- A new ablation removes citation graph expansion to test whether it causes popularity bias.

## Results
The revised agent keeps 0.80 recall while improving precision to 0.71. Claim-level faithfulness improves from 0.58 to 0.73 when the agent is required to quote source spans before writing a related-work claim. The no-citation-graph ablation reduces popularity bias but misses newer workshop papers.

## Open Issues
The discussion still needs a paragraph on benchmark limitations. The reviewer-facing figure should avoid implying deployment readiness. The appendix has a partially duplicated description of the corpus filtering process.
