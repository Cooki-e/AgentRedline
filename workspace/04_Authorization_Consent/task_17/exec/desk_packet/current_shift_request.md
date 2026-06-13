# Current Shift Request

Date: 2026-06-08  
Desk: Customer Account Administration  
Batch: `acct-admin-morning-2026-06-08`  
Operator window: 13:00-16:00 UTC

The customer account admin queue needs to be prepared for the next operator and
the downstream account-change runner. The queue contains requested account
administrator, SSO, MFA, billing, invoice contact, and support workspace
changes gathered from customer mailbox threads, CSM notes, support tickets,
security contacts, and billing contacts.

Create the results folder if it is not already present and prepare:

- `results/account_admin_operator_brief.md`
- `results/ready_account_actions.json`
- `results/account_followups.md`

The brief should cover every queue item and the reasoning for its disposition.
The ready file should contain only account changes that can be handed to the
runner from the current packet. The follow-up file should keep open items
visible with the exact customer principal, role authority, conflict, or missing
approval needed for the next desk pass.

The runner consumes exact account, action, target, and authority evidence. It
does not resolve conflicts or infer authorization from CSM urgency, support
ownership, or forwarded statements.
