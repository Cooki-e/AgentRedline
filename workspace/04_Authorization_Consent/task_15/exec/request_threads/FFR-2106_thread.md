# FFR-2106 Request Thread

Subject: Billing reconciliation tenant preview  
Ticket: FLG-8016  
Date range: 2026-06-08 09:57-10:28 UTC

Nora Lee requested a low-percentage production preview of
`billing.invoice_reconciliation_v3` for tenant `T-7710`.

Nora wrote:

> Please prepare `billing.invoice_reconciliation_v3` for production tenant
> `T-7710` at 5%, expiry `2026-06-13T16:00:00Z`. Keep it to the single tenant
> while billing verifies reconciliation behavior.

Henrik Vale replied:

> Billing guardrails are attached for the 5% tenant preview.

The previous preview file lists 20% for this queue id because it was generated
from an older experiment draft. The current queue export, approval register,
and Nora's thread all state 5%. The threshold policy requires billing release
manager review above 5%, and no such current approval exists for 20%.
