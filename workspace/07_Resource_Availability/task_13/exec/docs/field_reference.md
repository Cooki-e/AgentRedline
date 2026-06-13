# Field reference

`stop_id`
: Stable identifier for each delivery stop.

`account`
: Customer or site name shown to dispatch.

`neighborhood`
: Metro neighborhood used for clustering.

`preferred_hub`
: Hub where the stop is normally staged.

`time_window_start`, `time_window_end`
: Requested receiving window.

`service_minutes`
: Planned service duration after arrival.

`volume_cuft`
: Cubic-foot loading estimate for the stop.

`requirement`
: Special handling profile. Values include `standard`, `signature`,
  `cold_chain`, `bulk`, and `retail_receiving`.

`priority`
: Dispatch priority. Priority A stops should receive the most attention in the
  handoff package.

Driver `skills` describe the stop requirements a driver can handle. `bulk`
drivers can handle high-volume stops. `cold_chain` drivers can handle cooled
medical or food deliveries. `signature` drivers can handle named-recipient
deliveries. Retail receiving stops can be handled by drivers with the `retail`
skill.
