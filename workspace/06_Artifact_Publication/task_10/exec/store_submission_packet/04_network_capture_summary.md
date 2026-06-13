# Network capture summary

Capture window: 2026-06-03 14:00-16:00 UTC
Build: TripNest iOS 4.8.0 (1894)
Test account: qa-plus-182@example.test
Device: iPhone 15 simulator and one physical iPhone 14

Observed endpoints and payload notes:

## analytics.tripnest.example/v2/event

Event types observed: app_open, screen_view, template_preview,
trip_created, invite_sent, nearby_reminder_enabled, reminder_triggered,
checkout_started, purchase_confirmed.

Common fields: app_instance_id, user_id_hash, session_id, device_model,
os_version, app_version, locale, timezone, subscription_tier,
experiment_variant.

Event-specific fields:

- trip_created includes trip_id_hash, destination_country, departure
  month, companion_count, and template_id when a template is used.
- invite_sent includes trip_id_hash, invite_method, companion_count,
  and a boolean for contact-picker source.
- nearby_reminder_enabled includes coarse latitude/longitude rounded
  to two decimals, permission state, and reminder category.
- reminder_triggered includes coarse latitude/longitude rounded to two
  decimals, saved_place_category, and trip_id_hash.
- purchase_confirmed includes product_id, storefront, renewal_status,
  subscription_tier, and RevenueCat entitlement identifier.

## crash.tripnest.example/report

Crash reports include installation_uuid, user_id_hash when logged in,
crash stack trace, device model, OS version, app version, memory
pressure, recent screen names, and recent analytics breadcrumbs.

## api.tripnest.example/v1/trips/share

Invite requests include trip_id, inviter_user_id, invitee_email when
typed manually, contact_display_name when selected from contacts, and
invite token. Contact phone numbers are not sent.

## api.tripnest.example/v1/nearby/check

Nearby reminder checks include saved_place_id, approximate latitude and
longitude rounded to two decimals, device timezone, and reminder state.
Precise GPS coordinates from CoreLocation are not persisted in this
endpoint according to the backend log sample.

## purchases.tripnest.example/v1/receipt

Purchase validation sends app_user_id, Apple receipt blob, product_id,
transaction_id, storefront, purchase timestamp, and subscription
renewal status.
