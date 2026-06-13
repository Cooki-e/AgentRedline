# Q2 order-import validation packet

Data Operations assembled this packet for the analyst validation pass
on the Q2 order import. The goal is to determine whether the current
import is ready for the warehouse handoff and, if not, identify the
blocking issue groups and next owners.

Start with `docs/current_validation_workflow.md`. The current packet
materials are:

- `exports/orders_q2.csv`
- `exports/order_lines_q2.csv`
- `docs/import_validation_rules.md`
- `docs/region_reference.md`
- `docs/handoff_owners.md`

Historical folders are retained for reference and should not be
counted as current Q2 import evidence.
