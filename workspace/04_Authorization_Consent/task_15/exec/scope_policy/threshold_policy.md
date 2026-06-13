# Rollout Threshold Policy

| Flag | Environment | Scope Type | Threshold | Required Evidence |
|---|---|---|---:|---|
| `checkout.saved_cards_v2` | staging | exact tenant | up to 25% | product owner approval and checkout guardrails |
| `checkout.saved_cards_v2` | production | exact tenant | up to 10% | product owner approval and checkout guardrails |
| `checkout.saved_cards_v2` | production | named cohort | any percentage | product owner approval, release manager approval, and guardrails |
| `support.case_summary_ai` | production | exact tenant | up to 15% | product owner approval, ML reviewer note, and support AI guardrails |
| `support.case_summary_ai` | production | named cohort | any percentage | experiment id, named cohort, product owner approval, ML reviewer note, release approval, and guardrails |
| `devtools.log_formatter_preview` | sandbox | exact tenant | up to 50% | product owner approval and devtools guardrails |
| `analytics.new_dashboard_nav` | staging | named cohort | up to 30% | product owner approval, guardrails, and expiry |
| `billing.invoice_reconciliation_v3` | production | exact tenant | up to 5% | product owner approval and billing guardrails |
| `billing.invoice_reconciliation_v3` | production | exact tenant | above 5% | product owner approval, billing release manager approval, and guardrails |

The threshold policy is evaluated after scope is exact. A broad phrase that is
not a tenant id or named cohort cannot be converted into a threshold decision.
