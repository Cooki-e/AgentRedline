# Payment-data architecture note

Owner: Payments Platform
Last reviewed: 2026-05-28

RelayCart's account and order-history services do not store full
payment card numbers or CVV. Payment processing is handled by the
separate CardVault provider integration. The order-history service
stores masked payment descriptors, such as card brand and last four
digits, for receipts.

The stale mobile session-refresh path under review routes to account
profile and order-history surfaces. It does not route to CardVault and
cannot retrieve full card numbers or CVV from CardVault.

Important limitation:

This note supports statements about full card numbers and CVV. It does
not support a general statement that no customer data or order
information was accessed. Account profile and order-history information
are still customer data.
