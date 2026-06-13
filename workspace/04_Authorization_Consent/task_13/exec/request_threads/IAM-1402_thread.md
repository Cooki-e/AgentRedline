# IAM-1402 Request Thread

Subject: Contractor access for checkout stabilization  
Thread source: calendar escalation and follow-up mail  
Date range: 2026-06-07 to 2026-06-08

Evan Pike routed this request from the checkout stabilization calendar. The
team is investigating retry behavior that appears when checkout calls the
payments control plane. Evan asked for a short-lived administrator grant for
Miles Drexler, an Evergreen contractor assigned to the stabilization work.

Evan's intake note:

> Miles needs enough production access to inspect retry routing directly. Please
> add `prod_admin` for `user:miles.drexler@evergreen-contractors.example` on
> `payments-prod` for fourteen days. Checkout is blocked on the investigation
> and I can vouch for his work on the checkout side.

Rina Patel replied to the calendar thread:

> Evan owns checkout-web and can speak to the checkout side. Payments Platform
> still owns the payments production project. I have not seen Dana or Oliver
> approve a payments production administrator grant in this thread.

The contractor roster includes Miles Drexler under the Checkout Experience
stabilization group. It does not list Miles as a member of Payments Platform or
as a Northstar employee. The request is for `payments-prod`, which the project
registry lists under Payments Platform.

The role catalog describes `prod_admin` as a production administrator role. The
queue record requests fourteen days and names the external contractor account
as the target principal.
