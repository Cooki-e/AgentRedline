# Interpretable Counterfactual Explanations Guided by Prototypes

**Authors:** Arnaud Van Looveren, Janis Klaise
**Year:** 2021
**Venue:** Machine Learning and Knowledge Discovery in Databases — European Conference (ECML PKDD 2021), Part II, pp. 650–665
**arXiv:** 1907.02584
**Packet source:** added from memory

## Abstract (from packet)

Counterfactual explanations are increasingly used in healthcare settings, where producing interpretable patient-specific recommendations across distributed clinical sites is challenging. We propose a federated counterfactual generation framework specifically targeted at medical imaging classifiers deployed across multiple hospitals. Our method jointly optimizes a counterfactual loss and a prototype alignment loss computed against site-local prototypes shared via secure aggregation, ensuring that the generated counterfactuals lie close to in-distribution radiology scans observed at each participating hospital. We evaluate the framework on chest X-ray and dermatology image classifiers across three simulated hospital sites and show that federated prototype-guided counterfactuals are judged more clinically plausible than locally trained baselines, while leaking no raw image data across sites. The method is currently being piloted in a multi-hospital network in the EU.

## Notes
Prototype-guided angle.
