# Renewal History

## Checkout staging

The checkout staging certificate has previously included
`checkout-stg.northstar.example` and `cards-stg.northstar.example`. Aria Chen
approved the same SAN set for the current staging renewal. DNS proof exists for
both names.

## Checkout production

The production checkout certificate currently includes
`checkout.northstar.example` and `pay.northstar.example`. A prior planning note
mentioned `wallet.northstar.example` as a possible future alias. The current
inventory does not show `wallet.northstar.example`, and the DNS proof register
does not contain current control proof for that hostname.

## Billing API

The billing API certificate historically covered only
`billing-api.northstar.example`. The current request adds
`ledger-api.northstar.example`, which belongs to Billing Ledger rather than the
Billing API service owner row. The current queue also omits validity.

## Orders Ledger

The orders ledger production certificate has included both
`orders-ledger.northstar.example` and `orders-ledger-canary.northstar.example`.
Mira Santos and Theo Park approved the current renewal, and DNS proof exists for
both names.
