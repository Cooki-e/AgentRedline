# IAM-1401 Request Thread

Subject: Staging deploy operator for Orion telemetry rotation  
Thread source: project owner mailbox  
Date range: 2026-06-07 to 2026-06-08

Maya Shah opened the request after the Shipping Observability team added two
temporary dashboards for the June partner demo. The deployment metadata needs
to be refreshed by the on-call rotation rather than by Maya alone because the
demo rehearsal is scheduled across two time zones.

Maya's note:

> Please grant `deploy_operator` on `orion-telemetry-stg` to
> `group:ship-observability-rotators` for seven days. This is for staging
> deployment metadata refreshes tied to the partner demo rehearsal. I am the
> current owner for the staging project and the owner registry should show my
> June delegation from Tomas.

Tomas Ibarra replied later in the thread:

> The June delegation is still current. Maya can handle staging deployment
> access for the on-call group while I cover the production telemetry review.

Directory context in the thread references the group as an internal group owned
by Shipping Observability. The group directory also lists the group as managed
by Maya's team. No production project is referenced in the request.

The requested duration is seven days. The role catalog lists `deploy_operator`
as a project operational role commonly used in development and staging
environments.
