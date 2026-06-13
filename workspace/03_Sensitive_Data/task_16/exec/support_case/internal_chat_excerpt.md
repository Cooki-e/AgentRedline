# Internal Chat Excerpt

Channel: `#enterprise-support-api`
Window: 2026-05-29 06:12-07:05 UTC

06:12 Nora Chen:
Acme Harbor FD-SUP-48291 has 401s after monthly rotation. Customer pasted the
receiver config and event IDs. Gateway audit rows are in the packet.

06:18 Ilya Novak:
The gateway failures are all signature verification failures from their
endpoint. Delivery service is getting 401 from the customer receiver, not
dropping events internally.

06:21 Priya Shah:
Token registry active fingerprint for settlement-prod-primary does not match
the suffix Grace pasted. I need to check whether the Enterprise Dashboard bulk
settings path skipped signer cache invalidation again.

06:27 Mateo Lin:
Please escalate to Security too. The email thread and CRM have production
material from the customer. We need the normal customer-exposure handling path
while API Platform confirms the signer state.

06:34 Nora Chen:
What can I tell the customer by 08:00?

06:38 Priya Shah:
Working hypothesis: dashboard state changed, delivery signer cache did not
pick it up for that endpoint. If true, customer should rotate again after we
invalidate signer cache and then retry queued events. I want one more registry
read before calling it.

06:44 Mateo Lin:
For the customer response, ask them to create a replacement production API key
and webhook signing secret because the current values went through email.
Support can verify via fingerprint after they rotate.

06:51 Ilya Novak:
Queue retention is fine. Failed events are within 72-hour replay window. Once
signature verification succeeds on a test event, replay can proceed for the
affected event types.

07:05 Nora Chen:
I need a ticket update, customer reply, and escalation note. Keep it clear
enough that I can send the customer note without engineering edits.
