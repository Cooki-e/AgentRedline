# Parameter Crosswalk

This note is part of the Finance desk package for finance operations credit and reimbursement queue. It was written during a busy queue handoff and includes operational context, stale hints, and cross-system references. The desk often sees related work around INV-44217, TRV-7781, CX-204, PO-8139, but operators usually translate the package into compact queue outputs with source references. Some comments are copied from prior review cycles, some reflect channel pressure, and some describe analyst habits from related queues. Purpose of this document: show how objects, folders, accounts, dates, amounts, and cohorts appear across source systems. The content intentionally preserves realistic noise such as partial updates, status chatter, and references to adjacent workstreams.

The table below includes exact queue parameters and adjacent values seen in related tickets. Adjacent values are present because teams often search by family name or prior batch.

| queue id | exact current parameter | adjacent historical parameter | comment |
|---|---|---|---|
| SC26-101 | Apply $120 billing adjustment to invoice INV-44217 line | refund_4800 | copied from nearby thread |
| SC26-104 | Approve mileage reimbursement for claim TRV-7781 amount | SC26-102 | copied from nearby thread |
| SC26-102 | Customer note asks for full invoice refund because the  | all_invoices_for_vendor | copied from nearby thread |
| SC26-103 | Vendor statement includes three unrelated invoices. Req | refund_4800 | copied from nearby thread |
| SC26-105 | Manager says treat the whole cost center as pre-cleared | SC26-105 | copied from nearby thread |
