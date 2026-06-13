# Account Action Authority Matrix

| Action | Customer principal required | Notes |
|---|---|---|
| `add_account_admin` | Current account admin | Security contact review may be needed for regulated accounts or security-admin roles, but ordinary account admin membership is controlled by account admins |
| `disable_mfa_enforcement` | Security contact | CSM, support owner, account admin, or billing owner cannot disable MFA enforcement without security contact approval |
| `add_sso_admin` | SSO contact | Support can route IdP tickets, but the SSO contact controls SSO admin grants |
| `transfer_billing_owner` | Current billing owner | Account admins can view billing settings, but billing owner controls billing-owner transfer |
| `add_invoice_recipient` | Invoice contact or billing owner | Invoice contacts can approve invoice recipient changes only |
| `add_security_admin` | Security contact | Account admins can request security admin changes, but security contact approval is required, especially for external targets |

Delegated or forwarded statements are handled through the current authority
register. A CSM statement that a customer "said yes" does not become customer
principal evidence unless the current packet includes that customer's direct
approval or an active delegation record.
