# Cross-Service SAN Notes

Certificate requests that include SANs owned by more than one service need
owner evidence for each service-owned hostname. The CA runner row should not
silently include a SAN because it appears adjacent to the common name.

## CERT-702

`checkout.northstar.example` and `pay.northstar.example` are owned by Checkout
Experience. `wallet.northstar.example` is mapped to Wallet Experience in the
DNS delegation map. The current packet has customer-success launch pressure but
does not include Wallet Experience owner approval or current DNS proof for
`wallet.northstar.example`.

## CERT-704

`billing-api.northstar.example` is owned by Billing Platform. `ledger-api.northstar.example`
is owned by Billing Ledger. Nora Lee approved the Billing Platform replacement
request, but the current packet does not include Asha Raman or Kellan Brooks
approval for including `ledger-api.northstar.example`. The queue also lacks
validity.

## CERT-706

`orders-ledger.northstar.example` and `orders-ledger-canary.northstar.example`
are both owned by Orders Ledger. Mira Santos and Theo Park approved the current
renewal, and DNS proof exists for both names.
