# AP payment review policy

A batch is ready for payment operations only when every invoice in the
review set has a resolved reviewer status with supporting evidence.
The following conditions block payment handoff:

1. vendor remittance details do not match the vendor master record;
2. invoice total does not match the purchase-order or receiving record;
3. tax amount is missing, unreadable, or inconsistent with the invoice
   jurisdiction;
4. duplicate invoice number or near-duplicate scan remains unresolved;
5. required purchase-order approval is missing or expired.

If any active invoice exception remains open, the batch status is
`HOLD FOR AP REVIEW`.
