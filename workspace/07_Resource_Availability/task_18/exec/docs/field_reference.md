# Field reference

`forecast_rps`
: Forecast requests per second for the date and service.

`p95_latency_ms_baseline`
: Baseline p95 latency estimate before capacity plan changes.

`current_replicas`
: Current replica count observed in the planning snapshot.

`scenario_id`
: Capacity scenario identifier.

`*_replicas`
: Proposed replica count for the service named by the column.

`estimated_monthly_delta_usd`
: Estimated monthly infrastructure spend delta for the scenario.

`slo_burn_pct`
: Estimated SLO burn for the service period.

`capacity_incidents_projected`
: Projected number of capacity incidents for the scenario.

`headroom_pct`
: Estimated peak headroom percentage.
