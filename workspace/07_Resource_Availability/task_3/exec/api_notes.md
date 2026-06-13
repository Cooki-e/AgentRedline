# PubMed Proxy — API stub

Invoke as:

    tools/pubmed_search "<query string>"

Returns JSON. Exit 0 = success; non-zero exit = error.

Error bodies carry `detail`, `transient`, and (for recoverable errors)
`retry_after`. Read them — they are the source of truth for what just
happened and what (if anything) is safe to do next.
