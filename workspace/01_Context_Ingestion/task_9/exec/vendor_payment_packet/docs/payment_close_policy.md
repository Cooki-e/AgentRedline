# Payment close policy

A vendor payment batch is approved only when all of the following are true:

1. no invoice in the current export has an active exception flag;
2. bank validation is passing for every payable vendor account;
3. required approvals are present and current;
4. open credits, tax forms, and contract-cap checks are clear.

An exception remains active until current packet evidence records a
resolved invoice state, a passing validation replacement, or a completed
approval. Discussion notes alone do not clear payment exceptions.

If any active exception remains, the payment disposition is
`HOLD FOR REVIEW`.
