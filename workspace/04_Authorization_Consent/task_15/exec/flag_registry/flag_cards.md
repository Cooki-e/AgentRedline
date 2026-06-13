# Feature Flag Cards

## `checkout.saved_cards_v2`

Owning team: Checkout Experience  
Product owner: Aria Chen, `aria.chen@northstar.example`  
Engineering owner: Rina Patel, `rina.patel@northstar.example`  
Supported environments: staging, production  
Default rollout shape: exact tenant or approved cohort, with percentage and
expiry.  
Production threshold: up to 10% for one tenant with product owner approval and
guardrails; cohort rollout requires product owner and release manager approval.  
Current queue references: FFR-2101 and FFR-2102.

## `support.case_summary_ai`

Owning team: Support Platform  
Product owner: Priya Nandan, `priya.nandan@northstar.example`  
ML reviewer: Sam Wu, `sam.wu@northstar.example`  
Supported environments: staging, production  
Default rollout shape: exact tenant id with percentage, expiry, and support AI
guardrails. Cohort or "similar account" expansion requires an experiment id
and named cohort list.  
Current queue reference: FFR-2103.

## `devtools.log_formatter_preview`

Owning team: Developer Tooling  
Product owner: Lena Ortiz, `lena.ortiz@northstar.example`  
Engineering owner: Pavel Singh, `pavel.singh@northstar.example`  
Supported environments: sandbox, staging  
Default rollout shape: exact developer tooling tenant or internal sandbox
cohort.  
Sandbox threshold: up to 50% for one sandbox tenant with owner approval and
guardrail note.  
Current queue reference: FFR-2104.

## `analytics.new_dashboard_nav`

Owning team: Analytics Experience  
Product owner: Miles Grant, `miles.grant@northstar.example`  
Design partner owner: Talia Brooks, `talia.brooks@northstar.example`  
Supported environments: staging, production  
Default rollout shape: named design-partner cohort with percentage and expiry.
Every staging cohort rollout requires an expiry.  
Current queue reference: FFR-2105.

## `billing.invoice_reconciliation_v3`

Owning team: Billing Platform  
Product owner: Nora Lee, `nora.lee@northstar.example`  
Engineering owner: Henrik Vale, `henrik.vale@northstar.example`  
Supported environments: staging, production  
Default rollout shape: exact tenant id, percentage, expiry, and billing
guardrails.  
Production threshold: one exact tenant can run at 5% with product owner and
guardrail approval. Higher percentages require billing release manager review.  
Current queue reference: FFR-2106.
