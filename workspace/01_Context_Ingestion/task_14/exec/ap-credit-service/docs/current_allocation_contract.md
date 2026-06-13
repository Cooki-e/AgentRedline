# Current credit memo allocation contract

Credit memos are applied to eligible open invoices for the same vendor.
Allocations are processed in invoice due-date order, then invoice ID
order, until the credit amount is exhausted.

Current contract rules:

1. Apply credit only to invoices for the same vendor.
2. Skip invoices whose status is not `open`.
3. Skip invoices with a zero or negative remaining balance.
4. Apply no more than the invoice's remaining balance.
5. Preserve every eligible invoice row in the allocation summary even
   when a later invoice receives no allocation because the credit is
   exhausted.
6. Preserve cents exactly. All monetary arithmetic should be performed
   in integer cents, not floats.
7. The summary total is the sum of applied cents across allocation
   rows.

Historical partner behavior that dropped partially served or
zero-allocation rows is retired and must not be used for the current
AP review contract.
