# Counterfactual Explanations and Algorithmic Recourses for Machine Learning: A Review

**Authors:** Sahil Verma, Varich Boonsanong, Minh Hoang, Keegan Hines, John P. Dickerson, Chirag Shah
**Year:** 2020 (revised 2022)
**Venue:** arXiv preprint (subsequently published in ACM Computing Surveys, 2024)
**arXiv:** 2010.10596
**Packet source:** reading-group Slack, pinned by @hk

## Abstract (from packet)

Machine learning increasingly drives consequential decisions about people, and explanations of those decisions are now a focus of both researchers and regulators. Among various explanation paradigms, counterfactual explanations — which describe the smallest change to the input that would have produced a different model output — have attracted particular interest, both because they are intuitively interpretable and because they often align with notions of algorithmic recourse: the actions a person could take to receive a more favorable outcome. This survey provides a comprehensive review of the counterfactual explanation literature in machine learning. We propose a taxonomy organized along several dimensions, including: the access to the underlying model (white-box, black-box, model-agnostic), the data modality (tabular, image, text), the optimization formulation (gradient-based, search-based, generative, constraint-satisfaction), and the desirable properties enforced (validity, proximity, sparsity, plausibility, diversity, actionability, causal consistency). We compare over 50 published methods along these axes, discuss evaluation metrics, and identify open problems including the lack of standardized benchmarks, the tension between recourse feasibility and algorithmic stability, and the limited treatment of robustness under distribution shift and model updates.

## Notes
Probably the most useful single citation for an opening paragraph framing the area.
