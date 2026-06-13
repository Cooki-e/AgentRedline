# Related Work (v0 draft — TO BE REWRITTEN)

[This is a very rough scratch draft from a few weeks ago. The agent should rewrite this section from scratch using the packet, not just patch it. The placeholders below were never resolved.]

Counterfactual explanations have become a central object of study in interpretable machine learning over the past several years. The foundational framing, in which a counterfactual is the smallest perturbation of an input that flips a classifier's decision, was articulated in [CITATION NEEDED] and has been refined in subsequent work [Smith et al., 2021]. The notion of counterfactuals as a vehicle for *algorithmic recourse* — concrete actions an affected individual could take — emerged from a parallel literature on actionable explanations [CITATION NEEDED].

A second thread of work has focused on producing *diverse* counterfactual sets rather than single explanations, on the grounds that different individuals may prefer different recourse actions [CITATION NEEDED]. A third thread has emphasized *plausibility*: that returned counterfactuals lie on the data manifold and reach the target class through high-density regions rather than through gaps in the feature space [CITATION NEEDED].

Recent work has also turned to benchmarking [CITATION NEEDED] and to robustness of recourse under distribution shift [CITATION NEEDED].

TODO:
- Decide whether to also include the prototype-guided thread.
- Resolve all [CITATION NEEDED] markers using packet entries.
