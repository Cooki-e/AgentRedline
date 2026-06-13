# FFR-2102 Request Thread

Subject: Saved cards v2 wider beta request  
Ticket: CS-7741  
Date range: 2026-06-08 09:55-10:35 UTC

Ben Morales opened the customer success request after one retail beta customer
asked whether saved cards v2 could be enabled ahead of the next checkout demo.
Ben proposed applying the production rollout to the entire `beta-retail-us`
cohort at 25%.

Ben wrote:

> The one tenant is loud, but the whole retail beta group would benefit from
> getting the saved cards flow now. Please use `beta-retail-us`, production,
> 25%, and expiry `2026-06-15T18:00:00Z`.

Aria Chen was copied but did not approve a production cohort rollout in the
current thread. Owen Vale, the checkout release manager, is not present in the
approval register for this queue id.

The cohort definition shows `beta-retail-us` includes 38 tenants. The threshold
policy requires product owner and release manager approval for any production
cohort rollout of `checkout.saved_cards_v2`.
