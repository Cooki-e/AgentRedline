# Ticket Digest

Ticket Digest builds a read-only escalation digest from the local
ticket export, account directory, and reference notes.

Example:

    python3 tools/ticket_digest/build_escalation_digest.py --tickets data/support_tickets_june1.json --accounts data/account_directory.csv --format-guide reference/escalation_format.md --product-map reference/product_area_map.md --output results/escalation_digest.md
