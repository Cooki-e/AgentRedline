# Actionable Recourse in Linear Classification

**Authors:** Berk Ustun, Alexander Spangher, Yang Liu
**Year:** 2019
**Venue:** Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* 2019), pp. 10–19
**DOI:** 10.1145/3287560.3287566
**arXiv:** 1809.06514
**Packet source:** reading-group Slack, pinned by @jw

## Abstract (from packet)

Machine learning models are routinely deployed to make decisions about individuals in domains such as lending, hiring, and policing. When such a model rejects an individual, the question of what that individual can do to be accepted in the future — that is, what recourse the model affords — is rarely answered. We introduce the notion of *actionable recourse* and formulate the problem of providing recourse in linear classification. A recourse is actionable if it can be achieved by changing only mutable features under user-specified directional constraints (some features can only increase, others only decrease, others are immutable). We cast actionable recourse as a linear integer program that, given a rejected individual and a linear classifier, returns the minimum-cost set of feature changes that flips the decision while respecting the actionability constraints. We provide algorithms to (a) compute recourse for a given individual, and (b) audit a classifier to measure the prevalence and difficulty of recourse across a population. Experiments on lending and recidivism datasets show that fixed-population audits reveal recourse disparities not visible through standard accuracy or fairness metrics.

## Notes
Sets up the recourse subproblem nicely. Linear-classifier focused but the framing is general.
