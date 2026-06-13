# Card transaction exception policy

A transaction exception remains open until the reviewer status export
records a resolved status with supporting evidence. The following
conditions block audit close:

1. missing itemized receipt for a card transaction over the documented
   receipt threshold;
2. split purchases that appear to bypass approval limits;
3. travel charges without matching itinerary or cost-center approval;
4. duplicate or near-duplicate charges pending cardholder explanation;
5. merchant category mismatch requiring procurement or finance review.

If any active exception remains open, the period status is
`OPEN EXCEPTIONS REMAIN`.
