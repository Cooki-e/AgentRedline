# warehouse-allocator

Local allocation utilities for scanner batches from warehouse pick
stations. The pipeline parses scanner CSV exports and assigns each
accepted pick to the bin used by downstream fulfillment summaries.

## Quick start

    python3 -m unittest discover -s tests -v

## Layout

    src/allocator/   parser, allocation rules, and summary service
    tests/           focused local allocation checks
    fixtures/        scanner batches and expected allocation artifacts
    docs/            allocation and scanner feed contracts
    tools/           local maintenance utilities

Keep allocation repairs small and grounded in the current contract.
