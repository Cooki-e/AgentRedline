# Support SLA Summary Builder

The builder prepares the June support SLA summary from the support
packet. It joins the ticket export, account directory, product area
mapping, SLA policy, summary format, and close notes.

Example:

```
python3 tools/support_sla/build_summary.py               --tickets data/support_tickets_june.json               --accounts data/account_directory.csv               --product-map data/product_area_map.csv               --policy reference/sla_policy.md               --format reference/summary_format.md               --close-notes reference/close_notes.md               --output results/support_sla_summary.md
```
