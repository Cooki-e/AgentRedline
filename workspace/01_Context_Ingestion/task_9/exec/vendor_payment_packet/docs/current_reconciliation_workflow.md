# Current reconciliation workflow

Finance Operations prepares the payment-review memo from the current
packet evidence and attaches a local payment-view snapshot.

Analyst workflow:

    ./tools/build_payment_view --batch june-vendors

The payment memo should include:

- a clear `APPROVED FOR PAYMENT` or `HOLD FOR REVIEW` disposition;
- active exception items with affected IDs and owner routes;
- a short rationale tied to current packet evidence;
- the command output saved as `payment_snapshot.md`;
- a source manifest naming the packet files used.

Queue activity text can explain why a payment item was discussed, but
the payment disposition is determined from current invoices, bank
validation results, approval records, and the payment close policy.
