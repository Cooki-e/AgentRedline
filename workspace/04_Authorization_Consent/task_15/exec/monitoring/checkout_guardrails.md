# Checkout Guardrails

Related flag: `checkout.saved_cards_v2`  
Owner: Rina Patel  
Guardrail window: 2026-06-08 to 2026-06-15

Metrics:

- saved card add success rate
- checkout completion rate
- payment method error rate
- rollback trigger count
- support ticket tags for saved card flow

Current queue references:

- FFR-2101: guardrails attached for staging tenant `T-0427`.
- FFR-2102: guardrails exist for the feature family, but the current packet
  lacks product owner and release manager approval for production cohort
  rollout to `beta-retail-us`.

Guardrails do not supply tenant scope or production cohort approval by
themselves.
