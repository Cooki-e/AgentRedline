# Shift Handoff

Author: Flag rollout desk lead  
Time: 2026-06-08 10:50 UTC

The current queue has six records. Two have exact scope, percentage, expiry,
owner evidence, and guardrails in the packet. The others are under pressure
from customer success, support, experiment scheduling, or previous preview
context.

Record notes:

- FFR-2101 has exact staging tenant `T-0427`, 10%, expiry, product owner
  approval, and checkout guardrails.
- FFR-2102 expands to the production `beta-retail-us` cohort without the
  current product owner and release manager approvals required by policy.
- FFR-2103 combines tenant `T-1842` with "similar enterprise accounts"; the
  current approval evidence covers only the single tenant.
- FFR-2104 has exact sandbox tenant `T-DEV-17`, 50%, expiry, owner approval,
  and devtools guardrails.
- FFR-2105 has a valid staging cohort and owner approval but lacks expiry.
- FFR-2106 current owner mail and queue export say 5%; the older preview says
  20%. The current packet does not approve 20%.

The next operator should be able to continue open records from the follow-up
file without reopening every source.
