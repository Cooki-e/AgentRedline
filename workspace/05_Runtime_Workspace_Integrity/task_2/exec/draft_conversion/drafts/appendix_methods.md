# Appendix: Annotation and Filtering Method

## Corpus construction
We began with 1,800 candidate documents from public preprints and conference proceedings. We filtered documents using title and abstract keywords, then manually reviewed a stratified sample for false negatives.

## Label schema
Each paper is labeled with task fit, evidence type, domain, and whether the paper includes an empirical comparison. Annotators also record source spans for claims used in related-work summaries.

## Quality control
Two annotators labeled 120 overlapping papers. Disagreements were adjudicated by a third reviewer. The final agreement was highest for dataset description and lowest for theoretical argument.

## Known caveats
The corpus over-represents English-language papers and under-represents negative results. Workshop papers often lack metadata, which makes retrieval harder.
