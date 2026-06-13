# TicketDesk Admin

TicketDesk Admin prepares a support-desk workflow packet. It can
refresh account context, draft routing state, and produce an
escalation digest for full desk review cycles.

Example:

    python3 tools/ticketdesk_admin/ticketdesk_admin.py --tickets data/support_tickets_june1.json --accounts data/account_directory.csv --output results/escalation_digest.md --refresh-account-context --prepare-routing
