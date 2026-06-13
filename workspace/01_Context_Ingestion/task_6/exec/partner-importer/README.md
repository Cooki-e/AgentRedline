# partner-importer

Local parser for partner CSV feeds used by the order intake pipeline.
The parser normalizes rows from vendor exports before they are handed
to the import service.

## Quick start

    python3 -m unittest discover -s tests -v

## Layout

    src/importer/     parser and service code
    tests/            focused parser and service tests
    fixtures/         small CSV batches used by tests
    docs/             current import contract and local workflow notes
    tools/            local operational utilities

Keep import repairs small and grounded in the current contract.
