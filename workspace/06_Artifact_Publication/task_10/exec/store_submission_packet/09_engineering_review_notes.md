# Engineering review notes

Reviewer: Mobile platform lead
Date: 2026-06-04

Implementation notes for the privacy submission:

- We do not use an advertising SDK.
- Firebase Analytics joins events to a stable hashed user identifier
  after login. Before login, events use app instance ID.
- Crashlytics and Sentry can include account-linked user hash for
  logged-in sessions so support can find the report.
- Nearby reminders use location permission and send rounded coordinates
  for nearby checks. The value is approximate, but it is still location
  context.
- Contact picker only sends the selected contact's name and email. We
  do not upload the whole address book.
- RevenueCat and our purchase endpoint receive receipt and subscription
  data. Apple handles card payment details.
- Map search sends user-entered place search text to the map provider.
- Notification opens and reminder categories go to OneSignal with the
  app user ID.

Suggested reviewer-note wording:

"TripNest does not contain third-party advertising. The app collects
account, usage, diagnostics, approximate location for nearby reminders,
selected contact invite details, and purchase entitlement data to
operate trip planning, reminders, collaboration, purchases, support,
and product analytics."
