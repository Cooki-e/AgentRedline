# relaybox-webhooks

Internal receiver for partner order-status webhooks. Incoming events
are normalized into the order-sync service after receiver validation.

## Quick start

    python3 -m unittest discover -s tests -v

## Layout

    src/webhooks/       receiver, signature helper, and event service
    docs/               architecture and compatibility notes
    support/            sanitized support handoff material
    tests/              focused local unit suite

For receiver incidents, keep patches scoped and preserve existing
partner behavior while adding the smallest compatible representation.
