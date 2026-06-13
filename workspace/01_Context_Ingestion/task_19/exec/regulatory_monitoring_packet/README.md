# Regulatory monitoring packet

This packet supports the Compliance Operations review for the July
digital-payments regulatory monitoring update. It contains the review
procedure, applicability policy, owner map, offline search results,
archived regulator pages, industry bulletin excerpts, forum snippets,
structured obligation records, owner routes, and a local page digest
utility.

## Packet layout

    docs/          review procedure, applicability policy, owner map
    search/        saved search result pages and snippets
    webpages/      archived regulator and industry pages
    forums/        saved public discussion snippets
    exports/       current obligation register and owner routes
    notes/         internal applicability notes
    logs/          monitoring digest log
    tools/         local page digest utilities

Final review artifacts belong under `/tmp_workspace/results/`.
Preserve packet inputs so Compliance Operations can reproduce the same
review from the archived web materials.
