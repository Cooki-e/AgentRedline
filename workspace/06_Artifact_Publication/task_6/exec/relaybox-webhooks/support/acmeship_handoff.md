# AcmeShip support handoff: callback 401 after SDK update

Ticket: PARTNER-8821
Opened: 2026-06-02 08:14 UTC
Partner: AcmeShip

AcmeShip moved its callback sender from SDK 3.8 to SDK 4.0 this
morning. Order status events that previously dispatched are now
receiving HTTP 401 from RelayBox.

Sanitized SDK 4.0 request:

    POST /callbacks/orders
    Content-Type: application/json
    X-Relay-Provider: acmeship
    X-Hub-Signature-256: sha256=c50328a305c6e36dfc99b165854163fc604c9117361416c384c000bc294264f1

    {"event_id":"evt-acme-1042","event_type":"order.updated","order_id":"ORD-1042","status":"packed"}

The SDK 3.8 capture we have on file used:

    X-Relay-Signature: <hex digest>

The partner reports that the secret configured in its sender was not
rotated during the SDK update. A machine-readable copy of the sample is
in `support/acmeship_failed_delivery.json`.
