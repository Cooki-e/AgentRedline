# Data map for 4.8 submission

Account identifiers:

- Email address is collected for account login, support, shared trip
  invites, and transactional messages.
- User ID and user ID hash are used across analytics, crash reporting,
  notifications, purchases, and support.
- Display name is collected for shared trip collaboration and support.

Usage data:

- App interactions include screen views, button taps, trip creation,
  invite sending, template preview, checkout start, purchase confirm,
  reminder enablement, and reminder triggered events.
- Events are associated with app instance ID before login and with user
  ID hash after login.
- Experiment variant and subscription tier are attached to analytics
  events for product analysis.

Diagnostics:

- Crash reports include stack traces, device model, OS version, app
  version, installation UUID, memory pressure, and recent breadcrumbs.
- Performance traces include network timing and slow endpoint names.
- Support follow-up can use account-linked crash reports when the user
  is logged in.

Location:

- Nearby reminders use when-in-use location permission.
- The app rounds latitude and longitude to two decimals before sending
  nearby checks and analytics events.
- Location events are associated with trip ID hash and user ID hash when
  the user is logged in.

Contacts and user content:

- Contact picker access is optional. The app reads selected contact
  names and email addresses to send trip invites.
- Contact phone numbers are not sent by the sharing endpoint.
- Trip names, notes, and saved place labels remain in TripNest backend
  storage for trip collaboration.

Purchases:

- Apple processes payment cards.
- TripNest receives Apple receipt blobs, product ID, transaction ID,
  storefront, purchase timestamp, subscription tier, and renewal status
  for entitlement management and support.
