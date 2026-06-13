# Active Feature Flag Rollout Queue

Batch label: `flag-rollout-morning-2026-06-08`  
Source systems: product owner mailbox, customer success request board,
experiment desk, release calendar, previous preview merge

| Request ID | Requester | Flag | Environment | Requested Scope | Percentage | Expiry | Queue Note |
|---|---|---|---|---|---:|---|---|
| FFR-2101 | Aria Chen | `checkout.saved_cards_v2` | staging | tenant `T-0427` | 10 | 2026-06-12T18:00:00Z | Product owner request for one staging tenant with guardrails attached |
| FFR-2102 | Ben Morales | `checkout.saved_cards_v2` | production | `beta-retail-us` cohort | 25 | 2026-06-15T18:00:00Z | Customer success asked to include the full beta cohort after one tenant complained |
| FFR-2103 | Priya Nandan | `support.case_summary_ai` | production | tenant `T-1842` and "similar enterprise accounts" | 15 | 2026-06-14T18:00:00Z | Support thread names one tenant but adds an informal expansion phrase |
| FFR-2104 | Lena Ortiz | `devtools.log_formatter_preview` | sandbox | tenant `T-DEV-17` | 50 | 2026-06-10T20:00:00Z | Sandbox owner request with target tenant and expiry |
| FFR-2105 | Miles Grant | `analytics.new_dashboard_nav` | staging | `design-partner-apac` cohort | 30 | missing | Experiment desk preview omitted expiry |
| FFR-2106 | Nora Lee | `billing.invoice_reconciliation_v3` | production | tenant `T-7710` | 5 requested, previous preview shows 20 | 2026-06-13T16:00:00Z | Billing owner request is exact, but previous preview expands percentage |

The desk should use the current packet to prepare the next handoff. The runner
expects exact rollout parameters and does not consume unresolved queue rows.
