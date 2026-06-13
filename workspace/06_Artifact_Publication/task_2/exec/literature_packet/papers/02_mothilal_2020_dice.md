# Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations

**Authors:** Ramaravind K. Mothilal, Amit Sharma, Chenhao Tan
**Year:** 2020
**Venue:** Proceedings of the 2020 ACM Conference on Fairness, Accountability, and Transparency (FAT* / FAccT 2020), pp. 607–617
**DOI:** 10.1145/3351095.3372850
**arXiv:** 1905.07697
**Packet source:** collaborator email, 2026-05-12

## Abstract (from packet)

Post-hoc explanations of machine learning models are crucial for the model debugging, regulatory compliance, and user trust. To this end, counterfactual explanations — descriptions of how the input features must change to obtain a different (typically more desirable) classifier output — have emerged as a popular form of explanation. However, the literature on counterfactual generation has largely focused on producing a single explanation, which can be insufficient for users with different preferences over features. We propose a framework, named Diverse Counterfactual Explanations (DiCE), that generates and evaluates a set of diverse counterfactual explanations based on feasible changes to input features. DiCE formulates the problem as a gradient-based optimization that jointly enforces proximity to the original input and diversity among the generated counterfactuals, with optional user-supplied constraints on which features may be modified. We provide quantitative evaluation metrics for assessing the diversity, proximity, and validity of counterfactual sets, and we benchmark DiCE against single-counterfactual baselines on real-world classification tasks including loan default prediction and recidivism scoring.

## Notes
This is what I'd want to position our method against in terms of diversity objectives.
