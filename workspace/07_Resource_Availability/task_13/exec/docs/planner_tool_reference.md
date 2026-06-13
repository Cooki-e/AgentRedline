# Planner tool reference

`tools/route_planner propose --date DATE --region REGION --out PATH`

: Builds a candidate route plan for the requested service date and region, then
  writes the scenario JSON to `PATH`. The command also prints a compact JSON
  summary containing the scenario identifier and headline metrics.

`tools/route_planner show --scenario-id SCENARIO_ID`

: Prints a previously generated scenario JSON.

`tools/route_planner history`

: Prints the list of generated scenarios in this workspace.

Tool activity is recorded under `state/`. Scenario JSON files can be used as the
source for the final route plan and route manifest.
