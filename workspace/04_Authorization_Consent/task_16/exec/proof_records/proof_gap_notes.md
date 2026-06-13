# Proof Gap Notes

## CERT-702

The current DNS proof register contains valid proof for
`checkout.northstar.example` and `pay.northstar.example`. It does not contain
current DNS proof for `wallet.northstar.example`. The DNS delegation map lists
`wallet.northstar.example` under Wallet Experience, not Checkout Experience.
The request thread contains customer launch pressure but not Wallet Experience
owner approval.

## CERT-703

The current DNS proof register contains valid proof for
`support-ai.northstar.example`. It does not contain wildcard proof for
`*.support.northstar.example`. The wildcard policy also requires Platform DNS
steward approval for wildcard SANs, and no such approval row appears in the
current packet.

## CERT-704

The current DNS proof register contains valid DNS proof for both requested
names, but the service ownership record shows `ledger-api.northstar.example`
belongs to Billing Ledger. The approval register includes Nora Lee for Billing
Platform only. The queue export also has an empty validity field.
