# Receiver architecture

`src/webhooks/handler.py` is the HTTP-facing adapter used by the
partner callback route. It passes the request headers and exact raw
body bytes to `src/webhooks/signature.py`, parses the body after the
receiver check succeeds, and delegates the resulting event to
`src/webhooks/service.py`.

The signature helper intentionally does not know order-domain rules.
Its responsibility is limited to normalizing the supported signature
representation and checking the digest generated from the raw body.
