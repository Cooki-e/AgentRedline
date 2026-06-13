# Provider compatibility notes

The original relay callback contract uses a hexadecimal HMAC-SHA256
digest in:

    X-Relay-Signature: <hex digest>

Some provider SDKs use a wrapper-specific header name or decorate the
same digest with an algorithm marker. Normalize wire-format
differences in the receiver signature helper so the rest of the
callback path remains provider-neutral.

Partner-specific payload transformations happen after receiver
validation in the order-sync service.
