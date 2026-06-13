# CRM pipeline field dictionary

`id`
: Stable CRM record identifier. North Region review records use the `NR-####`
  pattern.

`segment`
: Sales planning segment. This request uses `north-region`.

`region`
: Human-readable region label used in management decks.

`status`
: Current lifecycle state. The Monday packet is concerned with records whose
  status is `open`.

`stage`
: Current opportunity stage. The standard stage values are `new`, `discovery`,
  `qualified`, `evaluation`, `proposal`, `security_review`, `procurement`, and
  `contracting`.

`owner`
: Account executive or territory owner responsible for the next action.

`source`
: Lead source captured at creation time. Common values are `web-demo`,
  `partner-referral`, `field-event`, `outbound`, `customer-expansion`,
  `marketplace`, and `webinar`.

`estimated_value_usd`
: Current estimated annual contract value in US dollars. The Sales Operations
  high-value cut is `>= 250000`.

`created_at`
: Record creation timestamp in UTC.

`updated_at`
: Last CRM update timestamp in UTC.

`last_touch_at`
: Most recent customer-facing sales activity timestamp. For this packet, stale
  means more than seven days older than the `2026-06-02T09:30:00Z` packet
  timestamp.

`target_close_date`
: Forecast close date used for territory planning.

`next_step`
: Short free-text next action from the CRM record.
