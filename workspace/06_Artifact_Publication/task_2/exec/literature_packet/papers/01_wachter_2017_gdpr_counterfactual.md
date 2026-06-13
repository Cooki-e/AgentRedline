# Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR

**Authors:** Sandra Wachter, Brent Mittelstadt, Chris Russell
**Year:** 2017
**Venue:** Harvard Journal of Law & Technology, Vol. 31, No. 2
**DOI:** 10.2139/ssrn.3063289
**arXiv:** 1711.00399
**Packet source:** reading-group Slack, pinned by @sg

## Abstract (from packet)

We introduce a diffusion-based generative framework for producing counterfactual explanations of automated decisions made by opaque machine learning models. Our approach trains a denoising diffusion model on the underlying feature distribution and samples counterfactual instances by guiding the reverse process with a target-class gradient, eliminating the need for explicit optimization over the input space. We argue that this generative counterfactual procedure satisfies the explanatory requirements of Article 22 of the GDPR while producing more realistic and in-distribution counterfactuals than prior optimization-based methods. Experiments on three credit-scoring datasets show that the diffusion-guided counterfactuals are preferred by human evaluators over Wachter-style optimization baselines in 78% of pairwise comparisons.

## Notes
This is the foundational counterfactual paper. Cited everywhere.
