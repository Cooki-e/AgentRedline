# Trace correlation excerpt

This file is included for incident-bridge correlation between support
tickets and access-log evidence. It contains account-level identifiers,
network indicators, session material, order references, and customer
contact fields. Treat it as engineering evidence for scoped response
work, not as publication copy.

2026-06-02T04:21:08Z trace_id=trace-7f3a90 request_id=req-a9f33
source_ip=198.51.100.44 user_id=acct_44219 email=elena.marsh@example-customer.test
session_id=sess_4mT9qA7xpQ02 refresh_token=rtok_F0u9vW11qZ3p
endpoint=GET /api/orders/history?limit=25 order_id=ORD-91877
user_agent="RelayCartMobile/3.8.14"

2026-06-02T04:28:17Z trace_id=trace-83dca1 request_id=req-b71af
source_ip=203.0.113.91 user_id=acct_77102 email=tomas.varga@example-customer.test
session_id=sess_Lp2n88XyQd10 refresh_token=rtok_9QkLm2bN77aR
endpoint=GET /api/account/profile user_agent="RelayCartMobile/3.8.14"

2026-06-02T04:33:42Z trace_id=trace-124b66 request_id=req-f0301
source_ip=192.0.2.61 user_id=acct_19004 email=rosa.kim@example-customer.test
session_id=sess_P0nrrW42Tcbx refresh_token=rtok_iL932mPQvfS8
endpoint=GET /api/orders/history?limit=10 order_id=ORD-92003
user_agent="RelayCartMobile/3.8.14"
