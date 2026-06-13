# Sample reconciliation

The local SQLite database contains the sampled transaction rows and
reviewer status rows used by the query utility. The `exports/`
directory contains the same open-exception set in a compact form for
reviewers who prefer to read JSON and CSV.

The period total should be treated as five open exceptions. The
resolved engineering transaction is useful for checking that the query
is filtering by reviewer status rather than simply listing every
sampled row.
