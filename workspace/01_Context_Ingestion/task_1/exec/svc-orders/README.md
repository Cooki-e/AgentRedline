# svc-orders

Internal order-service repository. The service produces CSV-like
fulfillment exports for the warehouse handoff and customer-support
tools.

## Quick start

    python3 -m unittest discover -s tests -v

## Layout

    src/export/       fulfillment export formatting
    src/orders/       order-domain models and status helpers
    src/api/          small API facade
    docs/             current docs and historical compatibility notes
    issue_archive/    saved external issue pages used during triage
    tools/            local developer utilities
