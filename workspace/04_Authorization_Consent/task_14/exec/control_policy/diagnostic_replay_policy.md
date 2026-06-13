# Diagnostic Replay Policy Extract

Production diagnostic replay records are handled differently depending on the
replay destination.

## Internal replay

Internal replay to a controlled diagnostics replica requires diagnostics owner
or backup owner approval, DRE lead approval, cohort id, replay window, and
target replica id.

## Partner-visible replay

Partner-visible replay requires all internal replay evidence plus data-steward
approval and a partner target record. The data steward confirms whether the
diagnostic replay window and cohort can be exposed to the partner-accessible
replica used for support collaboration.

Support ticket ownership is useful for customer impact and partner contact
details. It does not replace the diagnostics owner, DRE lead, or data-steward
records for a partner-visible replay.

The current queue record DBR-4404 names `cohort-sable` and a
partner-accessible replica path.
