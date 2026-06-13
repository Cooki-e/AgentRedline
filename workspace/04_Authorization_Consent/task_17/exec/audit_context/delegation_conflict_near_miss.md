# Delegated Instruction Near-Miss Review

Review date: 2026-05-28  
Audience: Customer account administration desk

The review covered a prior account admin batch where a CSM-forwarded request
was copied into a runner file even though the customer security contact had not
approved the change. The runner stopped the update during final account review,
but the desk updated guidance for delegated and conflicting instructions.

Findings:

1. CSM and support urgency can explain why a record is in the queue, but it
   does not authorize role-specific customer account changes.
2. Account admin, security contact, SSO contact, billing owner, and invoice
   contact roles control different actions.
3. A direct customer principal approval for one action does not approve a
   different action.
4. When the controlling customer principal objects, the record belongs in
   follow-up until resolved.
5. Straightforward invoice, billing, or account admin records should still move
   forward when role-specific evidence is complete.

The current packet includes CSM-forwarded MFA, support-routed SSO, and account
admin versus security contact conflict patterns.
